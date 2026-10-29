"""T04 Best-chunk similarity for every eval question (29 Oct)

Purpose: data for the 'similarity overlap' chart in the project book.
Result: 6 of 10 out-of-scope questions score above 0.725 and are stopped only by the crop guard.

Run from the repo root: python eval/experiments/t04_top1_similarity_dump.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import sys; sys.path.insert(0, ".")
from src.retrieve import retrieve
from eval.run_eval import load_questions
for q in load_questions("all"):
    print(f"{q['id']},{q['type']},{retrieve(q['question'], k=1)[0]['similarity']:.4f}")
