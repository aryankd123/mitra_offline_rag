"""Build or update the Chroma index: PDFs -> clean pages -> chunks -> embeddings -> upsert.

Usage:
    python -m src.ingest            # add/update chunks, remove chunks that no longer exist
    python -m src.ingest --rebuild  # drop the collection and build it again (needed after a config change)
"""
import argparse
import time

import config
from src.corpus import build_chunks_with_ids, load_and_clean_corpus
from src.embed import CachedEmbedder
from src.store import collection_metadata, get_client, get_collection


def ingest(rebuild=False, batch_size=128):
    client = get_client()
    if rebuild and config.COLLECTION in [c.name for c in client.list_collections()]:
        client.delete_collection(config.COLLECTION)
        print(f"Deleted collection {config.COLLECTION!r}")

    if config.COLLECTION in [c.name for c in client.list_collections()]:
        col = get_collection(client)  # raises if built with a different config
    else:
        col = client.create_collection(
            config.COLLECTION,
            configuration={"hnsw": {"space": "cosine"}},  # default is squared L2 (D-32)
            metadata=collection_metadata(),
        )

    t0 = time.perf_counter()
    pages = load_and_clean_corpus()
    chunks = build_chunks_with_ids(pages)
    print(f"{len(pages)} pages -> {len(chunks)} chunks ({time.perf_counter() - t0:.1f}s)")

    t0 = time.perf_counter()
    texts = [c.page_content for c in chunks]
    V = CachedEmbedder().embed_texts(texts, is_query=False)
    assert V.shape[1] == config.EMBED_DIM, f"embedding dim {V.shape[1]} != {config.EMBED_DIM}"
    print(f"Embedded {len(texts)} chunks ({time.perf_counter() - t0:.1f}s, cached vectors reused)")

    ids = [c.metadata["chunk_id"] for c in chunks]
    for s in range(0, len(ids), batch_size):
        col.upsert(
            ids=ids[s:s + batch_size],
            embeddings=V[s:s + batch_size].tolist(),
            documents=texts[s:s + batch_size],
            metadatas=[c.metadata for c in chunks[s:s + batch_size]],
        )

    stale = set(col.get(include=[])["ids"]) - set(ids)
    if stale:
        col.delete(ids=sorted(stale))
        print(f"Removed {len(stale)} stale chunks")

    print(f"Collection {config.COLLECTION!r}: {col.count()} chunks at {config.CHROMA_PATH}")
    return col


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rebuild", action="store_true", help="delete and rebuild the collection")
    ingest(rebuild=ap.parse_args().rebuild)
