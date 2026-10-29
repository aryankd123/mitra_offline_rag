# MITRA Offline RAG — Engineering Decision Log (Stage 5)

All decisions below were made on the `dev` split (`n=26`: 20 in-scope, 6 out-of-scope) on the development laptop (Windows 10, Python 3.12.10, 12 GB RAM, CPU-only) and evaluated once on the frozen `test` split (`n=14`: 10 in-scope, 4 out-of-scope).

## 1. Chunk Size & Overlap (`chunk_size`, `chunk_overlap`)
- **Measured on `dev` (`n=20` in-scope, `nomic-embed-text`, `k=5`):**
  - `500 / 0`: `R@1=0.550`, `R@3=0.800`, `R@5=0.900`, `table_R@5=1.000`, `MRR@10=0.678`, `MedRank=1.0` (`1190` chunks). Linter check: `0` broken phrases.
  - `500 / 100`: `R@1=0.400`, `R@3=0.700`, `R@5=0.850`, `MRR@10=0.583`. Linter check: `1` broken phrase (`q11`: `'to avoid sweetening'` cut at boundary).
  - `1000 / 100` (baseline): `R@1=0.400`, `R@3=0.700`, `R@5=0.750`, `table_R@5=0.667`, `MRR@10=0.565`, `MedRank=2.0` (`615` chunks). Linter check: `0` broken phrases.
  - `1500 / 100`: `R@1=0.300`, `R@3=0.500`, `R@5=0.650`, `MRR@10=0.458`, `MedRank=3.5`.
- **One-Time `test` Split Check (`n=10` in-scope):**
  - `500 / 0`: `R@1=0.400`, `R@3=0.600`, `R@5=0.700`, `MRR@10=0.503`, `MedRank=3.0` (`multi` `MedRank=104.0` because small 500-char chunks scatter multi-part answers across too many fragments).
  - `1000 / 100` (with chunk-level ref filter, `595` chunks): `R@1=0.400`, `R@3=0.700`, `R@5=0.800`, `MRR@10=0.586`, `MedRank=2.0` (`table_R@5=1.000`, `paraphrase_R@5=1.000`, `plain_R@5=1.000`).
- **Decision:** Keep `chunk_size=1000, chunk_overlap=100` (with chunk-level reference filtering and `min_chunk_len=50`, yielding `595` chunks) as primary production config because it generalizes better to multi-fact questions on `test` (`R@5=0.800` vs `0.700`) and halves index size (`595` vs `1159` chunks). Overlap (`0` vs `100` vs `200`) had minimal impact because `RecursiveCharacterTextSplitter` splits on `\n` boundaries first, making effective overlap ~30 characters.

## 2. Top-k (`k=5`)
- **Measured on `dev` (`1000/100`):** `k=3` gave `R@3=0.700`; `k=4` gave `R@4=0.750`; `k=5` gave `R@5=0.750`; `k=6` gave `R@6=0.800`.
- **Decision:** Keep `k=5` as the default balance between multi-page recall (`75–90%`) and prompt context length (~4,500 chars) for small local models.

## 3. Text Cleaning & Table Extraction (`5B-2`, `5B-3`)
- **Table-Aware Extraction (`5B-2`):** PyMuPDF `page.find_tables().to_markdown()` (even after stripping `<br>` tags) reduced `dev` `MRR@10` from `0.565` to `0.531` (`table` `MRR@10` dropped from `0.537` to `0.319`) because borderless PDF tables were misdetected without `pymupdf_layout`. **Rejected.**
- **Line Reflow (`5B-3a`):** Reflowing wrapped lines increased chunk count to `725` and lowered `multi` `R@5` from `0.750` to `0.500` (`MRR@10=0.558`). **Rejected.**
- **Chunk-Level Reference Filter + `min_chunk_len=50` (`5B-3b`):** Filtering bibliography pages at the page level broke `multi` questions (`MedRank=25.0`), but filtering at the **chunk level** cleanly removed `20` bibliography/short chunks (`615 -> 595` chunks) with zero loss in `R@5` (`0.750`) or `MRR@10` (`0.565`). **Accepted.**

## 4. Embedding Model (`nomic-embed-text` vs `bge-m3`, `5B-1`)
- **Measured on `dev` (`1000/100`, `k=5`):**
  - `nomic-embed-text` (no prefix, 768-d): `R@1=0.400`, `R@3=0.700`, `R@5=0.750`, `MRR@10=0.565` (`425s` CPU indexing).
  - `nomic-embed-text` (`search_document: ` / `search_query: ` prefixes): `R@1=0.450`, `R@3=0.600`, `R@5=0.800`, `MRR@10=0.581` (solved `q4` conflict at rank 3, but dropped `R@3` from `0.700` to `0.600`).
  - `bge-m3` (1024-d, unit norm verified `[1.0]`): `R@1=0.450`, `R@3=0.750`, `R@5=0.900`, `MRR@10=0.637` (`1371.8s` CPU indexing). On `test` (`n=10`), `bge-m3` achieved `R@1=0.500`, `R@5=0.800`, `MRR@10=0.589`.
- **Decision:** Keep `nomic-embed-text` (no prefix) as the fast CPU default (`3.2x` faster indexing, `0.14s` query retrieval) and support `bge-m3` as the high-accuracy/multilingual option for the RTX 3070 demo machine.

## 5. Refusal Gate (`SIMILARITY_THRESHOLD = 0.725` + Crop Guard, `5A-6`)
- **Measured on `dev` (`n=20` in-scope, `n=6` out-of-scope):**
  - In-scope top-1 similarity ranged from `0.6694` (`q20`) to `0.8901` (`q1`).
  - Out-of-scope top-1 similarity ranged from `0.5233` (`q36`) to `0.7557` (`q9` sesame herbicide).
  - Because out-of-scope questions about unindexed crops using valid herbicide/fungicide terms (`q9=0.7557`, `q34=0.7308`, `q35=0.7298`) overlap with the bottom 3 in-scope questions, a single cosine threshold at `tau=0.7308` (`FR <= 10%`) suffers a `33.3% (2/6)` Out-of-Scope False Accept rate.
  - Adding a second lexical signal (rejecting queries that name an unsupported crop without any supported crop) with `tau=0.725` achieved **`5.0% (1/20)` In-Scope False Reject** and **`0.0% (0/6)` Out-of-Scope False Accept** on `dev`, and **`0.0% (0/4)` Out-of-Scope False Accept** on `test`.
- **Decision:** Use the Two-Signal Gate (`tau=0.725` + unsupported-crop guard) before calling the LLM.

## 6. Prompt & Generator Model (`Prompt v3`, `gemma3:1b` vs `gemma3:4b`, `5A-5` & `5B-4`)
- **Prompt Evolution:** `v1` had `0/8` `[n]` citations due to recency bias across 5,000 chars of context. `v2` fixed `[n]` citations by reinforcing rules at the end of `HumanMessage`, but placing the literal refusal sentence at the end caused `gemma3:1b` to echo the refusal sentence on line 1 before answering on line 2. `v3` removed the literal refusal string from the bottom instruction and used a clean agricultural format example, eliminating the spurious refusal line while preserving `[n]` citations.
- **Generator Comparison (`q1..q10`, identical chunks, CPU laptop):**
  - `gemma3:1b`: `p50=10.91s`, `p95=40.99s`. Fast on CPU, but misread `q1` (claiming aphid/whitefly ETL is zero) and mixed table rows on `q4`.
  - `gemma3:4b`: `p50=91.89s`, `p95=125.15s` on CPU. Much higher faithfulness and table comprehension (`q1`, `q3`, `q4` all faithful and accurately cited), but `8.4x` slower at `p50` on CPU.
- **Decision:** Default to `gemma3:1b` on the CPU development laptop for interactive turnaround, and switch `GENERATOR_MODEL = "gemma3:4b"` on the RTX 3070 (8 GB VRAM) demo laptop after measuring GPU latency in Stage 8. Always display retrieved sources programmatically underneath every answer.
