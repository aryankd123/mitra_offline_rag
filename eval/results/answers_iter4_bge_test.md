# Stage 6 end-to-end answers (test, gemma3:4b, prompt v3, k=5)
Retrieval latency over 34 questions: p50=0.009s, p95=0.067s
Generation latency over 22 answered questions: p50=85.10s, p95=121.35s
End-to-end refusals (gate or model): in-scope wrongly refused 3/25 ['q64', 'q65', 'q83']; out-of-scope wrongly answered 0/9 []; refused by the model itself: []
Machine: Windows-10-10.0.19045-SP0, Intel64 Family 6 Model 78 Stepping 3, GenuineIntel; offline guard on, blocked: []


## q23 (in_scope / table) | top_sim=0.7244 | gen=167.572s
**Q:** According to the table of spray volume rates, which range in litres per hectare is classed as low volume for field crops?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.23 — low volume 50-200

**A:** The table of spray volume rates categorizes application volumes into high, medium, low, and very-low volumes [1]. Low volume is defined as 50-200 litres/ha for field crops [1]. Therefore, the range of 50-200 litres/hectare is classed as low volume for field crops [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 23 (similarity=0.7244, relevance=0.8954)
  [2] potato_disease-pest-management_cpri_2016_manual, page 21 (similarity=0.7004, relevance=0.3148)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.6537, relevance=0.1865)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.6435, relevance=0.0614)
  [5] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.6369, relevance=0.0476)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q24 (in_scope / multi) | top_sim=0.7787 | gen=78.91s
**Q:** Which fungus causes early blight concentric target-spot rings on potato leaves and what concentration of mancozeb 75% WP is sprayed to manage it?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.31;32 — alternaria solani; 0.2%

**A:** Early blight of potato is caused by Alternaria solani [2]. The disease develops as circular to oval brown to black lesions with concentric rings, producing a ‘target spot’ effect [2]. Spraying mancozeb 75% WP at a 0.2% concentration is recommended for managing early blight and leaf spot diseases [4].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 32 (similarity=0.7255, relevance=0.9824)
  [2] potato_disease-pest-management_cpri_2016_manual, page 31 (similarity=0.7782, relevance=0.9267)
  [3] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.7787, relevance=0.8053)
  [4] potato_disease-pest-management_cpri_2016_manual, page 56 (similarity=0.7176, relevance=0.7344)
  [5] potato_disease-pest-management_cpri_2016_manual, page 60 (similarity=0.7384, relevance=0.7176)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q25 (in_scope / plain) | top_sim=0.8009 | gen=76.308s
**Q:** For how many minutes should seed tubers be dipped in a 3% boric acid solution before storage to prevent soft rot and common scab?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.40 — 30 min

**A:** The tubers should be treated with a 3% boric acid solution for 30 minutes [2].  Treating the tubers with 3% boric acid for 30 min and drying them under shade minimizes infection during storage [2].  Additionally, the manual recommends a 3% boric acid treatment for 10-15 minutes before storage [3].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 40 (similarity=0.7701, relevance=0.9750)
  [2] potato_disease-pest-management_cpri_2016_manual, page 128 (similarity=0.7354, relevance=0.9642)
  [3] potato_disease-pest-management_cpri_2016_manual, page 42 (similarity=0.8009, relevance=0.9635)
  [4] potato_disease-pest-management_cpri_2016_manual, page 119 (similarity=0.7258, relevance=0.9555)
  [5] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7649, relevance=0.3528)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q26 (in_scope / paraphrase) | top_sim=0.7646 | gen=68.352s
**Q:** For how long can the cysts of the nematode that attacks potatoes stay alive in the ground when no host plant is grown there?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.76 — 20-30 years

**A:** The cysts can survive in soil for 20-30 years even in the absence of a suitable host crop [1]. Furthermore, the cysts can survive in soil for up to 6 years [2].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.7631, relevance=0.8928)
  [2] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7420, relevance=0.4676)
  [3] potato_disease-pest-management_cpri_2016_manual, page 75 (similarity=0.7622, relevance=0.4082)
  [4] potato_disease-pest-management_cpri_2016_manual, page 59 (similarity=0.7003, relevance=0.2824)
  [5] potato_disease-pest-management_cpri_2016_manual, page 74 (similarity=0.7646, relevance=0.2063)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q27 (in_scope / paraphrase) | top_sim=0.7395 | gen=87.3s
**Q:** Which tip shape should a knapsack sprayer have for putting weedkiller on a rice field?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.5 — flat fan nozzle

**A:** The most ideal machine for herbicide spray is lever operated knapsack sprayer with flood jet or flat fan nozzle [3]. Nozzles should be checked before spraying, and if required, it should be [3]. The sprayer should have a flat fan nozzle with a spray volume of 300 litres ha [6]. [6]

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7395, relevance=0.5801)
  [2] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7259, relevance=0.4676)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7063, relevance=0.3888)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7023, relevance=0.1585)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.6904, relevance=0.0223)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q28 (in_scope / table) | top_sim=0.8262 | gen=122.054s
**Q:** According to the recommended herbicides table for dry direct-sown rice, what is the application dose in g a.i./ha for Cyhalofop-butyl (Clincher)?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.7 — cyhalofop-butyl

**A:** Cyhalofop-butyl has a recommended dose of 100 g a.i. ha [3]. This application is advised for grassy weeds 12-15 DAS / OR 2-4 leaf stage of weeds [3]. The application dose is calculated as (30 × 2 × 100)/10 = 600 g [2].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7342, relevance=0.8832)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.8262, relevance=0.8831)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7284, relevance=0.7877)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7174, relevance=0.6012)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7576, relevance=0.5542)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q29 (in_scope / paraphrase) | top_sim=0.7779 | gen=96.529s
**Q:** Which dark-pigmented rice varieties does the article suggest planting to slowly wipe out the red-grained weed from a field over a few years?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.5 — p502

**A:** Purple-coloured cultivars, such as P502 and R575, are an effective option to gradually weed out weedy rice [1]. These cultivars deplete the weed seed bank within a few years [40]. The article notes that these plants have pigmented pericarp due to anthocyanins, cathekins, and catheolic tannins [5]. [5]

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7495, relevance=0.7543)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7456, relevance=0.3436)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7332, relevance=0.2449)
  [4] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.7525, relevance=0.2118)
  [5] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.7633, relevance=0.1922)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q30 (in_scope / table) | top_sim=0.7967 | gen=83.941s
**Q:** According to Table 1 on global weedy rice infestation, what percentage of rice area is infested in Cuba?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.5 — cuba

**A:** Cuba has an infestation of 80% [1]. This information is found in Table 1, which lists the infestation percentages for various countries [1]. The table also notes that infestations vary across different regions [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7967, relevance=0.9733)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7377, relevance=0.4617)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.7209, relevance=0.3750)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6754, relevance=0.1955)
  [5] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.6828, relevance=0.1224)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q31 (in_scope / table) | top_sim=0.7505 | gen=98.898s
**Q:** According to Table 1 in the Uttarakhand wheat study, what seed treatment chemical and dose per kg of seed was used in the FLD intervention?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.5 — 2.5 g carboxin

**A:** The technological intervention used 2.5 g Carboxin/Kg of seed as a seed treatment [1]. This was in contrast to the existing practices where no seed treatment was applied [1].  Furthermore, the recommended seed rate was 100 Kg/ha [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 5 (similarity=0.7505, relevance=0.9645)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6747, relevance=0.8774)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6846, relevance=0.2324)
  [4] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.7136, relevance=0.2035)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7134, relevance=0.1625)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q32 (in_scope / multi) | top_sim=0.6847 | gen=73.363s
**Q:** Which wild animal caused the most crop raiding damage in the Himalayan hills and what Rank Based Quotient (RBQ) score did wildlife damage receive in Table 7?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.4;6 — wild pig; 93.9

**A:** Crop damage by wildlife was a major constraint and ranked first under technological constraints [1]. The passage states that wild pig, porcupine, and mouse emerged as a major menace followed by crop raiding [1]. Wildlife damage received an RBQ score of 93.9 in Table 7 [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6847, relevance=0.7099)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6703, relevance=0.1697)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 6 (similarity=0.6431, relevance=0.0829)
  [4] potato_disease-pest-management_cpri_2016_manual, page 71 (similarity=0.6516, relevance=0.0640)
  [5] potato_disease-pest-management_cpri_2016_manual, page 114 (similarity=0.6286, relevance=0.0351)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q37 (out_of_scope / out_of_scope) | top_sim=0.7624 | GATED (unsupported_crop)
**Q:** What post-emergence dose of quizalofop-ethyl is recommended to control grassy weeds in blackgram (urdbean)?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7590, relevance=0.3455)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7624, relevance=0.3225)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 4 (similarity=0.7444, relevance=0.2909)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7484, relevance=0.1871)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.6946, relevance=0.1460)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q38 (out_of_scope / out_of_scope) | top_sim=0.7764 | GATED (unsupported_crop)
**Q:** What is the economic threshold level (ETL) for pink bollworm in Bt cotton using pheromone traps?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 19 (similarity=0.7764, relevance=0.0471)
  [2] potato_disease-pest-management_cpri_2016_manual, page 20 (similarity=0.6362, relevance=0.0348)
  [3] potato_disease-pest-management_cpri_2016_manual, page 20 (similarity=0.6500, relevance=0.0087)
  [4] potato_disease-pest-management_cpri_2016_manual, page 77 (similarity=0.6223, relevance=0.0087)
  [5] potato_disease-pest-management_cpri_2016_manual, page 94 (similarity=0.6455, relevance=0.0060)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q39 (out_of_scope / out_of_scope) | top_sim=0.6162 | GATED (low_relevance)
**Q:** What is the interest subvention percentage offered on short-term crop loans through a Kisan Credit Card (KCC)?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.5912, relevance=0.0029)
  [2] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.5742, relevance=0.0009)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.5599, relevance=0.0008)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.5630, relevance=0.0007)
  [5] rice_zinc-fertilizer_iiwm_2023_article, page 1 (similarity=0.5792, relevance=0.0006)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q40 (out_of_scope / out_of_scope) | top_sim=0.7330 | GATED (unsupported_crop)
**Q:** How should blister blight disease be managed using copper oxychloride and hexaconazole in Assam tea plantations?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.7035, relevance=0.1181)
  [2] potato_disease-pest-management_cpri_2016_manual, page 32 (similarity=0.6736, relevance=0.1162)
  [3] potato_disease-pest-management_cpri_2016_manual, page 107 (similarity=0.6860, relevance=0.1142)
  [4] potato_disease-pest-management_cpri_2016_manual, page 77 (similarity=0.6832, relevance=0.1104)
  [5] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.6774, relevance=0.0710)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q59 (out_of_scope / uncovered_topic) | top_sim=0.7476 | GATED (topic_not_covered)
**Q:** Which insecticide controls brown planthopper in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.7056, relevance=0.0759)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7476, relevance=0.0722)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.6848, relevance=0.0631)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7295, relevance=0.0415)
  [5] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.7063, relevance=0.0398)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q60 (out_of_scope / uncovered_topic) | top_sim=0.6707 | GATED (low_relevance)
**Q:** What causes false smut in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.6311, relevance=0.0139)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.6261, relevance=0.0100)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.6352, relevance=0.0072)
  [4] rice-wheat_nutrient-deficiencies_pau_2025_article, page 1 (similarity=0.6289, relevance=0.0057)
  [5] rice-wheat_nutrient-deficiencies_pau_2025_article, page 1 (similarity=0.6326, relevance=0.0052)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q61 (out_of_scope / uncovered_topic) | top_sim=0.6678 | GATED (low_relevance)
**Q:** How do I control loose smut of wheat?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.6580, relevance=0.0337)
  [2] wheat_karnal-bunt-black-point_hau_2023_article, page 1 (similarity=0.6285, relevance=0.0326)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.5965, relevance=0.0248)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.6678, relevance=0.0239)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.6206, relevance=0.0182)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q62 (out_of_scope / uncovered_topic) | top_sim=0.6514 | GATED (topic_not_covered)
**Q:** How do I manage tungro virus in paddy?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6238, relevance=0.0148)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6416, relevance=0.0126)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6514, relevance=0.0032)
  [4] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.6065, relevance=0.0011)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.5998, relevance=0.0010)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q63 (out_of_scope / uncovered_topic) | top_sim=0.6775 | GATED (low_relevance)
**Q:** What is the minimum support price for wheat this year?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 6 (similarity=0.6219, relevance=0.0285)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6326, relevance=0.0157)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6188, relevance=0.0113)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 1 (similarity=0.6273, relevance=0.0088)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6536, relevance=0.0073)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q64 (in_scope / short) | top_sim=0.7035 | GATED (low_relevance)
**Q:** How long should seed potatoes be dipped in boric acid?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.40 — 30 min

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 40 (similarity=0.6760, relevance=0.0931)
  [2] potato_disease-pest-management_cpri_2016_manual, page 42 (similarity=0.6751, relevance=0.0499)
  [3] potato_disease-pest-management_cpri_2016_manual, page 119 (similarity=0.6758, relevance=0.0312)
  [4] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.6885, relevance=0.0304)
  [5] potato_disease-pest-management_cpri_2016_manual, page 130 (similarity=0.6480, relevance=0.0262)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q65 (in_scope / short) | top_sim=0.6937 | GATED (low_relevance)
**Q:** Clincher dose in direct-seeded rice?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.7 — cyhalofop-butyl

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.6766, relevance=0.0745)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6916, relevance=0.0359)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.6611, relevance=0.0192)
  [4] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.6506, relevance=0.0168)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.6507, relevance=0.0118)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q66 (in_scope / short) | top_sim=0.7666 | gen=73.019s
**Q:** How long can potato cyst nematode cysts survive?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.76 — 20-30 years

**A:** Potato cyst nematode cysts can survive in soil for 20-30 years even in the absence of a suitable host crop [1]. The cysts are resistant to adverse weather conditions and contain 200-500 eggs [1].  Furthermore, some juveniles can remain dormant for several years before hatching [3].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.7459, relevance=0.8353)
  [2] potato_disease-pest-management_cpri_2016_manual, page 75 (similarity=0.7383, relevance=0.6275)
  [3] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.6986, relevance=0.4815)
  [4] potato_disease-pest-management_cpri_2016_manual, page 77 (similarity=0.6702, relevance=0.2834)
  [5] potato_disease-pest-management_cpri_2016_manual, page 72 (similarity=0.6863, relevance=0.1135)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q67 (in_scope / short) | top_sim=0.7632 | gen=91.022s
**Q:** What seed treatment was used in the Uttarakhand wheat demonstrations?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.5 — 2.5 g carboxin

**A:** A total of (Metsulfuron + Sulfosulfuron) @ 16 g ac-1 was sprayed 30-35 days after sowing in some of the demonstration plots in irrigated areas [1]. No herbicide was applied in rainfed areas [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.7316, relevance=0.9647)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7319, relevance=0.6712)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.7186, relevance=0.1282)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7284, relevance=0.1190)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7062, relevance=0.1011)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q68 (in_scope / short) | top_sim=0.8228 | gen=72.588s
**Q:** What causes early blight in potato?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.31 — alternaria solani

**A:** Early blight of potato is caused by Alternaria solani (Ell.&Mart) Jones & Grout [1]. The disease was first reported by Butler (1903) on potato leaves at Farrukhabad in Uttar Pradesh [1]. It causes symptoms such as circular to oval brown to black lesions with concentric rings, which produce a ‘target spot’ effect [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 31 (similarity=0.8228, relevance=0.9962)
  [2] potato_disease-pest-management_cpri_2016_manual, page 98 (similarity=0.7837, relevance=0.9482)
  [3] potato_disease-pest-management_cpri_2016_manual, page 78 (similarity=0.7376, relevance=0.8972)
  [4] potato_disease-pest-management_cpri_2016_manual, page 56 (similarity=0.7419, relevance=0.8814)
  [5] potato_disease-pest-management_cpri_2016_manual, page 60 (similarity=0.7681, relevance=0.7895)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q70 (in_scope / plain) | top_sim=0.7643 | gen=90.686s
**Q:** How much yield loss can Phalaris minor cause in wheat if left unattended?

**Expected:** wheat_phalaris-herbicide-resistance_hau_2020_article p.1 — 15-40%

**A:** Phalaris minor can lead to 15-40% or more yield loss if left unattended [1]. Heavy infestation of P. minor (2,000-3,000 plants/m2) can result in complete crop failure [4].  Under a P. minor population of 500 plants/m2, yield losses may go up to 50% [4].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.7376, relevance=0.9991)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 1 (similarity=0.6885, relevance=0.9804)
  [3] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.7193, relevance=0.8703)
  [4] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7003, relevance=0.8012)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7643, relevance=0.7158)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q73 (in_scope / plain) | top_sim=0.7626 | gen=85.061s
**Q:** What is the critical period of crop-weed competition in wheat?

**Expected:** wheat_phalaris-multiple-resistance_ndri_2021_article p.1 — 30-45 days after sowing

**A:** The critical period of crop-weed competition in wheat is 30-45 days after sowing [1]. This period is when wheat is dominated by various weed flora, including Phalaris minor [1]. The average yield loss caused by weeds is around 25-30% during this competitive phase [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-multiple-resistance_ndri_2021_article, page 1 (similarity=0.7092, relevance=0.9994)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.7137, relevance=0.2256)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.6991, relevance=0.1010)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.7076, relevance=0.0827)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.6554, relevance=0.0471)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q75 (in_scope / plain) | top_sim=0.7913 | gen=89.344s
**Q:** How many times higher isoproturon doses does resistant Phalaris minor need?

**Expected:** wheat_phalaris-multiple-resistance_ndri_2021_article p.2 — 3- 15 times higher

**A:** The resistant Phalaris minor requires 3-15 times higher doses of isoproturon for weed control [1].  Alternatively, it was reported that the resistant biotype needs 15 times higher doses of isoproturon [2].  Multiple herbicide-resistance has evolved in Phalaris minor, due to which sustainability of the wheat remains doubtful [4].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.7775, relevance=0.9477)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.7903, relevance=0.8976)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 3 (similarity=0.7037, relevance=0.6718)
  [4] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.6834, relevance=0.4124)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 3 (similarity=0.7298, relevance=0.2872)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q77 (in_scope / plain) | top_sim=0.8252 | gen=83.864s
**Q:** At what rate is paddy seed dressed with zinc for direct seeded rice?

**Expected:** rice_zinc-fertilizer_iiwm_2023_article p.3 — 2.8 g zinc per kg

**A:** The rate of seed dressing with ZnSO4 or Zn EDTA is about 2.8 g zinc per kg paddy seed [2]. Seed dressing is useful in alleviating zinc deficiency in direct seeded rice [2]. This method is particularly effective for addressing zinc deficiency during the initial 2 to 3 weeks of rice growth [2].

```
Retrieved sources: the model was shown these passages:
  [1] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.8252, relevance=0.9948)
  [2] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.8154, relevance=0.9187)
  [3] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.7817, relevance=0.1245)
  [4] rice_zinc-fertilizer_iiwm_2023_article, page 1 (similarity=0.7589, relevance=0.0390)
  [5] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.6868, relevance=0.0351)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q80 (in_scope / plain) | top_sim=0.8372 | gen=80.011s
**Q:** What urea spray is advised if wheat still shows nitrogen deficiency after the full soil dose of urea?

**Expected:** rice-wheat_nutrient-deficiencies_pau_2025_article p.2 — 3% urea solution

**A:** Spraying a 3% urea solution is advised if the crop still exhibits N deficiency after the full dose of urea has already been applied to the soil [1]. The spray should be applied in a crosswise manner to thoroughly cover the entire crop [1]. This recommendation is found in [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.8372, relevance=0.9943)
  [2] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.7050, relevance=0.1550)
  [3] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.7087, relevance=0.0982)
  [4] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.7360, relevance=0.0612)
  [5] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.7270, relevance=0.0518)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q83 (in_scope / plain) | top_sim=0.7556 | GATED (topic_not_covered)
**Q:** Which fungicide spray and stage are recommended against Karnal bunt of wheat?

**Expected:** wheat_karnal-bunt-black-point_hau_2023_article p.3 — propiconazole (tilt 25 ec) at heading stage

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_karnal-bunt-black-point_hau_2023_article, page 3 (similarity=0.7324, relevance=0.9656)
  [2] wheat_karnal-bunt-black-point_hau_2023_article, page 3 (similarity=0.6879, relevance=0.1823)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.6779, relevance=0.1260)
  [4] wheat_karnal-bunt-black-point_hau_2023_article, page 2 (similarity=0.6949, relevance=0.1147)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7071, relevance=0.1094)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q86 (in_scope / plain) | top_sim=0.7919 | gen=79.387s
**Q:** What spray volume per hectare should a knapsack sprayer give when applying rice herbicides?

**Expected:** rice_herbicide-weed-control_nrri_2018_brief p.2 — spray volume of 300 litres ha

**A:** A knapsack sprayer should have a spray volume of 300 litres ha [1, 6]. The passage also states that the sprayer should have a flat fan nozzle with a spray volume of 300 L ha [1, 6]. [1, 6]

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7343, relevance=0.9126)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7303, relevance=0.8327)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7919, relevance=0.3301)
  [4] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.6960, relevance=0.1929)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7445, relevance=0.1067)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q88 (in_scope / plain) | top_sim=0.6907 | gen=107.884s
**Q:** How much commercial product is needed for 2 ha at 30 g a.i./ha if the herbicide has 10% active ingredient?

**Expected:** rice_herbicide-weed-control_nrri_2018_brief p.3 — 600g

**A:** The application dose is calculated as (Recommended dose x Area x 100) / Active ingredient [1].  In this case, the calculation is (30 g a.i. ha x 2 ha x 100) / 10 = 600 g [2]. Therefore, 600 grams of the commercial product are needed [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.6876, relevance=0.9602)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6523, relevance=0.7915)
  [3] potato_disease-pest-management_cpri_2016_manual, page 21 (similarity=0.6541, relevance=0.2431)
  [4] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.6099, relevance=0.1849)
  [5] potato_disease-pest-management_cpri_2016_manual, page 20 (similarity=0.6487, relevance=0.0944)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q90 (in_scope / table) | top_sim=0.6669 | gen=88.128s
**Q:** What is the dose of penoxulam (Granite) for transplanted rice?

**Expected:** rice_herbicide-weed-control_nrri_2018_brief p.4 — penoxulam (granite)

**A:** Penoxulam (Granite) has a dose of 25 g a.i. ha-1 for broad-leaved and aquatic weeds with few sedges at the 3-4 leaf stage of weeds [1]. The application time for this herbicide is 15 DAS OR at 3-4 leaf stage of weeds [1].  It is recommended for mixed weed populations [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.6669, relevance=0.6807)
  [2] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.6509, relevance=0.0637)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6499, relevance=0.0368)
  [4] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.6361, relevance=0.0110)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.6239, relevance=0.0108)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q93 (in_scope / plain) | top_sim=0.8344 | gen=85.145s
**Q:** How many days after flowering do weedy rice seeds reach about 85% germinability?

**Expected:** rice_weedy-rice-control_crri_2013_brief p.4 — 85% at 20 days after flowering

**A:** Weedy rice seeds reach about 85% germinability at 20 days after flowering [1]. The passage states that “seeds are found viable at about nine days from the beginning of flowering, with a germinability of about 20%. This increases quickly and reaches about 85% at 20 days after flowering” [1]. Shattered grains show a lower germinability up to 24 days after flowering in comparison to that of non-shattered seeds [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-control_crri_2013_brief, page 4 (similarity=0.8279, relevance=0.9935)
  [2] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.8344, relevance=0.7895)
  [3] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.7937, relevance=0.7578)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7438, relevance=0.5506)
  [5] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.7303, relevance=0.5163)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:
