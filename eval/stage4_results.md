# Stage 4 Generation Results (gemma3:1b, k=5, threshold=0.765)

## q1 (in_scope / table)
- **Question:** What is the economic threshold level (ETL) for aphids and whiteflies when monitoring potato pests?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[20]` phrases `['2/100 leaves']`
- **Top-1 Similarity:** `0.8901` (Gated: `False`)
- **Timings:** retrieve `0.125s`, generate `32.653s`
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
- **Timings:** retrieve `0.306s`, generate `39.125s`
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
- **Timings:** retrieve `0.18s`, generate `28.285s`
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
- **Timings:** retrieve `0.259s`, generate `31.854s`
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
- **Timings:** retrieve `0.556s`, generate `33.281s`
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
- **Timings:** retrieve `0.44s`, generate `42.822s`
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
- **Timings:** retrieve `0.203s`, generate `42.477s`
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
- **Timings:** retrieve `0.202s`, generate `31.022s`
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
- **Timings:** retrieve `0.215s`, generate `0.0s`
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
- **Timings:** retrieve `0.233s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.6249`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `13` (`sim=0.6188`)
  - `[3]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `4` (`sim=0.6067`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.6065`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `136` (`sim=0.6055`)

**Model Answer:**
> I could not find this in my documents.

## q11 (in_scope / multi)
- **Question:** What is the effective application rate of CIPC sprout inhibitor per kg of potato tubers and at what temperature should processing potatoes be stored to avoid sweetening?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[9, 11]` phrases `['25 mg a.i.', 'to avoid sweetening']`
- **Top-1 Similarity:** `0.8540` (Gated: `False`)
- **Timings:** retrieve `0.241s`, generate `30.554s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `131` (`sim=0.8540`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `9` (`sim=0.8430`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `131` (`sim=0.8421`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `11` (`sim=0.7855`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `119` (`sim=0.7400`)

**Model Answer:**
> The effective application rate of CIPC (isopropyl-N-(3-chlorophenyl) carbamate) is 25 mg a.i. per kg tubers at 10-12°C.

## q12 (in_scope / paraphrase)
- **Question:** How much foreign exchange money does India save each year by producing its own healthy breeder seed tubers instead of importing them from Europe?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[8]` phrases `['484 million']`
- **Top-1 Similarity:** `0.7827` (Gated: `False`)
- **Timings:** retrieve `0.385s`, generate `28.953s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `110` (`sim=0.7827`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `8` (`sim=0.7536`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `10` (`sim=0.7350`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `10` (`sim=0.7299`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `11` (`sim=0.7008`)

**Model Answer:**
> I could not find this in my documents.

## q13 (in_scope / plain)
- **Question:** Which potato variety imported from Denmark in 1953 introduced the wart pathogen into the Darjeeling hills?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[14]` phrases `['furore']`
- **Top-1 Similarity:** `0.8375` (Gated: `False`)
- **Timings:** retrieve `0.582s`, generate `28.236s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `14` (`sim=0.8375`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `58` (`sim=0.8060`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `13` (`sim=0.7669`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `36` (`sim=0.7609`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `14` (`sim=0.7567`)

**Model Answer:**
> With the introduction of variety Furore from Denmark in 1953

## q14 (in_scope / plain)
- **Question:** How many grams of Streptocycline are required for 1 hectare when applied at a 50 ppm concentration in 500 litres of spray solution?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[21]` phrases `['25 g']`
- **Top-1 Similarity:** `0.7606` (Gated: `True`)
- **Timings:** retrieve `0.298s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `21` (`sim=0.7606`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `21` (`sim=0.6916`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `23` (`sim=0.6718`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.6570`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `20` (`sim=0.6540`)

**Model Answer:**
> I could not find this in my documents.

## q15 (in_scope / table)
- **Question:** According to Table 2 on pesticide compatibility, is Lime Sulphur compatible or incompatible when mixed with Mancozeb 75 WP?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[22]` phrases `['lime sulphur + mancozeb 75 wp']`
- **Top-1 Similarity:** `0.8186` (Gated: `False`)
- **Timings:** retrieve `0.155s`, generate `35.228s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `22` (`sim=0.8186`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `22` (`sim=0.7845`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `22` (`sim=0.7281`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `23` (`sim=0.7253`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `23` (`sim=0.6747`)

**Model Answer:**
> Incompatible

## q16 (in_scope / paraphrase)
- **Question:** Why must farm workers avoid wearing footwear made of animal hide or woven cloth when spraying agricultural chemicals?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[27]` phrases `['leather or fabric shoes']`
- **Top-1 Similarity:** `0.7286` (Gated: `True`)
- **Timings:** retrieve `0.23s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `27` (`sim=0.7286`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `26` (`sim=0.6997`)
  - `[3]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.6478`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `115` (`sim=0.6433`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `67` (`sim=0.6332`)

**Model Answer:**
> I could not find this in my documents.

## q17 (in_scope / plain)
- **Question:** What rate of stable bleaching powder per hectare should be applied in furrows at planting time to reduce bacterial wilt in potato?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[37]` phrases `['12 kg/ha']`
- **Top-1 Similarity:** `0.8259` (Gated: `False`)
- **Timings:** retrieve `0.186s`, generate `24.315s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `37` (`sim=0.8259`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `37` (`sim=0.7468`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `123` (`sim=0.7464`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `38` (`sim=0.7390`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `9` (`sim=0.7362`)

**Model Answer:**
> 32

## q18 (in_scope / paraphrase)
- **Question:** Planting which cucurbit vegetable as a trap crop causes whiteflies to lose their ability to transmit apical leaf curl virus after feeding on it?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[67]` phrases `['cucumber']`
- **Top-1 Similarity:** `0.7951` (Gated: `False`)
- **Timings:** retrieve `0.224s`, generate `27.74s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `48` (`sim=0.7951`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `67` (`sim=0.7738`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `48` (`sim=0.7636`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `112` (`sim=0.7466`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `62` (`sim=0.7451`)

**Model Answer:**
> 6.

## q19 (in_scope / multi)
- **Question:** What row spacing in centimetres is required in dry direct-sown rice when using a mechanical power weeder and at how many days after emergence is it operated?
- **Expected:** `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` pages `[4]` phrases `['25 cm', '30 dae']`
- **Top-1 Similarity:** `0.7644` (Gated: `True`)
- **Timings:** retrieve `0.225s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `2` (`sim=0.7644`)
  - `[2]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7317`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `6` (`sim=0.7281`)
  - `[4]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7138`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7063`)

**Model Answer:**
> I could not find this in my documents.

## q20 (in_scope / paraphrase)
- **Question:** Why should a clogged herbicide nozzle never be cleared by blowing air through it with your lips?
- **Expected:** `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` pages `[6]` phrases `['blowing on them with the mouth']`
- **Top-1 Similarity:** `0.6694` (Gated: `True`)
- **Timings:** retrieve `0.131s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `5` (`sim=0.6694`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `94` (`sim=0.6583`)
  - `[3]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `5` (`sim=0.6556`)
  - `[4]` `rice_weedy-rice-options_dwsr_2013_article` page `2` (`sim=0.6490`)
  - `[5]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.6480`)

**Model Answer:**
> I could not find this in my documents.

## q21 (in_scope / plain)
- **Question:** Up to what percentage of applied fertilizer nitrogen can weedy red rice consume in a paddy field?
- **Expected:** `rice_weedy-rice-options_dwsr_2013_article` pages `[1]` phrases `['60%']`
- **Top-1 Similarity:** `0.7408` (Gated: `True`)
- **Timings:** retrieve `0.131s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.7408`)
  - `[2]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7328`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.7312`)
  - `[4]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7308`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7276`)

**Model Answer:**
> I could not find this in my documents.

## q22 (in_scope / multi)
- **Question:** What was the Seed Replacement Rate (SRR) in Uttarakhand and how did average wheat productivity in the hills compare to the tarai plains?
- **Expected:** `wheat_rust-resistant-varieties-economics_vpkas_2020_article` pages `[1]` phrases `['31.6', '1028']`
- **Top-1 Similarity:** `0.8225` (Gated: `False`)
- **Timings:** retrieve `0.177s`, generate `42.341s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.8225`)
  - `[2]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.7834`)
  - `[3]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.7657`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.7616`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.7595`)

**Model Answer:**
> Low seed replacement rate, problems in distribution of seed, weak extension mechanism, and lack of awareness among the farmers were the major factors behind the lack of promotion of certified seeds in the state (State Agriculture Plan, Uttarakhand, 2012-17). As a result of the above described factors, majority of the hill farmers are still cultivating indigenous wheat varieties which can be characterized by having tall and weak stem, more biological yield, small ear head, low harvest index, late maturity, less responsive to higher doses of inputs, and susceptible to rusts and various other diseases.

## q23 (in_scope / table)
- **Question:** According to the table of spray volume rates, which range in litres per hectare is classed as low volume for field crops?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[23]` phrases `['low volume 50-200']`
- **Top-1 Similarity:** `0.7244` (Gated: `True`)
- **Timings:** retrieve `0.284s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `23` (`sim=0.7244`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `21` (`sim=0.7004`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `24` (`sim=0.6713`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.6556`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.6534`)

**Model Answer:**
> I could not find this in my documents.

## q24 (in_scope / multi)
- **Question:** Which fungus causes early blight concentric target-spot rings on potato leaves and what concentration of mancozeb 75% WP is sprayed to manage it?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[31, 32]` phrases `['alternaria solani', '0.2%']`
- **Top-1 Similarity:** `0.7787` (Gated: `False`)
- **Timings:** retrieve `0.201s`, generate `30.414s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `30` (`sim=0.7787`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `31` (`sim=0.7782`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `30` (`sim=0.7502`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `60` (`sim=0.7384`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `31` (`sim=0.7340`)

**Model Answer:**
> 75%WP/chlorothalonil 75%WP/propineb 70%WP

## q25 (in_scope / plain)
- **Question:** For how many minutes should seed tubers be dipped in a 3% boric acid solution before storage to prevent soft rot and common scab?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[40]` phrases `['30 min']`
- **Top-1 Similarity:** `0.8009` (Gated: `False`)
- **Timings:** retrieve `0.367s`, generate `29.847s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `42` (`sim=0.8009`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `40` (`sim=0.7701`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `57` (`sim=0.7649`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `72` (`sim=0.7598`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `57` (`sim=0.7468`)

**Model Answer:**
> 30

## q26 (in_scope / paraphrase)
- **Question:** For how long can the cysts of the nematode that attacks potatoes stay alive in the ground when no host plant is grown there?
- **Expected:** `potato_disease-pest-management_cpri_2016_manual` pages `[76]` phrases `['20-30 years']`
- **Top-1 Similarity:** `0.7646` (Gated: `True`)
- **Timings:** retrieve `0.476s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `74` (`sim=0.7646`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `76` (`sim=0.7631`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `75` (`sim=0.7622`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `57` (`sim=0.7420`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `74` (`sim=0.7328`)

**Model Answer:**
> I could not find this in my documents.

## q27 (in_scope / paraphrase)
- **Question:** Which tip shape should a knapsack sprayer have for putting weedkiller on a rice field?
- **Expected:** `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` pages `[5]` phrases `['flat fan nozzle']`
- **Top-1 Similarity:** `0.7023` (Gated: `True`)
- **Timings:** retrieve `0.225s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `5` (`sim=0.7023`)
  - `[2]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `5` (`sim=0.6993`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.6893`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.6860`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `6` (`sim=0.6848`)

**Model Answer:**
> I could not find this in my documents.

## q28 (in_scope / table)
- **Question:** According to the recommended herbicides table for dry direct-sown rice, what is the application dose in g a.i./ha for Cyhalofop-butyl (Clincher)?
- **Expected:** `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` pages `[7]` phrases `['cyhalofop-butyl']`
- **Top-1 Similarity:** `0.8262` (Gated: `False`)
- **Timings:** retrieve `0.385s`, generate `32.57s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.8262`)
  - `[2]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.7577`)
  - `[3]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7357`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7342`)
  - `[5]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `6` (`sim=0.7218`)

**Model Answer:**
> 100

## q29 (in_scope / paraphrase)
- **Question:** Which dark-pigmented rice varieties does the article suggest planting to slowly wipe out the red-grained weed from a field over a few years?
- **Expected:** `rice_weedy-rice-options_dwsr_2013_article` pages `[5]` phrases `['p502']`
- **Top-1 Similarity:** `0.7779` (Gated: `False`)
- **Timings:** retrieve `0.367s`, generate `61.377s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weedy-rice-options_dwsr_2013_article` page `1` (`sim=0.7779`)
  - `[2]` `rice_weedy-rice-options_dwsr_2013_article` page `6` (`sim=0.7607`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `1` (`sim=0.7569`)
  - `[4]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.7495`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.7456`)

**Model Answer:**
> Table 1. Weedy rice infestation across the world 
Country 
Infestation (%) 
Reference 
 
Europe 
40–75 
44 
Italy 
70 
45 
Malaysia 
74 
28, 29 
USA (Arkansas) 
60 
46, 47 
Brazil 
40 
48, 49 
Senegal 
55 
48, 49 
Cuba 
80 
48, 49 
Costa Rica 
60 
48, 49 
 
150 kg/ha. In some Asian countries farmers are using 
high seeding rates to suppress weeds and compensate for 
poor seed quality and crop establishment36. Line sowing  
using tractor-mounted seeders can ease detection of weeds 
as all inter-row rice would be weedy rice. And these emerging 
plants can be easily rouged manually or by use of chemi-
cals. Application of glyphosate, paraquat to leaf blades of 
weedy rice through special wick applicators may be help-
ful39
.

## q30 (in_scope / table)
- **Question:** According to Table 1 on global weedy rice infestation, what percentage of rice area is infested in Cuba?
- **Expected:** `rice_weedy-rice-options_dwsr_2013_article` pages `[5]` phrases `['cuba']`
- **Top-1 Similarity:** `0.7967` (Gated: `False`)
- **Timings:** retrieve `0.225s`, generate `32.902s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.7967`)
  - `[2]` `rice_weedy-rice-options_dwsr_2013_article` page `3` (`sim=0.7377`)
  - `[3]` `rice_weedy-rice-options_dwsr_2013_article` page `2` (`sim=0.7209`)
  - `[4]` `rice_weedy-rice-options_dwsr_2013_article` page `4` (`sim=0.7046`)
  - `[5]` `rice_weedy-rice-options_dwsr_2013_article` page `5` (`sim=0.6971`)

**Model Answer:**
> 80

## q31 (in_scope / table)
- **Question:** According to Table 1 in the Uttarakhand wheat study, what seed treatment chemical and dose per kg of seed was used in the FLD intervention?
- **Expected:** `wheat_rust-resistant-varieties-economics_vpkas_2020_article` pages `[5]` phrases `['2.5 g carboxin']`
- **Top-1 Similarity:** `0.7505` (Gated: `True`)
- **Timings:** retrieve `0.879s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `5` (`sim=0.7505`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `50` (`sim=0.7169`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `91` (`sim=0.7136`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.7134`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.7062`)

**Model Answer:**
> I could not find this in my documents.

## q32 (in_scope / multi)
- **Question:** Which wild animal caused the most crop raiding damage in the Himalayan hills and what Rank Based Quotient (RBQ) score did wildlife damage receive in Table 7?
- **Expected:** `wheat_rust-resistant-varieties-economics_vpkas_2020_article` pages `[4, 6]` phrases `['wild pig', '93.9']`
- **Top-1 Similarity:** `0.6847` (Gated: `True`)
- **Timings:** retrieve `0.789s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `4` (`sim=0.6847`)
  - `[2]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `4` (`sim=0.6703`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `71` (`sim=0.6516`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.6488`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.6460`)

**Model Answer:**
> I could not find this in my documents.

## q33 (out_of_scope / out_of_scope)
- **Question:** What is the farmer premium percentage for Kharif foodcrops under the Pradhan Mantri Fasal Bima Yojana (PMFBY)?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.6957` (Gated: `True`)
- **Timings:** retrieve `0.268s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.6957`)
  - `[2]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.6834`)
  - `[3]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.6748`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `7` (`sim=0.6678`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.6667`)

**Model Answer:**
> I could not find this in my documents.

## q34 (out_of_scope / out_of_scope)
- **Question:** What pre-emergence dose of oxadiargyl is recommended per hectare for weed control in cumin (jeera) fields?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.7308` (Gated: `True`)
- **Timings:** retrieve `0.368s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `4` (`sim=0.7308`)
  - `[2]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7244`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `92` (`sim=0.7228`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `5` (`sim=0.7224`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `93` (`sim=0.7100`)

**Model Answer:**
> I could not find this in my documents.

## q35 (out_of_scope / out_of_scope)
- **Question:** Which systemic fungicide should be sprayed to control powdery mildew and anthracnose in mango orchards?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.7298` (Gated: `True`)
- **Timings:** retrieve `0.277s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `85` (`sim=0.7298`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `90` (`sim=0.7084`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `85` (`sim=0.6941`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `30` (`sim=0.6911`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `91` (`sim=0.6843`)

**Model Answer:**
> I could not find this in my documents.

## q36 (out_of_scope / out_of_scope)
- **Question:** What UART baud rate and parity settings are used by the Jetson Xavier to send steering commands to the Arduino?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.5233` (Gated: `True`)
- **Timings:** retrieve `0.276s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `17` (`sim=0.5233`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `104` (`sim=0.5216`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `84` (`sim=0.5185`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `3` (`sim=0.5131`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `85` (`sim=0.5131`)

**Model Answer:**
> I could not find this in my documents.

## q37 (out_of_scope / out_of_scope)
- **Question:** What post-emergence dose of quizalofop-ethyl is recommended to control grassy weeds in blackgram (urdbean)?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.7624` (Gated: `True`)
- **Timings:** retrieve `0.283s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `7` (`sim=0.7624`)
  - `[2]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `4` (`sim=0.7444`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `92` (`sim=0.7302`)
  - `[4]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `5` (`sim=0.7218`)
  - `[5]` `rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief` page `4` (`sim=0.7061`)

**Model Answer:**
> I could not find this in my documents.

## q38 (out_of_scope / out_of_scope)
- **Question:** What is the economic threshold level (ETL) for pink bollworm in Bt cotton using pheromone traps?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.7764` (Gated: `False`)
- **Timings:** retrieve `0.272s`, generate `23.732s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `19` (`sim=0.7764`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `25` (`sim=0.6784`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `19` (`sim=0.6624`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `114` (`sim=0.6558`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `82` (`sim=0.6514`)

**Model Answer:**
> I could not find this in my documents.

## q39 (out_of_scope / out_of_scope)
- **Question:** What is the interest subvention percentage offered on short-term crop loans through a Kisan Credit Card (KCC)?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.6162` (Gated: `True`)
- **Timings:** retrieve `0.428s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `8` (`sim=0.6162`)
  - `[2]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.6004`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `124` (`sim=0.5936`)
  - `[4]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `1` (`sim=0.5931`)
  - `[5]` `wheat_rust-resistant-varieties-economics_vpkas_2020_article` page `4` (`sim=0.5912`)

**Model Answer:**
> I could not find this in my documents.

## q40 (out_of_scope / out_of_scope)
- **Question:** How should blister blight disease be managed using copper oxychloride and hexaconazole in Assam tea plantations?
- **Expected:** `` pages `[]` phrases `[]`
- **Top-1 Similarity:** `0.7330` (Gated: `True`)
- **Timings:** retrieve `0.323s`, generate `0.0s`
- **Top-5 Sources Passed to Prompt:**
  - `[1]` `potato_disease-pest-management_cpri_2016_manual` page `30` (`sim=0.7330`)
  - `[2]` `potato_disease-pest-management_cpri_2016_manual` page `57` (`sim=0.7095`)
  - `[3]` `potato_disease-pest-management_cpri_2016_manual` page `60` (`sim=0.7038`)
  - `[4]` `potato_disease-pest-management_cpri_2016_manual` page `30` (`sim=0.7035`)
  - `[5]` `potato_disease-pest-management_cpri_2016_manual` page `123` (`sim=0.6914`)

**Model Answer:**
> I could not find this in my documents.
