"""Cross-encoder reranking (Iteration 4, D-64).

Embedding search compares a question vector with passage vectors made separately, so it measures topic, not
"does this passage answer this question". A cross-encoder reads question and passage as one input and returns
one relevance score. It can't be precomputed, so it only re-scores the embedding shortlist.

Runs an ONNX model with onnxruntime and the model's own tokenizer.json (both packages were already installed),
so no PyTorch. Files come from `python -m src.rerank --download` (needs internet once) and are then read from
config.MODELS_DIR only.
"""
import argparse
import json

import numpy as np

import config

_loaded = {}  # model name -> (tokenizer, onnxruntime session, input names)


def _load(name):
    if name not in _loaded:
        import onnxruntime as ort
        from tokenizers import Tokenizer
        folder = config.MODELS_DIR / name
        tok = Tokenizer.from_file(str(folder / "tokenizer.json"))
        tok.enable_truncation(max_length=config.RERANK_MAX_TOKENS)  # pairs: the longer text (the passage) is cut
        pad_id = json.loads((folder / "config.json").read_text(encoding="utf-8"))["pad_token_id"]  # BERT 0, XLM-R 1
        tok.enable_padding(pad_id=pad_id, pad_token=tok.id_to_token(pad_id))
        session = ort.InferenceSession(str(folder / config.RERANK_MODELS[name]["onnx"]),
                                       providers=["CPUExecutionProvider"])
        _loaded[name] = (tok, session, {i.name for i in session.get_inputs()})
    return _loaded[name]


def score(question, passages, model, batch_size=8):
    """Relevance of each passage to the question, 0..1 (sigmoid of the model's single output)."""
    tok, session, inputs = _load(model)
    logits = []
    for start in range(0, len(passages), batch_size):
        enc = tok.encode_batch([(question, p) for p in passages[start:start + batch_size]])
        feed = {"input_ids": np.array([e.ids for e in enc], dtype=np.int64),
                "attention_mask": np.array([e.attention_mask for e in enc], dtype=np.int64)}
        if "token_type_ids" in inputs:  # BERT marks question tokens 0 and passage tokens 1; XLM-RoBERTa has no such input
            feed["token_type_ids"] = np.array([e.type_ids for e in enc], dtype=np.int64)
        logits.extend(session.run(None, feed)[0][:, 0])
    return (1 / (1 + np.exp(-np.array(logits, dtype=np.float64)))).tolist()


def rerank(question, chunks, model, k=config.TOP_K):
    """Re-order retrieve() results by cross-encoder score; adds "rerank_score" to each chunk, returns the best k."""
    scores = score(question, [c["text"] for c in chunks], model)
    for c, s in zip(chunks, scores):
        c["rerank_score"] = round(s, 4)  # rounded for display; the order uses the full value
    order = sorted(range(len(chunks)), key=lambda i: -scores[i])  # stable: ties keep the embedding order
    return [chunks[i] for i in order[:k]]


def download(name):
    """One-time download of a model's ONNX file, tokenizer and config at the pinned revision."""
    from huggingface_hub import hf_hub_download
    spec = config.RERANK_MODELS[name]
    for f in [spec["onnx"], "tokenizer.json", "config.json"]:
        path = hf_hub_download(spec["repo"], f, revision=spec["revision"], local_dir=config.MODELS_DIR / name)
        print("  ", path)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Download a reranker model (needs internet once).")
    ap.add_argument("--download", nargs="+", choices=sorted(config.RERANK_MODELS), required=True)
    for name in ap.parse_args().download:
        print(name)
        download(name)
