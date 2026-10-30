"""T09 OCR for the two scanned rice leaflets with RapidOCR (30 Oct, Iteration 3)

Purpose: the two PDFs in data/pending_ocr/ have no text layer (text was converted to vector outlines), so they
cannot be indexed. Test whether RapidOCR (pip-only, ONNX models bundled, so offline) reads them well enough,
at which resolution, how fast, and with no network access (offline guard on).
Method: render each PDF page with PyMuPDF; each page is a two-page spread, so OCR the left and right halves
separately to keep the reading order; check three reference sentences typed by hand from page 2 of the
herbicide leaflet.

Run from the repo root: python eval/experiments/t09_ocr_rapidocr.py
"""
import difflib, sys, time
sys.path.insert(0, ".")
import numpy as np
import pymupdf
from rapidocr_onnxruntime import RapidOCR
from src import netguard
from src.corpus import norm_text

netguard.install()
PDF = "data/pending_ocr/rice_herbicide-weed-control_nrri_2018_brief.pdf.pdf"
REFS = [
    "Apply granular herbicides by mixing with little wet sand at 10-12 kg ha",
    "Use knapsack sprayer having flat fan nozzle with spray volume of 300 litres ha",
    "sequential application of bispyribac sodium followed by fenoxaprop-p-ethyl shows effective control of both the early and late emergent weeds",
]

def best_ratio(ref, text):
    ref, text = norm_text(ref), norm_text(text)
    if ref in text:
        return 1.0
    n, best = len(ref), 0.0
    for i in range(0, max(1, len(text) - n + 1), 5):
        best = max(best, difflib.SequenceMatcher(None, ref, text[i:i + n]).ratio())
    return best

def ocr_half(engine, img):
    result, _ = engine(img)
    if not result:
        return ""
    # sort boxes top-to-bottom, then left-to-right within a line
    rows = sorted(result, key=lambda r: (round(r[0][0][1] / 12), r[0][0][0]))
    return "\n".join(r[1] for r in rows)

engine = RapidOCR()
with pymupdf.open(PDF) as pdf:
    page = pdf[1]
    for dpi in (150, 200, 300):
        t0 = time.perf_counter()
        pix = page.get_pixmap(dpi=dpi)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
        half = img.shape[1] // 2
        text = ocr_half(engine, img[:, :half]) + "\n" + ocr_half(engine, img[:, half:])
        secs = time.perf_counter() - t0
        scores = [round(best_ratio(r, text), 3) for r in REFS]
        print(f"dpi={dpi}: {secs:.1f}s for one spread, {len(text)} chars, reference match {scores}")
    print("\n--- sample (300 dpi, right half, first 600 chars) ---\n" + ocr_half(engine, img[:, half:])[:600])
print("\nblocked network attempts:", netguard.attempts())
