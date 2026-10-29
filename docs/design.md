# Mitra Offline RAG Chatbot: Design and Workflow

> **Note (29 Oct 2026):** the original design document from the planning phase (written before any code ran). What was actually built, and where it deviates from this plan, is in **section 15** at the bottom and in `DECISIONS.md`.

Status: design written before implementation; nothing in sections 1–14 had been run at the time.

## 1. Context and constraints

- Windows 10. The original MacBook that ran the heavy model is gone. The final run will happen on a friend's laptop with an NVIDIA GPU (reported as RTX 3050; VRAM unknown).
- Chatbot language: English only for now. Purpose when built: answering farmers' queries (crop and weed/disease questions; the team's models covered a sesame crop/weed detector and a disease detector).

## 2. Verified facts about the existing chatbot (`IP/webapp/app.py` in the MITRA repo)

- Flask app; `Ollama(model="gemma:2b")` (comment mentions `gemma:7b`); which Gemma model was actually run is not recorded.
- For every question it runs a **DuckDuckGo web search** ("agriculture farming <question>"), pastes the results into an f-string prompt and asks for four sections (Direct Answer, Explanation, Implementation, Additional Tips); refuses non-agricultural questions through the prompt only.
- That is web-search-augmented generation, **not RAG**: no embeddings, no vector store, no private knowledge base. It needs the internet at question time, returns no sources, and runs `app.run(debug=True)`.
- Pinned versions in the repo (Python side): `langchain==0.3.23`, `langchain-community==0.3.21`.

## 3. Goals and non-goals

Goals:

- G1: Answer English agricultural questions **only from a curated local document set**, with numbered citations.
- G2: Work with **no internet at question time** (proved by a test with the network off).
- G3: Say "I do not have this in my documents" instead of guessing.
- G4: Measured quality: retrieval recall@k and MRR, answer faithfulness (manual), refusal behaviour, latency p50/p95 on the development hardware.

Non-goals (for now): multilingual support, fine-tuning, image questions, a polished front end, running on the rover's Jetson.

## 4. Architecture

Ingest (run once per document set): documents, then split into chunks, then embed each chunk, then store vectors with metadata (source file, page, chunk id).

Query (every question): embed the question with the **same** embedding model, search top-k chunks, drop chunks below a similarity threshold, build a prompt with numbered context and rules, call the local LLM, return answer plus sources plus timings.

Components, all local:

| Component | Choice | Notes |
|---|---|---|
| Runtime | Ollama | one local server hosting both the chat model and the embedding model |
| Chat model | development: `gemma3:1b` (815 MB); target: `gemma3:4b` (3.3 GB) | sizes from the Ollama library page; pick the final one by measurement |
| Embedding model | `nomic-embed-text` via Ollama (to be confirmed with `ollama pull`) | read the vector length from the first embedding rather than trusting a number; test with and without nomic's task prefixes (`search_document:` / `search_query:`) on the eval set |
| Vector store | Chroma, persistent on disk | metadata filtering, simple API |
| Orchestration | LangChain (LCEL `a | b | c`) | CampusX style |
| Service | FastAPI + one static HTML page | `POST /ask`, `GET /health` |
| Evaluation | plain Python script and JSONL test set | no framework |

## 5. Decision log

| ID | Decision | Alternatives | Why | Revisit when |
|---|---|---|---|---|
| R1 | Offline RAG, not web-search augmentation | keep DuckDuckGo | works without connectivity, answers are grounded and checkable | never |
| R2 | Ollama as runtime | llama.cpp directly, vLLM | simplest on Windows, one command to pull models, HTTP API | need batching or higher throughput |
| R3 | Dev model `gemma3:1b`, target `gemma3:4b` | other families | Gemma continuity with the original project; 1B runs on any laptop; 4B fits a small GPU | eval shows 4B too slow or 1B too weak |
| R4 | Embeddings through Ollama | sentence-transformers | one runtime, fewer dependencies | eval shows another model retrieves better |
| R5 | Chroma persistent store | FAISS | metadata and persistence built in; the corpus is small | corpus grows beyond about a million chunks |
| R6 | Brute-force-quality exact search at this scale | approximate indexes | a few thousand chunks need no approximate index | corpus size jump |
| R7 | `RecursiveCharacterTextSplitter`, parameters chosen by experiment | fixed token splitter | respects paragraph and sentence boundaries | tables or scanned PDFs dominate |
| R8 | Similarity threshold plus top-k | top-k only | lets the bot refuse out-of-scope questions | eval shows the threshold hurts recall |
| R9 | Grounded prompt with a fixed refusal sentence and numbered citations | free-form prompt | reduces hallucination; sources are checkable | never |
| R10 | Evaluation harness **before** tuning | tune by eye | numbers drive every parameter | never |
| R11 | FastAPI | Flask (old code), Streamlit | async, request validation, auto docs; Streamlit hides the design | never |
| R12 | Settings in environment variables via one `config.py` | constants in code | different machines (own laptop, friend's laptop) | never |
| R13 | Network-off test and telemetry off | trust defaults | proves the offline claim | never |
| R14 | Single-turn answers first; chat history later | history from day one | history-aware rewriting adds an extra model call | after acceptance tests pass |
| R15 | New, separate repo, e.g. `mitra-offline-rag` | push into the team repo | the MITRA repo belongs to an organisation; develop and test separately first | fully tested and ready to merge into the team repo |

## 6. Repository layout

```
mitra-offline-rag/
  README.md  SOURCES.md  requirements.txt  .env.example  .gitignore
  data/raw/          (source PDFs; do not commit if licensing is unclear)
  data/chroma/       (generated; gitignored)
  eval/questions.jsonl   eval/results/
  notebooks/         (01_embeddings, 02_chunking, 03_retrieval, 04_chain)
  src/mitra_rag/config.py  ingest.py  retrieve.py  chain.py  api.py  eval.py
  static/index.html
  tests/
```

Module contracts (planned):

```python
# ingest.py
def load_documents(raw_dir) -> list[Document]
def split_documents(docs, chunk_size, chunk_overlap) -> list[Document]
def build_index(chunks, persist_dir, embedding_model) -> None

# retrieve.py
def get_retriever(persist_dir, embedding_model, k, threshold)
def retrieve(question) -> list[tuple[Document, float]]     # chunk and score

# chain.py
def build_chain(retriever, llm) -> Runnable
def answer(question) -> dict   # {"answer", "sources", "timings_ms"}
```

Likely imports (verify by running, then pin exact versions with `pip freeze` into `requirements.txt`):

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
```

## 7. Knowledge base

The quality ceiling of the whole system is the documents. **Open decision:** which crops and topics (the team's vision models covered sesame weeds and crop diseases) and which documents. Guidelines:

- Prefer public, freely downloadable extension material (agricultural universities, ICAR institutes, Krishi Vigyan Kendras, FAO). Check each document's permission to reuse.
- Keep `SOURCES.md` with title, publisher, URL, date and licence for every file.
- Start with 10 to 20 documents. Check PDF text extraction by eye: tables and scanned pages extract badly, and scanned PDFs need OCR (a later task).
- Curated documents also reduce prompt-injection risk compared with live web results.

## 8. Prompt template (starting point, to be tested)

```
You are an agricultural assistant for farmers. Use ONLY the numbered context below.
If the context does not contain the answer, reply exactly: "I do not have this in my documents."
Cite the sources you use like [1] or [2]. Keep the answer short and practical.

Context:
{context}

Question: {question}
```

`format_docs` should number each chunk and include its source and page, so citations can be mapped back.

## 9. Evaluation design

- `eval/questions.jsonl`: 30 to 40 hand-written questions, each with the source file and page (or a distinctive phrase) where the answer lives, plus 10 deliberately out-of-scope questions.
- Retrieval metrics: **recall@k** (a relevant chunk appears in the top k) and **MRR** (mean of 1 divided by the rank of the first relevant chunk).
- Answer checks (manual, small): is every claim supported by a cited chunk; is the refusal sentence used for out-of-scope questions.
- Latency: p50 and p95 of retrieval time and generation time, reported with the exact machine and model.
- Experiment grid for Stage 5: chunk size {500, 1000, 1500} characters, overlap {0, 100, 200}, k {3, 4, 6}. Record the table in the README.
- Threshold: plot or print score distributions for in-scope versus out-of-scope questions and choose the threshold from them. Chroma returns a distance (lower is better); with a cosine space, similarity is 1 minus distance. Version-dependent detail: how to set the cosine space on a collection; check the installed Chroma's documentation.

## 10. Workflow: stages with acceptance checks

Time estimates are for planning only (about 14 to 16 hours in total); Stages 7 and 9 are optional.

**Stage 0: environment (about 1.5 h).** Python 3.11 or 3.12, a virtual environment (`py -3.11 -m venv .venv`; activate with `.venv\Scripts\Activate.ps1`; if scripts are blocked, `Set-ExecutionPolicy -Scope Process Bypass`), install Ollama for Windows, `ollama pull gemma3:1b` and the embedding model, run `nvidia-smi` on the target laptop to learn the VRAM. Acceptance: `ollama run gemma3:1b` answers a question; a short Python script gets one embedding and prints its length.

**Stage 1: embeddings by hand (about 1.5 h).** Compute cosine similarity of real sentence embeddings with NumPy. Acceptance: related sentences score higher than unrelated ones; the reason is written down.

**Stage 2: documents and chunking (about 2 h).** Load PDFs with `PyPDFLoader`, inspect the extracted text, split with different sizes, count chunks (check against the chunk-count formula, remembering characters not tokens). Acceptance: a chunk-statistics printout and three bad-extraction examples noted.

**Stage 3: vector store and retrieval (about 2 h).** Build the Chroma index from the chunks; query it; inspect scores. Acceptance: for 10 hand-picked questions, the printed top-3 chunks make sense, and the wrong ones are explained.

**Stage 4: the generation chain (about 2 h).** Write the prompt and LCEL chain; return answer plus sources. Acceptance: grounded answers with citations; out-of-scope question gets the refusal sentence.

**Stage 5: evaluation and tuning (about 2 h).** Build `eval.py`, run the experiment grid, pick chunk size, overlap, k and threshold from the numbers. Acceptance: a results table committed to the repo and the chosen parameters in `config.py`.

**Stage 6: service, UI and offline proof (about 2 h).** FastAPI `/ask` and `/health`, a single static page, timings in the response. Run with the network disabled. Acceptance: the whole flow works offline; the eval script passes with Wi-Fi off.

**Stage 7 (optional): history-aware answers (about 1.5 h).** Rewrite follow-up questions into standalone ones with the model, then retrieve. Measure the latency cost.

**Stage 8: packaging and benchmark on the friend's laptop (about 1.5 h).** README with exact setup steps, pinned `requirements.txt`, a one-command start, measured latency on that laptop with the exact model and VRAM. Acceptance: someone else can run it from the README.

**Stage 9 (optional, separate track): telemetry assistant.** A LangChain interface for hardware logs. Build only after Stages 0 to 6 pass: a synthetic telemetry generator, a serial parser, rows stored in SQLite, and a LangChain tool-calling layer in which the model fills a **structured filter** (field, operator, value, time range) that the code executes with parameterised SQL (never model-written SQL). Label it as a reference implementation.


## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Poor PDF extraction (tables, scans) | inspect extracted text early; OCR only if needed; prefer text-based documents |
| Embedding model mismatches the domain | compare two embedding models on the eval set |
| Hallucination despite the prompt | threshold, refusal sentence, manual faithfulness checks |
| 3050 laptop VRAM too small (VRAM is unknown) | start with `gemma3:1b`; check `nvidia-smi`; measure before choosing the 4B model |
| One GPU serialises generation | measure latency; limit concurrent requests; capacity is about 1 divided by latency per second (Little's Law) |
| Chroma or Python wheel problems on Windows | note the error; fallback store is FAISS CPU |
| Library API drift | pin versions after the first working run |
| Telemetry or tracing sending data out | keep Chroma telemetry off and LangChain tracing unset; verify with the network-off test |

## 15. As built — status and deviations (29 Oct 2026)

| Stage | Status | Where |
|---|---|---|
| 0–2 | ✅ | `notebooks/01`, `02` |
| 3 | ✅ | `notebooks/03`, `eval/stage3_results.md` |
| 4 | ✅ | `notebooks/04`, `eval/stage4_*.md` |
| 5 | ✅ | `notebooks/05`, `docs/decision_log.md`, `eval/results/experiments.csv`, `config.py` |
| 6 | ⏳ built and tested on the dev laptop; Wi-Fi-off / AWS no-egress run pending | `src/api.py`, `static/index.html`, `src/netguard.py` |
| 7 | ⬜ optional, later iteration | — |
| 8 | packaging ✅ (`python -m src.api` is the one-command start); laptop benchmark **optional**, AWS EC2 CPU stand-in (D-46) | `README.md`, `requirements.txt`, `.env.example`, `docs/aws_offline_test.md` |
| 9 | ⬜ optional, later iteration | — |

Deviations from the plan above (each with its reason in `DECISIONS.md`):

- **R6 is wrong as worded:** Chroma's index is HNSW (approximate). Measured top-5 identical to exact NumPy search on this corpus (D-37).
- **Loader:** PyMuPDF instead of `PyPDFLoader` (minutes → ~1 s; `langchain-community` no longer maintained) (D-22).
- **R8 threshold:** implemented as a two-signal gate on the *top-1* similarity (τ = 0.725) plus an unsupported-crop guard, not as a per-chunk filter (D-42). Single threshold had 33% out-of-scope false accepts on dev.
- **Refusal sentence:** "I could not find this in my documents." (Stage 4 prompt work).
- **Orchestration:** plain function calls (`retrieve` → `format_context` → `ChatOllama.invoke`) rather than an LCEL chain.
- **Eval set:** `eval/questions.csv` (40 questions, dev/test split) instead of JSONL; metrics R@1/3/5, MRR@10, median gold rank, gate false-reject/false-accept.
- **Layout:** flat `src/` package (`corpus, embed, store, ingest, retrieve, answer, ask, api`) instead of `src/mitra_rag/`; `SOURCES.csv` instead of `SOURCES.md`.
