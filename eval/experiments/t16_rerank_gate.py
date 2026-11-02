"""T16 Gate on the reranker score: does it separate answerable from unanswerable dev questions? (1 Nov)

Purpose: option B of D-64. Keep the crop guard and topic-gap check, replace the cosine threshold (tau = 0.725) with
a threshold theta on the best reranker score among the 30 candidates. Uses the scores saved by t15 (no model runs).
Today (option A, cosine tau): wrongly refused 3/48, wrongly answered 3/12 (q46, q47, q48).
Prediction written before the run (Aryan, 1 Nov): q46 and q48 both refused.

Rule for choosing theta, fixed before looking at the scores: the fewest wrong decisions on dev (false refusals +
false answers); among ties, the fewest false answers; theta placed halfway between the two neighbouring scores.
Also prints the overlap: in-scope questions scoring at or below the highest out-of-scope one, i.e. what a theta
that refuses every out-of-scope question would cost.

Result (E-35, test 57):
  A  cosine tau 0.725         wrongly refused 3/48 (q20, q52, q55), wrongly answered 3/12 (q46, q47, q48)
  B  minilm-l6, theta 0.035   wrongly refused 0/48, wrongly answered 2/12: q46 scores 0.81, q48 0.66 (fooled)
  B  bge-m3-int8, theta 0.171 wrongly refused 1/48 (q16, 0.099), wrongly answered 0/12
bge gap: highest out-of-scope reaching the check q48 0.134, next in-scope q45 0.208, so any theta in between
gives the same result. First run placed theta at 0.137 because the cut list included early-stopped questions
(q43 0.141, stopped by the topic gap); fixed so only questions reaching the score check place theta.
q16 ("footwear made of animal hide or woven cloth") is a paraphrase both rerankers fail to link to its passage.
Prediction (Aryan): q46 and q48 both refused -> right for bge, wrong for MiniLM.
Outcome: Passed for bge; MiniLM can't fix the gate.

Run from the repo root: python eval/experiments/t16_rerank_gate.py
"""
import json
import sys
sys.path.insert(0, ".")
import config
from src.answer import gate
from eval.run_eval import load_questions

saved = json.load(open(config.ROOT / "eval" / "results" / "rerank_scores_dev.json", encoding="utf-8"))
qs = {q["id"]: q for q in load_questions("dev")}
# crop guard + topic gap only: top_sim=1.0 switches the cosine check off
early = {i: gate(qs[i]["question"], 1.0, saved[i]["crop"])[0] for i in saved}
ins = [i for i in saved if saved[i]["type"] == "in_scope"]
oos = [i for i in saved if saved[i]["type"] == "out_of_scope"]


def count(refuse):
    fr = [i for i in ins if refuse(i)]
    fa = [i for i in oos if not refuse(i)]
    return fr, fa


fr, fa = count(lambda i: early[i] is not None or saved[i]["cosine"][0] < config.SIMILARITY_THRESHOLD)
print(f"A  cosine tau {config.SIMILARITY_THRESHOLD}: wrongly refused {len(fr)}/{len(ins)} {fr}, wrongly answered {len(fa)}/{len(oos)} {fa}")
print(f"   stopped early (crop guard / topic gap): {sorted(i for i in saved if early[i])}")

for model in config.RERANK_MODELS:
    best = {i: max(saved[i][model]) for i in saved}
    # Only questions that reach the score check can place theta; first version also used early-stopped ones,
    # which put theta at 0.137, next to q43 (stopped by the topic gap) instead of mid-gap (test 57)
    cuts = sorted({best[i] for i in saved if not early[i]})
    options = []
    for lo, hi in zip([0.0] + cuts, cuts + [1.0]):
        theta = (lo + hi) / 2
        fr, fa = count(lambda i: early[i] is not None or best[i] < theta)
        options.append((len(fr) + len(fa), len(fa), theta, fr, fa))
    errors, n_fa, theta, fr, fa = min(options, key=lambda o: (o[0], o[1]))
    print(f"\nB  {model}: theta {theta:.4f} -> wrongly refused {len(fr)}/{len(ins)} {fr}, wrongly answered {n_fa}/{len(oos)} {fa}")
    print("   out-of-scope best scores (not stopped early):",
          sorted((round(best[i], 4), i) for i in oos if not early[i]))
    top_oos = max([best[i] for i in oos if not early[i]] or [0])
    print("   in-scope best scores at or below the highest out-of-scope one:",
          sorted((round(best[i], 4), i) for i in ins if best[i] <= top_oos))
    print("   q46, q48:", {i: round(best[i], 4) for i in ("q46", "q48")})
