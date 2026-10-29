# DECISIONS.md — Mitra Offline RAG

Decision log, experiment results and corrections. Newest stage at the bottom.
**Status:** ✅ Final · 🟡 Provisional (to be decided by measurement) · ⏸ Deferred
Every entry says *why* and *what evidence* — so it can be defended in an interview.
Detailed Stage 5 numbers: [`docs/decision_log.md`](docs/decision_log.md). All runs: [`eval/results/experiments.csv`](eval/results/experiments.csv).

---

## A. Scope and project decisions

| ID | Decision | Why | Status |
|---|---|---|---|
| D-01 | Build a true RAG pipeline (local retrieval over curated PDFs) instead of the original "web search per question" bot. | Original bot needed internet and wasn't RAG. RAG grounds answers in chosen documents. | ✅ |
| D-02 | Fully offline at runtime; prove it with a Wi-Fi-off test (Stage 8). | Core claim of the project. | ✅ |
| D-03 | Choose every parameter from an eval set, not by feel. | Defensible numbers; the results table is the interview evidence. | ✅ |
| D-04 | Own repo (`mitra_offline_rag`) first; push to the org's MITRA repo once fully tested. | Original repo belongs to an organisation; Aryan has access to push later. | ✅ |
| D-05 | Notebooks first, then move stable code into modules. | Learning style (CampusX); inspect intermediate values. Modules done in Stage 6 (D-45). | ✅ |
| D-06 | Phase A = English corpus, offline. Hindi and online mode → next iteration. | Aryan reads Hindi but can't write ~20 Hindi eval Q&As; offline core first. | ✅ |
| D-07 | Mitra is academic / non-commercial. | Stated by Aryan; makes the ICAR Data Use Licence applicable. | ✅ |
| D-08 | Finish Stages 0–6 before endsems (2nd week of Nov 2026); Stages 7 and 9 optional. | ~18–20 h available vs 14–16 h estimate; little slack. | ✅ |
| D-09 | Safety rule: answer only from retrieved text, always cite source + year, refuse when retrieval is weak. | Herbicide/fertiliser doses can harm crops and people; documents disagree (see E-08). | ✅ |
| D-10 | Optional online mode later: search restricted to official government domains for "latest scheme" questions; web text treated as untrusted and cited; offline fallback shows each scheme doc's "last verified" date. | Scheme facts go stale (PM-KISAN guidelines 2018-19 vs instalments through 2026). | ⏸ |

## B. Environment

| ID | Decision | Why / evidence | Status |
|---|---|---|---|
| D-11 | Python 3.12 venv (not system 3.14). | New Python versions often lack pre-built wheels for Chroma and its dependencies → source builds fail on Windows. Not verified per package; chose safety. | ✅ |
| D-12 | Ollama as local model server; Python is its HTTP client. | Simple local runtime for both LLM and embeddings. | ✅ |
| D-13 | Generator: `gemma3:1b` on the CPU dev laptop; `gemma3:4b` candidate for the GPU demo laptop. | 5B-4: 4b more faithful (q1, q3, q4) but p50 91.9 s vs 10.9 s on CPU. Final choice after Stage 8 GPU latency. | 🟡 |
| D-14 | Use `python -m pip`, not bare `pip`. | Folder renamed after venv creation; launcher scripts hold the old path. | ✅ |
| D-15 | `.gitignore`: `.venv/`, `data/chroma/`, `data/raw/`, `data/pending_ocr/`, `data/excluded/`, `data/embed_cache.sqlite`, `__pycache__/`. | PDFs and index must not be distributed; the 88 MB embedding cache was tracked until 29 Oct (would hit GitHub's 100 MB limit). | ✅ |

## C. Embeddings

| ID | Decision | Why / evidence | Status |
|---|---|---|---|
| D-16 | Cosine similarity as the relevance measure. | Measures direction, ignores length; long passage and short question on same topic still match. | ✅ |
| D-17 | Embedding model: `nomic-embed-text` (768-d) as default; `bge-m3` as the high-accuracy / Hindi option. | 5B-1 dev: bge-m3 R@5 0.90 vs 0.75, but 3.2× slower indexing on CPU; test R@5 equal (0.80). Model name stored in collection metadata and checked at query time. | ✅ |
| D-18 | Task prefixes not used. | 5B-1 on real chunks: prefixes R@5 0.80 but R@3 dropped 0.70 → 0.60. | ✅ |
| D-19 | Thresholds are model-specific; choose the "too weak to answer" threshold from labelled data. | Unrelated text scores ~0.35–0.40 on nomic, not ~0 (E-02). Value: D-42. | ✅ |

## D. Documents, loading, cleaning, chunking

| ID | Decision | Why / evidence | Status |
|---|---|---|---|
| D-20 | Filename convention `<crop>_<topic>_<org>_<year>_<kind>.pdf`, parsed into metadata; `assert kind in KINDS`. | Filename is the schema; wrong field count / kind fails loudly. | ✅ |
| D-21 | Folders by status: `data/raw/`, `data/pending_ocr/`, `data/excluded/`. Track every file in `SOURCES.csv`. | Licences differ per item; attribution needs URL + date. `SOURCES.csv` drafted 29 Oct with TODOs. | ✅ |
| D-22 | Loader: PyMuPDF used directly; build `langchain_core` `Document`s ourselves. | PyPDF took ~5–6 min vs PyMuPDF < 10 s (later 1.1 s). `langchain-community` no longer maintained. PyMuPDF is AGPL/commercial — fine for academic use, re-check if distributed. | ✅ |
| D-23 | Page numbers 1-based; `source` = filename only. | Match PDF viewer for citations; don't show local paths to farmers. | ✅ |
| D-24 | Clean boilerplate: drop lines on ≥ max(5, 50% of a doc's pages) with length ≥ 10; map `` → `•`. | Potato manual header lines on 136/142 pages; two bullet characters. | ✅ |
| D-25 | Split per page (chunks never cross pages). | Keeps page citation correct. | ✅ |
| D-26 | `RecursiveCharacterTextSplitter`, chunk_size 1000, overlap 100. | 5A-1: 500/0 best on dev (R@5 0.90) but worse on test (0.70 vs 0.80) and on multi-page questions; 1000/100 halves the index. | ✅ |
| D-27 | Reflow rejected; table-aware extraction rejected; chunk-level reference filter + min_chunk_len 50 accepted (615 → 595 chunks). | 5B-2, 5B-3a, 5B-3b in `docs/decision_log.md` §3. | ✅ |
| D-28 | OCR for `pending_ocr/` files — optional (Stage 7 candidate). | Best weed document has no text layer. | ⏸ |
| D-29 | Exclude `rice_ghg-monitoring_crri_2011_brief.pdf`. | Emissions measurement; no farmer advice. | ✅ |

## E. Vector store

| ID | Decision | Why / evidence | Status |
|---|---|---|---|
| D-30 | **Chroma** (embedded, persistent on disk), FAISS as fallback (design doc R5). | Embedded like SQLite → no server on demo laptop; persistence, IDs, metadata filters built in. | ✅ |
| D-31 | Alternatives rejected for now: FAISS, Qdrant, LanceDB, plain NumPy. Switch triggers: multi-user server → Qdrant; GPU-scale/tuning → FAISS. | Structural facts from comparison posts (benchmark claims ignored). | ✅ |
| D-32 | Set cosine space explicitly: `configuration={"hnsw": {"space": "cosine"}}`. | Default is squared L2. Verified: `configuration_json["hnsw"]["space"] == "cosine"` on the rebuilt index. | ✅ |
| D-33 | `Settings(anonymized_telemetry=False)`. | Telemetry defaults to on; Stage 8 network-off test is the real proof. | ✅ |
| D-34 | Never use Chroma's built-in default embedder; always pass our Ollama vectors. | Avoid silent model mismatch and downloads. | ✅ |
| D-35 | Store `embed_model, dim, doc_prefix, query_prefix, chunk_size, chunk_overlap, min_chunk_len, drop_reference_chunks` in collection metadata; refuse to query on mismatch. | Implemented in `src/store.py:get_collection` (29 Oct); tested by setting `EMBED_MODEL="bge-m3"` → clear error. | ✅ |
| D-36 | Stable chunk IDs `doc_id:p<page>:c<n>`; write with `upsert`; delete IDs that no longer exist. | Re-runs don't duplicate; adding a PDF = `python -m src.ingest`. | ✅ |
| D-37 | Chroma's index is HNSW (approximate), not brute-force. | Stage 3: Chroma top-5 = NumPy exact top-5 on q1–q10 (5/5 overlap). Stage 6: Chroma metrics identical to the NumPy-matrix eval on dev and test (E-11). **Superseded by D-58** (exact search) after E-17. | ✅ |

## F. Evaluation

| ID | Decision | Status |
|---|---|---|
| D-38 | Eval set `eval/questions.csv`: 40 questions, `dev` 26 (20 in / 6 out of scope), `test` 14 (10 / 4). Hit = expected doc + expected page + answer phrase in chunk (`match` any/all). Test split used once for final configs. | ✅ |
| D-39 | Eval questions must stay within corpus coverage (rice weeds, potato disease/pest, wheat rust economics). | ✅ |

## G. Stage 5 — tuning (details in `docs/decision_log.md`)

| ID | Decision | Evidence | Status |
|---|---|---|---|
| D-40 | k = 5. | dev R@3 0.70 / R@5 0.75 / R@6 0.80; k=5 keeps context ~4.5k chars for small models. | ✅ |
| D-41 | Prompt v3 (no literal refusal string at the end; format example). | v1: 0/8 citations; v2: echoed refusal sentence on line 1. **But see E-12: the example's content leaks into answers.** | 🟡 |
| D-42 | Two-signal gate: top-1 similarity ≥ 0.725 **and** no unsupported crop named without a supported one. | dev: false reject 1/20, false accept 0/6. test: false accept 0/4, **false reject 3/10** (E-11). | 🟡 |
| D-43 | Always print retrieved sources programmatically under every answer (not trusting the model's citations). | Model citations are unreliable at 1b. | ✅ |

## H. Stage 6 — modules

| ID | Decision | Why | Status |
|---|---|---|---|
| D-44 | Freeze parameters in `config.py`; all modules read from it. | One place to change; collection metadata checked against it (D-35). | ✅ |
| D-45 | `src/` modules: `corpus`, `embed` (sqlite cache), `store`, `ingest`, `retrieve`, `answer`, `ask` (CLI); `eval/run_eval.py` evaluates through Chroma. | Needed for the demo laptop and the org repo; notebooks stay as the learning record. | ✅ |
| D-46 | Stage 8 on the friend's laptop becomes optional; an AWS EC2 free-plan CPU instance (largest eligible: m7i-flex.large) is the stand-in: clean install from `requirements.txt`, pull models, then remove outbound network access and run the eval. | Access to the friend's laptop is uncertain (Aryan, 29 Oct). AWS gives a clean machine + a verifiable no-network test. No GPU on the free plan, so it measures CPU latency only. PDFs on a private instance = still private use; never expose it publicly. | 🟡 |
| D-47 | Ship a complete, simple build first; add complexity (OCR, more documents, Hindi, online mode) in later iterations. | Aryan, 29 Oct: endsems approaching; a working end-to-end build is worth more than half-done extras. | ✅ |
| D-48 | Stage 6 service = FastAPI (`POST /ask`, `GET /health`) + one static page with no external resources, bound to 127.0.0.1; one generation at a time (lock). | Design R11 (FastAPI over Streamlit: "Streamlit hides the design"); offline page can't load CDNs; one local model serialises work anyway (design §11). | ✅ |
| D-49 | `src/netguard.py`: audit hook that blocks and records non-loopback DNS/connects; on by default in the API, `--offline-guard` in the eval. | Design R13. Checkable on every run; covers our Python process only — Ollama is separate, so the network-off test stays the real proof. | ✅ |
| D-50 | Env overrides only for machine-specific settings (generator model, data dir, host/port, guard); measured parameters stay constants. | Design R12 is about machines; changing chunking/k/τ needs a new eval run, so they must not drift silently. | ✅ |
| D-51 | Stages 7 (history-aware answers) and 9 (telemetry assistant) → later iterations. | D-47; design marks both optional. | ⏸ |
| D-52 | Anything for Aryan to review or read (plans, questions, interview prep) goes in a separate project book (kept outside the repo) with diagrams, not a `.md` file. | Aryan, 29 Oct: `.md` is hard to view; he prepares for interviews by reading these. Repo `.md` files stay as the engineering record. | ✅ |
| D-53 | Iteration 2 plan: eval v2 → crop routing → gate re-check on dev → generator decision → offline run. Reranker, more documents, OCR, Stage 7/9, Hindi → Iteration 3. | E-15; Aryan: "start by correcting the issues" (29 Oct). | ✅ |

## I. Iteration 2 — answer quality (29 Oct)

| ID | Decision | Why / evidence | Status |
|---|---|---|---|
| D-54 | **Eval v2:** +28 questions (now 68). Dev: +8 `uncovered_topic` out-of-scope (covered crop, topic not in corpus, incl. Aryan's rice-diseases question) and +10 `short` rewordings of dev questions. Test: +5 and +5 of the same kinds, written before any tuning and not looked at until the final check. Drafted on 29 Oct and marked "pending second review" in `notes`. `eval/lint_questions.py` (port of the notebook linter) passes on all 68. | E-15: the old set had no same-crop/uncovered-topic questions, so the gate looked perfect. | 🟡 review |
| D-55 | **Generator `gemma3:4b`** (Aryan, 29 Oct). `MITRA_GENERATOR_MODEL=gemma3:1b` for a fast CPU demo. Ollama `keep_alive=30m` so the model stays loaded. | E-15(f): 4b refused the blast question, 1b answered with unrelated facts; 1b refused 0/19 on its own. E-16: 1b cannot judge answerability. | ✅ |
| D-56 | **Crop routing:** the crop named in the question (synonyms: paddy→rice, gehun→wheat, aloo/potatoes→potato) restricts search to that crop and overrides the UI dropdown, with a note to the user. Two crops named → no routing. | Dev v2: R@5 unchanged; removes cross-crop passages (E-15 d). | ✅ |
| D-57 | **Topic-gap rule (third gate signal):** refuse when the question uses a word that is in ≥ 20 chunks of other crops but in 0 chunks of the routed crop; the refusal names the word ("The rice documents never mention: disease."). τ stays 0.725. | E-16: dev v2 FR 4/30 → 4/30, FA 3/14 → 1/14. Everyday words occur in ≤ 11 other-crop chunks, topic words in ≥ 34, so 20 sits in a wide gap (not a knife-edge). Rejected: τ 0.73 (FA 1/14 only by moving the line past q42 at 0.7253), IDF word coverage (FR 8/30), LLM yes/no judge (E-16). | ✅ |
| D-58 | **Exact search:** Chroma remains the store; retrieval is exact cosine in NumPy over its vectors (loaded once per process). Restart the API after re-ingest. | E-17: HNSW missed the true nearest chunk for q52 in 2 of 3 process runs; exact search is deterministic and < 1 ms at 595 chunks. Matches design R6. Revisit above ~100k chunks. | ✅ |
| D-60 | **Topic-gap rule v2:** flag a word only if its absence from the asked crop is statistically surprising: (1 − p)^n < α, p = share of other-crop chunks containing it, n = the asked crop's chunk count; α = 0.01 (conventional, fixed before looking at test). Replaces "≥ 20 other-crop chunks". | E-22: v1 refused "which type of weed removal strategy for my wheat crop" on "type" because potato has 516 chunks and wheat 33. Dev unchanged (FR 5/31, FA 1/13; q45 now refused by similarity instead of "root"). Seen test: q59 (rice insecticide) now passes the topic check. α = 0.001 would look better on test; not chosen, that would be tuning on test. | ✅ |
| D-59 | Answers are tidied in code: lines joined, leading "[n] " / "3. " list markers removed. Prompt stays v3 for now. | 1B answers started lines with "[1]"; v4 with placeholders made 1B output worse (E-16), so prompt changes wait for a 4b measurement. | 🟡 |

---

## Experiment log (measured values)

| ID | Experiment | Result | Takeaway |
|---|---|---|---|
| E-01 | `nomic-embed-text` via `OllamaEmbeddings` | Vector length **768** | Measured, not quoted. |
| E-02 | 6 toy sentences vs "How do I control weeds in sesame?" (nomic, no prefix) | herbicide-sesame 0.867, leaf spot 0.717, wheat 0.502, segfault 0.395, cricket 0.358 | Order right; unrelated text ≈ 0.35–0.40, not 0. Same-crop-wrong-topic scores high (risk). |
| E-03 | "til" query, no shared keywords (nomic, no prefix) | Top-2 correct (0.636, 0.598); leaf spot 0.542; margin **0.056** | Supports meaning over keywords; separation weak. |
| E-04 | Same with prefixes | Margin **0.018**; order changed | Prefixes worse on this toy test (not representative). |
| E-05 | Hindi query | nomic: margin **−0.173**. bge-m3: margin **+0.066**, shape (6, 1024) | nomic unusable for Hindi; bge-m3 promising, not proven. |
| E-06 | Chunk counts (4 PDFs, 164 pages) | After cleaning: **1176 / 615 / 432 / 600** for (500,50) / (1000,100) / (1500,150) / (1000,0) | Cleaning removed ~4.1%. Avg chunk 835 chars. |
| E-07 | Per-page formula check at 1000/100 | `Counter({0: 160, -1: 4})` | Real stride > 900, leftover absorbed. |
| E-08 | Fenoxaprop-p-ethyl timing in dry DSR | text: 25–28 DAE; table: 18–20 DAS; file 1 table: 15–20 DAS | Documents disagree → must cite source/year. |
| E-09 | gemma3:1b free answer about Indian crops | Sugarcane under "fruits", circular claims, unverified % | "Before" example: why RAG. |
| E-10 | Stage 5 sweeps (chunking, k, embed model, prefixes, tables, reflow, filters, gate, 1b vs 4b) | see `docs/decision_log.md` and `experiments.csv` | |
| E-11 | Stage 6: `src/` pipeline via Chroma, 595 chunks (29 Oct) | dev R@1/3/5 0.40/0.70/0.75, MRR 0.5653; test 0.40/0.70/0.80, MRR 0.5861 — identical to the notebook. Gate: dev FR 1/20 (q20), FA 0/6; **test FR 3/10 (q23 0.7244, q27 0.7023, q32 0.6847)**, FA 0/4 | Port is faithful. τ = 0.725 is too strict for paraphrase/multi questions on unseen data; don't retune on test. |
| E-12 | `src.ask` end-to-end, gemma3:1b (29 Oct) | Bleaching powder: "12 kg/ha **when sowing in rows 20 cm apart**" — the last phrase is copied from the prompt v3 example. Fenoxaprop: no timing given, conflict missed (gold at rank 9). Sesame: refused by crop guard. Generate 36–48 s on CPU. Dev `--generate` run (19 answered, p50 32.9 s, p95 48.6 s): leak seen in **0/19** (q17 dev wording answered cleanly), q4 still repeats "60 g a.i./ha" three times with no timing. | Leak is occasional (1 of 22 generated answers so far) but put a false condition into a dose answer → fix with a content-free example and re-check on dev. |

| E-13 | Stage 6 API smoke test (29 Oct) | `/health` ok (595 chunks, guard on, 0 blocked). Sesame → refused (crop guard). Bleaching-powder q17 wording → "12 kg/ha … in furrows" [1], p.37, generate 42.1 s. **"For how many minutes should seed tubers be dipped in 3% boric acid?" → refused: correct page (p.40) ranked 1st at 0.7187 < 0.725**; the full test wording (q25) scores 0.8009. | Short real-user questions score lower than the long eval questions → gate is wording-sensitive. Evidence for revisiting D-42 on dev (e.g. add short rewordings to dev). |
| E-15 | Diagnosis of weak web-UI answers (29 Oct). Aryan asked "what do you know about the diseases in rice crops and how would you prevent them" (dropdown Potato, then Rice) | (a) 0 rice chunks contain "disease" (161 potato chunks do) → no correct answer exists. (b) 7 probe questions written for diagnosis on covered crops / uncovered topics: **4 of 7 pass the gate** (top-1 0.68–0.77; in-scope range 0.67–0.89). (c) 6 of 10 eval out-of-scope questions score ≥ 0.725 and are stopped only by the crop guard. (d) 9 of 150 top-5 chunks for eval in-scope questions come from another crop; BLB-in-rice probe retrieved 4 potato pages. (e) Crop routing (filter by crop named in the question): eval R@5 unchanged 0.767, FR 4/30, FA 0/10; BLB probe now refused; 3 of 7 probes still answered. (f) `gemma3:1b` self-refused 0 of 19 answered dev questions; on "fungicide for rice blast" 1b answered with herbicide facts, **4b refused**; 4b 73–187 s per answer on CPU | The eval set had a blind spot: no same-crop / uncovered-topic questions, so FA 0/10 overstated the gate. Similarity alone can't detect topic coverage. Plan in the project book (Iteration 2). |
| E-16 | Gate options on dev v2 (30 in-scope, 14 out-of-scope), 29 Oct | No routing, τ 0.725: FR 4/30, FA 4/14. Routing: FR 4, FA 3. Routing + τ 0.73: FR 5, FA 1. IDF word-coverage ≥ 0.5: FR 7–8, FA 1–2. Topic-gap rule (≥ 20): **FR 4, FA 1 (q47 mandi price)**. `gemma3:1b` yes/no judge: YES on all 14 subset questions incl. 3 unanswerable, 24–36 s each (prompt processing on CPU). Prompt v4 (placeholder example, check-first rule) with 1b: refused q47, but answers degraded ("Page 34.", "Recommended dose = 60 2.") and q46 invented diseases "Opaline, Silica, Lignin" | A small model can't be the safety check; the code-side gate must be. The topic-gap rule uses corpus statistics, not a hand list. |
| E-17 | HNSW vs exact search, 29 Oct | Same cached query vector, three separate processes: q52 top-1 0.6468 (Chroma) vs 0.6819 (exact) in 2 of 3 runs, overlap@5 4/5; other queries identical. Chroma HNSW config: ef_search 100, M 16 | Approximate search is not repeatable across runs here; switched to exact (D-58). Exact dev results identical over 3 runs. |
| E-18 | Dev v2 end to end with `gemma3:4b` (routing, exact search, three-signal gate, prompt v3), 29 Oct; `eval/results/answers_7_iter2_4b_dev.md` | Out-of-scope wrongly answered **0/14** (gate 13, model refused q47 itself). In-scope wrongly refused 5/30 (q20, q52, q53, q55 by gate; q50 by the model, correctly: retrieval had missed its page, rank 12). Generation p50 78.1 s, p95 102.3 s (27 answered, CPU); retrieval p50 0.005 s | 4b + gate together refuse every dev out-of-scope question. |
| E-19 | Automatic answer check (`eval/answer_check.py`): expected answer phrase in the answer | 4b: 18/25 answered in-scope contain the phrase; on the 19 both answered, 4b 12 vs 1b 10. Meta phrases ("the context states"): 4b 3/25, 1b 5/19. Prompt-example leak: 0 in both. Of 4b's 7 misses: q1, q4, q19, q21 = retrieval missed the page; q3, q11 = correct but worded differently; **q2 = wrong**: gave the direct-germination range (4–30 °C, opt. 25 °C) as the sporangia-formation range (3–26 °C, opt. 18–22 °C) from the same paragraph (p.29) | Phrase match undercounts correct answers and can't see faithfulness: manual grading stays. Even 4b mixes numbers within one passage → source list under every answer stays essential. |
| E-23 | q59 ("Which insecticide controls brown planthopper in rice?") end to end under D-60, 29 Oct | Passes the gate (topic check no longer fires on "insecticide": chance 0.06; similarity 0.7476); `gemma3:4b` answers "I could not find this in my documents." (102 s). Also checked: the `src/corpus.py` bullet line maps U+F0B7 → "•" (a terminal display showed "�"; 0 of 595 chunks contain U+FFFD) | Out-of-scope answered stays 0 of 22 end to end under v2; the model is the second line of defence it was chosen to be. |
| E-22 | Aryan in the web UI, 29 Oct 22:20: (a) "which type of weed removal strategy for my rice crop" (dropdown Potato) → routed to rice, answered from the weedy-rice article (stale seed-bed, mechanical weeding, herbicides) [2,3][5], top-4 passages all from that article; (b) same for wheat → refused: "The wheat documents never mention: type." (`t08`) | (a) grounded, but the dry-direct-seeded weed brief never reached the top 4, so the answer is narrower than the corpus allows. (b) false refusal: "type" is in 7% of other-crop chunks, chance of 0 in wheat's 33 chunks = 0.09 (not evidence). After D-60 it is refused by similarity (0.695 < 0.725), yet the wheat article answers it (Table 1 p.5: two manual weedings / Total (metsulfuron + sulfosulfuron)); a plainer wording passes at 0.727 | The v1 rule ignored crop size → D-60. Chatty wording lowers similarity → over-refusal work in Iteration 3 (e.g. strip pleasantries before embedding; per-document diversity in top-k). |
| E-21 | Review of eval v2 (29 Oct, 21:05): q45 "crown root initiation" moved from out-of-scope to in-scope `table` — Table 1, wheat p.5 lists "CRI Stage" as the first critical irrigation | The absent-term lint searched the spelled-out words, not the abbreviation, so it passed a wrong label. With the fix, dev = 31 in-scope / 13 out-of-scope: gate FR 5/31 (q45 refused by the topic-gap rule on "root"), FA 1/13; 4b end to end (E-18, run on the old label) becomes FR 6/31, FA 0/13 | Abbreviations defeat the lint and the topic-gap rule alike. Second topic-gap false positive after q29 (E-20). |
| E-20 | **Test split v2, run once** with the Iteration 2 config + `gemma3:4b`, 29 Oct; `eval/results/answers_7_iter2_4b_test.md` | Out-of-scope wrongly answered **0/9** (incl. 5 unseen uncovered-topic). In-scope wrongly refused **6/15**: q23, q27, q32, q64, q65 by τ 0.725; **q29 by the topic-gap rule** — "planting" is in 64 potato chunks and 0 rice chunks (rice text says "transplanted", "sowing"; the rule only strips a plural "s"). R@5 0.80 on the original 10 (unchanged), 0.60 on the 5 short. Answer phrase present 8/9 answered. Generation p50 94.4 s, p95 111.5 s | Safe on unseen data but over-refuses (40%). Not fixed here: changing the rule after seeing test would be tuning on test. Next: better word normalisation (lemmas), checked on new held-out questions, since the v2 test split is now seen. |
| E-14 | Eval with offline guard, all 40 questions (29 Oct) | R@5 0.767 (n=30), gate FR 4/30, FA 0/10; guard PASS, no non-loopback access | Our process stays on localhost; Wi-Fi-off / AWS no-egress test still to do. |

## Corrections (things that were wrong earlier)

- Design doc R6 said "brute-force exact search" → Chroma uses HNSW (approximate).
- I claimed the two sesame-weed test sentences share few words → they share "weeds" and "sesame"; the "til" query was added as a fairer test.
- `1067.pdf` was first matched to a DWR extension folder → it is the Current Science article.
- A third-party guide claimed bge-m3's score floor is ~0.42 → measured cricket sentence at 0.286.
- Chunk-count explanation: it's the **splitter**, not the loader.
- Bugs found in Aryan's code: `cosine_loop` used norm(a) twice; double `.pdf.pdf` extension; `print` inside the inner page loop.
- `config.py` froze `CHUNK_SIZE=500, CHUNK_OVERLAP=0` while the decision log chose 1000/100 → fixed to 1000/100 on 29 Oct.
- `docs/decision_log.md` §5 reported only test false accepts (0/4) for the gate; test false rejects are 3/10 (E-11).
- Demo laptop was "RTX 3050, VRAM unknown" in the handoff notes and "RTX 3070, 8 GB" in the decision log → confirm with `nvidia-smi`.
- On 29 Oct a Streamlit/Gradio page was proposed for Stage 6 before the original design doc was found; the doc's R11 chose FastAPI + static page, which is what was built.
- The first version assumed `httpx.ConnectError` is a subclass of Python's `ConnectionError` → it isn't; and the ollama client raises either depending on the call. Both are caught now.
- q45 (wheat irrigation at crown root initiation) was labelled out-of-scope; the wheat table covers it as "CRI Stage" (E-21). E-16/E-18 dev figures were computed with the wrong label; corrected figures are in E-21.
- D-37 / E-11 concluded Chroma HNSW = exact search on this corpus. That held for the questions tested then, but E-17 found a query where HNSW missed the nearest chunk in 2 of 3 runs. "Measured equal on 10 questions" was not enough evidence for "equal"; search is now exact (D-58).

## Open questions

- Friend's laptop: confirm GPU / VRAM with `nvidia-smi` (3050 or 3070?).
- Citation page number for journal articles: PDF page vs printed page.
- Licence checks: the two journal articles; confirm file 4's KRISHI record; fill `SOURCES.csv` TODOs.
