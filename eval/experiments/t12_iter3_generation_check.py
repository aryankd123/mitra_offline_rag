"""T12 End-to-end answers for the dev questions the Iteration 3 documents touch (30 Oct)

Purpose: retrieval and gate numbers (t11) don't show what the user sees. This runs gemma3:4b on
  - the 17 new in-scope dev questions (q44 + q69-q94): can the model answer from the new articles and OCR text?
  - q45, q53: refused in Iteration 2, now pass the gate (q45 only via an off-topic "first irrigation" chunk)
  - q46, q47, q48: out of scope but now pass the gate: does the model refuse on its own?
and writes eval/results/answers_iter3_dev_touched.md for grading by hand (checkboxes).

Result (E-32, test 54): in scope 0/19 refused; expected phrase in 9/19 (automatic). First read by hand: 13/19
give the asked fact (q69, q76, q91, q94 worded differently); 6 wrong: q45, q71, q79, q85, q89 answered from the
wrong chunks after retrieval missed (gold rank 12-49), none refused; q78 read the wrong table row. q87 cited
"[13]", an OCR list number. Out of scope: q47, q48 refused by the model; q46 (rice diseases) answered about
weedy rice. Generation p50 88 s; 4 answers took 490-765 s (cause not measured).
Outcome: Failed as a safety net. When retrieval misses, gemma3:4b answers with nearby facts instead of refusing.

Run from the repo root (Ollama running): python eval/experiments/t12_iter3_generation_check.py
"""
import sys
sys.path.insert(0, ".")
import config
from eval.run_eval import load_questions, write_answers

IDS = {"q44", "q45", "q53", "q46", "q47", "q48"}
qs = [q for q in load_questions("dev") if q["id"] in IDS or int(q["id"][1:]) >= 69]
print(f"{len(qs)} questions")
write_answers("dev (Iteration 3 touched)", qs, config.ROOT / "eval" / "results" / "answers_iter3_dev_touched.md")
