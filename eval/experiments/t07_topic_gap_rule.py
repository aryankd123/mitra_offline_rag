"""T07 Topic-gap rule: a word common for other crops but absent for the asked crop (29 Oct, E-16)

Purpose: catch 'covered crop, uncovered topic' questions using corpus statistics.
Result: with any foreign word: FR 7/30 (everyday words like 'sprayed' tripped it). With words in >= 20
other-crop chunks: FR 4/30, FA 1/14 (PASSED: adopted as D-57).

Run from the repo root: python eval/experiments/t07_topic_gap_rule.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import re, sys
from collections import Counter, defaultdict
sys.path.insert(0, ".")
from src.retrieve import retrieve
from src.store import get_collection
from src.answer import route, has_unsupported_crop
from eval.run_eval import load_questions
import config

STOP = set("""a an the and or of in on at to for from by with without into about over under is are was were be been being do does did
done how what which who whom whose why when where should would could can may might must will shall it its this that these those there
their them they you your i we our us me my he she his her than then so such per each any all some most more much many very also not
no yes if as up out off ok know tell give get use used using make made need needed recommended recommend""".split())
def stem(w): return w[:-1] if len(w) > 4 and w.endswith("s") and not w.endswith("ss") else w
def toks(t): return {stem(w) for w in re.findall(r"[a-z]+", t.lower()) if len(w) >= 3 and w not in STOP and w not in config.CROP_SYNONYMS}

got = get_collection().get(include=["documents", "metadatas"])
df = defaultdict(Counter)  # crop -> term -> chunk count
for d, m in zip(got["documents"], got["metadatas"]):
    for w in toks(d): df[m["crop"]][w] += 1

def foreign_terms(q, crop):
    if not crop: return []
    return sorted(w for w in toks(q) if df[crop][w] == 0 and any(df[c][w] > 0 for c in df if c != crop))

for split in ["dev"]:
    F = []
    for q in load_questions(split):
        crop = route(q["question"])[0]
        sim = retrieve(q["question"], k=1, crop=crop)[0]["similarity"]
        F.append((q, crop, sim, foreign_terms(q["question"], crop), has_unsupported_crop(q["question"])))
    ins = [f for f in F if f[0]["type"] == "in_scope"]; oos = [f for f in F if f[0]["type"] != "in_scope"]
    for tau in [0.70, 0.71, 0.72, 0.725, 0.73]:
        for use_x in [False, True]:
            ok = lambda f: not f[4] and f[2] >= tau and not (use_x and f[3])
            print(f"tau={tau:<5} foreign-term rule={use_x!s:<5} FR={sum(not ok(f) for f in ins)}/{len(ins)} {[f[0]['id'] for f in ins if not ok(f)]}  "
                  f"FA={sum(ok(f) for f in oos)}/{len(oos)} {[f[0]['id'] for f in oos if ok(f)]}")
    print("\nquestions with foreign terms:")
    for q, crop, sim, x, u in F:
        if x: print(f"  {q['id']:<4} {q['type'][:6]} crop={crop} sim={sim:.3f} foreign={x}")

print("\nchunk counts in other crops for each foreign term:")
for q, crop, sim, x, u in F:
    if x: print(f"  {q['id']:<4} {q['type'][:6]} " + ", ".join(f"{w}={sum(df[c][w] for c in df if c != crop)}" for w in x))
for mindf in [5, 10, 20]:
    def ok(f, tau=0.725):
        q, crop, sim, x, u = f
        major = [w for w in x if sum(df[c][w] for c in df if c != crop) >= mindf]
        return not u and sim >= tau and not major
    print(f"min other-crop chunks={mindf:<3} FR={sum(not ok(f) for f in ins)}/{len(ins)} {[f[0]['id'] for f in ins if not ok(f)]}  "
          f"FA={sum(ok(f) for f in oos)}/{len(oos)} {[f[0]['id'] for f in oos if ok(f)]}")
