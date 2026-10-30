# Mitra Offline RAG

An offline question-answering assistant for farmers. It answers **only** from a small set of curated agricultural PDFs, cites the document and page for every answer, and refuses when the documents don't cover the question. Everything — embeddings, vector search, and the language model — runs locally through [Ollama](https://ollama.com); no internet is needed at question time.

It replaces the original Mitra chatbot, which ran a DuckDuckGo search per question and pasted the results into the prompt (web-search-augmented generation, needed connectivity, returned no sources).

## How it works

```
ingest (once):  PDF pages ─ PyMuPDF (RapidOCR if a page has no text layer) ─► clean boilerplate ─► 1000-char chunks per page ─► nomic-embed-text ─► Chroma (store)
query:          question ─► route to the crop it names ─► embed ─► exact top-5 cosine search ─► gate ─► numbered-context prompt ─► gemma3:4b ─► answer + sources
```

The **gate** refuses before calling the model when any of three checks fires:

1. the question names a crop with no documents (e.g. sesame, mango);
2. it uses a word that never appears in the asked crop's documents although its absence would be very unlikely by chance, (1 − p)ⁿ < 0.01 with p its share of other-crop chunks and n the crop's chunk count ("The rice documents never mention: diseases.");
3. the best chunk's cosine similarity is below 0.725.

Every answer is followed by the list of passages the model was shown, so citations can be checked. Search is exact NumPy cosine over the vectors stored in Chroma (Chroma's approximate HNSW search was not repeatable here, see `DECISIONS.md` E-17).

All parameters were chosen by measurement on the dev split of the hand-written evaluation questions; see [Results](#results) and [`DECISIONS.md`](DECISIONS.md).

## Setup

Requirements: Python 3.12, Ollama, ~2 GB disk for models. Tested on Windows 10 (CPU only, 12 GB RAM).

```powershell
# 1. Python environment
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1            # bash: source .venv/bin/activate
python -m pip install -r requirements.txt

# 2. Models (needs internet once)
ollama pull nomic-embed-text
ollama pull gemma3:4b                 # default generator; gemma3:1b for a fast CPU demo

# 3. Documents: place the PDFs listed in SOURCES.csv (status "raw" or "raw (OCR)") in data/raw/.
#    They are not in this repo (licences). Filenames must follow <crop>_<topic>_<org>_<year>_<kind>.pdf

# 4. Build the index
python -m src.ingest                  # expect: 194 pages -> 726 chunks
#    The first run OCRs 8 leaflet pages (about 25 s each on CPU); the text is cached in data/ocr_cache/.
```

Run every command from the repo root.

## Use

```powershell
python -m src.api                     # web page at http://127.0.0.1:8000  (API docs: /docs)
python -m src.ask "What rate of bleaching powder controls bacterial wilt in potato?"
python -m src.ask                     # interactive
```

API: `POST /ask` with `{"question": "...", "crop": "potato" | "rice" | "wheat" | null}` returns the answer, gate decision, sources (doc, page, year, similarity) and `timings_ms`. `GET /health` reports Ollama, models, index and the offline guard.

Machine-specific settings (generator model, data folder, host/port) are environment variables — see [`.env.example`](.env.example). Example for a quick CPU demo: `$env:MITRA_GENERATOR_MODEL = "gemma3:1b"`. Restart the server after re-running ingest.

## Evaluation

```powershell
python -m eval.run_eval --split dev                 # retrieval metrics + gate, appends to eval/results/experiments.csv
python -m eval.run_eval --split test --generate     # also generates answers to eval/stage6_answers_test.md for manual grading
python -m eval.run_eval --split all --offline-guard --no-log
python -m eval.answer_check eval/results/answers_<run>.md   # does each answer contain its expected phrase?
python -m eval.lint_questions                               # every question checked against the PDFs
```

`eval/questions.csv` has 94 questions (dev 60, test 34; 73 in-scope, 21 out-of-scope), each with the expected document, page and an answer phrase. Out-of-scope questions include other crops, schemes, and topics the documents don't cover for a covered crop (e.g. rice diseases). A retrieval hit means a top-k chunk is on the expected page **and** contains the answer phrase. Every experiment, including failed ones, is logged in `DECISIONS.md` and its script kept in `eval/experiments/`.

## Offline proof

1. `src/netguard.py` blocks and records any non-localhost connection from the Python process; it is on by default in the API and available as `--offline-guard` in the eval. It does not cover Ollama, which is a separate program.
2. The real test: pull the models, then turn the network off (or remove outbound access on a cloud VM — see [`docs/aws_offline_test.md`](docs/aws_offline_test.md)) and run the eval and the web page.

Chroma telemetry is disabled in code; LangChain tracing must stay unset (`LANGCHAIN_TRACING_V2`).

## Results

Measured 29 Oct 2026 on the dev laptop (Windows 10, CPU only, 12 GB RAM): `nomic-embed-text`, chunks 1000/100, k = 5, crop routing, exact search, three-check gate, `gemma3:4b`. The test split was run once, after all choices were made on dev. Full history in [`eval/results/experiments.csv`](eval/results/experiments.csv).

| Split | In-scope n | Recall@1 | Recall@3 | Recall@5 | MRR@10 |
|---|---|---|---|---|---|
| dev v2 | 31 | 0.42 | 0.68 | 0.74 | 0.570 |
| test v2 | 15 | 0.33 | 0.60 | 0.73 | 0.504 |
| test, original 10 questions | 10 | | | 0.80 | |

End to end (gate, then the model, which can also refuse):

| | dev v2 | test v2 |
|---|---|---|
| Out-of-scope questions wrongly answered | 0 / 13 | 0 / 9 |
| In-scope questions wrongly refused | 6 / 31 | 6 / 15 |
| Answered questions containing the expected answer phrase | 18 / 25 | 8 / 9 |
| Generation time, median (95th percentile) | 78 s (102 s) | 94 s (112 s) |

Retrieval itself takes about 5–11 ms per question.

**Iteration 3** (30 Oct: 11 PDFs, 2 read with OCR, 726 chunks, questions v3), dev split only so far: Recall@5 0.750, MRR@10 0.563 on 48 in-scope questions (0.765 on the 17 new ones). The gate wrongly refuses 3 of 48 but wrongly answers **3 of 12** out-of-scope questions, up from 1 of 13: more documents raise the best similarity for any question, and a single passing mention of a word silences the topic-gap check (`DECISIONS.md` E-30). End to end with `gemma3:4b` on the 22 dev questions this iteration touched: the model refused 2 of the 3 leaked out-of-scope questions but answered "diseases in rice" with weedy-rice facts; 6 of 19 in-scope answers were wrong, 5 of them after retrieval missed the right page (the model answered from nearby passages instead of refusing; E-32). The test split v3 has not been run.

Earlier results (Stage 5, 40 questions, `gemma3:1b`): see `DECISIONS.md` and the project book.

## Known limitations

- **Over-refusal.** 12 of 46 real questions are refused: 9 by the 0.725 similarity threshold (mostly short or paraphrased questions) and 2 by the topic-gap check (v1) on word forms ("planting" vs "transplanted"; "root" for "CRI stage"). Topic-gap v2 fixed "root" and the live false refusal on "type"; "planting" remains. Chatty questions ("Hi could you tell me…") score lower and are refused more often.
- **Faithfulness.** `gemma3:4b` still occasionally swaps numbers within one passage (q2: germination vs sporangia temperature) or takes the wrong table row (q78), and when retrieval misses the right page it tends to answer from nearby passages rather than refuse. Always check the answer against the listed passages.
- **Speed.** About 1–2 minutes per answer on CPU; a GPU or `MITRA_GENERATOR_MODEL=gemma3:1b` (faster, but it never refuses by itself) for demos.
- **Gate depends on the corpus.** τ = 0.725 and the topic-gap check were tuned on 595 chunks; with 726 chunks two uncovered rice questions pass the gate (see Results). Re-check the gate after every ingest.
- **OCR text** (two leaflets) has missing spaces and merged photo captions; overview chunks from these leaflets rank high for many rice questions.
- Small corpus: 11 PDFs, 71% of chunks from one potato manual. No rice diseases or government schemes.
- The eval v2 and v3 questions (q41–q94) were added on 29–30 Oct and are pending a second review.
- English only. Single-turn (no follow-up questions).

## Repository

```
config.py        frozen parameters + env overrides
src/             corpus, ocr (RapidOCR + cache), embed (sqlite cache), store, ingest, retrieve (exact search), coverage (topic gap),
                 answer (routing + gate + generation), ask (CLI), api (FastAPI), netguard
static/          index.html (no external resources)
eval/            questions.csv, run_eval.py, answer_check.py, lint_questions.py, results/, experiments/ (one script per test)
notebooks/       01–05, the exploration behind every decision
docs/            design.md (original plan + as-built), decision_log.md (Stage 5), aws_offline_test.md
DECISIONS.md     every decision with evidence; SOURCES.csv: document provenance and licences
```

Documents are used for academic, non-commercial purposes; PDFs, the index and the embedding cache are never committed.
