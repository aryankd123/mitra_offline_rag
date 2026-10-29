"""Chroma client and collection access, shared by ingest and retrieve."""
import chromadb
from chromadb.config import Settings

import config


def collection_metadata():
    """What the index was built with (D-35). Queries refuse to run if the embedder differs."""
    return {
        "embed_model": config.EMBED_MODEL,
        "dim": config.EMBED_DIM,
        "doc_prefix": config.DOC_PREFIX or "none",
        "query_prefix": config.QUERY_PREFIX or "none",
        "chunk_size": config.CHUNK_SIZE,
        "chunk_overlap": config.CHUNK_OVERLAP,
        "min_chunk_len": config.MIN_CHUNK_LEN,
        "drop_reference_chunks": config.DROP_REFERENCE_CHUNKS,
    }


def get_client():
    return chromadb.PersistentClient(path=str(config.CHROMA_PATH),
                                     settings=Settings(anonymized_telemetry=False))


def get_collection(client=None):
    """Open the existing index and check it was built with the current config."""
    col = (client or get_client()).get_collection(config.COLLECTION)
    expected = collection_metadata()
    stored = col.metadata or {}
    diffs = {k: (stored.get(k), v) for k, v in expected.items() if stored.get(k) != v}
    if diffs:
        raise RuntimeError(
            f"Index {config.COLLECTION!r} was built with a different config (stored, current): {diffs}. "
            "Run `python -m src.ingest --rebuild`."
        )
    return col
