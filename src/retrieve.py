"""Top-k retrieval: exact cosine search over the vectors stored in Chroma (design R6, E-17).

Chroma stays the store (persistence, IDs, metadata, upserts). Its HNSW index is approximate and missed the
true nearest chunk in 2 of 3 runs for one dev question, so search is done exactly in NumPy: at 595 chunks
that is one 595 x 768 matrix product. Revisit if the corpus grows past ~100k chunks.
Restart the process after `python -m src.ingest` so the in-memory copy is reloaded.
"""
import numpy as np

import config
from src.embed import CachedEmbedder
from src.store import get_collection

_embedder = None
_index = None  # ids, unit vectors, documents, metadatas, crop per row


def _resources():
    # Loaded once per process; get_collection() checks the index matches config (D-35)
    global _embedder, _index
    if _index is None:
        got = get_collection().get(include=["embeddings", "documents", "metadatas"])
        E = np.asarray(got["embeddings"], dtype=np.float64)
        E /= np.clip(np.linalg.norm(E, axis=1, keepdims=True), 1e-12, None)
        _index = {
            "ids": got["ids"], "E": E, "docs": got["documents"], "metas": got["metadatas"],
            "crops": np.array([m["crop"] for m in got["metadatas"]]),
        }
        _embedder = CachedEmbedder()
    return _embedder, _index


def retrieve(question, k=config.TOP_K, crop=None):
    """Return up to k chunks as dicts, highest cosine similarity first."""
    embedder, ix = _resources()
    sims = ix["E"] @ embedder.embed_query(question)
    if crop:
        sims = np.where(ix["crops"] == crop, sims, -np.inf)
    order = [i for i in np.argsort(-sims, kind="stable")[:k] if np.isfinite(sims[i])]
    return [
        {
            "id": ix["ids"][i],
            "text": ix["docs"][i],
            "doc_id": ix["metas"][i]["doc_id"],
            "page": int(ix["metas"][i]["page"]),
            "year": int(ix["metas"][i]["year"]),
            "similarity": round(float(sims[i]), 4),
        }
        for i in order
    ]
