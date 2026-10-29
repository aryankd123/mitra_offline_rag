"""Check eval/questions.csv against the PDFs (ported from 05_evaluation, cell 0).

    python -m eval.lint_questions

in_scope rows: every answer phrase must be on an expected page AND inside one indexed chunk of that page.
out_of_scope rows: every term after "absent:" in notes must appear on no page (word boundary).
Exit code 1 on any error.
"""
import csv
import re
import sys
from collections import Counter, defaultdict

import config
from src.corpus import build_chunks_with_ids, load_and_clean_corpus, norm_text


def lint(csv_path=config.QUESTIONS_CSV):
    pages = load_and_clean_corpus()
    page_text = {(d.metadata["doc_id"], d.metadata["page"]): norm_text(d.page_content) for d in pages}
    chunk_text = defaultdict(list)
    for c in build_chunks_with_ids(pages):
        chunk_text[(c.metadata["doc_id"], c.metadata["page"])].append(norm_text(c.page_content))

    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    errors, seen, counts = [], set(), Counter()
    for n, r in enumerate(rows, start=2):
        qid, qtype, split = r["id"].strip(), r["type"].strip(), r["split"].strip()
        where = f"row {n} ({qid})"
        if qid in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(qid)
        if split not in {"dev", "test"}:
            errors.append(f"{where}: split {split!r}")
        counts[(split, qtype, r["tag"].strip())] += 1

        doc_id = r["doc_id"].strip()
        exp_pages = [int(p) for p in r["expected_pages"].split(";") if p.strip()]
        phrases = [norm_text(p) for p in r["answer_phrases"].split(";") if p.strip()]

        if qtype == "in_scope":
            if not (doc_id and exp_pages and phrases and r["match"].strip() in {"any", "all"}):
                errors.append(f"{where}: incomplete in_scope fields")
                continue
            for ph in phrases:
                if not any(ph in page_text.get((doc_id, p), "") for p in exp_pages):
                    errors.append(f"{where}: phrase {ph!r} not on pages {exp_pages} of {doc_id}")
                elif not any(ph in t for p in exp_pages for t in chunk_text.get((doc_id, p), [])):
                    errors.append(f"{where}: phrase {ph!r} on the page but cut across chunks")
        elif qtype == "out_of_scope":
            if doc_id or exp_pages or phrases:
                errors.append(f"{where}: out_of_scope row must leave doc_id/pages/phrases empty")
            notes = r["notes"].lower()
            if "absent:" not in notes:
                errors.append(f"{where}: notes need 'absent: term; term'")
                continue
            for term in [norm_text(t) for t in notes.split("absent:", 1)[1].split(";") if t.strip()]:
                pat = re.compile(r"\b" + re.escape(term) + r"\b")
                hits = [f"{d}:p{p}" for (d, p), t in page_text.items() if pat.search(t)]
                if hits:
                    errors.append(f"{where}: absent term {term!r} found on {hits[:3]}")
        else:
            errors.append(f"{where}: type {qtype!r}")

    print("Counts by (split, type, tag):")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    for e in errors:
        print("  [ERROR]", e)
    print(f"{len(rows)} questions, {len(errors)} error(s)")
    return errors


if __name__ == "__main__":
    sys.exit(1 if lint() else 0)
