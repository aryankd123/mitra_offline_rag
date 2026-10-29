"""T08 Topic-gap rule v2: flag a word only if its absence from the asked crop is statistically surprising (29 Oct)

Purpose: fix false refusals like "The wheat documents never mention: type." (Aryan, web UI). The v1 rule
(word in >= 20 other-crop chunks, 0 in the asked crop) ignores crop size: potato has 516 chunks, rice 46,
wheat 33, so ordinary words easily pass 20 in potato. v2: p = share of other-crop chunks containing the word;
probability of seeing it in none of the n chunks of the asked crop by chance = (1 - p) ** n; flag if < alpha.
Designed on dev + live examples only; test v2 numbers are reported but the split is already seen (E-20).

Run from the repo root: python eval/experiments/t08_topic_gap_significance.py
"""
import re, sys
from collections import Counter
sys.path.insert(0, ".")
import config
from src.coverage import _chunk_counts, _stem, terms
from src.store import get_collection
from src.retrieve import retrieve
from src.answer import route, has_unsupported_crop
from eval.run_eval import load_questions

n = Counter(m["crop"] for m in get_collection().get(include=["metadatas"])["metadatas"])
df = _chunk_counts()

def gaps_v1(q, crop):
    return sorted({w for w in terms(q) if crop and df[crop][w] == 0 and sum(df[c][w] for c in df if c != crop) >= 20})

def gaps_v2(q, crop, alpha):
    out = []
    for w in sorted(terms(q)):
        if not crop or df[crop][w] > 0:
            continue
        p = sum(df[c][w] for c in df if c != crop) / sum(n[c] for c in n if c != crop)
        if (1 - p) ** n[crop] < alpha:
            out.append(f"{w}:{(1 - p) ** n[crop]:.0e}")
    return out

LIVE = ["Hi could you tell me if i can use which type of weed removal strategy for my wheat crop",
        "Hi could you tell me if i can use which type of weed removal strategy for my rice crop",
        "Ok what do you know about the diseases in rice crops and how would you prevent them"]
for q in LIVE:
    crop = route(q)[0]
    print(f"LIVE {q[:60]!r}\n     v1={gaps_v1(q, crop)}  v2(0.01)={gaps_v2(q, crop, 0.01)}  v2(0.001)={gaps_v2(q, crop, 0.001)}")

for split in ["dev", "test"]:
    rows = []
    for q in load_questions(split):
        crop = route(q["question"])[0]
        sim = retrieve(q["question"], k=1, crop=crop)[0]["similarity"]
        rows.append((q, crop, sim))
    for name, fn in [("v1 (>=20 chunks)", lambda q, c: gaps_v1(q, c)),
                     ("v2 alpha=0.01", lambda q, c: gaps_v2(q, c, 0.01)),
                     ("v2 alpha=0.001", lambda q, c: gaps_v2(q, c, 0.001))]:
        ins = oos = fr = fa = 0; fr_ids, fa_ids, topic = [], [], []
        for q, crop, sim in rows:
            g = fn(q["question"], crop)
            refused = has_unsupported_crop(q["question"]) or bool(g) or sim < config.SIMILARITY_THRESHOLD
            if g: topic.append(f"{q['id']}{'*' if q['type'] == 'in_scope' else ''}")
            if q["type"] == "in_scope":
                ins += 1; fr += refused; fr_ids += [q["id"]] if refused else []
            else:
                oos += 1; fa += not refused; fa_ids += [q["id"]] if not refused else []
        print(f"{split:<4} {name:<16} wrongly refused {fr}/{ins} {fr_ids}  wrongly passed {fa}/{oos} {fa_ids}  topic-gap fired on {topic} (* = real question)")
