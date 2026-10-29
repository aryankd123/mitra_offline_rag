"""FastAPI service (design Stage 6): GET / (static page), POST /ask, GET /health.

Run from the repo root:
    python -m src.api          # http://127.0.0.1:8000 ; API docs at /docs
"""
import threading
import time
from typing import Literal

import httpx
import ollama
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import config
from src import netguard
from src.answer import answer_question
from src.store import get_collection

if config.OFFLINE_GUARD:
    netguard.install()

app = FastAPI(title="Mitra Offline RAG", version=config.PROMPT_VERSION)

# One generation at a time: a single local model serialises work anyway (design §11), and the
# embedding cache's sqlite connection is shared across worker threads.
_answer_lock = threading.Lock()


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    crop: Literal["potato", "rice", "wheat"] | None = None


class Source(BaseModel):
    ref: int
    doc_id: str
    page: int
    year: int
    similarity: float


class AskResponse(BaseModel):
    answer: str
    gated: bool
    gate_reason: str | None
    gate_detail: str | None
    top_similarity: float
    crop_used: str | None
    crop_note: str | None
    sources: list[Source]
    generator: str
    prompt_version: str
    timings_ms: dict[str, float]


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(config.STATIC_DIR / "index.html")


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    t0 = time.perf_counter()
    try:
        with _answer_lock:
            res = answer_question(req.question.strip(), crop=req.crop)
    except (httpx.ConnectError, ConnectionError):  # ollama client raises either, depending on the call
        raise HTTPException(503, "Cannot reach Ollama. Start it with `ollama serve` or the Ollama app.")
    except RuntimeError as e:  # index built with a different config (src/store.py)
        raise HTTPException(503, str(e))
    t = res["timings"]
    return AskResponse(
        answer=res["answer"],
        gated=res["gated"],
        gate_reason=res["gate_reason"],
        gate_detail=res["gate_detail"],
        top_similarity=res["top_similarity"],
        crop_used=res["crop_used"],
        crop_note=res["crop_note"],
        sources=res["sources"],
        generator=res["generator"],
        prompt_version=res["prompt_version"],
        timings_ms={
            "retrieve": round(t["retrieve_s"] * 1000, 1),
            "generate": round(t["generate_s"] * 1000, 1),
            "total": round((time.perf_counter() - t0) * 1000, 1),
        },
    )


@app.get("/health")
def health():
    checks = {"offline_guard": {"installed": netguard.installed(), "blocked": netguard.attempts()}}

    try:
        names = {m.model for m in ollama.list().models}
        wanted = [config.EMBED_MODEL, config.GENERATOR_MODEL]
        missing = [w for w in wanted if w not in names and f"{w}:latest" not in names]
        checks["ollama"] = {"ok": not missing, "missing_models": missing}
    except (httpx.ConnectError, ConnectionError) as e:
        checks["ollama"] = {"ok": False, "error": str(e)}

    try:
        col = get_collection()
        checks["index"] = {"ok": col.count() > 0, "chunks": col.count(), "metadata": col.metadata}
    except Exception as e:  # missing collection or config mismatch
        checks["index"] = {"ok": False, "error": str(e)}

    ok = checks["ollama"]["ok"] and checks["index"]["ok"] and not checks["offline_guard"]["blocked"]
    return {
        "status": "ok" if ok else "degraded",
        "generator": config.GENERATOR_MODEL,
        "embed_model": config.EMBED_MODEL,
        "top_k": config.TOP_K,
        "threshold": config.SIMILARITY_THRESHOLD,
        **checks,
    }


def main():
    uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)


if __name__ == "__main__":
    main()
