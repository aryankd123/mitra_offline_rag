"""T15 Rerankers on dev: speed on this laptop, retrieval after re-ordering, hub chunks (1 Nov)

Purpose: compare ms-marco-MiniLM-L6-v2 and bge-reranker-v2-m3 (int8) re-ordering the top 30 of embedding search
(D-64) on the 60 dev questions. Measures seconds to score 30 passages (model load excluded), Recall@1/3/5 and
MRR@10 against the current search (R@5 0.750, MRR 0.563; ceiling R@5 0.938, test 55), and how many rice top-5
lists still contain the herbicide leaflet intro chunk (9 of 21 today, test 53). Offline guard on.
Predictions written before the run (Aryan, 1 Nov): Recall@5 above 0.90 with MiniLM.
Saves every candidate's cosine and reranker score to eval/results/rerank_scores_dev.json for t16 (gate).

Result (E-34, test 56), dev 48 in scope, offline guard: 0 network attempts.
  embeddings only   R@1 0.417  R@3 0.688  R@5 0.750  MRR@10 0.563  hub chunk in 9/21 rice top-5 lists
  minilm-l6         R@1 0.500  R@3 0.771  R@5 0.833  MRR@10 0.655  hub 7/21  4.41 s p50, 6.25 s p95
  bge-m3-int8       R@1 0.625  R@3 0.854  R@5 0.917  MRR@10 0.753  hub 4/21  38.63 s p50, 76.59 s p95
bge lifts q50 29->1, q89 22->1, q79 12->1, q21 16->1, q20 22->2, q45 15->2; drops q94 3->6, q44 1->3.
One bge question took 4359 s: the laptop slept (CPU time 64 min in 105 min of wall time). Not run with
python -u, so nothing was visible until the end; long runs now use -u.
Prediction (Aryan): R@5 above 0.90 with MiniLM -> wrong for MiniLM (0.833), right for bge (0.917).
Outcome: Passed. Both help; bge is clearly better but about 9x slower on this CPU.

Run from the repo root: python eval/experiments/t15_reranker_dev.py
"""
import json
import sys
import time
sys.path.insert(0, ".")
import numpy as np

import config
from src import netguard
from src.answer import route
from src.corpus import norm_text
from src.rerank import score
from src.retrieve import retrieve
from eval.run_eval import gold_rank, is_hit_at_k, load_questions, summarize

netguard.install()
HUB = "rice_herbicide-weed-control_nrri_2018_brief:p1:c0"
qs = load_questions("dev")
cands = {}
for q in qs:
    crop = route(q["question"])[0]
    ranked = retrieve(q["question"], k=config.RERANK_CANDIDATES, crop=crop)
    for c in ranked:
        c["text_norm"] = norm_text(c["text"])
    cands[q["id"]] = (crop, ranked)


def metrics(order_of):
    recs = []
    for q in qs:
        if q["type"] != "in_scope":
            continue
        ranked = order_of(q)
        rank = gold_rank(ranked, q)
        recs.append({"r1": float(is_hit_at_k(ranked, q, 1)), "r3": float(is_hit_at_k(ranked, q, 3)),
                     "r5": float(is_hit_at_k(ranked, q, 5)), "rr10": 1 / rank if rank and rank <= 10 else 0.0,
                     "rank": rank, "id": q["id"]})
    hub = sum(HUB in [c["id"] for c in order_of(q)[:5]] for q in qs if cands[q["id"]][0] == "rice")
    return summarize(recs), {r["id"]: r["rank"] for r in recs}, hub


base, base_ranks, base_hub = metrics(lambda q: cands[q["id"]][1])
n_rice = sum(c == "rice" for c, _ in cands.values())
print(f"embedding only        {base}  hub chunk in {base_hub}/{n_rice} rice top-5 lists")

saved = {q["id"]: {"type": q["type"], "crop": cands[q["id"]][0],
                   "ids": [c["id"] for c in cands[q["id"]][1]],
                   "cosine": [c["similarity"] for c in cands[q["id"]][1]]} for q in qs}
for model in config.RERANK_MODELS:
    score("warm-up", ["load the model"], model)  # first call loads the ONNX session; not timed
    times, scores = [], {}
    for q in qs:
        crop, ranked = cands[q["id"]]
        t0 = time.perf_counter()
        scores[q["id"]] = score(q["question"], [c["text"] for c in ranked], model)
        times.append(time.perf_counter() - t0)
        saved[q["id"]][model] = [round(s, 6) for s in scores[q["id"]]]
    reorder = lambda q: [c for _, c in sorted(zip(scores[q["id"]], cands[q["id"]][1]), key=lambda t: -t[0])]
    m, ranks, hub = metrics(reorder)
    moved = {i: (base_ranks[i], ranks[i]) for i in ranks if ranks[i] != base_ranks[i]}
    print(f"\n{model:<21} {m}  hub chunk in {hub}/{n_rice} rice top-5 lists")
    print(f"  seconds per question (30 passages): p50 {np.percentile(times, 50):.2f}, p95 {np.percentile(times, 95):.2f}, max {max(times):.2f}")
    print(f"  gold rank changes (before, after): {moved}")

json.dump(saved, open(config.ROOT / "eval" / "results" / "rerank_scores_dev.json", "w", encoding="utf-8"), indent=0)
print("\nnetwork attempts blocked:", netguard.attempts())
