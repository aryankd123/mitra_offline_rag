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
