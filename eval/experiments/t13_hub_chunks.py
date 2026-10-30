"""T13 Are some new chunks "hubs" that rank high for almost any question of their crop? (30 Oct)

Purpose: t11 showed the weedy-rice leaflet at rank 1 for rice questions it can't answer (stem borer, rice
diseases, brine). A hub is a chunk that lands in many questions' top-k regardless of topic; it pushes gold
chunks down and lifts the top similarity the gate looks at. For each document: share of the crop's chunks vs
share of top-5 slots across the dev questions routed to that crop (ratio > 1 = over-represented), the chunks
that appear most often, and how many of those slots were for questions labelled with a different document.

Result (E-31, test 53): rice: weedy-rice leaflet (OCR) 15.8% of chunks but 28.6% of top-5 slots (1.8x),
24 of 30 slots off-label; herbicide leaflet (OCR) 1.3x, its intro chunk p1:c0 in 9 of 21 top-5 lists.
Wheat: both Phalaris articles ~1.8x, but mostly on Phalaris questions (dev topic mix, not hubs).
Outcome: Mixed. Overview chunks act as hubs; this test can't tell overview wording from OCR noise.

Run from the repo root: python eval/experiments/t13_hub_chunks.py
"""
import sys
from collections import Counter, defaultdict
sys.path.insert(0, ".")
from src.answer import route
from src.retrieve import _resources, retrieve
from eval.run_eval import load_questions

_, ix = _resources()
chunks_per_doc = Counter(m["doc_id"] for m in ix["metas"])
crops_of_doc = {m["doc_id"]: set(m["crop"].split("-")) for m in ix["metas"]}

slots = defaultdict(Counter)       # crop -> doc -> top-5 slots
off_label = defaultdict(Counter)   # crop -> doc -> slots on questions labelled with another doc (or out of scope)
chunk_hits = Counter()
n_q = Counter()
for q in load_questions("dev"):
    crop = route(q["question"])[0]
    if not crop:
        continue
    n_q[crop] += 1
    for c in retrieve(q["question"], k=5, crop=crop):
        slots[crop][c["doc_id"]] += 1
        off_label[crop][c["doc_id"]] += c["doc_id"] != q["doc_id"]
        chunk_hits[c["id"]] += 1

for crop in sorted(slots):
    total_chunks = sum(n for d, n in chunks_per_doc.items() if crop in crops_of_doc[d])
    total_slots = sum(slots[crop].values())
    print(f"\n{crop}: {n_q[crop]} dev questions, {total_chunks} chunks, {total_slots} top-5 slots")
    for doc, s in slots[crop].most_common():
        share_c, share_s = chunks_per_doc[doc] / total_chunks, s / total_slots
        print(f"  {doc[:52]:<52} chunks {share_c:5.1%}  slots {share_s:5.1%}  ratio {share_s / share_c:4.1f}"
              f"  off-label {off_label[crop][doc]}/{s}")

print("\nChunks in the most dev top-5 lists:")
for cid, n in chunk_hits.most_common(8):
    print(f"  {n:>2}  {cid}")
