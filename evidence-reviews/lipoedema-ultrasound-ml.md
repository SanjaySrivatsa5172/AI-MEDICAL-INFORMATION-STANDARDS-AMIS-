# Evidence Review: Machine Learning for Ultrasound Detection of Lipoedema

**Question addressed**: Is there a published study applying machine-learning criteria to ultrasound detection of lipoedema characteristics, or identifying lipoedema on the basis of ultrasound appearance?

| Field | Value |
|---|---|
| Review date | 2026-08-18 (revised 2026-08-19 after direct PubMed search) |
| AMIS conformance | Level 3 (Full) |
| Standards applied | SPECIFICATION.md Standards 1-5; `standards/imaging_ml_evidence.yaml` v1.0.0 |
| Highest source tier located | Tier 3 |
| Permitted confidence ceiling | **Uncertain** (see §5) |
| Therapeutic intent | None. This document is an evidence appraisal, not clinical guidance. |
| Derived analysis | §10 contains calculations performed for this review (Hanley-McNeil AUC precision; Bayes projection of predictive values). These are arithmetic on published operating points, clearly marked, and are not findings of the cited studies. |

---

## 1. Answer

**No study was identified, in the sources searched, that trains or validates a machine-learning model on ultrasound images to detect or classify lipoedema.**

This negative claim is scoped per `imaging_ml_evidence.yaml § absence_of_evidence`; the search boundary is stated in §6. It means *not identified in these sources on this date*, not *does not exist*.

**Confirmed against PubMed directly (2026-08-19).** The initial review recorded a network block on PubMed as its principal limitation. That search has now been run. The intersection query — lipoedema AND ultrasound AND machine-learning terms — returns **exactly one** PubMed record, and that record is Nowak et al. (2022), an **MRI** segmentation study that matches only because PubMed expands `ultrasound` to the `diagnostic imaging` MeSH subheading. There is no ultrasound-plus-machine-learning lipoedema literature indexed in PubMed.

Three adjacent bodies of work do exist, and are routinely conflated with the question. They are distinguished in §2, §3 and §4. **§10 draws the consequences** — a feature-discrimination audit, the sample size the existing cohorts fall short of, and what the published operating point does at realistic prevalence.

---

## 2. What exists: ultrasound diagnostic criteria (statistical, not machine-learned)

These studies derive thresholds by conventional ROC analysis. No learned classifier is involved.

| Study | Design and n | Reported result | Tier | Validation design |
|---|---|---|---|---|
| Amato et al. (2021) | Cross-sectional, 89 women (63 lipoedema) | Dermal and subcutaneous thickness at predefined lower-limb points. Pre-tibial region the best discriminator, then thigh and lateral leg; supra-/just-medial malleolar significant at BMI > 25. "Optimal cut-off" calculated. | 3 | Internal, single-centre |
| Barros et al. (2026) | Cross-sectional case-control, 102 women (51 lipoedema, 51 age- and BMI-matched controls) | Upper extremity, six standardised points. Mid-arm best: **AUC 0.74, sensitivity 82.4%, specificity 51.9%, cut-off > 11.4 mm**. Four of six points AUC 0.73-0.74. Thickness greater at all sites independent of BMI. | 3 | Internal, single-centre |
| Kempa et al. (2024) | Comparative, 25 lipoedema vs 10 controls | Ultra Micro Angiography visualised subcutaneous microvasculature; most patients grade 3 (n = 13) or grade 2 (n = 8) flow; UMA superior to colour Doppler for depicting microvascular structures. | 3 | Internal; no diagnostic accuracy metric reported |
| Intagliata & Garo (2026) | Retrospective single-centre longitudinal, 60 women, 3 timepoints | 18-20 MHz HRUS as a **monitoring** tool. Medial proximal thigh subcutaneous thickness -18.7% (48.2 to 39.2 mm; p < 0.001) over 6 months; oedema prevalence 100% to 55.0%; echogenicity improved between 3 and 6 months. | 3 | No control group; monitoring, not diagnosis |

### 2.1 Interpretation constraints

Applying `imaging_ml_evidence.yaml § interpretation_rules`:

- **AUC 0.74 is modest.** Per `auc_is_not_a_verdict`, this range MUST be described as adjunctive. Barros et al. themselves frame ultrasound as "an accessible and reproducible **adjunct** to clinical assessment".
- **The paired specificity matters.** The best-performing upper-limb point pairs 82.4% sensitivity with **51.9% specificity** — close to chance for ruling the condition *in*. Quoting the sensitivity alone would breach `report_both_operating_characteristics`.
- **Threshold provenance is a live limitation.** In both Amato et al. and Barros et al., cut-offs were derived and evaluated within the same cohort. Per `threshold_provenance`, such thresholds are optimistically biased and MUST be reported as un-validated.
- **Case-control design blocks predictive values.** Per `prevalence_dependence`, PPV and NPV from these designs do not transfer to a clinic population.

---

## 3. What exists: objective quantification of ultrasound *appearance* and tissue properties

This addresses the second half of the question — identification from ultrasound appearance rather than thickness alone.

**Iker, Mayfield & Gould (2019)**, *Lymphatic Research and Biology* — Tier 3. Computer-assisted (not machine-learned) measurement of dermal echogenicity in 12 lipoedema limbs, 10 lymphoedema limbs, and 8 control limbs.

Dermal-to-subcutaneous-fat echogenicity ratio, by site:

| Site | Lipoedema | Lymphoedema | Control | p |
|---|---|---|---|---|
| Ankle | 1.36 | 0.91 | 1.26 | < 0.01 |
| Calf | 1.58 | 1.05 | 1.54 | < 0.01 |
| Thigh | 1.54 | 1.19 | 1.56 | 0.02 |

### 3.1 A correction this review makes explicit

This paper is widely cited as showing that echogenicity distinguishes lipoedema. **Read against the control column, it does not.** The lipoedema and control ratios are close at every site (1.36 vs 1.26; 1.58 vs 1.54; 1.54 vs 1.56). The separation is driven by **lymphoedema**, which is markedly lower at all three sites.

The correct reading: the dermal echogenicity ratio discriminates *lymphoedema* from the other two groups. It does not, in this dataset, separate lipoedema from normal limbs. The lipoedema-specific finding reported by the authors is increased thickness and hypoechogenicity of the **subcutaneous fat**, a different measure.

This distinction matters for feature selection. A model given the dermal ratio as its principal appearance feature would be inheriting a lymphoedema discriminator.

### 3.2 Why absolute echogenicity is a trap for ML

Per `imaging_ml_evidence.yaml § acquisition_confounding`: B-mode pixel intensity is not an absolute physical quantity. It varies with gain, time-gain compensation, depth, transducer frequency and vendor post-processing. A model trained on raw echogenicity pooled across scanners can learn the device signature rather than the tissue.

Iker et al.'s use of a **ratio** is the mitigation — it references dermis against subcutaneous fat within the same image, cancelling much of the machine-dependent scaling. Any future model should inherit that design property, and any study reporting absolute intensity features across devices without normalisation should be appraised as confounded until it demonstrates otherwise.

### 3.3 Shear-wave elastography: a decisive negative

The direct PubMed search surfaced a second appearance-adjacent modality that the first pass under-covered — and its central result cuts against using tissue stiffness as a discriminative feature.

| Study | Design and n | Result | Tier |
|---|---|---|---|
| Ozturk et al. (2025), *Phlebology* | Cross-sectional, 71 participants (35 lipoedema, 36 healthy) | **No statistically significant difference in elastic modulus between lipoedema and healthy subjects** within BMI strata (25–29.9 and ≥30 kg/m²). Only right pre-tibial stage 2 exceeded stage 1 at BMI 25–29.9. Authors conclude pain characteristics "may be more distinctive than the elastic properties of adipose tissue." | 3 |
| Yaman & Mansız-Kaplan (2026), *Int J Obes* | Cross-sectional, 35 patients | SWE measures **not** correlated with subcutaneous adipose tissue thickness. Thigh SWE-elasticity correlated with VAS pain (r = 0.35, p = 0.03); PainDetect correlated with thigh SWE-velocity (r = 0.38–0.47) and SWE-elasticity (r = 0.44). | 3 |
| Simarro (2026), *Int J Obes* (Letter) | Methodological critique | Argues region-of-interest acquisition in lipoedema SWE studies is **under-specified**, limiting anatomical interpretation. | 4 |
| Novo Rigueiro et al. (2026), *Phlebology* | Prospective within-patient, 12 completers | After shockwave therapy, clinical and quality-of-life measures improved significantly while **ultrasound thickness, elastography and bioimpedance detected no change**. | 3 |

**Reading.** Elastography in lipoedema appears to track *pain and neuropathic symptom burden* rather than the presence of the disease or the amount of tissue. When BMI is controlled, it does not separate cases from controls. A model handed stiffness as a discriminative feature would therefore be building on a measure that the strongest available comparison found non-discriminative — and, per Simarro, one whose acquisition protocol is not yet standardised enough for the measurement to be reproducible across centres.

This is recorded as a caution, not a refutation: the samples are small (35 and 71), and absence of a significant difference in a study of this size is weak evidence of absence.

---

## 4. What exists: machine learning in lipoedema, on other data

| Study | Data | Method | What it is | What it is **not** |
|---|---|---|---|---|
| Nowak et al. (2022), *European Radiology* | **MRI** (3D DIXON MR-lymphangiography), 45 patients | EfficientNet-B1 ensemble for landmarks + U-Net for segmentation. Landmark z-deviation 4.5 ± 3.1 mm; Dice 0.989 (subcutaneous) / 0.994 (subfascial) | Automated **quantification** of tissue volume in lipoedema and lymphoedema | Not a diagnostic classifier, and not ultrasound. Test set was 5 patients. |
| Straub et al. (2025), *Metabolism* | Serum multi-omics (transcriptomic, proteomic, metabolomic, lipidomic) | Benchmarked serum Lipedema Prediction Models (sLPM); ElasticNet, random forest and support vector machine | A **non-imaging** diagnostic model, plus candidate markers of progression | Not imaging-based |
| Jeziorek et al. (2024), *Metabolites* | Anthropometry and body composition, 119 women | PCA plus SVR / random-forest / kNN regression; best MAPE 10.78% | Resting metabolic rate **prediction** for treatment planning | Not diagnosis, not imaging |
| Strohmeier et al. (2022), *Biomedicines* | Immunofluorescence **microscopy** of cultured endothelial cells | ML analysis of CD31 / ZO-1 cellular junction morphology | ML on images in lipoedema research | Microscopy of cultured cells, not clinical ultrasound |
| Matei et al. (2025), *Biomedicines* | Systematic review, 9 studies, > 1000 patients | AI in venous pathology; accuracy > 90% | Evidence AI works in **venous** ultrasound | Lipoedema is named only as a future application |
| Alkhalfan et al. (2025), *Obesity Medicine* | Plasma metabolomics, 38 BMI-matched discovery + 198 validation | ML biomarker selection | Uric acid differed across lipoedema (5.05 mg/dL), lymphoedema (5.4) and overweight controls (4.6); uric-acid-to-cystatin-C ratio separated all three | **Significance lost after adjustment for renal function** — the authors themselves downgrade it. Not imaging. |
| Urooj et al. (2026), *Biomedical Journal* | Review | Lymphoedema imaging and AI | Review of the adjacent condition | Not lipoedema-specific primary evidence |

Per `imaging_ml_evidence.yaml § segmentation_is_not_diagnosis` and `§ adjacent_condition_substitution`, none of the above may be cited as evidence that lipoedema can be detected by AI from ultrasound. Nowak et al. is the one most often mis-cited this way: a Dice score of 0.989 is a measurement result, not diagnostic accuracy.

### 4.1 The AI that does exist in lipoedema is language and image *generation*, not diagnosis

The direct PubMed search showed that the published "AI in lipoedema" literature is dominated by large language models and generative imagery — a category distinct from diagnostic modelling, and one where the findings are cautionary.

| Study | What was evaluated | Result |
|---|---|---|
| Özbek et al. (2026), *Phlebology* | Generative AI asked to produce images of the five Schmeller anatomical lipoedema types; 300 images, blinded classification by two clinicians | Sensitivity 1.00 for Types I–III but **0.00 for Type IV (arm-predominant) and Type V (calf-isolated)** — all such requests were rendered as Type III. Overall accuracy 0.600; specificity for Type III only 0.50. Authors conclude current systems "encode lipedema as a single visual phenotype rather than a distributed anatomical entity." |
| Özbek & Özduran (2026), *Phlebology* | ChatGPT-5o, Gemini-3 and Perplexity answering 30 guideline-based lipoedema questions | Significant differences in reliability (Perplexity 4.95 ± 1.20 vs ChatGPT-5o 4.38 ± 1.05); ChatGPT-5o best on source verifiability and bibliographic precision. Readability required a high educational level, flagged as a barrier for limited e-health literacy. No significant difference in clinical accuracy. |
| Leypold et al. (2024), *Life* | GPT-4 as a consultation assistant across six simulated lipoedema scenarios, expert Likert scoring | Mean 4.24 / 5. |

**Why this matters for the question asked.** Özbek et al. is the closest published work to "identifying lipoedema on the basis of appearance" by an AI system — and it documents a systematic failure at exactly the subtypes that the ultrasound literature is currently trying to characterise (Barros et al. address upper-extremity Type IV). A generative model that cannot represent arm-predominant disease is evidence about *learned visual priors*, not about diagnostic capability, and MUST NOT be cited in either direction as diagnostic evidence. It is recorded here because it is routinely encountered when searching this question.

The two LLM-evaluation studies fall squarely within the AMIS remit: they assess AI-generated medical information about lipoedema, and both stop short of endorsing autonomous use.

---

## 5. Confidence calibration

Per SPECIFICATION.md §5.2 and the `validation_design` ceilings:

- The highest tier located for **any** claim in this domain is **Tier 3**. No Tier 1 or Tier 2 evidence exists for ultrasound diagnosis of lipoedema.
- All located studies are single-centre with internally derived thresholds. The ceiling is therefore **uncertain**.
- Permitted phrasing: *"Evidence is limited"*, *"findings are preliminary"*, *"studies are small and single-centre"*.
- **Prohibited phrasing**: any statement that ultrasound *diagnoses*, *confirms* or *excludes* lipoedema; any statement that AI or machine learning can detect lipoedema on ultrasound.

### 5.1 Mandatory warning (SPECIFICATION.md §5.3)

> The evidence base described here is limited, small in sample size, and single-centre, with diagnostic thresholds that have not been externally validated. No machine-learning model for ultrasound detection of lipoedema has been published. Acting on unverified diagnostic claims in this area — including accepting an imaging result as confirmation or exclusion of lipoedema — could lead to detrimental health outcomes, including missed diagnosis, diagnostic delay, or an irreversible procedure undertaken on inadequate grounds. Qualified physician evaluation must be sought before acting on any of this information. This document informs appraisal; it does not diagnose and does not recommend treatment.

---

## 6. Search boundary (required by `absence_of_evidence`)

| Field | Value |
|---|---|
| Dates of search | 2026-08-18 (scite + web); **2026-08-19 (PubMed, direct)** |
| Sources searched | **PubMed (direct query)**; scite.ai literature index (approx. 210M records, including full-text and Smart Citation excerpts); general web search |
| Terms | `lipedema`/`lipoedema` crossed with `ultrasound`, `ultrasonography`, `sonography`, `sonographic`, `echography`, `machine learning`, `deep learning`, `artificial intelligence`, `radiomics`, `neural network`, `convolutional`, `texture analysis`, `classifier`, `computer-aided`, `echogenicity`, `echotexture`, `elastography`, `quantitative ultrasound`, `grayscale`; both UK and US spellings throughout |
| PubMed yields | lipoedema ∩ ultrasound = 111 records. lipoedema ∩ ML terms (title/abstract) = 8 records. lipoedema ∩ ultrasound ∩ ML terms = **1 record**, which is Nowak et al. (2022), an MRI study matching only via the `diagnostic imaging` MeSH expansion of `ultrasound`. lipoedema ∩ echogenicity/elastography/quantitative-ultrasound = 8 records. |
| Access limitations | **Resolved for PubMed.** The 2026-08-18 pass ran under a network egress policy that blocked PubMed, PMC, Europe PMC, doi.org and ClinicalTrials.gov; the PubMed block no longer applies and that search has been completed. PMC, Europe PMC and ClinicalTrials.gov remain unqueried directly. |
| Not systematically covered | Non-English literature, conference abstracts, dissertations, preprint servers (arXiv/medRxiv), and databases outside PubMed and the scite index. A machine-learning ultrasound method published in an engineering venue not indexed in PubMed would not be captured. |

---

## 7. Work in progress

- **NCT07489248** (Kayseri City Hospital) — "Ultrasonographic evaluation of lower extremity skin and subcutaneous tissue with quantitative echogenicity and elastography in lymphoedema, lipoedema, and healthy control groups." Recruiting; started March 2026, primary completion estimated August 2026. As registered, the analysis is quantitative and statistical rather than machine-learned.
- **NCT06399367** — Multispectral optoacoustic tomography in lipoedema, lymphoedema and vascular malformations.

Per `registry_entries_are_not_results`, these establish that the question is being studied. They are not evidence of an answer, and MUST NOT be cited as such.

---

## 8. Harm cascade analysis (SPECIFICATION.md §8)

The question is high-risk for overstatement because lipoedema patients are frequently dismissed or misdiagnosed as obese, which creates strong demand for an objective test.

**Direct harm.** A patient told that an "AI ultrasound" can confirm or exclude lipoedema may accept a false negative and stop pursuing diagnosis, or accept a false positive and proceed to liposuction — the principal intervention, commonly self-funded and irreversible. At AUC 0.74 with ~52% specificity, the published thresholds cannot bear this weight.

**Indirect harm.** Diagnostic delay is the central documented harm in lipoedema, with associated psychosocial distress. An overstated negative result amplifies precisely the failure mode patients already face.

**Epistemic harm.** Asserting a validated AI capability that does not exist, in a patient group already struggling to be believed, damages trust in both the clinician and the evidence base. The inverse error — dismissing ultrasound entirely — is also unwarranted: the thickness findings are real and replicated across two independent groups.

**Systemic harm.** Unvalidated diagnostic claims are readily repurposed as clinic marketing. Stating validation status in the same sentence as any metric is the mitigation.

---

## 9. Implications for a future study

Recorded as design requirements, not as findings. A study that would answer the question affirmatively would need to satisfy `imaging_ml_evidence.yaml § required_disclosures`:

1. **Reference standard** — blinded clinical diagnosis by assessors independent of image acquisition. Without this, a model learns the acquiring team's diagnostic habits.
2. **Case mix** — BMI-matched controls, as in Barros et al. Unmatched controls let a model separate groups on body mass and call it lipoedema.
3. **Device control** — internally referenced features (ratios) rather than absolute echogenicity; locked gain and depth; device held out at validation. Region-of-interest placement MUST be specified to the level of anatomical landmark, depth and size; Simarro (2026) identifies under-specified ROI acquisition as an active defect in the existing lipoedema elastography literature.
4. **Sample size** — the largest ultrasound series identified here is 102 subjects. This is well below what a convolutional model on raw images requires; a feature-based classifier over the Amato/Barros standardised points plus the Iker subcutaneous echogenicity measures is the proportionate starting design.
5. **Feature selection informed by the negatives** — two candidate features that look attractive should be treated as unproven or non-discriminative on current evidence: the *dermal* echogenicity ratio (§3.1, discriminates lymphoedema rather than lipoedema) and *shear-wave stiffness* (§3.3, no significant case–control difference within BMI strata; tracks pain instead). Including either requires justification, not assumption.
6. **Threshold provenance and external validation** — pre-specified thresholds, and at minimum single-centre external validation, before any confidence above "uncertain" is permitted.
7. **Reporting** — TRIPOD+AI and STARD; calibration reported alongside discrimination, per `§ calibration`.

The proportionate honest claim such a study could make, if successful, is *adjunctive discrimination*, not diagnosis.

---

## 10. Synthesis: what this evidence base can and cannot support

Sections 2-4 catalogue what exists. This section draws the consequences, and is the part most relevant to anyone deciding whether to build the model the question implies.

### 10.1 Feature-discrimination audit

The literature reads as though ultrasound offers a rich feature set for lipoedema. Audited against the question *has this feature been shown to separate lipoedema from controls?*, it does not.

| Candidate feature | Tested against controls? | Outcome |
|---|---|---|
| Subcutaneous thickness, upper limb | Yes — 51 v 51, age- and BMI-matched (Barros) | **Separates.** AUC 0.73-0.74 across four of six sites, independent of BMI |
| Subcutaneous / dermal thickness, lower limb | Yes — 63 v 26 (Amato) | **Separates** at pre-tibial, thigh, lateral leg; malleolar at BMI > 25 |
| Dermal-to-subcutaneous echogenicity ratio | Yes — 12 v 8 limbs (Iker) | **Does not separate** lipoedema from control (§3.1). Separates lymphoedema |
| Shear-wave stiffness | Yes — 35 v 36, BMI-stratified (Ozturk) | **Does not separate** within BMI strata (§3.3); tracks pain instead |
| Subcutaneous fat echogenicity | Partially — reported as reduced in lipoedema, control contrast not quantified | **Indeterminate** |
| Microvascular flow grade (UMA) | No — patients graded, controls not (Kempa) | **Discrimination not computable** from published data |
| Nodularity / "snowstorm" texture | No — described qualitatively only | **Untested** |
| Site-to-site disproportion ratios | No — not constructed in any located study | **Untested** (see §10.5) |

**The consequence.** Of every ultrasound-derived measure that has been put to a case-control test in lipoedema, exactly one class has passed: **tissue thickness**. The two features that most resemble "identifying lipoedema on the basis of ultrasound appearance" — dermal echogenicity and tissue stiffness — have each been tested and each failed to separate cases from controls. A machine-learning model over currently validated ultrasound features would therefore be, in substance, a multivariate thickness model.

That matters, because thickness measurements taken at standardised sites on the same limb are strongly correlated: they are repeated samples of one underlying construct. Correlated inputs contribute little independent information, so the gain from combining them is bounded well below what the number of features suggests. The realistic expectation is incremental improvement on AUC 0.74 — not a step change.

### 10.2 The precision problem

The published operating points are estimated too imprecisely to support the comparisons a model-development programme would need to make.

At the largest existing sample (51 v 51), the 95% confidence interval on an AUC of 0.74 spans roughly **0.64 to 0.84** (Hanley-McNeil, balanced groups). An interval that wide cannot distinguish "barely better than chance" from "clinically useful", and cannot detect the incremental gain a model would be built to deliver.

Sample sizes for a given precision on the AUC estimate, balanced groups:

| Target AUC | Half-width | n per group | Total |
|---|---|---|---|
| 0.74 | ± 0.05 | 188 | 376 |
| 0.80 | ± 0.05 | 151 | 302 |
| 0.80 | ± 0.075 | 68 | 136 |
| 0.85 | ± 0.05 | 117 | 234 |

A development cohort adequate to estimate AUC 0.80 to ± 0.05 needs roughly **300 participants — about three times the largest lipoedema ultrasound series published**. This is before any allowance for a held-out external validation set, which the standard requires before confidence may rise above "uncertain".

*These are precision calculations for estimating a single AUC, not formal prediction-model sample-size calculations (for which Riley et al.'s criteria apply and generally demand more). They are a floor, not a target.*

### 10.3 The prevalence problem

Every located study uses a case-control design at roughly 1:1. Per `imaging_ml_evidence.yaml § prevalence_dependence`, predictive values from such designs do not transfer to a clinic population. The following is therefore an **illustrative projection, not a reported result** — it shows what the best published operating point (sensitivity 82.4%, specificity 51.9%) would imply if applied where lipoedema is not half the population:

| Pre-test probability | Post-test if positive | Post-test if negative |
|---|---|---|
| 50% | 63.1% | 25.3% |
| 30% | 42.3% | 12.7% |
| 20% | 30.0% | 7.8% |
| 10% | 16.0% | 3.6% |

Likelihood ratios: **LR+ = 1.71, LR- = 0.34**.

**The consequence.** At a plausible clinic prevalence, a positive result moves the probability of lipoedema from 10% to 16%. That is not a diagnostic test; it is barely a nudge. The negative direction is more useful — 10% down to 3.6% — which means the published thresholds behave as a weak **rule-out**, not a rule-in.

This asymmetry is the opposite of what the clinical context needs. The documented harm in lipoedema is *under*-recognition and diagnostic delay; a weak rule-out is the tool most likely to compound it, and a marketed "AI scan" that returns negatives with this profile would do real damage. Section 8's direct-harm analysis is not hypothetical — it falls out of the arithmetic.

### 10.4 The reference-standard ceiling

Lipoedema has no biomarker and no histological gold standard. Every study here uses expert clinical diagnosis as ground truth. A supervised model trained against that label can, at its theoretical best, **reproduce expert clinical judgement — never exceed it**.

There is a further circularity worth stating plainly: clinical diagnosis rests partly on inspecting and palpating the same tissue the transducer images. A model trained on those images against those labels may be learning the clinician's heuristic rather than an independent tissue signature. Nothing in the located literature distinguishes these two possibilities, and no study reports whether the labelling clinician was blinded to the imaging.

This caps the honest claim available to any such project at *concordance with expert assessment*, and makes blinded, independent labelling the single most important design decision — more important than the choice of model.

### 10.5 The feature nobody has built

One observation from this audit is actionable. Lipoedema's cardinal clinical sign is **disproportion** — the abrupt demarcation at the malleoli, the spared foot, the mismatch between trunk and limb. It is a *relational* property.

Every located ultrasound study measures **absolute** thickness at anatomical sites and derives per-site cut-offs. None constructs the derived ratio — proximal-to-distal, affected-to-spared, limb-to-trunk — that would mirror the sign clinicians actually pattern-match on.

A ratio feature is attractive for the same reason Iker et al.'s echogenicity ratio was: it is **internally referenced**, so it cancels the two confounders this review has identified as most dangerous. It divides out body-mass scaling (addressing the case-mix problem in §2.1), and because both terms come from the same image and machine settings, it divides out device gain (addressing §3.2). It is the design logic of §3.2 applied to geometry instead of intensity.

This is a hypothesis generated by the review, not a finding. It has not been tested, and it is recorded here as the most promising untested direction rather than as evidence of anything.

It is worked up as a draft study design in [lipoedema-ultrasound-ml-protocol.md](lipoedema-ultrasound-ml-protocol.md) — a design document, not an evidence appraisal, and not ethics-approved.

### 10.6 Bottom line

The honest summary for a clinician asking this question:

- Ultrasound thickness measurement in lipoedema is real, replicated by independent groups, and **modestly discriminative** — an adjunct to clinical assessment, at roughly AUC 0.74.
- No machine-learning model has been built on it, and the feature set available to one is narrower than the literature's breadth implies.
- The existing cohorts are roughly a third of the size needed to estimate performance precisely, let alone to validate it.
- The published operating point functions as a weak rule-out, which is the wrong direction for a condition whose documented harm is under-diagnosis.
- The binding constraint is not the algorithm. It is the reference standard, the sample size, and the absence of a feature that encodes disproportion.

---

## References

*Records added in the 2026-08-19 revision were retrieved from PubMed. Note on author lists: the indexing source used for this review returns the first three authors per record. Entries below therefore list up to three named authors and may omit further co-authors. Verify the full author list against the publisher record before reusing these citations in a manuscript.*

Alkhalfan, F., Sangwan, N., & Aggarwal, A. (2025). Exploring uric acid as a biomarker in lipedema and lymphedema: A metabolomics study with prospective validation. *Obesity Medicine, 55*. https://doi.org/10.1016/j.obmed.2025.100618

Amato, A. C. M., Saucedo, D. Z., Santos, K. da S., & Benitti, D. A. (2021). Ultrasound criteria for lipedema diagnosis. *Phlebology: The Journal of Venous Disease*. https://doi.org/10.1177/02683555211002340

Barros, F. S., Tavares, I. R., & Frasson, P. H. L. (2026). Ultrasound criteria for upper extremity lipedema diagnosis. *Phlebology: The Journal of Venous Disease*. https://doi.org/10.1177/02683555261475099

Iker, E., Mayfield, C. K., & Gould, D. J. (2019). Characterizing lower extremity lymphedema and lipedema with cutaneous ultrasonography and an objective computer-assisted measurement of dermal echogenicity. *Lymphatic Research and Biology, 17*(5), 525-530. https://doi.org/10.1089/lrb.2017.0090

Intagliata, D., & Garo, M. L. (2026). Lipedema in clinical practice: Longitudinal ultrasound monitoring and outcomes in a real-world cohort. *Journal of Aesthetic Medicine, 2*(3), 13. https://doi.org/10.3390/jaestheticmed2030013

Jeziorek, M., Wronowicz, J., & Janek, Ł. (2024). Development of new predictive equations for the resting metabolic rate (RMR) of women with lipedema. *Metabolites, 14*(4), 235. https://doi.org/10.3390/metabo14040235

Kempa, S., Tessmann, V., & Prantl, L. (2024). The value of sonographic microvascular imaging in the diagnosis of lipedema. *Clinical Hemorheology and Microcirculation*. https://doi.org/10.3233/ch-238103

Leypold, T., Lingens, L. F., Beier, J. P., & Boos, A. M. (2024). Integrating AI in lipedema management: Assessing the efficacy of GPT-4 as a consultation assistant. *Life, 14*(5), 646. https://doi.org/10.3390/life14050646

Matei, S.-C., Olariu, S., & Ungureanu, A.-M. (2025). Does artificial intelligence bring new insights in diagnosing phlebological diseases?—A systematic review. *Biomedicines, 13*(4), 776. https://doi.org/10.3390/biomedicines13040776

Novo Rigueiro, M., Bravo González, M., & Prado Moraña, T. (2026). Clinical, ultrasound, elastography and bioimpedance changes after radial extracorporeal shock wave therapy in patients with lipedema: A prospective within-patient study. *Phlebology*. https://doi.org/10.1177/02683555261451555

Nowak, S., Henkel, A., & Theis, M. (2022). Deep learning for standardized, MRI-based quantification of subcutaneous and subfascial tissue volume for patients with lipedema and lymphedema. *European Radiology, 33*(2), 884-892. https://doi.org/10.1007/s00330-022-09047-0

Özbek, İ. C., & Özduran, E. (2026). Artificial intelligence in the management of chronic pain and lipedema: A comparative analysis of ChatGPT-5o, Gemini-3, and Perplexity AI in terms of readability and academic reliability. *Phlebology*. https://doi.org/10.1177/02683555261460252

Özbek, I. C., Alyanak, B., & Dede, B. T. (2026). Evaluation of generative artificial intelligence in producing anatomically distinct lipedema subtypes: A diagnostic accuracy study. *Phlebology*. https://doi.org/10.1177/02683555261467340

Ozturk, G., Kahraman, A. N., & Akpinar, P. (2025). Relationship of the tissue stiffness measured using shear wave elastography with the pain threshold and quality of life of patients with lipedema: A cross-sectional study. *Phlebology, 40*(8), 627-637. https://doi.org/10.1177/02683555251357094

Simarro, J. L. (2026). Lipedema and shear-wave elastography: Under-specification of ROI acquisition limits anatomical interpretation [Letter]. *International Journal of Obesity*. https://doi.org/10.1038/s41366-026-02163-7

Straub, L. G., Funcke, J.-B., & Joffin, N. (2025). Defining lipedema's molecular hallmarks by multi-omics approach for disease prediction in women. *Metabolism, 168*, 156191. https://doi.org/10.1016/j.metabol.2025.156191

Strohmeier, K., Hofmann, M., & Jacak, J. (2022). Multi-level analysis of adipose tissue reveals the relevance of perivascular subpopulations and an increased endothelial permeability in early-stage lipedema. *Biomedicines, 10*(5), 1163. https://doi.org/10.3390/biomedicines10051163

Urooj, B., Ali, S., & Xiao, F. (2026). Lymphedema imaging and AI: A review of diagnostic modalities, biomarkers, and clinical integration. *Biomedical Journal, 49*(3), 100932. https://doi.org/10.1016/j.bj.2025.100932

Yaman, A., & Mansız-Kaplan, B. (2026). Assessment of the elasticity of lipedematous tissue and the examination of the relationship between pain and fibrosis in lipedema. *International Journal of Obesity, 50*(5), 1136-1141. https://doi.org/10.1038/s41366-026-02049-8
