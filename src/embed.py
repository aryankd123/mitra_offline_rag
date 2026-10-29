"""Ollama embeddings with an on-disk sqlite cache (ported from 05_evaluation)."""
import hashlib
import json
import sqlite3

import numpy as np
from langchain_ollama import OllamaEmbeddings

import config


class CachedEmbedder:
    """Cache key = sha256(model, prefix, text); returns unit-length float64 rows."""

    def __init__(self, model_name=config.EMBED_MODEL, doc_prefix=config.DOC_PREFIX,
                 query_prefix=config.QUERY_PREFIX, cache_path=config.CACHE_PATH):
        self.model_name = model_name
        self.doc_prefix = doc_prefix
        self.query_prefix = query_prefix
        self.emb = OllamaEmbeddings(model=model_name)
        # The API calls this from worker threads, one request at a time (lock in src/api.py)
        self.conn = sqlite3.connect(str(cache_path), check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS embeddings (cache_key TEXT PRIMARY KEY, vec_json TEXT NOT NULL)")
        self.conn.commit()

    def _key(self, prefix, text):
        return hashlib.sha256(f"{self.model_name}\0{prefix}\0{text}".encode("utf-8")).hexdigest()

    def embed_texts(self, texts, is_query=False, batch_size=32):
        prefix = self.query_prefix if is_query else self.doc_prefix
        keys = [self._key(prefix, t) for t in texts]
        results = [None] * len(texts)
        missing = []
        cur = self.conn.cursor()
        for idx, k in enumerate(keys):
            row = cur.execute("SELECT vec_json FROM embeddings WHERE cache_key = ?", (k,)).fetchone()
            if row is not None:
                results[idx] = json.loads(row[0])
            else:
                missing.append(idx)
        for s in range(0, len(missing), batch_size):
            b_idx = missing[s:s + batch_size]
            b_in = [prefix + texts[i] for i in b_idx]
            vecs = [self.emb.embed_query(b_in[0])] if (is_query and len(b_in) == 1) else self.emb.embed_documents(b_in)
            for i, v in zip(b_idx, vecs):
                results[i] = v
                cur.execute("INSERT OR REPLACE INTO embeddings (cache_key, vec_json) VALUES (?, ?)", (keys[i], json.dumps(v)))
            self.conn.commit()
        mat = np.array(results, dtype=np.float64)
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        return mat / np.clip(norms, 1e-12, None)

    def embed_query(self, text):
        return self.embed_texts([text], is_query=True)[0]
