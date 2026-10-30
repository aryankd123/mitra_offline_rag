"""Evaluate the frozen pipeline end to end through src/ (routing, exact search over the Chroma store, gate).

Usage (from the repo root):
    python -m eval.run_eval --split dev
    python -m eval.run_eval --split test --generate   # also runs the LLM and writes eval/stage6_answers_test.md
    python -m eval.run_eval --split dev --no-log      # don't append to experiments.csv
    python -m eval.run_eval --split all --offline-guard --no-log   # fails if anything tries to leave localhost
"""
import argparse
import csv
import json
import platform
from datetime import datetime

import numpy as np

import config
from src import netguard
from src.answer import answer_question, gate, route
from src.corpus import norm_text
from src.retrieve import retrieve

RANK_DEPTH = 50  # how deep we look for the gold rank; MRR is cut at 10
QUESTIONS_VERSION = "v3"  # v3 = v2 + q69-q94 for the Iteration 3 documents, q44 relabelled in scope


def load_questions(split):
    rows = []
    with open(config.QUESTIONS_CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if split != "all" and r["split"].strip() != split:
                continue
            rows.append({
                "id": r["id"].strip(),
                "question": r["question"].strip(),
                "type": r["type"].strip(),
                "tag": r["tag"].strip(),
                "doc_id": r["doc_id"].strip(),
                "expected_pages": [int(p) for p in r["expected_pages"].split(";") if p.strip()],
                "answer_phrases": [norm_text(p) for p in r["answer_phrases"].split(";") if p.strip()],
                "match": r["match"].strip(),
            })
    return rows


# Hit rule from 05_evaluation: expected doc + expected page + answer phrase in chunk text;
# for match='all' every phrase must appear somewhere in the top-k union.
def chunk_matches_phrase(c, q, ph):
    return c["doc_id"] == q["doc_id"] and c["page"] in q["expected_pages"] and ph in c["text_norm"]


def is_hit_at_k(ranked, q, k):
    top_k = ranked[:k]
    found = [any(chunk_matches_phrase(c, q, ph) for c in top_k) for ph in q["answer_phrases"]]
    return any(found) if q["match"] == "any" else all(found)


def gold_rank(ranked, q):
    return next((r for r in range(1, len(ranked) + 1) if is_hit_at_k(ranked, q, r)), None)


def summarize(recs):
    if not recs:
        return {"n": 0}
    return {
        "n": len(recs),
        "recall@1": round(float(np.mean([r["r1"] for r in recs])), 4),
        "recall@3": round(float(np.mean([r["r3"] for r in recs])), 4),
        "recall@5": round(float(np.mean([r["r5"] for r in recs])), 4),
        "mrr@10": round(float(np.mean([r["rr10"] for r in recs])), 4),
        "median_gold_rank": float(np.median([r["rank"] or RANK_DEPTH for r in recs])),
    }


def evaluate(split):
    qs = load_questions(split)
    in_recs, gate_rows = [], []
    for q in qs:
        crop = route(q["question"])[0]  # same routing as answer_question
        ranked = retrieve(q["question"], k=RANK_DEPTH, crop=crop)
        for c in ranked:
            c["text_norm"] = norm_text(c["text"])
        top_sim = ranked[0]["similarity"]
        reason, _ = gate(q["question"], top_sim, crop)
        gate_rows.append({"id": q["id"], "type": q["type"], "tag": q["tag"], "top_sim": top_sim,
                          "refused": reason is not None, "reason": reason})
        if q["type"] == "in_scope":
            rank = gold_rank(ranked, q)
            in_recs.append({
                "id": q["id"], "tag": q["tag"], "rank": rank, "top_sim": top_sim,
                "r1": float(is_hit_at_k(ranked, q, 1)),
                "r3": float(is_hit_at_k(ranked, q, 3)),
                "r5": float(is_hit_at_k(ranked, q, 5)),
                "rr10": 1.0 / rank if rank and rank <= 10 else 0.0,
            })
    return qs, in_recs, gate_rows


def write_answers(split, qs, path):
    lines = [f"# Stage 6 end-to-end answers ({split}, {config.GENERATOR_MODEL}, prompt {config.PROMPT_VERSION}, k={config.TOP_K})", ""]
    gen_times, ret_times, e2e = [], [], []
    for q in qs:
        res = answer_question(q["question"])
        ret_times.append(res["timings"]["retrieve_s"])
        if not res["gated"]:
            gen_times.append(res["timings"]["generate_s"])
        refused = res["answer"].strip().lower().startswith(config.REFUSAL_SENTENCE.lower())
        e2e.append((q, refused, res["gated"]))
        lines += [
            f"## {q['id']} ({q['type']} / {q['tag']}) | top_sim={res['top_similarity']:.4f} | "
            f"{'GATED (' + res['gate_reason'] + ')' if res['gated'] else 'gen=' + str(res['timings']['generate_s']) + 's'}",
            f"**Q:** {q['question']}", "",
            f"**Expected:** {q['doc_id'] or '(refusal)'} p.{';'.join(map(str, q['expected_pages']))} — "
            f"{'; '.join(q['answer_phrases'])}", "",
            f"**A:** {res['answer']}", "",
            "```", res["sources_block"], "```",
            "Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:", "",
        ]
        print(f"  {q['id']} done")
    summary = [f"Retrieval latency over {len(ret_times)} questions: "
               f"p50={np.percentile(ret_times, 50):.3f}s, p95={np.percentile(ret_times, 95):.3f}s"]
    if gen_times:
        summary.append(f"Generation latency over {len(gen_times)} answered questions: "
                       f"p50={np.percentile(gen_times, 50):.2f}s, p95={np.percentile(gen_times, 95):.2f}s")
    ins = [(q, r, g) for q, r, g in e2e if q["type"] == "in_scope"]
    oos = [(q, r, g) for q, r, g in e2e if q["type"] != "in_scope"]
    summary.append(
        f"End-to-end refusals (gate or model): in-scope wrongly refused {sum(r for _, r, _ in ins)}/{len(ins)} "
        f"{[q['id'] for q, r, _ in ins if r]}; out-of-scope wrongly answered {sum(not r for _, r, _ in oos)}/{len(oos)} "
        f"{[q['id'] for q, r, _ in oos if not r]}; refused by the model itself: {[q['id'] for q, r, g in e2e if r and not g]}")
    summary.append(f"Machine: {platform.platform()}, {platform.processor() or 'unknown CPU'}; "
                   f"offline guard {'on, blocked: ' + str(netguard.attempts()) if netguard.installed() else 'off'}\n")
    lines[1:1] = summary
    print("\n".join(summary))
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    ap.add_argument("--generate", action="store_true", help="also run the LLM and write an answers file")
    ap.add_argument("--no-log", action="store_true", help="don't append a row to experiments.csv")
    ap.add_argument("--run-id", help="name for the experiments.csv row (default 6_modules_chroma_<split>)")
    ap.add_argument("--offline-guard", action="store_true",
                    help="block and report any non-loopback network access (src/netguard.py)")
    args = ap.parse_args()
    if args.offline_guard:
        netguard.install()

    qs, in_recs, gate_rows = evaluate(args.split)
    overall = summarize(in_recs)
    print(f"\n[{args.split}] {len(qs)} questions (routing + exact search + gate)")
    print("  OVERALL   ", overall)
    for tag in sorted({r["tag"] for r in in_recs}):
        print(f"  {tag:<10}", summarize([r for r in in_recs if r["tag"] == tag]))
    print("\n  Per-question gold rank / top-1 similarity:")
    for r in in_recs:
        print(f"    {r['id']:<4} {r['tag']:<10} rank={str(r['rank']):<5} top_sim={r['top_sim']:.4f}")

    ins = [g for g in gate_rows if g["type"] == "in_scope"]
    oos = [g for g in gate_rows if g["type"] == "out_of_scope"]
    fr = sum(g["refused"] for g in ins)
    fa = sum(not g["refused"] for g in oos)
    print(f"\n  Gate (crop guard + topic gap alpha={config.TOPIC_GAP_ALPHA} + similarity tau={config.SIMILARITY_THRESHOLD}):")
    print(f"    in-scope false reject:     {fr}/{len(ins)}  {[g['id'] + ':' + g['reason'] for g in ins if g['refused']]}")
    print(f"    out-of-scope false accept: {fa}/{len(oos)}  {[(g['id'], g['top_sim']) for g in oos if not g['refused']]}")
    for tag in sorted({g["tag"] for g in gate_rows}):
        rows = [g for g in gate_rows if g["tag"] == tag]
        wrong = [g for g in rows if g["refused"] == (g["type"] == "in_scope")]
        kind = "wrongly refused" if rows[0]["type"] == "in_scope" else "wrongly answered"
        print(f"      tag {tag:<16} {len(wrong)}/{len(rows)} {kind}")

    if not args.no_log:
        cfg = {"chunk_size": config.CHUNK_SIZE, "chunk_overlap": config.CHUNK_OVERLAP, "k": config.TOP_K,
               "min_chunk_len": config.MIN_CHUNK_LEN, "embed_model": config.EMBED_MODEL,
               "threshold": config.SIMILARITY_THRESHOLD, "crop_guard": True, "search": "exact (numpy)",
               "crop_routing": config.CROP_ROUTING, "topic_gap_alpha": config.TOPIC_GAP_ALPHA,
               "generator": config.GENERATOR_MODEL, "questions": QUESTIONS_VERSION}
        with open(config.EXPERIMENTS_CSV, "a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerow([
                args.run_id or f"6_modules_chroma_{args.split}", datetime.now().strftime("%Y-%m-%d %H:%M"), json.dumps(cfg),
                args.split, len(qs), overall["recall@1"], overall["recall@3"], overall["recall@5"],
                overall["mrr@10"], overall["median_gold_rank"],
                round(fa / max(1, len(oos)), 4), round(fr / max(1, len(ins)), 4),
                "src/ modules; exact search; gate = crop guard + topic gap + threshold",
            ])
        print(f"\n  Appended row to {config.EXPERIMENTS_CSV.name}")

    if args.generate:
        out = (config.ROOT / "eval" / "results" / f"answers_{args.run_id}.md" if args.run_id
               else config.ROOT / "eval" / f"stage6_answers_{args.split}.md")
        write_answers(args.split, qs, out)
    if args.offline_guard:
        blocked = netguard.attempts()
        print(f"\n  Offline guard: {'PASS, no non-loopback network access' if not blocked else 'FAIL, blocked ' + str(blocked)}")
        if blocked:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
