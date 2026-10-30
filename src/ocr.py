"""OCR for PDF pages that have no text layer (Iteration 3, D-61).

Two leaflets store their text as vector outlines, so PyMuPDF extracts nothing. Each page is rendered to an
image and read with RapidOCR (ONNX models ship inside the pip package, so this works offline). Landscape
pages are two-page spreads: the left and right halves are read separately so the columns don't interleave.
Results are cached as text files, because OCR takes about a minute per spread on a CPU.
"""
import re
import statistics

import numpy as np

import config

_engine = None


def _get_engine():
    global _engine
    if _engine is None:
        from rapidocr_onnxruntime import RapidOCR  # imported lazily: only needed when a page has no text
        _engine = RapidOCR()
    return _engine


def _lines_from_boxes(result):
    """Group OCR boxes into lines by vertical overlap, then order each line left to right.

    A fixed pixel band breaks when the resolution changes (test 45), so lines are grouped relative to the
    median box height instead.
    """
    if not result:
        return []
    boxes = []
    for quad, text, _score in result:
        ys = [p[1] for p in quad]
        boxes.append({"x": min(p[0] for p in quad), "cy": (min(ys) + max(ys)) / 2, "h": max(ys) - min(ys), "text": text})
    tol = 0.5 * statistics.median(b["h"] for b in boxes)
    lines = []
    for b in sorted(boxes, key=lambda b: b["cy"]):
        if lines and abs(b["cy"] - lines[-1]["cy"]) <= tol:
            lines[-1]["boxes"].append(b)
        else:
            lines.append({"cy": b["cy"], "boxes": [b]})
    return [" ".join(b["text"] for b in sorted(line["boxes"], key=lambda b: b["x"])) for line in lines]


def clean(text):
    """Fix the superscript in "ha⁻¹", which OCR reads as "ha1", "ha'" or "ha''" (test 48)."""
    return re.sub(r"\bha(?:-1|1|''|'|’’|’|\")(?=[\s).,;:]|$)", "ha-1", text)


def ocr_page(page, cache_key):
    """Text of one PyMuPDF page via OCR, cached raw in config.OCR_CACHE_DIR/<cache_key>.txt, returned cleaned."""
    cache = config.OCR_CACHE_DIR / f"{cache_key}.txt"
    if cache.exists():
        return clean(cache.read_text(encoding="utf-8"))
    pix = page.get_pixmap(dpi=config.OCR_DPI)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    halves = [img[:, : img.shape[1] // 2], img[:, img.shape[1] // 2 :]] if page.rect.width > page.rect.height else [img]
    lines = []
    for part in halves:
        # use_cls=False: every line in these leaflets is upright, and the angle classifier flipped one line
        # upside down and dropped others (test 46); without it OCR is also ~2.7x faster
        result, _ = _get_engine()(part, use_cls=config.OCR_USE_CLS)
        lines += _lines_from_boxes(result)
    text = "\n".join(lines)
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text, encoding="utf-8")
    return clean(text)
