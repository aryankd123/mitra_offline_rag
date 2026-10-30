"""T11 What did adding seven documents do to the questions we already had? (30 Oct)

Purpose: the Iteration 3 dev run mixes two changes, new questions and new documents. The four original PDFs
still produce the same 595 chunks, so hiding the seven new documents from search and from the topic-gap word
counts reproduces the Iteration 2 index exactly. Each dev question is run on both corpora and every change in
gold rank or gate decision is printed with the reason. Expected first line: old corpus = Iteration 2 numbers
(R@5 0.742, false reject 5/31, false accept 1/13), otherwise the masking is wrong.

Result (E-30, test 52): masked run = Iteration 2 exactly (R@5 0.742, MRR 0.570, FR 5/31, FA 1/13).
All 11 documents: R@5 0.742, MRR 0.539; 9 gold chunks pushed down (q4 9->20, q21 6->16, q50 12->29).
Gate: q53 now passes (gold rank 2), q45 passes only via an off-topic "first irrigation" chunk (gold rank 15),
q46 (rice diseases) and q48 (stem borer) are now answered: "disease" is in 4 rice chunks, so the absence
test no longer fires, and weedy-rice leaflet chunks lift the top similarity past tau. New questions: R@5 0.765.
Outcome: Mixed. More documents weaken both gate signals; the gate must be re-checked on every corpus change.

Run from the repo root: python eval/experiments/t11_corpus_growth_effect.py
"""
import sys
sys.path.insert(0, ".")
import src.coverage as coverage
import src.retrieve as retrieve_mod
from src.store import get_collection
from eval.run_eval import evaluate, summarize

OLD_DOCS = {
    "potato_disease-pest-management_cpri_2016_manual",
    "rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief",
    "rice_weedy-rice-options_dwsr_2013_article",
    "wheat_rust-resistant-varieties-economics_vpkas_2020_article",
}


class OldDocsOnly:
    """Wraps the Chroma collection; get() returns only the chunks of the four original documents."""
    def __init__(self, col):
        self.col = col

    def get(self, include):
        got = self.col.get(include=sorted(set(include) | {"metadatas"}))
        keep = [i for i, m in enumerate(got["metadatas"]) if m["doc_id"] in OLD_DOCS]
        out = {"ids": [got["ids"][i] for i in keep]}
        for key in include:  # retrieve.py asks for embeddings/documents/metadatas, coverage.py for documents/metadatas
            out[key] = [got[key][i] for i in keep]
        return out


def run(masked):
    real = get_collection()
    source = (lambda: OldDocsOnly(real)) if masked else (lambda: real)
    retrieve_mod.get_collection = coverage.get_collection = source
    retrieve_mod._index = None  # force both caches to rebuild from the chosen corpus
    coverage._df = coverage._n_chunks = None
    qs, in_recs, gate_rows = evaluate("dev")
    return {q["id"]: q for q in qs}, {r["id"]: r for r in in_recs}, {g["id"]: g for g in gate_rows}


def report(name, ids, qs, recs, gates, oos_ids):
    rs = [recs[i] for i in ids if i in recs]
    fr = [i for i in ids if i in recs and gates[i]["refused"]]
    fa = [i for i in oos_ids if not gates[i]["refused"]]
    print(f"{name:<40} n={len(rs):<3} R@5={summarize(rs)['recall@5']:<6} MRR@10={summarize(rs)['mrr@10']:<6} "
          f"false reject {len(fr)}/{len(rs)} {fr}  false accept {len(fa)}/{len(oos_ids)} {fa}")


qs, old_recs, old_gates = run(masked=True)
_, new_recs, new_gates = run(masked=False)

num = lambda i: int(i[1:])
old_in = [i for i in qs if num(i) <= 68 and i != "q44" and qs[i]["type"] == "in_scope"]
old_oos = [i for i in qs if num(i) <= 68 and qs[i]["type"] == "out_of_scope"]
new_in = [i for i in qs if num(i) >= 69]

# q44 was out of scope in v2; on the old corpus it is judged with its old label
old_gates_oos_v2 = old_oos + ["q44"]
report("old questions, old corpus (= Iter 2)", old_in, qs, old_recs, old_gates, old_gates_oos_v2)
report("old questions, new corpus", old_in, qs, new_recs, new_gates, old_oos)
report("new questions q69+, new corpus", new_in + ["q44"], qs, new_recs, new_gates, [])

print("\nChanges on old questions (old corpus -> new corpus):")
for i in old_in + old_oos:
    o, n = old_gates[i], new_gates[i]
    ro, rn = (old_recs[i]["rank"], new_recs[i]["rank"]) if i in old_recs else (None, None)
    if o["refused"] != n["refused"] or ro != rn or o["reason"] != n["reason"]:
        print(f"  {i:<4} {qs[i]['type']:<12} rank {str(ro):>4} -> {str(rn):<4} "
              f"gate {o['reason'] or 'answer'} ({o['top_sim']:.3f}) -> {n['reason'] or 'answer'} ({n['top_sim']:.3f})"
              f"  | {qs[i]['question'][:70]}")
