"""Load PDFs, clean boilerplate, split into chunks with stable IDs (ported from 05_evaluation)."""
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import config

KINDS = {"brief", "bulletin", "manual", "article", "guideline", "leaflet"}


def norm_text(text, join_hyphen_linebreaks=False):
    """Same normalisation for phrases, pages and chunks (used by the eval hit rule)."""
    s = unicodedata.normalize("NFKC", text)
    if join_hyphen_linebreaks:
        s = re.sub(r"[-‐‑‒–—−]\s*\n\s*", "", s)
    s = s.lower()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = re.sub(r"\s+%", "%", s)
    return " ".join(s.split())


def meta_from_name(path):
    crop, topic, org, year, kind = path.stem.split("_")
    assert kind in KINDS, f"unexpected kind {kind!r} in {path.name}"
    return {"doc_id": path.stem, "crop": crop, "topic": topic, "org": org, "year": int(year), "kind": kind}


def load_and_clean_corpus(raw_dir=config.RAW_DIR):
    """One Document per PDF page (1-based page numbers), with per-document boilerplate lines removed."""
    pages = []
    for p in sorted(Path(raw_dir).glob("*.pdf")):
        with pymupdf.open(str(p)) as pdf:
            for i, page in enumerate(pdf):
                meta = meta_from_name(p)
                meta.update({"source": p.name, "page": i + 1})
                pages.append(Document(page_content=page.get_text(), metadata=meta))

    by_doc = defaultdict(list)
    for d in pages:
        by_doc[d.metadata["doc_id"]].append(d)

    # Boilerplate = line on >= max(5, 50% of the doc's pages) and length >= 10 (D-24)
    for doc_pages in by_doc.values():
        counts = Counter(
            l.strip() for d in doc_pages
            for l in set(d.page_content.splitlines()) if l.strip()
        )
        cutoff = max(5, 0.5 * len(doc_pages))
        boiler = {l for l, n in counts.items() if n >= cutoff and len(l) >= 10}
        for d in doc_pages:
            text = d.page_content.replace("", "•")
            d.page_content = "\n".join(l for l in text.splitlines() if l.strip() not in boiler)
    return pages


def is_reference_chunk_only(text):
    """Heuristic for bibliography chunks (5B-3b): numbered author entries + many years, or many years + journal markers."""
    t_low = text.lower()
    numbered_refs = len(re.findall(r"(?:^|\n)\s*\d{1,2}\.\s+[A-Z][a-z]+", text))
    years = len(re.findall(r"\b(19\d\d|20\d\d)\b", text))
    return (numbered_refs >= 3 and years >= 3) or (years >= 8 and ("pp." in t_low or "journal" in t_low))


def build_chunks_with_ids(pages_list, chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP,
                          min_len=config.MIN_CHUNK_LEN, drop_refs=config.DROP_REFERENCE_CHUNKS, separators=None):
    """Split per page (chunks never cross pages) and assign IDs `doc_id:p<page>:c<n>`.

    n counts only the chunks that survive filtering (same as 05_evaluation). Note: gold_chunk_ids in
    questions.csv were written from the unfiltered 1000/100 chunks, so the eval hit rule uses
    page + answer phrase, not chunk IDs.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=separators or ["\n\n", "\n", " ", ""],
    )
    seen = Counter()
    chunks_out = []
    for c in splitter.split_documents(pages_list):
        if len(c.page_content.strip()) < min_len:
            continue
        if drop_refs and is_reference_chunk_only(c.page_content):
            continue
        key = (c.metadata["doc_id"], int(c.metadata["page"]))
        c.metadata = dict(c.metadata)
        c.metadata["chunk_id"] = f"{key[0]}:p{key[1]}:c{seen[key]}"
        seen[key] += 1
        chunks_out.append(c)
    ids = [c.metadata["chunk_id"] for c in chunks_out]
    assert len(ids) == len(set(ids)), "duplicate chunk IDs"
    return chunks_out
