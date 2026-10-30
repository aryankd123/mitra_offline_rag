"""T10 OCR settings on the herbicide leaflet's page 3 (30 Oct, Iteration 3)

Purpose: an eye check of page 3 (test 46) found two dropped list items (6 and 13), one line read upside down
(the angle classifier flipped it), a photo caption merged into a list item, and missing spaces. Test which
RapidOCR settings recover the lost lines: angle classifier off (every line here is upright), a lower
text-confidence cut-off, and a higher resolution. Score = hand-typed sentences from page 3 found exactly,
plus whether upside-down text appears.

Run from the repo root: python eval/experiments/t10_ocr_settings.py
"""
import sys, time
sys.path.insert(0, ".")
import numpy as np
import pymupdf
from rapidocr_onnxruntime import RapidOCR
from src.corpus import norm_text
from src.ocr import _lines_from_boxes

PDF = "data/raw/rice_herbicide-weed-control_nrri_2018_brief.pdf"
REFS = {
    "item 13": "Spray from a height of around 50 cm above the target weeds",
    "item 6": "Wash the spray machine properly before and after each application",
    "flipped line": "properly after each day's work and dried in open sun",
    "item 15": "Check the spraying equipment and accessories before spraying",
}
UPSIDE_DOWN = "uado u pap"

def read(engine, page, dpi, **kw):
    pix = page.get_pixmap(dpi=dpi)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    lines = []
    for part in (img[:, : img.shape[1] // 2], img[:, img.shape[1] // 2:]):
        result, _ = engine(part, **kw)
        lines += _lines_from_boxes(result)
    return "\n".join(lines)

variants = [
    ("default (as ingested)", 200, {}),
    ("angle classifier off", 200, {"use_cls": False}),
    ("cls off + text_score 0.3", 200, {"use_cls": False, "text_score": 0.3}),
    ("cls off, 300 dpi", 300, {"use_cls": False}),
]
engine = RapidOCR()
with pymupdf.open(PDF) as pdf:
    page = pdf[2]
    for name, dpi, kw in variants:
        t0 = time.perf_counter()
        text = norm_text(read(engine, page, dpi, **kw))
        found = {k: norm_text(v) in text for k, v in REFS.items()}
        print(f"{name:<26} {time.perf_counter() - t0:5.1f}s  found {sum(found.values())}/4 {[k for k, v in found.items() if not v] or ''}  upside-down text: {UPSIDE_DOWN in text}")
