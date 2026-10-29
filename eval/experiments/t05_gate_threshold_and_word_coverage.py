"""T05 Re-pick the threshold and try an IDF word-coverage signal on dev v2 (29 Oct, E-16)

Purpose: find a gate that refuses uncovered-topic questions without refusing real ones.
Result: tau 0.73 + routing: FR 5/30, FA 1/14, but only by moving the line past q42 (0.7253), a knife-edge.
Word coverage >= 0.5: FR 7-8/30 because paraphrase questions avoid the documents' words (REJECTED).

Run from the repo root: python eval/experiments/t05_gate_threshold_and_word_coverage.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import math, re, sys
from collections import Counter
sys.path.insert(0, ".")
import numpy as np
from src.retrieve import retrieve
from src.store import get_collection
from src.corpus import norm_text
from eval.run_eval import load_questions, is_hit_at_k

CROPS = {"rice": "rice", "paddy": "rice", "wheat": "wheat", "gehun": "wheat", "potato": "potato", "potatoes": "potato", "aloo": "potato"}
UNSUP = {"sesame","til","cumin","jeera","mango","blackgram","urdbean","cotton","tea","coffee","apple","banana","citrus","grapevine"}
STOP = set("""a an the and or of in on at to for from by with without into about over under is are was were be been being do does did
done how what which who whom whose why when where should would could can may might must will shall it its this that these those there
their them they you your i we our us me my he she his her than then so such per each any all some most more much many very also not
no yes if as up out off ok know tell give get use used using make made need needed recommended recommend""".split())

def stem(w): return w[:-1] if len(w) > 4 and w.endswith("s") and not w.endswith("ss") else w
def toks(t): return {stem(w) for w in re.findall(r"[a-z]+", t.lower()) if len(w) >= 3 and w not in STOP and w not in CROPS}
def crop_of(q):
    f = {CROPS[w] for w in re.findall(r"[a-z]+", q.lower()) if w in CROPS}
    return f.pop() if len(f) == 1 else None
def unsup(q):
    ws = set(re.findall(r"[a-z]+", q.lower()))
    return bool(ws & UNSUP) and not bool(ws & set(CROPS))

docs = get_collection().get(include=["documents"])["documents"]
N = len(docs); df = Counter(w for d in docs for w in toks(d))
idf = lambda w: math.log(N / (1 + df.get(w, 0)))

def features(q, routing):
    ch = retrieve(q["question"], k=50, crop=crop_of(q["question"]) if routing else None)
    for c in ch: c["text_norm"] = norm_text(c["text"])
    qt = toks(q["question"]); ct = set().union(*(toks(c["text"]) for c in ch[:5]))
    w_all = sum(idf(w) for w in qt) or 1
    cov = sum(idf(w) for w in qt if w in ct) / w_all
    missing = sorted((w for w in qt if w not in ct), key=lambda w: -idf(w))
    hit5 = is_hit_at_k(ch, q, 5) if q["type"] == "in_scope" else None
    return dict(id=q["id"], type=q["type"], tag=q["tag"], sim=ch[0]["similarity"], cov=cov, unsup=unsup(q["question"]), missing=missing[:3], hit5=hit5)

qs = load_questions("dev")
for routing in [False, True]:
    F = [features(q, routing) for q in qs]
    ins = [f for f in F if f["type"] == "in_scope"]; oos = [f for f in F if f["type"] != "in_scope"]
    print(f"\n===== routing={routing}  R@5={np.mean([f['hit5'] for f in ins]):.3f} (n={len(ins)})")
    for tau in [0.70, 0.71, 0.72, 0.725, 0.73, 0.74]:
        for cmin in [0.0, 0.5, 0.6, 0.7, 0.75, 0.8]:
            ok = lambda f: (not f["unsup"]) and f["sim"] >= tau and f["cov"] >= cmin
            fr = sum(not ok(f) for f in ins); fa = [f["id"] for f in oos if ok(f)]
            frs = [f["id"] for f in ins if not ok(f)]
            if cmin in (0.0,) or len(fa) <= 2:
                print(f"  tau={tau:<5} cov>={cmin:<4} FR={fr:>2}/{len(ins)} FA={len(fa):>2}/{len(oos)}  FA={fa} FR={frs}")
    if routing:
        print("\n  per-question (routing on):")
        for f in sorted(F, key=lambda f: (f["type"], f["cov"])):
            print(f"   {f['id']:<4} {f['type'][:6]:<6} {f['tag'][:10]:<10} sim={f['sim']:.3f} cov={f['cov']:.2f} unsup={int(f['unsup'])} hit5={f['hit5']} missing={f['missing']}")
