"""T06 gemma3:1b as a yes/no answerability judge, and prompt v4 (29 Oct, E-16)

Purpose: let the model decide whether the passages answer the question.
Result: judge said YES to all 14, including 3 unanswerable, at 24-36 s each (FAILED).
Prompt v4 refused 1 of 3 unanswerable but degraded answers and invented 'Opaline, Silica, Lignin' (FAILED).

Run from the repo root: python eval/experiments/t06_llm_judge_and_prompt_v4.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import re, sys, time
sys.path.insert(0, ".")
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from src.retrieve import retrieve
from src.answer import format_context
from eval.run_eval import load_questions

CROPS = {"rice": "rice", "paddy": "rice", "wheat": "wheat", "gehun": "wheat", "potato": "potato", "potatoes": "potato", "aloo": "potato"}
def crop_of(q):
    f = {CROPS[w] for w in re.findall(r"[a-z]+", q.lower()) if w in CROPS}
    return f.pop() if len(f) == 1 else None

V4 = ("You are an offline agricultural assistant for farmers.\n"
      "Rules:\n"
      "1. First check whether the Context passages answer the Question for the crop and topic asked. If they do not "
      "(for example they are about a different crop, pest, disease or practice), output only: I could not find this in my documents.\n"
      "2. Otherwise answer in 1 to 3 plain sentences using only facts stated in the passages.\n"
      "3. End every sentence with the number of the passage it comes from, like [1] or [2].\n"
      "4. If two passages give different numbers or timings for the same thing, give both with their citations.\n"
      "5. Never add numbers, doses, dates or conditions that are not in the passages. Do not start with phrases like 'The context states'.\n\n"
      "Format example (placeholders, not facts):\n<fact from a passage> [1]. <second fact> [2].")
JUDGE = ("Question: {q}\n\nPassages:\n{ctx}\n\nDo these passages contain the information needed to answer this question "
         "for the crop and topic asked? Reply with exactly one word: YES or NO.")

llm = ChatOllama(model="gemma3:1b", temperature=0)
ids = ["q42", "q46", "q47", "q17", "q5", "q49", "q12", "q8", "q4", "q22", "q58", "q54", "q13", "q50"]
qs = [q for q in load_questions("dev") if q["id"] in ids]
for q in qs:
    ch = retrieve(q["question"], k=5, crop=crop_of(q["question"]))
    ctx = format_context(ch)
    t = time.perf_counter()
    j = llm.invoke([HumanMessage(content=JUDGE.format(q=q["question"], ctx=ctx))]).content.strip()
    tj = time.perf_counter() - t
    t = time.perf_counter()
    a = llm.invoke([SystemMessage(content=V4), HumanMessage(content=f"Context:\n{ctx}\n\nQuestion: {q['question']}\nAnswer:")]).content.strip()
    ta = time.perf_counter() - t
    print(f"\n{q['id']} {q['type'][:6]} sim={ch[0]['similarity']:.3f} | judge={j[:12]!r} ({tj:.1f}s) | v4 ({ta:.1f}s):\n   {a[:350]}", flush=True)
