"""Crop routing + three-signal refusal gate + prompt v3 + generation (ported from 04_generation / 05_evaluation)."""
import re
import time

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

import config
from src.coverage import topic_gaps
from src.retrieve import retrieve

SYSTEM_PROMPT_V3 = (
    "You are an offline agricultural assistant for the MITRA rover.\n"
    "Rules:\n"
    "1. Answer the question in 1 to 3 complete sentences using ONLY the relevant passage(s) from the Context.\n"
    "2. Ignore any Context passages that do not help answer the question.\n"
    "3. Cite the passage number in square brackets like [1] or [2] at the end of every sentence.\n"
    "4. If two passages give different numbers or timings for the same thing, state both versions with their citations.\n"
    "5. Never invent numbers, doses, or dates. If none of the passages answer the question, output only: "
    "I could not find this in my documents.\n\n"
    "Example format:\n"
    "The recommended seed rate is 35-40 kg/ha when sowing in rows 20 cm apart [1]. "
    "If a mechanical power weeder is used, rows should be spaced 25 cm apart [1]."
)

_llm = None


def get_llm():
    global _llm
    if _llm is None:
        # keep_alive: a 4B model takes seconds to load, so keep it in memory between questions
        _llm = ChatOllama(model=config.GENERATOR_MODEL, temperature=config.TEMPERATURE, keep_alive=config.KEEP_ALIVE)
    return _llm


def has_unsupported_crop(question):
    """Second gate signal (5A-6): names a crop we have no documents for, and no crop we do."""
    words = set(re.findall(r"\b[a-z]+\b", question.lower()))
    return bool(words & config.UNSUPPORTED_CROPS) and not bool(words & config.SUPPORTED_CROPS)


def route(question, crop=None):
    """Pick the crop to search: the one named in the question wins over the UI filter (E-15).

    Returns (crop_used, note); note explains an override. Two crops named -> no routing (search all).
    """
    if not config.CROP_ROUTING:
        return crop, None
    named = {config.CROP_SYNONYMS[w] for w in re.findall(r"\b[a-z]+\b", question.lower()) if w in config.CROP_SYNONYMS}
    if len(named) != 1:
        return crop, None
    named = named.pop()
    note = (f"Searched {named} documents: the question names {named}, the crop filter said {crop}."
            if crop and crop != named else None)
    return named, note


def gate(question, top_sim, crop=None):
    """(None, None) if we may answer, otherwise (reason, detail) for the refusal.

    Three signals: unsupported crop named (5A-6), topic not covered for the asked crop (E-16),
    best-chunk similarity below the threshold (D-42).
    """
    if has_unsupported_crop(question):
        return "unsupported_crop", None
    if config.TOPIC_GAP_ALPHA:
        gaps = topic_gaps(question, crop)
        if gaps:
            return "topic_not_covered", f"The {crop} documents never mention: {', '.join(gaps)}."
    if top_sim < config.SIMILARITY_THRESHOLD:
        return "low_similarity", None
    return None, None


def tidy(ans):
    """Join lines and drop list markers ("[1] ", "3. ") that small models put at line starts."""
    lines = [l.strip() for l in ans.splitlines() if l.strip()]
    # gemma3:1b sometimes echoes the refusal sentence on line 1 and then answers (see 5A-5)
    if len(lines) > 1 and config.REFUSAL_SENTENCE.lower() in lines[0].lower():
        lines = lines[1:]
    return " ".join(re.sub(r"^(\[\d+\]|\d+\.)\s+", "", l) for l in lines)


def format_context(chunks):
    return "\n\n".join(
        f"[{idx}] ({c['doc_id']}, page {c['page']})\n{c['text'].strip()}"
        for idx, c in enumerate(chunks, start=1)
    )


def format_programmatic_sources(sources, gated=False):
    header = ("Refused before generation; closest passages found:" if gated
              else "Retrieved sources: the model was shown these passages:")
    lines = [header]
    for s in sources:
        lines.append(f"  [{s['ref']}] {s['doc_id']}, page {s['page']} (similarity={s['similarity']:.4f})")
    return "\n".join(lines)


def answer_question(question, k=config.TOP_K, crop=None):
    crop_used, crop_note = route(question, crop)
    t0 = time.perf_counter()
    chunks = retrieve(question, k=k, crop=crop_used)
    t_retrieve = time.perf_counter() - t0

    top_sim = chunks[0]["similarity"] if chunks else 0.0
    sources = [
        {"ref": i + 1, "doc_id": c["doc_id"], "page": c["page"], "year": c["year"], "similarity": c["similarity"]}
        for i, c in enumerate(chunks)
    ]
    result = {
        "prompt_version": config.PROMPT_VERSION,
        "generator": config.GENERATOR_MODEL,
        "sources": sources,
        "top_similarity": top_sim,
        "crop_used": crop_used,
        "crop_note": crop_note,
    }

    reason, detail = gate(question, top_sim, crop_used)
    if reason:
        return {**result, "answer": config.REFUSAL_SENTENCE, "gated": True, "gate_reason": reason, "gate_detail": detail,
                "sources_block": format_programmatic_sources(sources, gated=True),
                "timings": {"retrieve_s": round(t_retrieve, 3), "generate_s": 0.0}}

    user_prompt = (
        f"Context:\n{format_context(chunks)}\n\n"
        f"Question: {question}\n"
        "Instruction: Write 1 to 3 complete sentences answering the Question using ONLY the relevant "
        "Context passage(s) above, and put [1], [2], etc. at the end of every sentence.\n"
        "Answer:"
    )
    t1 = time.perf_counter()
    response = get_llm().invoke([SystemMessage(content=SYSTEM_PROMPT_V3), HumanMessage(content=user_prompt)])
    t_generate = time.perf_counter() - t1

    return {**result, "answer": tidy(response.content), "gated": False, "gate_reason": None, "gate_detail": None,
            "sources_block": format_programmatic_sources(sources),
            "timings": {"retrieve_s": round(t_retrieve, 3), "generate_s": round(t_generate, 3)}}
