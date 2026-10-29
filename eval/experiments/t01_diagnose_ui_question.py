"""T01 Diagnose the weak web-UI answer (29 Oct, E-15)

Purpose: find why 'what do you know about the diseases in rice crops...' was answered.
Checks the question under each crop filter, whether disease terms exist in the corpus, and 6 probe
questions on covered crops with uncovered topics.
Result: no rice chunk mentions 'disease'; the old gate answered 4 of 7 probes (FAILED: gate too weak).

Run from the repo root: python eval/experiments/t01_diagnose_ui_question.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import re, csv, sys
sys.path.insert(0, ".")
import config
from src.retrieve import retrieve
from src.answer import has_unsupported_crop
import config
def gate_reason(q, sim):  # the gate as it was before Iteration 2: crop guard + threshold only
    if has_unsupported_crop(q): return "unsupported_crop"
    return "low_similarity" if sim < config.SIMILARITY_THRESHOLD else None
from src.store import get_collection
from src.corpus import norm_text

col = get_collection()
allc = col.get(include=["documents", "metadatas"])
texts = [norm_text(t) for t in allc["documents"]]

def show(q, crop=None):
    ch = retrieve(q, k=5, crop=crop)
    r = gate_reason(q, ch[0]["similarity"])
    print(f"\nQ: {q!r} crop={crop} -> {'REFUSE '+r if r else 'ANSWER'}")
    for c in ch:
        print(f"   {c['similarity']:.4f} {c['doc_id'][:40]:<40} p{c['page']}")

UQ = "Ok what do you know about the diseases in rice crops and how would you prevent them"
for crop in [None, "potato", "rice"]:
    show(UQ, crop)

print("\n=== corpus term check (chunks containing term) ===")
for t in ["blast", "sheath blight", "brown spot", "bacterial leaf blight", "phalaris", "irrigation", "disease"]:
    hits = [m["doc_id"].split("_")[0] for tt, m in zip(texts, allc["metadatas"]) if re.search(r"\b" + re.escape(t) + r"\b", tt)]
    from collections import Counter
    print(f"  {t!r}: {Counter(hits)}")

PROBES = [
    "What fungicide controls blast disease in rice?",
    "How do I manage sheath blight in paddy?",
    "How do I control brown spot disease of rice?",
    "Which herbicide controls Phalaris minor in wheat?",
    "What is the irrigation schedule for wheat?",
    "What are the symptoms of bacterial leaf blight in rice?",
]
print("\n=== same-crop, uncovered-topic probes ===")
for q in PROBES:
    show(q)
