"""T03 Does the generator refuse on its own? gemma3:1b vs 4b (29 Oct, E-15f)

Purpose: check whether the model can catch unanswerable questions the gate lets through.
Result: 4b refused the rice-blast question, 1b answered with unrelated herbicide facts; both answered the
bleaching-powder control correctly; 4b took 73-187 s (led to D-55, gemma3:4b).

Run from the repo root: python eval/experiments/t03_generator_refusal_1b_vs_4b.py
Re-runs may differ slightly from the logged result: search became exact (D-58) after this test.
"""
import sys, time
sys.path.insert(0, ".")
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from src.retrieve import retrieve
from src.answer import SYSTEM_PROMPT_V3, format_context

QS = [("Ok what do you know about the diseases in rice crops and how would you prevent them", "rice"),
      ("What fungicide controls blast disease in rice?", "rice"),
      ("What rate of stable bleaching powder per hectare should be applied in furrows at planting time to reduce bacterial wilt in potato?", "potato")]
for model in ["gemma3:4b", "gemma3:1b"]:
    llm = ChatOllama(model=model, temperature=0)
    for q, crop in QS:
        ch = retrieve(q, k=5, crop=crop)
        prompt = (f"Context:\n{format_context(ch)}\n\nQuestion: {q}\nInstruction: Write 1 to 3 complete sentences answering the Question using ONLY the relevant "
                  "Context passage(s) above, and put [1], [2], etc. at the end of every sentence.\nAnswer:")
        t = time.perf_counter()
        out = llm.invoke([SystemMessage(content=SYSTEM_PROMPT_V3), HumanMessage(content=prompt)]).content.strip()
        print(f"\n[{model}] {time.perf_counter()-t:.1f}s  Q: {q[:70]}\n  -> {out[:400]}")
