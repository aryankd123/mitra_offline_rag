"""Topic-gap check: is the question's topic covered for the crop it asks about? (Iteration 2, D-57, D-60)

For each question word that never appears in the asked crop's chunks, ask how surprising that absence is:
p = share of the other crops' chunks that contain the word, n = number of chunks of the asked crop.
If the word were as common here as elsewhere, the chance of seeing it in none of the n chunks is (1 - p) ** n.
Below TOPIC_GAP_ALPHA the absence is not chance: the documents don't cover that topic for this crop.

Example (Iteration 2 corpus): "disease" is in 38% of potato/wheat chunks; rice has 46 chunks; (1 - 0.38) ** 46 = 3e-10
-> refuse. "type" is in 7% of potato/rice chunks; wheat has 33 chunks; (1 - 0.07) ** 33 = 0.09 -> not evidence, keep going.
v1 used a fixed ">= 20 other-crop chunks" cut-off, which ignored crop size (potato 516 chunks, wheat 33)
and refused ordinary words like "type" (E-22).
Known weakness (E-30): one passing mention is enough to silence it. Since Iteration 3, "disease" occurs in 4 of
120 rice chunks, so "diseases in rice" is no longer flagged although no document covers rice diseases.
"""
import re
from collections import Counter, defaultdict

import config
from src.store import get_collection

STOPWORDS = set("""a an the and or of in on at to for from by with without into about over under is are was were be been being
do does did done how what which who whom whose why when where should would could can may might must will shall it its this that
these those there their them they you your i we our us me my he she his her than then so such per each any all some most more much
many very also not no yes if as up out off ok know tell give get use used using make made need needed recommended recommend""".split())

_df = None        # crop -> Counter(term -> number of chunks containing it)
_n_chunks = None  # crop -> number of chunks


def _stem(w):
    return w[:-1] if len(w) > 4 and w.endswith("s") and not w.endswith("ss") else w


def terms(text):
    return {_stem(w) for w in re.findall(r"[a-z]+", text.lower())
            if len(w) >= 3 and w not in STOPWORDS and w not in config.CROP_SYNONYMS}


def _chunk_counts():
    global _df, _n_chunks
    if _df is None:
        got = get_collection().get(include=["documents", "metadatas"])
        _df, _n_chunks = defaultdict(Counter), Counter()
        for doc, meta in zip(got["documents"], got["metadatas"]):
            t = terms(doc)
            for crop in meta["crop"].split("-"):  # a "rice-wheat" chunk counts for both crops
                _df[crop].update(t)
                _n_chunks[crop] += 1
    return _df


def chance_of_absence(word, crop):
    """Probability that `word` (a stem) appears in none of `crop`'s chunks if it were as common as in the other crops."""
    df = _chunk_counts()
    others = [c for c in _n_chunks if c != crop]
    p = sum(df[c][word] for c in others) / max(1, sum(_n_chunks[c] for c in others))
    return (1 - p) ** _n_chunks[crop]


def topic_gaps(question, crop):
    """Words the question uses whose absence from `crop`'s documents is statistically surprising.

    Returned as the user wrote them ("virus", not the stem "viru").
    """
    if not crop:
        return []
    df = _chunk_counts()
    gaps = set()
    for word in re.findall(r"[a-z]+", question.lower()):
        w = _stem(word)
        if w in terms(word) and df[crop][w] == 0 and chance_of_absence(w, crop) < config.TOPIC_GAP_ALPHA:
            gaps.add(word)
    return sorted(gaps)
