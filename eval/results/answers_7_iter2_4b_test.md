# Stage 6 end-to-end answers (test, gemma3:4b, prompt v3, k=5)
Retrieval latency over 24 questions: p50=0.011s, p95=0.022s
Generation latency over 9 answered questions: p50=94.40s, p95=111.54s
End-to-end refusals (gate or model): in-scope wrongly refused 6/15 ['q23', 'q27', 'q29', 'q32', 'q64', 'q65']; out-of-scope wrongly answered 0/9 []; refused by the model itself: []
Machine: Windows-10-10.0.19045-SP0, Intel64 Family 6 Model 78 Stepping 3, GenuineIntel; offline guard off


## q23 (in_scope / table) | top_sim=0.7244 | GATED (low_similarity)
**Q:** According to the table of spray volume rates, which range in litres per hectare is classed as low volume for field crops?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.23 — low volume 50-200

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 23 (similarity=0.7244)
  [2] potato_disease-pest-management_cpri_2016_manual, page 21 (similarity=0.7004)
  [3] potato_disease-pest-management_cpri_2016_manual, page 24 (similarity=0.6713)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.6556)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6534)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q24 (in_scope / multi) | top_sim=0.7787 | gen=94.396s
**Q:** Which fungus causes early blight concentric target-spot rings on potato leaves and what concentration of mancozeb 75% WP is sprayed to manage it?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.31;32 — alternaria solani; 0.2%

**A:** Early blight of potato is caused by Alternaria solani [2]. A spray schedule of minimum of four fungicides sprays is recommended, it can be increase or decrease depending upon disease pressure [1]. Proper dose and proper time of spraying is very important, and Mancozeb 75%WP @ 0.2% should be sprayed as soon as weather conditions become congenial for late blight [1].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.7787)
  [2] potato_disease-pest-management_cpri_2016_manual, page 31 (similarity=0.7782)
  [3] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.7502)
  [4] potato_disease-pest-management_cpri_2016_manual, page 60 (similarity=0.7384)
  [5] potato_disease-pest-management_cpri_2016_manual, page 31 (similarity=0.7340)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q25 (in_scope / plain) | top_sim=0.8009 | gen=74.287s
**Q:** For how many minutes should seed tubers be dipped in a 3% boric acid solution before storage to prevent soft rot and common scab?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.40 — 30 min

**A:** Tubers should be treated with a 3% boric acid solution for 30 minutes before or after cold storage [2]. The manual recommends this treatment to dry the tubers under shade before storage or planting [2].  [2]

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 42 (similarity=0.8009)
  [2] potato_disease-pest-management_cpri_2016_manual, page 40 (similarity=0.7701)
  [3] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7649)
  [4] potato_disease-pest-management_cpri_2016_manual, page 72 (similarity=0.7598)
  [5] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7468)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q26 (in_scope / paraphrase) | top_sim=0.7646 | gen=114.699s
**Q:** For how long can the cysts of the nematode that attacks potatoes stay alive in the ground when no host plant is grown there?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.76 — 20-30 years

**A:** The cysts can survive in soil for 20-30 years even in the absence of a suitable host crop [2].  The cysts are resistant to adverse weather conditions and can remain viable for this extended period [2].  This long survival time is due to the hardened cyst forming around the eggs [2].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 74 (similarity=0.7646)
  [2] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.7631)
  [3] potato_disease-pest-management_cpri_2016_manual, page 75 (similarity=0.7622)
  [4] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7420)
  [5] potato_disease-pest-management_cpri_2016_manual, page 74 (similarity=0.7328)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q27 (in_scope / paraphrase) | top_sim=0.7023 | GATED (low_similarity)
**Q:** Which tip shape should a knapsack sprayer have for putting weedkiller on a rice field?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.5 — flat fan nozzle

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7023)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.6993)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6893)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6860)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6800)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q28 (in_scope / table) | top_sim=0.8262 | gen=106.805s
**Q:** According to the recommended herbicides table for dry direct-sown rice, what is the application dose in g a.i./ha for Cyhalofop-butyl (Clincher)?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.7 — cyhalofop-butyl

**A:** The recommended dose for Cyhalofop-butyl (Clincher) is 100 g a.i. ha [1]. This calculation is based on the formula: (30 × 2 × 100)/10 = 600 g [1].  The application dose is specified in the table for Cyhalofop-butyl [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.8262)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7577)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7357)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7342)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7218)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q29 (in_scope / paraphrase) | top_sim=0.7779 | GATED (topic_not_covered)
**Q:** Which dark-pigmented rice varieties does the article suggest planting to slowly wipe out the red-grained weed from a field over a few years?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.5 — p502

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7779)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7569)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7495)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7456)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7439)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q30 (in_scope / table) | top_sim=0.7967 | gen=84.268s
**Q:** According to Table 1 on global weedy rice infestation, what percentage of rice area is infested in Cuba?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.5 — cuba

**A:** Cuba has an infestation of 80% [1]. This information is found in Table 1 on weedy rice infestation across the world [1]. The table lists Cuba with an infestation percentage of 80 [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7967)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7377)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.7209)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7046)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6914)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q31 (in_scope / table) | top_sim=0.7505 | gen=96.408s
**Q:** According to Table 1 in the Uttarakhand wheat study, what seed treatment chemical and dose per kg of seed was used in the FLD intervention?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.5 — 2.5 g carboxin

**A:** The technological intervention utilized 2.5 g Carboxin/Kg of seed as a seed treatment [1]. Existing practices involved no seed treatment [1]. This information is found in Table 1 of document [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 5 (similarity=0.7505)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7134)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7062)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6882)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6846)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q32 (in_scope / multi) | top_sim=0.6847 | GATED (low_similarity)
**Q:** Which wild animal caused the most crop raiding damage in the Himalayan hills and what Rank Based Quotient (RBQ) score did wildlife damage receive in Table 7?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.4;6 — wild pig; 93.9

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6847)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6703)
  [3] potato_disease-pest-management_cpri_2016_manual, page 71 (similarity=0.6516)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6488)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.6444)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q37 (out_of_scope / out_of_scope) | top_sim=0.7624 | GATED (unsupported_crop)
**Q:** What post-emergence dose of quizalofop-ethyl is recommended to control grassy weeds in blackgram (urdbean)?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7624)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 4 (similarity=0.7444)
  [3] potato_disease-pest-management_cpri_2016_manual, page 92 (similarity=0.7302)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7218)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 4 (similarity=0.7061)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q38 (out_of_scope / out_of_scope) | top_sim=0.7764 | GATED (unsupported_crop)
**Q:** What is the economic threshold level (ETL) for pink bollworm in Bt cotton using pheromone traps?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 19 (similarity=0.7764)
  [2] potato_disease-pest-management_cpri_2016_manual, page 25 (similarity=0.6784)
  [3] potato_disease-pest-management_cpri_2016_manual, page 19 (similarity=0.6624)
  [4] potato_disease-pest-management_cpri_2016_manual, page 114 (similarity=0.6558)
  [5] potato_disease-pest-management_cpri_2016_manual, page 82 (similarity=0.6514)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q39 (out_of_scope / out_of_scope) | top_sim=0.6162 | GATED (low_similarity)
**Q:** What is the interest subvention percentage offered on short-term crop loans through a Kisan Credit Card (KCC)?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 8 (similarity=0.6162)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6004)
  [3] potato_disease-pest-management_cpri_2016_manual, page 124 (similarity=0.5936)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.5931)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.5912)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q40 (out_of_scope / out_of_scope) | top_sim=0.7330 | GATED (unsupported_crop)
**Q:** How should blister blight disease be managed using copper oxychloride and hexaconazole in Assam tea plantations?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.7330)
  [2] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.7095)
  [3] potato_disease-pest-management_cpri_2016_manual, page 60 (similarity=0.7038)
  [4] potato_disease-pest-management_cpri_2016_manual, page 30 (similarity=0.7035)
  [5] potato_disease-pest-management_cpri_2016_manual, page 123 (similarity=0.6914)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q59 (out_of_scope / uncovered_topic) | top_sim=0.7476 | GATED (topic_not_covered)
**Q:** Which insecticide controls brown planthopper in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7476)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.7269)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7072)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7025)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6924)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q60 (out_of_scope / uncovered_topic) | top_sim=0.6707 | GATED (low_similarity)
**Q:** What causes false smut in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6707)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6673)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6524)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.6492)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 2 (similarity=0.6459)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q61 (out_of_scope / uncovered_topic) | top_sim=0.6235 | GATED (low_similarity)
**Q:** How do I control loose smut of wheat?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.6235)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6179)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 8 (similarity=0.6102)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6097)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6046)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q62 (out_of_scope / uncovered_topic) | top_sim=0.6514 | GATED (topic_not_covered)
**Q:** How do I manage tungro virus in paddy?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6514)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6416)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 3 (similarity=0.6416)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.6296)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6238)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q63 (out_of_scope / uncovered_topic) | top_sim=0.6775 | GATED (low_similarity)
**Q:** What is the minimum support price for wheat this year?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6775)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.6689)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6635)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 4 (similarity=0.6617)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6536)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q64 (in_scope / short) | top_sim=0.7035 | GATED (low_similarity)
**Q:** How long should seed potatoes be dipped in boric acid?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.40 — 30 min

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] potato_disease-pest-management_cpri_2016_manual, page 123 (similarity=0.7035)
  [2] potato_disease-pest-management_cpri_2016_manual, page 57 (similarity=0.6885)
  [3] potato_disease-pest-management_cpri_2016_manual, page 130 (similarity=0.6877)
  [4] potato_disease-pest-management_cpri_2016_manual, page 110 (similarity=0.6764)
  [5] potato_disease-pest-management_cpri_2016_manual, page 40 (similarity=0.6760)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q65 (in_scope / short) | top_sim=0.6937 | GATED (low_similarity)
**Q:** Clincher dose in direct-seeded rice?

**Expected:** rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief p.7 — cyhalofop-butyl

**A:** I could not find this in my documents.

```
Refused before generation; closest passages found:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.6937)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.6916)
  [3] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6900)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.6889)
  [5] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 2 (similarity=0.6849)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q66 (in_scope / short) | top_sim=0.7666 | gen=78.069s
**Q:** How long can potato cyst nematode cysts survive?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.76 — 20-30 years

**A:** Potato cyst nematode cysts can survive in soil for 20-30 years even in the absence of a suitable host crop [2]. The life cycle is completed in 35-40 days and generally, one generation is completed in one year [2].  These cysts are resistant to adverse weather conditions and contain 200-500 eggs [2].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 74 (similarity=0.7666)
  [2] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.7459)
  [3] potato_disease-pest-management_cpri_2016_manual, page 75 (similarity=0.7383)
  [4] potato_disease-pest-management_cpri_2016_manual, page 74 (similarity=0.7250)
  [5] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.6986)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q67 (in_scope / short) | top_sim=0.7632 | gen=88.065s
**Q:** What seed treatment was used in the Uttarakhand wheat demonstrations?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.5 — 2.5 g carboxin

**A:** VL Gehun 953 and VL Gehun 907 were the improved varieties demonstrated in the farmers’ fields [1]. These varieties were notified for timely sown rainfed and irrigated conditions in the hills of Uttarakhand [2]. The demonstrations involved the use of these specific wheat varieties to increase yield and improve the benefit-cost ratio [3].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7632)
  [2] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.7614)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 7 (similarity=0.7510)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.7474)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 1 (similarity=0.7446)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q68 (in_scope / short) | top_sim=0.8228 | gen=95.524s
**Q:** What causes early blight in potato?

**Expected:** potato_disease-pest-management_cpri_2016_manual p.31 — alternaria solani

**A:** Early blight of potato is caused by Alternaria solani (Ell.&Mart) Jones & Grout [1]. The disease initially appears on the lower leaves and later develops on the upper leaves, characterized by circular to oval brown to black lesions with concentric rings [1]. It is a serious disease that occurs in relatively warm and humid regions and is economically important worldwide [4].

```
Retrieved sources: the model was shown these passages:
  [1] potato_disease-pest-management_cpri_2016_manual, page 31 (similarity=0.8228)
  [2] potato_disease-pest-management_cpri_2016_manual, page 32 (similarity=0.7955)
  [3] potato_disease-pest-management_cpri_2016_manual, page 60 (similarity=0.7845)
  [4] potato_disease-pest-management_cpri_2016_manual, page 98 (similarity=0.7837)
  [5] potato_disease-pest-management_cpri_2016_manual, page 126 (similarity=0.7801)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:
