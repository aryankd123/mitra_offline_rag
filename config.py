"""Frozen configuration for MITRA Offline RAG (selected from Stage 5 dev experiments).

Machine-specific settings can be overridden with environment variables (design R12), e.g. for a fast CPU demo:
    $env:MITRA_GENERATOR_MODEL = "gemma3:1b"
Measured parameters (chunking, k, threshold) are constants on purpose: changing them needs a new eval run.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("MITRA_DATA_DIR", ROOT / "data"))
RAW_DIR = DATA_DIR / "raw"
CHROMA_PATH = DATA_DIR / "chroma" / "mitra"
CACHE_PATH = DATA_DIR / "embed_cache.sqlite"
QUESTIONS_CSV = ROOT / "eval" / "questions.csv"
EXPERIMENTS_CSV = ROOT / "eval" / "results" / "experiments.csv"
STATIC_DIR = ROOT / "static"
COLLECTION = "mitra_chunks"

EMBED_MODEL = "nomic-embed-text"
EMBED_DIM = 768
DOC_PREFIX = ""
QUERY_PREFIX = ""

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
MIN_CHUNK_LEN = 50
DROP_REFERENCE_CHUNKS = True

# OCR for pages with no text layer (src/ocr.py, Iteration 3)
OCR_ENABLED = True
OCR_MIN_CHARS = 20  # a page with fewer extracted characters than this is treated as an image page
OCR_DPI = 200       # 150 and 300 were tested too (test 45); 200 read all reference sentences
OCR_USE_CLS = False  # text-angle classifier off: it flipped a line upside down and lost others (test 46)
OCR_CACHE_DIR = DATA_DIR / "ocr_cache"

TOP_K = 5
SIMILARITY_THRESHOLD = 0.725

# Cross-encoder reranking (src/rerank.py, Iteration 4, D-64). Files are downloaded once with
# `python -m src.rerank --download` into MODELS_DIR, then loaded from disk only.
MODELS_DIR = DATA_DIR / "models"
RERANK_CANDIDATES = 30  # embedding shortlist to re-score; Recall@30 = 0.938 on dev (test 55)
RERANK_MODELS = {  # name -> Hugging Face repo, pinned revision, ONNX file, gate threshold chosen on dev (test 57)
    "minilm-l6": {"repo": "cross-encoder/ms-marco-MiniLM-L6-v2",
                  "revision": "233902d25c440f23af6f7d6e94d2946bac0bee0a", "onnx": "onnx/model.onnx",
                  "threshold": 0.035},
    "bge-m3-int8": {"repo": "onnx-community/bge-reranker-v2-m3-ONNX",
                    "revision": "6f5ff65298512715a1e669753bc754d2bc8f367b", "onnx": "onnx/model_int8.onnx",
                    "threshold": 0.171},
}
RERANK_MAX_TOKENS = 512  # question + passage, longer pairs are cut from the passage end
# bge chosen by Aryan on 1 Nov (dev: Recall@5 0.917, gate 1/48 wrongly refused, 0/12 wrongly answered; 39 s median
# on this CPU). "minilm-l6" = fast mode (4 s, but rice diseases / stem borer get answers); "" = no reranking.
RERANK_MODEL = os.environ.get("MITRA_RERANK_MODEL", "bge-m3-int8")
# Gate on the best reranker score (0..1) instead of SIMILARITY_THRESHOLD; None = keep the cosine check
RERANK_THRESHOLD = RERANK_MODELS[RERANK_MODEL]["threshold"] if RERANK_MODEL else None

# Word in the question -> crop in the metadata. Routing searches only that crop's chunks (Iteration 2, D-54).
CROP_SYNONYMS = {
    "rice": "rice", "paddy": "rice",
    "wheat": "wheat", "gehun": "wheat",
    "potato": "potato", "potatoes": "potato", "aloo": "potato",
}
CROP_ROUTING = True
TOPIC_GAP_ALPHA = 0.01  # src/coverage.py: flag a word whose absence has < 1% chance; 0 disables the check
SUPPORTED_CROPS = set(CROP_SYNONYMS)
UNSUPPORTED_CROPS = {
    "sesame", "til", "cumin", "jeera", "mango", "blackgram", "urdbean",
    "cotton", "tea", "coffee", "apple", "banana", "citrus", "grapevine",
}

# gemma3:4b chosen 29 Oct (D-55): it refuses uncovered questions itself; 1b never did. "gemma3:1b" for a fast CPU demo.
GENERATOR_MODEL = os.environ.get("MITRA_GENERATOR_MODEL", "gemma3:4b")
KEEP_ALIVE = os.environ.get("MITRA_KEEP_ALIVE", "30m")  # how long Ollama keeps the model loaded after a question
TEMPERATURE = 0
PROMPT_VERSION = "v3"
REFUSAL_SENTENCE = "I could not find this in my documents."

API_HOST = os.environ.get("MITRA_API_HOST", "127.0.0.1")  # localhost only by default
API_PORT = int(os.environ.get("MITRA_API_PORT", "8000"))
OFFLINE_GUARD = os.environ.get("MITRA_OFFLINE_GUARD", "1") == "1"  # block non-loopback connections (src/netguard.py)
