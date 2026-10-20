# Stage 3 Retrieval Evaluation Results

## 1. Hit@k Table (In-Scope & Out-of-Scope)

| ID | Type | Tag | Hit@1 | Hit@3 | Hit@5 | First Rank | Top-1 Similarity |
|---|---|---|---|---|---|---|---|
| q1 | in_scope | table | False | False | False | None | 0.8901 |
| q2 | in_scope | multi | True | True | True | 1 | 0.8391 |
| q3 | in_scope | plain | True | True | True | 1 | 0.8141 |
| q4 | in_scope | conflict | False | False | False | None | 0.7722 |
| q5 | in_scope | plain | False | True | True | 3 | 0.8067 |
| q6 | in_scope | plain | True | True | True | 1 | 0.8585 |
| q7 | in_scope | table | False | True | True | 2 | 0.7776 |
| q8 | in_scope | paraphrase | False | True | True | 3 | 0.7743 |
| q9 | out_of_scope | out_of_scope | None | None | None | None | 0.7557 |
| q10 | out_of_scope | out_of_scope | None | None | None | None | 0.6249 |

## 2. Chroma HNSW vs. Brute-Force NumPy Top-5

| ID | Overlap@5 | Top-1 Same | Chroma Top-1 ID | Brute-Force Top-1 ID |
|---|---|---|---|---|
| q1 | 5/5 | True | `potato_disease-pest-management_cpri_2016_manual:p19:c2` | `potato_disease-pest-management_cpri_2016_manual:p19:c2` |
| q2 | 5/5 | True | `potato_disease-pest-management_cpri_2016_manual:p29:c1` | `potato_disease-pest-management_cpri_2016_manual:p29:c1` |
| q3 | 5/5 | True | `potato_disease-pest-management_cpri_2016_manual:p34:c2` | `potato_disease-pest-management_cpri_2016_manual:p34:c2` |
| q4 | 5/5 | True | `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief:p6:c0` | `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief:p6:c0` |
| q5 | 5/5 | True | `rice_weedy-rice-options_dwsr_2013_article:p4:c0` | `rice_weedy-rice-options_dwsr_2013_article:p4:c0` |
| q6 | 5/5 | True | `rice_weedy-rice-options_dwsr_2013_article:p5:c1` | `rice_weedy-rice-options_dwsr_2013_article:p5:c1` |
| q7 | 5/5 | True | `wheat_rust-resistant-varieties-economics_vpkas_2020_article:p4:c5` | `wheat_rust-resistant-varieties-economics_vpkas_2020_article:p4:c5` |
| q8 | 5/5 | True | `potato_disease-pest-management_cpri_2016_manual:p123:c1` | `potato_disease-pest-management_cpri_2016_manual:p123:c1` |
| q9 | 5/5 | True | `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief:p7:c0` | `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief:p7:c0` |
| q10 | 5/5 | True | `wheat_rust-resistant-varieties-economics_vpkas_2020_article:p3:c1` | `wheat_rust-resistant-varieties-economics_vpkas_2020_article:p3:c1` |

## 3. Score Distribution Summary

- **Min in-scope top-1 similarity:** `0.7722`
- **Max out-of-scope top-1 similarity:** `0.7557`
- **Gap (`min_in - max_out`):** `0.0165`
