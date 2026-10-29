"""T02 Crop routing: filter search by the crop named in the question (29 Oct, E-15e)

Purpose: test whether routing removes wrong-crop passages without hurting recall.
Result: eval R@5 unchanged (0.767), wrong-crop chunks 9 -> 7 of 150, leaf-blight probe now refused;
3 of 7 probes still answered (PARTIAL: adopted as D-56, not enough alone).

Run from the repo root: python eval/experiments/t02_crop_routing.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import re, sys
sys.path.insert(0, ".")
import numpy as np
import config
from src.retrieve import retrieve
from src.answer import has_unsupported_crop
import config
def gate_reason(q, sim):  # the gate as it was before Iteration 2: crop guard + threshold only
    if has_unsupported_crop(q): return "unsupported_crop"
    return "low_similarity" if sim < config.SIMILARITY_THRESHOLD else None
from src.corpus import norm_text
from eval.run_eval import load_questions, is_hit_at_k, gold_rank

CROP_WORDS = {"rice": "rice", "paddy": "rice", "wheat": "wheat", "gehun": "wheat", "potato": "potato", "potatoes": "potato", "aloo": "potato"}
def detect(q):
    found = {CROP_WORDS[w] for w in re.findall(r"[a-z]+", q.lower()) if w in CROP_WORDS}
    return found.pop() if len(found) == 1 else None

qs = load_questions("all")
for routing in [False, True]:
    recs, contam, fr, fa = [], [], 0, 0
    for q in qs:
        crop = detect(q["question"]) if routing else None
        ranked = retrieve(q["question"], k=50, crop=crop)
        for c in ranked: c["text_norm"] = norm_text(c["text"])
        refused = gate_reason(q["question"], ranked[0]["similarity"]) is not None
        if q["type"] == "in_scope":
            exp_crop = q["doc_id"].split("_")[0]
            contam.append(sum(c["doc_id"].split("_")[0] != exp_crop for c in ranked[:5]))
            recs.append((is_hit_at_k(ranked, q, 5), (lambda r: 1/r if r and r <= 10 else 0)(gold_rank(ranked, q))))
            fr += refused
        else:
            fa += not refused
    n_in = len(recs)
    print(f"routing={routing}: R@5={np.mean([r[0] for r in recs]):.3f} MRR@10={np.mean([r[1] for r in recs]):.3f} "
          f"other-crop chunks in top5: {sum(contam)}/{5*n_in} ({np.mean([c>0 for c in contam])*100:.0f}% of questions) "
          f"FR={fr}/{n_in} FA={fa}/{len(qs)-n_in}")

det = [(q["id"], detect(q["question"]), q["doc_id"].split("_")[0] if q["doc_id"] else "-") for q in qs if q["type"]=="in_scope"]
print("in-scope with no crop word:", [d[0] for d in det if d[1] is None], " wrong crop:", [d for d in det if d[1] and d[1]!=d[2]])

PROBES = ["Ok what do you know about the diseases in rice crops and how would you prevent them",
    "What fungicide controls blast disease in rice?", "How do I manage sheath blight in paddy?",
    "How do I control brown spot disease of rice?", "Which herbicide controls Phalaris minor in wheat?",
    "What is the irrigation schedule for wheat?", "What are the symptoms of bacterial leaf blight in rice?"]
print("\nprobes with routing:")
for q in PROBES:
    ch = retrieve(q, k=5, crop=detect(q))
    r = gate_reason(q, ch[0]["similarity"])
    print(f"  {'REFUSE' if r else 'ANSWER'} top1={ch[0]['similarity']:.4f} crops={[c['doc_id'].split('_')[0] for c in ch]}  {q[:60]}")
