"""T14 How much could a reranker gain at most? Recall of the embedding shortlist (1 Nov)

Purpose: a reranker only re-orders the N chunks that embedding search returns, so Recall@N of the current search
is the ceiling for Recall@5 after reranking. Measured on dev for N = 5, 10, 20, 30, 50 (no reranker involved),
to choose N before any reranker is tried. Questions whose gold chunk is outside N can't be helped.

Result (E-33, test 55): dev (48 in scope): Recall@5 0.750, @10 0.771, @20 0.854, @30 0.938, @50 0.958.
Gold at rank 6-50: q1 9, q79 12, q45 15, q21 16, q4 20, q20 22, q89 22, q71 27, q50 29, q85 49; outside 50: q19, q57.
Outcome: Passed. Rerank the top 30: ceiling 0.938; going to 50 adds one question (q85) for 20 more model runs.

Run from the repo root: python eval/experiments/t14_shortlist_ceiling.py
"""
import sys
sys.path.insert(0, ".")
from src.answer import route
from src.corpus import norm_text
from src.retrieve import retrieve
from eval.run_eval import gold_rank, load_questions

ranks = {}
for q in load_questions("dev"):
    if q["type"] != "in_scope":
        continue
    ranked = retrieve(q["question"], k=50, crop=route(q["question"])[0])
    for c in ranked:
        c["text_norm"] = norm_text(c["text"])
    ranks[q["id"]] = gold_rank(ranked, q)

n = len(ranks)
for N in (5, 10, 20, 30, 50):
    hit = [i for i, r in ranks.items() if r and r <= N]
    print(f"Recall@{N:<2} = {len(hit)}/{n} = {len(hit) / n:.3f}")
print("gold rank 6-50:", sorted(((r, i) for i, r in ranks.items() if r and 5 < r <= 50)))
print("not in top 50:", [i for i, r in ranks.items() if not r])
