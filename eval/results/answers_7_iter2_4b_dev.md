# Stage 6 end-to-end answers (dev, gemma3:4b, prompt v3, k=5)
Retrieval latency over 44 questions: p50=0.005s, p95=0.014s
Generation latency over 27 answered questions: p50=78.11s, p95=102.27s
End-to-end refusals (gate or model): in-scope wrongly refused 5/30 ['q20', 'q50', 'q52', 'q53', 'q55']; out-of-scope wrongly answered 0/14 []; refused by the model itself: ['q47', 'q50']
Machine: Windows-10-10.0.19045-SP0, Intel64 Family 6 Model 78 Stepping 3, GenuineIntel; offline guard off


## q1 (in_scope / table) | top_sim=0.8901 | gen=103.629s
**Q:** What is the economic threshold level (ETL) for aphids and whiteflies when monitoring potato pests?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.20 — 2/100 leaves

**A:** Economic threshold levels (ETLs) for common potato pests are given in Table 1 [1]. Monitoring is not necessary in situations where a pest is continually present and the threshold is zero, such as for viral diseases in seed potatoes [1]. The morphological identification and monitoring the population of insect vectors, including aphids and whiteflies, is crucial for healthy potato production [4].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 19 (similarity=0.8901)
  [2] potato_disease-pest-management_cpri_2016_manual, page 19 (similarity=0.7718)
  [3] potato_disease-pest-management_cpri_2016_manual, page 68 (similarity=0.7652)
  [4] potato_disease-pest-management_cpri_2016_manual, page 62 (similarity=0.7592)
  [5] potato_disease-pest-management_cpri_2016_manual, page 62 (similarity=0.7561)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q2 (in_scope / multi) | top_sim=0.8391 | gen=84.752s
**Q:** What temperature range and relative humidity are required for sporangia formation and indirect germination in potato late blight?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.29 — 3 to 26; 6 to 15

**A:** Sporangia formation requires high relative humidity (>90%) and a temperature range of 4 to 30 °C, with an optimum of 25 °C [2]. Indirect germination occurs at a temperature range of 6 to 15 °C (optimum 12 °C) by means of zoospore production [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 29 (similarity=0.8391)
  [2] potato_disease-pest-management_cpri_2016_manual, page 29 (similarity=0.7840)
  [3] potato_disease-pest-management_cpri_2016_manual, page 56 (similarity=0.7617)
  [4] potato_disease-pest-management_cpri_2016_manual, page 58 (similarity=0.7510)
  [5] potato_disease-pest-management_cpri_2016_manual, page 98 (similarity=0.7393)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q3 (in_scope / plain) | top_sim=0.8141 | gen=75.377s
**Q:** How can bacterial wilt in potato be distinguished from fungal wilts in the field using a stem cut section?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.34 — clear water

**A:** Within a few minutes, a whitish thread-like streaming can be observed coming out from the cut end of the stem into water, which represents the bacterial ooze exuding from the cut ends of colonized tissues [1]. This distinguishes bacterial wilt from other fungal wilts [1]. The streaming indicates the bacterial nature of the disease [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.8141)
  [2] potato_disease-pest-management_cpri_2016_manual, page 18 (similarity=0.7835)
  [3] potato_disease-pest-management_cpri_2016_manual, page 40 (similarity=0.7686)
  [4] potato_disease-pest-management_cpri_2016_manual, page 37 (similarity=0.7623)
  [5] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.7617)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q4 (in_scope / conflict) | top_sim=0.7722 | gen=85.11s
**Q:** When should fenoxaprop-p-ethyl be sprayed in dry direct-sown rice and at what dose?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.4;7 — 25-28 dae; 18-20 das

**A:** Fenoxaprop-p-ethyl should be applied between 18-20 days after sowing (DAS) or at the 3-5 leaf stage of weeds [2]. The recommended dose for fenoxaprop-p-ethyl is 60 g a.i. ha [2].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7722)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7034)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.6982)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.6903)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6867)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q5 (in_scope / plain) | top_sim=0.8067 | gen=74.45s
**Q:** How is a 2% brine solution used as a preventive measure for weed management in dry direct-sown rice?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.3 — 2% brine

**A:** A 2% brine solution can be used to clean seeds by dipping them, which helps select high-density seeds and separates floating weed seeds [3]. It also cleans seeds by dipping them in a 2% brine solution [3].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.8067)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.8052)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 3 (similarity=0.7766)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.7699)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7608)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q6 (in_scope / plain) | top_sim=0.8585 | gen=91.559s
**Q:** Why can post-emergence selective herbicides not be used to control weedy rice in a normal paddy field and how does Clearfield rice solve this?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.5 — clearfield

**A:** Due to the non-availability of selective herbicides to control weedy rice infestation [1], the management of weedy rice with post-emergence herbicides is not possible [1]. Clearfield (CL) rice is a mutated rice that is resistant to imidazoli-none herbicides, acetolactate synthase (ALS) inhibitors [1], offering a solution to this problem.

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.8585)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7911)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7869)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7847)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7799)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q7 (in_scope / table) | top_sim=0.7776 | gen=99.099s
**Q:** What are the recommended seed rate and fertilizer dose (N:P2O5:K2O) for improved wheat varieties VL Gehun 907 and VL Gehun 953 compared to existing farmer practices?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.5 — 120:60:40

**A:** The recommended seed rate for VL Gehun 907 and VL Gehun 953 is 100 Kg/ha when compared to the existing practice of 125 Kg/ha [2]. Furthermore, the recommended fertilizer dose is 120:60:40 kg N:P2O5:K2O /ha for VL Gehun 907 and VL Gehun 953, whereas farmers used no fertilizer [2].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.7776)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 5 (similarity=0.7708)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7701)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.7636)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7582)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q8 (in_scope / paraphrase) | top_sim=0.7743 | gen=71.697s
**Q:** Without using chemicals how can a farmer use summer heat and plastic sheets to kill soil-borne black scurf fungus in potato fields?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.56 — solarization

**A:** Soil solarization by using polythene mulch during peak summer increases soil temperature to 45-61 0C which kills harmful bacteria and other pathogens [3].  The passage also states that soil solarization with transparent polyethylene mulching during hot summer months is very effective for control of the soil borne part of the disease [4].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 123 (similarity=0.7743)
  [2] potato_disease-pest-management_cpri_2016_manual, page 60 (similarity=0.7713)
  [3] potato_disease-pest-management_cpri_2016_manual, page 56 (similarity=0.7636)
  [4] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7544)
  [5] potato_disease-pest-management_cpri_2016_manual, page 37 (similarity=0.7512)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q9 (out_of_scope / out_of_scope) | top_sim=0.7557 | GATED (unsupported_crop)
**Q:** Which herbicide is recommended to control weeds in a sesame (til) crop?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7557)
  [2] potato_disease-pest-management_cpri_2016_manual, page 92 (similarity=0.7368)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7328)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.7300)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7177)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q10 (out_of_scope / out_of_scope) | top_sim=0.6249 | GATED (low_similarity)
**Q:** What is the latest installment amount and eligibility criteria under the PM-KISAN government scheme for farmers?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6249)
  [2] potato_disease-pest-management_cpri_2016_manual, page 13 (similarity=0.6188)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6066)
  [4] potato_disease-pest-management_cpri_2016_manual, page 136 (similarity=0.6055)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6048)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q11 (in_scope / multi) | top_sim=0.8540 | gen=70.976s
**Q:** What is the effective application rate of CIPC sprout inhibitor per kg of potato tubers and at what temperature should processing potatoes be stored to avoid sweetening?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.9;11 — 25 mg a.i.; to avoid sweetening

**A:** The CIPC (isopropyl-Nchlorophenyl carbamate) sprout inhibitor is most effective when applied at 25 mg a.i. per kg tubers [2]. Processing potatoes should be stored at 10-12°C to avoid sugar accumulation and sweetening [1], [3].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 131 (similarity=0.8540)
  [2] potato_disease-pest-management_cpri_2016_manual, page 9 (similarity=0.8430)
  [3] potato_disease-pest-management_cpri_2016_manual, page 131 (similarity=0.8421)
  [4] potato_disease-pest-management_cpri_2016_manual, page 11 (similarity=0.7855)
  [5] potato_disease-pest-management_cpri_2016_manual, page 119 (similarity=0.7400)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q12 (in_scope / paraphrase) | top_sim=0.7827 | gen=80.682s
**Q:** How much foreign exchange money does India save each year by producing its own healthy breeder seed tubers instead of importing them from Europe?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.8 — 484 million

**A:** The country saves about 484 million US dollars annually because India produces its own breeder’s seed [1]. This saving is due to most Asian countries like Pakistan, Bangladesh, and China continuing to import seed potatoes from Europe [1]. Micropropagation and effective viral diagnostics have sustained the National Potato Seed Production Programme by producing about 2600 tonnes of breeder’s seed annually [2].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 110 (similarity=0.7827)
  [2] potato_disease-pest-management_cpri_2016_manual, page 8 (similarity=0.7536)
  [3] potato_disease-pest-management_cpri_2016_manual, page 10 (similarity=0.7350)
  [4] potato_disease-pest-management_cpri_2016_manual, page 10 (similarity=0.7299)
  [5] potato_disease-pest-management_cpri_2016_manual, page 11 (similarity=0.7008)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q13 (in_scope / plain) | top_sim=0.8375 | gen=74.068s
**Q:** Which potato variety imported from Denmark in 1953 introduced the wart pathogen into the Darjeeling hills?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.14 — furore

**A:** With the introduction of variety Furore from Denmark in 1953, the wart pathogen was also introduced which made Darjeeling hills unfit for quality seed production [2]. The passage states that this variety introduced the wart pathogen into the region [2]. This resulted in a legal ban on movement of potatoes from the state of West Bengal [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 14 (similarity=0.8375)
  [2] potato_disease-pest-management_cpri_2016_manual, page 58 (similarity=0.8060)
  [3] potato_disease-pest-management_cpri_2016_manual, page 13 (similarity=0.7669)
  [4] potato_disease-pest-management_cpri_2016_manual, page 36 (similarity=0.7609)
  [5] potato_disease-pest-management_cpri_2016_manual, page 14 (similarity=0.7567)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q14 (in_scope / plain) | top_sim=0.7606 | gen=109.927s
**Q:** How many grams of Streptocycline are required for 1 hectare when applied at a 50 ppm concentration in 500 litres of spray solution?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.21 — 25 g

**A:** The amount of pesticide needed can be calculated using the formula: Amount of pesticide needed (g or ml) = ppm x 0.001 x quantity of spray solution (L) [2].  Specifically, for 500 litres of spray solution at 50 ppm, the calculation is 50 x 0.001 x 500 = 25 g [2].  It is important to follow the Directions for Use section of the pesticide label to ensure the correct amount is applied [5]. [5]

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 21 (similarity=0.7606)
  [2] potato_disease-pest-management_cpri_2016_manual, page 21 (similarity=0.6916)
  [3] potato_disease-pest-management_cpri_2016_manual, page 23 (similarity=0.6718)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6570)
  [5] potato_disease-pest-management_cpri_2016_manual, page 20 (similarity=0.6540)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q15 (in_scope / table) | top_sim=0.8186 | gen=88.73s
**Q:** According to Table 2 on pesticide compatibility, is Lime Sulphur compatible or incompatible when mixed with Mancozeb 75 WP?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.22 — lime sulphur + mancozeb 75 wp

**A:** Lime Sulphur + Mancozeb 75 WP is listed as incompatible [1]. The passage states that this combination “Incompatible” [1]. This information is found in passage [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 22 (similarity=0.8186)
  [2] potato_disease-pest-management_cpri_2016_manual, page 22 (similarity=0.7845)
  [3] potato_disease-pest-management_cpri_2016_manual, page 22 (similarity=0.7281)
  [4] potato_disease-pest-management_cpri_2016_manual, page 23 (similarity=0.7253)
  [5] potato_disease-pest-management_cpri_2016_manual, page 23 (similarity=0.6748)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q16 (in_scope / paraphrase) | top_sim=0.7286 | gen=81.557s
**Q:** Why must farm workers avoid wearing footwear made of animal hide or woven cloth when spraying agricultural chemicals?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.27 — leather or fabric shoes

**A:** Leather or fabric shoes should never be worn as they absorb pesticides [1]. These absorbed pesticides can then come into contact with the body [1]. Protective footwear should be calf-high and worn with the legs of the protective pants on the outside to prevent spray from getting in [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 27 (similarity=0.7286)
  [2] potato_disease-pest-management_cpri_2016_manual, page 26 (similarity=0.6997)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6478)
  [4] potato_disease-pest-management_cpri_2016_manual, page 115 (similarity=0.6433)
  [5] potato_disease-pest-management_cpri_2016_manual, page 67 (similarity=0.6332)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q17 (in_scope / plain) | top_sim=0.8259 | gen=71.97s
**Q:** What rate of stable bleaching powder per hectare should be applied in furrows at planting time to reduce bacterial wilt in potato?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.37 — 12 kg/ha

**A:** The recommended application rate of stable bleaching powder is 12 kg/ha at the time of potato planting in furrows along with fertilizer [1]. Chemical control using this powder reduces the pathogen population and gives effective control of bacterial wilt [1].  [2]

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 37 (similarity=0.8259)
  [2] potato_disease-pest-management_cpri_2016_manual, page 37 (similarity=0.7468)
  [3] potato_disease-pest-management_cpri_2016_manual, page 123 (similarity=0.7464)
  [4] potato_disease-pest-management_cpri_2016_manual, page 38 (similarity=0.7390)
  [5] potato_disease-pest-management_cpri_2016_manual, page 9 (similarity=0.7362)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q18 (in_scope / paraphrase) | top_sim=0.7951 | gen=78.939s
**Q:** Planting which cucurbit vegetable as a trap crop causes whiteflies to lose their ability to transmit apical leaf curl virus after feeding on it?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.67 — cucumber

**A:** Cucumber (Cucumissativus) can be used as a trap crop to provide temporary protection [2]. Whiteflies lose their viruliferous capacity after feeding on cucumber [2]. This is because cucumber is a favoured host plant for whiteflies but a non-host for virus [2].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 48 (similarity=0.7951)
  [2] potato_disease-pest-management_cpri_2016_manual, page 67 (similarity=0.7738)
  [3] potato_disease-pest-management_cpri_2016_manual, page 48 (similarity=0.7636)
  [4] potato_disease-pest-management_cpri_2016_manual, page 112 (similarity=0.7466)
  [5] potato_disease-pest-management_cpri_2016_manual, page 62 (similarity=0.7451)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q19 (in_scope / multi) | top_sim=0.7644 | gen=70.037s
**Q:** What row spacing in centimetres is required in dry direct-sown rice when using a mechanical power weeder and at how many days after emergence is it operated?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.4 — 25 cm; 30 dae

**A:** In dry direct-sown rice, rows should be spaced 25 cm apart when using a mechanical power weeder [2]. The application of oxyflourfen is effective 12–15 days after emergence [3].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.7644)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7317)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7138)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7063)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7032)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q20 (in_scope / paraphrase) | top_sim=0.6694 | GATED (low_similarity)
**Q:** Why should a clogged herbicide nozzle never be cleared by blowing air through it with your lips?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.6 — blowing on them with the mouth

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.6694)
  [2] potato_disease-pest-management_cpri_2016_manual, page 94 (similarity=0.6583)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.6556)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.6490)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6480)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q21 (in_scope / plain) | top_sim=0.7408 | gen=74.227s
**Q:** Up to what percentage of applied fertilizer nitrogen can weedy red rice consume in a paddy field?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.1 — 60%

**A:** Weedy rice can consume a significant portion of applied fertilizer nitrogen [2]. Increasing rice crop interference could help suppress weedy rice growth and hence reduce weedy rice consumption of applied nitrogen [2]. The passage does not specify a precise percentage, but indicates that weedy rice can consume a substantial amount of nitrogen [2].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7408)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7328)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7312)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7308)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7276)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q22 (in_scope / multi) | top_sim=0.8225 | gen=89.55s
**Q:** What was the Seed Replacement Rate (SRR) in Uttarakhand and how did average wheat productivity in the hills compare to the tarai plains?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.1 — 31.6; 1028

**A:** The Seed Replacement Rate (SRR) in Uttarakhand is 31.6% [1]. Productivity of wheat in the hilly areas was 1028 kg/ha, while productivity in the tarai areas was 3510 kg/ha [2]. This represents a significant gap of 2482 kg/ha between the two regions [2].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.8225)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7834)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.7657)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7616)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7595)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q33 (out_of_scope / out_of_scope) | top_sim=0.6957 | GATED (low_similarity)
**Q:** What is the farmer premium percentage for Kharif foodcrops under the Pradhan Mantri Fasal Bima Yojana (PMFBY)?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6957)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6834)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6748)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6667)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.6658)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q34 (out_of_scope / out_of_scope) | top_sim=0.7308 | GATED (unsupported_crop)
**Q:** What pre-emergence dose of oxadiargyl is recommended per hectare for weed control in cumin (jeera) fields?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 4 (similarity=0.7308)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7244)
  [3] potato_disease-pest-management_cpri_2016_manual, page 92 (similarity=0.7228)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7224)
  [5] potato_disease-pest-management_cpri_2016_manual, page 93 (similarity=0.7100)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q35 (out_of_scope / out_of_scope) | top_sim=0.7298 | GATED (unsupported_crop)
**Q:** Which systemic fungicide should be sprayed to control powdery mildew and anthracnose in mango orchards?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 85 (similarity=0.7298)
  [2] potato_disease-pest-management_cpri_2016_manual, page 90 (similarity=0.7084)
  [3] potato_disease-pest-management_cpri_2016_manual, page 85 (similarity=0.6941)
  [4] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.6911)
  [5] potato_disease-pest-management_cpri_2016_manual, page 91 (similarity=0.6843)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q36 (out_of_scope / out_of_scope) | top_sim=0.5233 | GATED (low_similarity)
**Q:** What UART baud rate and parity settings are used by the Jetson Xavier to send steering commands to the Arduino?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 17 (similarity=0.5233)
  [2] potato_disease-pest-management_cpri_2016_manual, page 104 (similarity=0.5216)
  [3] potato_disease-pest-management_cpri_2016_manual, page 84 (similarity=0.5185)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.5131)
  [5] potato_disease-pest-management_cpri_2016_manual, page 85 (similarity=0.5131)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q41 (out_of_scope / uncovered_topic) | top_sim=0.7078 | GATED (topic_not_covered)
**Q:** How do I manage sheath blight in paddy?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7078)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6956)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6789)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6690)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6645)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q42 (out_of_scope / uncovered_topic) | top_sim=0.7253 | GATED (topic_not_covered)
**Q:** What fungicide controls blast disease in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7253)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7085)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7053)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7009)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6887)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q43 (out_of_scope / uncovered_topic) | top_sim=0.7008 | GATED (topic_not_covered)
**Q:** What are the symptoms of bacterial leaf blight in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7008)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.6653)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6637)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6588)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.6586)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q44 (out_of_scope / uncovered_topic) | top_sim=0.6273 | GATED (low_similarity)
**Q:** Which herbicide controls Phalaris minor in wheat?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6273)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6198)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 5 (similarity=0.6159)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6147)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6084)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q45 (out_of_scope / uncovered_topic) | top_sim=0.6776 | GATED (topic_not_covered)
**Q:** Should wheat get its first irrigation at the crown root initiation stage?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 8 (similarity=0.6776)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6715)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6577)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.6576)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6554)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q46 (out_of_scope / uncovered_topic) | top_sim=0.7541 | GATED (topic_not_covered)
**Q:** Ok what do you know about the diseases in rice crops and how would you prevent them

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7541)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7527)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7479)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7430)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.7394)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q47 (out_of_scope / uncovered_topic) | top_sim=0.7283 | gen=63.411s
**Q:** What is the market price of potato in the mandi this month?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 79 (similarity=0.7283)
  [2] potato_disease-pest-management_cpri_2016_manual, page 10 (similarity=0.7015)
  [3] potato_disease-pest-management_cpri_2016_manual, page 122 (similarity=0.7015)
  [4] potato_disease-pest-management_cpri_2016_manual, page 4 (similarity=0.6902)
  [5] potato_disease-pest-management_cpri_2016_manual, page 11 (similarity=0.6827)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q48 (out_of_scope / uncovered_topic) | top_sim=0.7159 | GATED (low_similarity)
**Q:** How do I control stem borer in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7159)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7149)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7047)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7031)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7001)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q49 (in_scope / short) | top_sim=0.7607 | gen=78.108s
**Q:** Bleaching powder dose for bacterial wilt in potato?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.37 — 12 kg/ha

**A:** The recommended chemical control for bacterial wilt involves the application of stable bleaching powder at 12 kg/ha when sowing in furrows [1].  Additionally, the passage states that the application of bleaching powder alongside fertilizer reduces the pathogen population [1]. I could not find this in my documents.

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 37 (similarity=0.7607)
  [2] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.7122)
  [3] potato_disease-pest-management_cpri_2016_manual, page 37 (similarity=0.7086)
  [4] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.6953)
  [5] potato_disease-pest-management_cpri_2016_manual, page 123 (similarity=0.6938)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q50 (in_scope / short) | top_sim=0.7924 | gen=69.109s
**Q:** How is brine used against weeds in direct-seeded rice?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.3 — 2% brine

**A:** I could not find this in my documents.

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7924)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.7746)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7690)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7546)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7510)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q51 (in_scope / short) | top_sim=0.8364 | gen=69.008s
**Q:** Which potato variety brought wart disease to Darjeeling?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.14 — furore

**A:** The introduction of variety Furore from Denmark in 1953 introduced the wart pathogen to Darjeeling hills [2]. This variety was brought in from Denmark [2].  [2]

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 58 (similarity=0.8364)
  [2] potato_disease-pest-management_cpri_2016_manual, page 14 (similarity=0.8122)
  [3] potato_disease-pest-management_cpri_2016_manual, page 4 (similarity=0.7612)
  [4] potato_disease-pest-management_cpri_2016_manual, page 16 (similarity=0.7567)
  [5] potato_disease-pest-management_cpri_2016_manual, page 36 (similarity=0.7565)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q52 (in_scope / short) | top_sim=0.6819 | GATED (low_similarity)
**Q:** Streptocycline needed per hectare at 50 ppm?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.21 — 25 g

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 21 (similarity=0.6819)
  [2] potato_disease-pest-management_cpri_2016_manual, page 119 (similarity=0.6468)
  [3] potato_disease-pest-management_cpri_2016_manual, page 42 (similarity=0.6389)
  [4] potato_disease-pest-management_cpri_2016_manual, page 77 (similarity=0.6306)
  [5] potato_disease-pest-management_cpri_2016_manual, page 73 (similarity=0.6302)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q53 (in_scope / short) | top_sim=0.7160 | GATED (low_similarity)
**Q:** How much fertilizer nitrogen can weedy rice take up?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.1 — 60%

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7160)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7095)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7043)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6939)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6886)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q54 (in_scope / short) | top_sim=0.7574 | gen=73.034s
**Q:** How to tell bacterial wilt from fungal wilt in potato?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.34 — clear water

**A:** A whitish thread-like streaming can be observed coming out from cut end of stem sections in clear water, distinguishing bacterial wilt from other fungal wilts [2]. This streaming represents the bacterial ooze exuding from the cut ends of colonized tissues [2]. Furthermore, placing stem cut sections in clear water allows for the observation of this characteristic streaming [2].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 18 (similarity=0.7574)
  [2] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.7505)
  [3] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.7490)
  [4] potato_disease-pest-management_cpri_2016_manual, page 34 (similarity=0.7426)
  [5] potato_disease-pest-management_cpri_2016_manual, page 38 (similarity=0.7376)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q55 (in_scope / short) | top_sim=0.6423 | GATED (low_similarity)
**Q:** What is Clearfield rice?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.5 — clearfield

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.6423)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6042)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6022)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.5961)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.5951)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q56 (in_scope / short) | top_sim=0.8001 | gen=68.055s
**Q:** CIPC dose for stored potatoes?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.9 — 25 mg a.i.

**A:** The treated potatoes are necessary to treat the stored potatoes with a sprout suppressant like CIPC (Isopropyl N-(3-chlorophenyl) carbamate) [1]. The CIPC dose is 25 mg a.i. per kg tubers when applied [4].  It is necessary to treat the stored potatoes with a sprout suppressant like CIPC [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 131 (similarity=0.8001)
  [2] potato_disease-pest-management_cpri_2016_manual, page 131 (similarity=0.7857)
  [3] potato_disease-pest-management_cpri_2016_manual, page 11 (similarity=0.7471)
  [4] potato_disease-pest-management_cpri_2016_manual, page 9 (similarity=0.7348)
  [5] potato_disease-pest-management_cpri_2016_manual, page 129 (similarity=0.7209)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q57 (in_scope / short) | top_sim=0.7616 | gen=93.098s
**Q:** Row spacing for a power weeder in direct-seeded rice?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.4 — 25 cm

**A:** Rows should be spaced 25 cm apart if a mechanical power weeder is used [1]. High weed infestation is a major constraint for adoption of DSR, as emerging seedlings in direct-sown fields are less competitive with concurrently emerged weeds [1].  There are 3 methods of direct-sown rice (DSR) i.e., dry seeding (sowing dry seeds in to dry soil), wet seeding (sowing of pre-germinated/sprouted seeds on wet puddled soils) and water seeding (seeds sown in to standing water) [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.7616)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7455)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7445)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7295)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7208)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q58 (in_scope / short) | top_sim=0.8042 | gen=80.032s
**Q:** Late blight temperature range for sporangia?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.29 — 3 to 26

**A:** Sporangia are formed in a wide range of temperature (3 to 26 °C), with an optimum of 18-22 °C [1]. The optimum temperature for direct germination is a range of 4 to 30 °C, with an optimum of 25 °C [1]. High relative humidity (> 90%) is required for spore formation and germination [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 29 (similarity=0.8042)
  [2] potato_disease-pest-management_cpri_2016_manual, page 29 (similarity=0.7438)
  [3] potato_disease-pest-management_cpri_2016_manual, page 96 (similarity=0.7398)
  [4] potato_disease-pest-management_cpri_2016_manual, page 96 (similarity=0.7246)
  [5] potato_disease-pest-management_cpri_2016_manual, page 96 (similarity=0.7177)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:
