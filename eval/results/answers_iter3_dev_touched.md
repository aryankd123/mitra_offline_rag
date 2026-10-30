# Stage 6 end-to-end answers (dev (Iteration 3 touched), gemma3:4b, prompt v3, k=5)
Retrieval latency over 22 questions: p50=0.026s, p95=0.360s
Generation latency over 22 answered questions: p50=87.83s, p95=661.97s
End-to-end refusals (gate or model): in-scope wrongly refused 0/19 []; out-of-scope wrongly answered 1/3 ['q46']; refused by the model itself: ['q47', 'q48']
Machine: Windows-10-10.0.19045-SP0, Intel64 Family 6 Model 78 Stepping 3, GenuineIntel; offline guard off


## q44 (in_scope / plain) | top_sim=0.8226 | gen=158.098s
**Q:** Which herbicide controls Phalaris minor in wheat?

**Expected:** wheat_phalaris-herbicide-resistance_hau_2020_article p.3;4 — clodinafop; sulfosulfuron; pinoxaden

**A:** Several herbicide/herbicide mixtures have been recommended for efficient weed management in wheat [5]. Intra-group combinations of herbicides such as ACCase inhibitor (clodinafop/fenoxaprop/pinoxaden) with ACCase inhibitor and ALS inhibitor (sulfosulfuron/mesosulfuron + iodosulfuron) with ALS inhibitor were compatible and resulted in effective control of Phalaris minor [5].  Additionally, the use of herbicides with a different mode of action either as herbicide mixture, or sequential application of herbicide rotation year after year will be helpful for the effective management of P. minor resistance and delay the resistance development [5].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-herbicide-resistance_hau_2020_article, page 3 (similarity=0.8226)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.8225)
  [3] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.8159)
  [4] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.8155)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.8122)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q45 (in_scope / table) | top_sim=0.7297 | gen=85.281s
**Q:** Should wheat get its first irrigation at the crown root initiation stage?

**Expected:** wheat_rust-resistant-varieties-economics_vpkas_2020_article p.5 — cri stage

**A:** Wheat should receive its first irrigation preferably before the first irrigation or a week after first irrigation [1]. This timing is recommended to allow for optimal wheat growth and competitiveness [1]. The passage also suggests this timing helps reduce Phalaris minor infestation [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.7297)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.6825)
  [3] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 8 (similarity=0.6776)
  [4] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 2 (similarity=0.6715)
  [5] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.6696)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q46 (out_of_scope / uncovered_topic) | top_sim=0.7855 | gen=76.378s
**Q:** Ok what do you know about the diseases in rice crops and how would you prevent them

**Expected:** (refusal) p. — 

**A:** Weedy rice poses a significant threat to rice farming due to its morphological variability and high biological affinity with cultivated varieties [3]. Preventive measures, such as using certified seeds and cleaning machinery, are essential to reduce the chances of weedy rice infestation [1].  A cultural strategy of burning rice stubbles after harvest can also help control weedy rice [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.7855)
  [2] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.7707)
  [3] rice_weedy-rice-control_crri_2013_brief, page 4 (similarity=0.7610)
  [4] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.7546)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7541)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q47 (out_of_scope / uncovered_topic) | top_sim=0.7283 | gen=59.374s
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

## q48 (out_of_scope / uncovered_topic) | top_sim=0.7532 | gen=61.232s
**Q:** How do I control stem borer in rice?

**Expected:** (refusal) p. — 

**A:** I could not find this in my documents.

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.7532)
  [2] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.7515)
  [3] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.7341)
  [4] rice_weedy-rice-control_crri_2013_brief, page 4 (similarity=0.7304)
  [5] rice_weedy-rice-control_crri_2013_brief, page 4 (similarity=0.7296)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q53 (in_scope / short) | top_sim=0.7257 | gen=75.385s
**Q:** How much fertilizer nitrogen can weedy rice take up?

**Expected:** rice_weedy-rice-options_dwsr_2013_article p.1 — 60%

**A:** Red rice may take up to 60% of applied fertilizer nitrogen [2]. Burgos et al. report that weedy rice has high nitrogen use efficiency for biomass production than cultivated rice [2]. Furthermore, increasing rice crop interference could help reduce weedy rice growth significantly [4].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.7257)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 1 (similarity=0.7160)
  [3] rice_zinc-fertilizer_iiwm_2023_article, page 2 (similarity=0.7145)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7095)
  [5] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.7043)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q69 (in_scope / plain) | top_sim=0.7830 | gen=126.645s
**Q:** What doses of clodinafop and sulfosulfuron are recommended against Phalaris minor in wheat?

**Expected:** wheat_phalaris-herbicide-resistance_hau_2020_article p.3 — clodinafop (60 g/ha); sulfosulfuron (25 g/ha)

**A:** Clodinafop is recommended at a dose of 60 g/ha, while sulfosulfuron is recommended at a dose of 25 g/ha [3].  Furthermore, double the dose of clodinafop is recommended for biotypes that have developed resistance [3].  The development of cross-resistance against clodinafop was observed in many areas [3].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.7830)
  [2] wheat_phalaris-herbicide-resistance_hau_2020_article, page 3 (similarity=0.7757)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 3 (similarity=0.7674)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.7609)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7477)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q71 (in_scope / short) | top_sim=0.7694 | gen=86.036s
**Q:** Pinoxaden dose for Phalaris minor in wheat?

**Expected:** wheat_phalaris-herbicide-resistance_hau_2020_article p.4 — pinoxaden 40-50

**A:** The efficacy of newly introduced pinoxaden, mesosulfuron + iodosulfuron (RM) herbicides was tested against Phalaris minor biotypes in Haryana [1].  The recommended dose of pinoxaden is 125-150 DAS [2].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-herbicide-resistance_hau_2020_article, page 3 (similarity=0.7694)
  [2] wheat_phalaris-herbicide-resistance_hau_2020_article, page 4 (similarity=0.7632)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7421)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 2 (similarity=0.7407)
  [5] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.7177)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q72 (in_scope / plain) | top_sim=0.7521 | gen=82.737s
**Q:** How long do Phalaris minor seeds stay dormant after harvest?

**Expected:** wheat_phalaris-herbicide-resistance_hau_2020_article p.2 — six months

**A:** P. minor seeds remain dormant for six months after harvesting [1]. Even under anaerobic conditions, their seeds enter into secondary dormancy [1].  Mature seeds after harvesting remain dormant for the period of six months and thereafter germination increases up to 98% [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7521)
  [2] potato_disease-pest-management_cpri_2016_manual, page 76 (similarity=0.7114)
  [3] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.7006)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 1 (similarity=0.6945)
  [5] potato_disease-pest-management_cpri_2016_manual, page 111 (similarity=0.6910)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q74 (in_scope / plain) | top_sim=0.7753 | gen=764.744s
**Q:** By how much does a wheat seed rate of 150 kg/ha reduce Phalaris minor biomass?

**Expected:** wheat_phalaris-multiple-resistance_ndri_2021_article p.3 — more than 40%

**A:** Higher seed rate 150 kg/ha reduces Phalaris minor biomass by more than 40% [2]. It has been found that higher seed rate 150 kg/ha reduces biomass of P. minor by more than 40% [2].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_phalaris-herbicide-resistance_hau_2020_article, page 2 (similarity=0.7753)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.7722)
  [3] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.7401)
  [4] wheat_phalaris-herbicide-resistance_hau_2020_article, page 1 (similarity=0.7260)
  [5] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.7127)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q76 (in_scope / plain) | top_sim=0.9168 | gen=554.436s
**Q:** When do zinc deficiency symptoms appear in transplanted rice?

**Expected:** rice_zinc-fertilizer_iiwm_2023_article p.1 — 2 to 3 weeks after transplanting

**A:** Zinc deficiency symptoms typically manifest 2–3 weeks after transplanting in rice [1, 2, 3]. The symptoms appear on the second or third leaf from the top, and are characterized by brown blotches and streaks [2, 3]. Regular consumption of low zinc rice induces stunted growth, improper development, and diseases due to low immunity [3].

```
Retrieved sources: the model was shown these passages:
  [1] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.9168)
  [2] rice_zinc-fertilizer_iiwm_2023_article, page 1 (similarity=0.8843)
  [3] rice_zinc-fertilizer_iiwm_2023_article, page 1 (similarity=0.8617)
  [4] rice_zinc-fertilizer_iiwm_2023_article, page 1 (similarity=0.8011)
  [5] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.8005)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q78 (in_scope / table) | top_sim=0.8239 | gen=667.63s
**Q:** How much zinc sulphate heptahydrate per hectare supplies 2.5 kg of zinc to rice?

**Expected:** rice_zinc-fertilizer_iiwm_2023_article p.3 — 12.5 kg/ha

**A:** The soil application of Zinc at 5 kg/ha uses ZnSO4.7H2O at 25 kg/ha [1]. Additionally, the seedling root dip method utilizes 0.1% zinc solution, and the rate of seed dressing with ZnSO4 or Zn EDTA is about 2.8 g zinc per kg paddy seed [1, 2].

```
Retrieved sources: the model was shown these passages:
  [1] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.8239)
  [2] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.7918)
  [3] rice_zinc-fertilizer_iiwm_2023_article, page 2 (similarity=0.7832)
  [4] rice_zinc-fertilizer_iiwm_2023_article, page 4 (similarity=0.7773)
  [5] rice_zinc-fertilizer_iiwm_2023_article, page 1 (similarity=0.7759)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q79 (in_scope / plain) | top_sim=0.8513 | gen=489.646s
**Q:** How much 21% zinc sulfate per acre corrects zinc deficiency in the rice-wheat system?

**Expected:** rice-wheat_nutrient-deficiencies_pau_2025_article p.3 — 25 kg of zinc sulfate (21%) per acre

**A:** If the deficiency is observed in the current crop, apply 16 kg of zinc sulfate monohydrate per acre [2]. Additionally, in severely deteriorated soils, broadcast 16 kg of zinc sulfate monohydrate per ha mixed with an equal quantity of dry soil over the affected patches [2].

```
Retrieved sources: the model was shown these passages:
  [1] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.8513)
  [2] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.8407)
  [3] rice_zinc-fertilizer_iiwm_2023_article, page 2 (similarity=0.8172)
  [4] rice_zinc-fertilizer_iiwm_2023_article, page 3 (similarity=0.8099)
  [5] rice_zinc-fertilizer_iiwm_2023_article, page 2 (similarity=0.8056)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q81 (in_scope / paraphrase) | top_sim=0.7483 | gen=104.37s
**Q:** How should the nitrogen dose be changed for wheat sown after mid-December?

**Expected:** rice-wheat_nutrient-deficiencies_pau_2025_article p.2 — reduce n application by 25%

**A:** Reduce N application by 25% from the recommended dose to account for the reduced growth period and lower temperatures [1]. This adjustment is recommended for crops sown after mid-December [1]. The passage states that a 25% reduction is advised to compensate for these conditions [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.7483)
  [2] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.6796)
  [3] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.6741)
  [4] wheat_phalaris-multiple-resistance_ndri_2021_article, page 3 (similarity=0.6457)
  [5] wheat_rust-resistant-varieties-economics_vpkas_2020_article, page 3 (similarity=0.6375)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q82 (in_scope / plain) | top_sim=0.8255 | gen=96.219s
**Q:** How is a 0.5% manganese sulfate spray prepared for manganese-deficient wheat?

**Expected:** rice-wheat_nutrient-deficiencies_pau_2025_article p.3 — 1.0 kg of manganese sulfate in 200 liters of water

**A:** A 0.5% manganese sulfate solution is prepared by dissolving 1.0 kg of manganese sulfate in 200 liters of water [1]. This solution is then applied as a foliar spray 2 to 4 days before the first irrigation [1]. The recommended concentration is 0.5% manganese sulfate solution (1.0 kg of manganese sulfate in 200 liters of water) [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.8255)
  [2] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.7861)
  [3] rice-wheat_nutrient-deficiencies_pau_2025_article, page 2 (similarity=0.6975)
  [4] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.6909)
  [5] rice-wheat_nutrient-deficiencies_pau_2025_article, page 3 (similarity=0.6860)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q84 (in_scope / plain) | top_sim=0.7885 | gen=165.439s
**Q:** Which district had the lowest Karnal bunt incidence in northern Haryana in rabi 2021-22?

**Expected:** wheat_karnal-bunt-black-point_hau_2023_article p.3 — ambala (0.042%)

**A:** Ambala had the lowest Karnal bunt incidence in northern Haryana in rabi 2021-22, with an infection range of 0.042-0.10% [1]. The incidence of the disease was lowest in Ambala (0.042%) followed by Kurukshetra (0.082%) [1]. Table 1 shows that infected samples of Karnal bunt were lowest in Ambala (57.14%) [1].

```
Retrieved sources: the model was shown these passages:
  [1] wheat_karnal-bunt-black-point_hau_2023_article, page 3 (similarity=0.7885)
  [2] wheat_karnal-bunt-black-point_hau_2023_article, page 7 (similarity=0.7671)
  [3] wheat_karnal-bunt-black-point_hau_2023_article, page 5 (similarity=0.7600)
  [4] wheat_karnal-bunt-black-point_hau_2023_article, page 2 (similarity=0.7571)
  [5] wheat_karnal-bunt-black-point_hau_2023_article, page 3 (similarity=0.7511)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q85 (in_scope / plain) | top_sim=0.7866 | gen=89.621s
**Q:** At what rate are granular herbicides mixed with wet sand for rice fields?

**Expected:** rice_herbicide-weed-control_nrri_2018_brief p.2 — little wet sand at 10-12 kg ha

**A:** Very few granular formulations are available and these are generally applied in rice field as sand-mix [3]. For best weed control, instructions are given in the package that should be carefully read and followed the label which states the rate/doses, adjuvant, combinations and other requirements of the product [3]. The recommended dose is 8-10 days after sowing (DAS) for Bispyribac Sodium [5].

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7866)
  [2] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7413)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 7 (similarity=0.7324)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.7293)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7253)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q87 (in_scope / plain) | top_sim=0.7360 | gen=79.465s
**Q:** From what height above the target weeds should herbicide be sprayed?

**Expected:** rice_herbicide-weed-control_nrri_2018_brief p.3 — around 50 cm above the target weeds

**A:** Spray from a height of around 50 cm above the target weeds [13]. The protocol recommends spraying perpendicular to the wind to minimize drift [13]. It is advised to maintain a spray height of approximately 50 cm [13].

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7360)
  [2] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7340)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7315)
  [4] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 5 (similarity=0.7151)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 3 (similarity=0.7121)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q89 (in_scope / table) | top_sim=0.7993 | gen=97.097s
**Q:** Which herbicide is recommended for rice nursery beds in transplanted rice?

**Expected:** rice_herbicide-weed-control_nrri_2018_brief p.4 — pyrazosulfuron ethyl

**A:** Pre-sowing application of anti-germinative herbicides like molinate at 7.2 kg ha-1 is recommended to prevent germination of weedy rice seeds [5].  The protocol for herbicide-based weed control in rice suggests pre-sowing application of herbicides [4].  Additionally, the use of pretilachlor at 1.5 kg ha-1 at least 20 days before rice planting is recommended [5].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-options_dwsr_2013_article, page 5 (similarity=0.7993)
  [2] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7864)
  [3] rice_weed-mgmt-dry-direct-seeded_nrri_2019_brief, page 6 (similarity=0.7731)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.7692)
  [5] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.7645)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q91 (in_scope / plain) | top_sim=0.8219 | gen=84.13s
**Q:** What pre-planting dose of pretilachlor controls weedy rice and how long before planting is it applied?

**Expected:** rice_weedy-rice-control_crri_2013_brief p.2 — pretilachlor at 1.5 kg ha-1 at least 20 days before rice

**A:** Pretilachlor at 1.5 kg ha-1 is applied at least 20 days before rice planting to prevent germination of weedy rice seeds [2]. The protocol recommends this application as a pre-sowing technique to manage weedy rice [2]. It is also used in direct-sown rice fields to suppress early weed flashes [4].

```
Retrieved sources: the model was shown these passages:
  [1] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.8219)
  [2] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.8172)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.8064)
  [4] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.8030)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.7824)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q92 (in_scope / plain) | top_sim=0.7765 | gen=85.368s
**Q:** At what growth stage is maleic hydrazide sprayed on weedy rice plants?

**Expected:** rice_weedy-rice-control_crri_2013_brief p.2 — at the heading stage

**A:** Maleic hydrazide is sprayed on weedy rice plants at the heading stage [1]. It should be done before the milky-stage of cultivated rice to avoid negative effects on yield and seed viability [1]. The passage also states that spraying of maleic hydrazide helps in reducing seed viability [1].

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-control_crri_2013_brief, page 2 (similarity=0.7765)
  [2] rice_herbicide-weed-control_nrri_2018_brief, page 1 (similarity=0.7653)
  [3] rice_herbicide-weed-control_nrri_2018_brief, page 2 (similarity=0.7505)
  [4] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.7451)
  [5] rice_herbicide-weed-control_nrri_2018_brief, page 4 (similarity=0.7429)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:

## q94 (in_scope / paraphrase) | top_sim=0.8258 | gen=76.406s
**Q:** How can a farmer stop weedy rice seeds from getting into the field in the first place?

**Expected:** rice_weedy-rice-control_crri_2013_brief p.3 — clean seed

**A:** Farmers should purchase certified seeds from authorized stockists to prevent the spread of weedy rice [2]. Additionally, using clean machinery, particularly from infested fields, can prevent the introduction of weedy rice seeds [3].  [3]

```
Retrieved sources: the model was shown these passages:
  [1] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.8258)
  [2] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.8243)
  [3] rice_weedy-rice-control_crri_2013_brief, page 3 (similarity=0.8188)
  [4] rice_weedy-rice-options_dwsr_2013_article, page 4 (similarity=0.8115)
  [5] rice_weedy-rice-control_crri_2013_brief, page 1 (similarity=0.8096)
```
Faithful: ☐ yes ☐ partly ☐ no | Cites correct passage: ☐ | Notes:
