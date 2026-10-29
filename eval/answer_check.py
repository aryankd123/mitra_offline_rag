"""Score a generated answers file automatically (Iteration 2).

    python -m eval.answer_check eval/results/answers_7_iter2_4b_dev.md [other_answers.md ...]

For each answered in-scope question: does the answer contain an expected answer phrase (same normalisation as the
retrieval hit rule)? Also flags meta phrases ("the context states"), leaked prompt-example text and missing [n]
citations. A phrase match is a proxy for correctness, not a faithfulness grade: the manual checkboxes stay.
"""
import re
import sys

from eval.run_eval import load_questions
from src.corpus import norm_text

LEAKS = ["20 cm apart", "35-40 kg/ha"]  # content of the prompt v3 format example


def parse(path):
    text = open(path, encoding="utf-8").read()
    out = {}
    for block in re.split(r"\n## ", text)[1:]:
        qid = block.split()[0]
        m = re.search(r"\*\*A:\*\* (.*?)\n\n```", block, re.S)
        if m:
            out[qid] = m.group(1).strip()
    return out


def score(path, qs):
    answers = parse(path)
    rows = []
    for q in qs:
        a = answers.get(q["id"])
        if q["type"] != "in_scope" or a is None or a.lower().startswith("i could not find"):
            continue
        an = norm_text(a)
        hits = [ph in an for ph in q["answer_phrases"]]
        rows.append({
            "id": q["id"],
            "phrase": any(hits) if q["match"] == "any" else all(hits),
            "cited": bool(re.search(r"\[\d\]", a)),
            "meta": bool(re.search(r"\b(the )?(context|text|passage)s? (states?|says|mentions|highlights|suggests|describes)", a, re.I)),
            "leak": any(l in an for l in LEAKS),
        })
    n = len(rows)
    print(f"{path}: {n} answered in-scope")
    for k in ["phrase", "cited", "meta", "leak"]:
        print(f"  {k:<7} {sum(r[k] for r in rows)}/{n}  {[r['id'] for r in rows if r[k] != (k in ('phrase', 'cited'))]}")
    return {r["id"]: r for r in rows}


if __name__ == "__main__":
    qs = load_questions("all")
    results = [score(p, qs) for p in sys.argv[1:]]
    if len(results) == 2:
        common = sorted(set(results[0]) & set(results[1]), key=lambda s: int(s[1:]))
        a = sum(results[0][i]["phrase"] for i in common)
        b = sum(results[1][i]["phrase"] for i in common)
        print(f"on the {len(common)} questions both answered: answer phrase present {a} vs {b}")
