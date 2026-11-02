"""T17 How many candidates must the reranker score? Quality vs depth from saved scores (1 Nov)

Purpose: bge-reranker-v2-m3 takes 38.6 s per question at 30 candidates on this laptop (p95 76.6 s, over Aryan's
60 s limit; test 56). Time grows with the number of passages scored, so scoring only the first N embedding
candidates is the obvious saving. Uses the scores saved by t15 (no model runs): for N = 5..30, Recall@5 and MRR
after re-ordering the first N, and the gate (crop guard + topic gap + best score of the first N, theta by the
t16 rule). Time is estimated as measured time x N/30; the chosen N must be timed for real afterwards.

Result (E-36, test 58), bge-m3-int8: N=5 R@5 0.750 (can't change top 5), gate 2/48 refused, 0/12 answered,
est. 6 s; N=10 0.750; N=15 0.792; N=20 0.812, gate 1/48, 0/12, est. 26 s; N=25 0.875, est. 32 s; N=30 0.917, 39 s.
minilm-l6: R@5 0.750 -> 0.833 from N=5 to 30; gate wrongly answers q46 (and q48 from N=15) at every depth.
Outcome: Passed. Depth buys retrieval, not safety: bge's gate works from 5 candidates. Aryan chose bge with
30 candidates (1 Nov) over N=20 or MiniLM, accepting a p95 above his 60 s limit on this CPU.

Run from the repo root: python eval/experiments/t17_rerank_depth.py
"""
import json
import sys
sys.path.insert(0, ".")
import numpy as np

import config
from src.answer import gate
from src.corpus import norm_text
from src.retrieve import retrieve
from src.answer import route
from eval.run_eval import gold_rank, load_questions

saved = json.load(open(config.ROOT / "eval" / "results" / "rerank_scores_dev.json", encoding="utf-8"))
qs = {q["id"]: q for q in load_questions("dev")}
early = {i: gate(qs[i]["question"], 1.0, saved[i]["crop"])[0] for i in saved}
chunks = {}
for i, q in qs.items():  # same candidates as t15, in embedding order
    ranked = retrieve(q["question"], k=config.RERANK_CANDIDATES, crop=route(q["question"])[0])
    assert [c["id"] for c in ranked] == saved[i]["ids"], i
    for c in ranked:
        c["text_norm"] = norm_text(c["text"])
    chunks[i] = ranked
P50 = {"minilm-l6": 4.41, "bge-m3-int8": 38.63}  # measured at N = 30 (t15)

for model in config.RERANK_MODELS:
    print(model)
    for n in (5, 10, 15, 20, 25, 30):
        r5, rr = [], []
        best = {}
        for i, q in qs.items():
            s = saved[i][model][:n]
            order = sorted(range(n), key=lambda j: -s[j]) + list(range(n, len(chunks[i])))
            ranked = [chunks[i][j] for j in order]
            best[i] = max(s)
            if q["type"] == "in_scope":
                rank = gold_rank(ranked, q)
                r5.append(bool(rank and rank <= 5))
                rr.append(1 / rank if rank and rank <= 10 else 0.0)
        cuts = sorted({best[i] for i in qs if not early[i]})
        options = []
        for lo, hi in zip([0.0] + cuts, cuts + [1.0]):
            th = (lo + hi) / 2
            fr = [i for i in qs if qs[i]["type"] == "in_scope" and (early[i] or best[i] < th)]
            fa = [i for i in qs if qs[i]["type"] == "out_of_scope" and not early[i] and best[i] >= th]
            options.append((len(fr) + len(fa), len(fa), th, fr, fa))
        _, _, th, fr, fa = min(options, key=lambda o: (o[0], o[1]))
        print(f"  N={n:<2} R@5 {np.mean(r5):.3f}  MRR@10 {np.mean(rr):.3f}  gate theta {th:.3f}: "
              f"wrongly refused {len(fr)} {fr}, wrongly answered {len(fa)} {fa}  est. p50 {P50[model] * n / 30:.1f} s")
