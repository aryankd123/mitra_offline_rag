# Stage 4 Generation Results (gemma3:1b, k=5, threshold=0.765)

## q1 (in_scope / table)
- **Question:** What is the economic threshold level (ETL) for aphids and whiteflies when monitoring potato pests?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[20]` phrases `['2/100 leaves']`
- **Top-1 Similarity:** `0.8901` (Gated: `False`)
- **Timings:** retrieve `0.137s`, generate `32.563s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `19` (`sim=0.8901`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `19` (`sim=0.7718`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `68` (`sim=0.7652`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `62` (`sim=0.7592`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `62` (`sim=0.7561`)

**Model Answer:**
> Threshold Levels
Thresholds are the levels of pest populations at which you should take pest control action if you want to

## q2 (in_scope / multi)
- **Question:** What temperature range and relative humidity are required for sporangia formation and indirect germination in potato late blight?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[29]` phrases `['3 to 26', '6 to 15']`
- **Top-1 Similarity:** `0.8391` (Gated: `False`)
- **Timings:** retrieve `0.164s`, generate `36.611s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `29` (`sim=0.8391`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `29` (`sim=0.7840`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `56` (`sim=0.7617`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `58` (`sim=0.7510`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `98` (`sim=0.7393`)

**Model Answer:**
> The context states that indirect germination generally occurs at temperature ranges of 6 to 15 °C (optimum 12 °C) by means of zoospore production, and that direct germination takes place under warm temperature (a range of 4 to 30 °C optimum being 25 °C).  The context also specifies that >80% is essential for lesions expansion, and >90% is required for spore formation.

## q3 (in_scope / plain)
- **Question:** How can bacterial wilt in potato be distinguished from fungal wilts in the field using a stem cut section?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[34]` phrases `['clear water']`
- **Top-1 Similarity:** `0.8141` (Gated: `False`)
- **Timings:** retrieve `0.134s`, generate `32.238s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `34` (`sim=0.8141`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `18` (`sim=0.7835`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `40` (`sim=0.7686`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `37` (`sim=0.7623`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `34` (`sim=0.7617`)

**Model Answer:**
> In clear water as shown in Fig. 1c.

## q4 (in_scope / conflict)
- **Question:** When should fenoxaprop-p-ethyl be sprayed in dry direct-sown rice and at what dose?
- **Expected:** `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` pages `[4, 7]` phrases `['25-28 dae', '18-20 das']`
- **Top-1 Similarity:** `0.7722` (Gated: `False`)
- **Timings:** retrieve `0.166s`, generate `37.389s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.7722`)
  - `[2]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7034`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.6982`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `2` (`sim=0.6903`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.6867`)

**Model Answer:**
> Recommended dose = 60

## q5 (in_scope / plain)
- **Question:** How is a 2% brine solution used as a preventive measure for weed management in dry direct-sown rice?
- **Expected:** `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` pages `[3]` phrases `['2% brine']`
- **Top-1 Similarity:** `0.8067` (Gated: `False`)
- **Timings:** retrieve `0.139s`, generate `35.867s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.8067`)
  - `[2]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.8052`)
  - `[3]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `3` (`sim=0.7766`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `2` (`sim=0.7699`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7608`)

**Model Answer:**
> Cleaning seeds by dipping in 2% brine solution helps in selection of high-density seeds and separation of floating weed seeds.

## q6 (in_scope / plain)
- **Question:** Why can post-emergence selective herbicides not be used to control weedy rice in a normal paddy field and how does Clearfield rice solve this?
- **Expected:** `rice_weedy-rice-options_dwsr_2013_article` pages `[5]` phrases `['clearfield']`
- **Top-1 Similarity:** `0.8585` (Gated: `False`)
- **Timings:** retrieve `0.195s`, generate `42.323s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.8585`)
  - `[2]` `rice_weedy-rice-options_dwsr_2013_article` page `1` (`sim=0.7911`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7869`)
  - `[4]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7847`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7799`)

**Model Answer:**
> Post-emergence selective herbicides are not used to control weedy rice in a normal paddy field because of the presence of a biosimilar of AA genome complex (Box 2) in the conspecific weedy rice (Oryza sativa f. spontanea, Poaceae). The text states that the conspecific weedy rice (Oryza sativa f. spontanea, Poaceae) is a biosimilar of AA genome complex (Box 2) and that the emanating smoke from these herbicides is a major source of air pollution, leading to bans in several countries.

## q7 (in_scope / table)
- **Question:** What are the recommended seed rate and fertilizer dose (N:P2O5:K2O) for improved wheat varieties VL Gehun 907 and VL Gehun 953 compared to existing farmer practices?
- **Expected:** `wheat_rust-resistant-varieties-economics_vpkas_2020_article` pages `[5]` phrases `['120:60:40']`
- **Top-1 Similarity:** `0.7776` (Gated: `False`)
- **Timings:** retrieve `0.202s`, generate `43.214s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `4` (`sim=0.7776`)
  - `[2]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `5` (`sim=0.7708`)
  - `[3]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.7701`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.7636`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.7582`)

**Model Answer:**
> The context states that the recommended fertilizer dose for VL Gehun 907 and VL Gehun 953 is 120:60:40 kg N:P2O5:K2O, while the recommended practice for local varieties is 125 kg/ha.

## q8 (in_scope / paraphrase)
- **Question:** Without using chemicals how can a farmer use summer heat and plastic sheets to kill soil-borne black scurf fungus in potato fields?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[56]` phrases `['solarization']`
- **Top-1 Similarity:** `0.7743` (Gated: `False`)
- **Timings:** retrieve `0.141s`, generate `30.14s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `123` (`sim=0.7743`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `60` (`sim=0.7713`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `56` (`sim=0.7636`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `57` (`sim=0.7544`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `37` (`sim=0.7512`)

**Model Answer:**
> The context states that soil solarization by using polythene mulch during peak summer increases the soil temperature to 45-61 0C which kills harmful bacteria and other pathogens.

## q9 (out_of_scope / out_of_scope)
- **Question:** Which herbicide is recommended to control weeds in a sesame (til) crop?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.7557` (Gated: `True`)
- **Timings:** retrieve `0.122s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7557`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `92` (`sim=0.7368`)
  - `[3]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7328`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `2` (`sim=0.7300`)
  - `[5]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.7177`)

**Model Answer:**
> I could not find this in my documents.

## q10 (out_of_scope / out_of_scope)
- **Question:** What is the latest installment amount and eligibility criteria under the PM-KISAN government scheme for farmers?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.6249` (Gated: `True`)
- **Timings:** retrieve `0.118s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.6249`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `13` (`sim=0.6188`)
  - `[3]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `4` (`sim=0.6067`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.6065`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `136` (`sim=0.6055`)

**Model Answer:**
> I could not find this in my documents.
