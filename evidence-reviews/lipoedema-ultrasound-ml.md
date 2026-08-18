# Evidence Review: Machine Learning for Ultrasound Detection of Lipoedema

**Question addressed**: Is there a published study applying machine-learning criteria to ultrasound detection of lipoedema characteristics, or identifying lipoedema on the basis of ultrasound appearance?

| Field | Value |
|---|---|
| Review date | 2026-08-18 |
| AMIS conformance | Level 3 (Full) |
| Standards applied | SPECIFICATION.md Standards 1-5; `standards/imaging_ml_evidence.yaml` v1.0.0 |
| Highest source tier located | Tier 3 |
| Permitted confidence ceiling | **Uncertain** (see §5) |
| Therapeutic intent | None. This document is an evidence appraisal, not clinical guidance. |

---

## 1. Answer

**No study was identified, in the sources searched, that trains or validates a machine-learning model on ultrasound images to detect or classify lipoedema.**

This negative claim is scoped per `imaging_ml_evidence.yaml § absence_of_evidence`; the search boundary is stated in §6. It means *not identified in these sources on this date*, not *does not exist*.

Three adjacent bodies of work do exist, and are routinely conflated with the question. They are distinguished in §2, §3 and §4.

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

## 3. What exists: objective quantification of ultrasound *appearance*

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

---

## 4. What exists: machine learning in lipoedema, on other data

| Study | Data | Method | What it is | What it is **not** |
|---|---|---|---|---|
| Nowak et al. (2022), *European Radiology* | **MRI** (3D DIXON MR-lymphangiography), 45 patients | EfficientNet-B1 ensemble for landmarks + U-Net for segmentation. Landmark z-deviation 4.5 ± 3.1 mm; Dice 0.989 (subcutaneous) / 0.994 (subfascial) | Automated **quantification** of tissue volume in lipoedema and lymphoedema | Not a diagnostic classifier, and not ultrasound. Test set was 5 patients. |
| Straub et al. (2025), *Metabolism* | Serum multi-omics | Prediction models from serum factors | A **non-imaging** diagnostic model | Not imaging-based |
| Jeziorek et al. (2024), *Metabolites* | Anthropometry and body composition, 119 women | PCA plus SVR / random-forest / kNN regression; best MAPE 10.78% | Resting metabolic rate **prediction** for treatment planning | Not diagnosis, not imaging |
| Strohmeier et al. (2022), *Biomedicines* | Immunofluorescence **microscopy** of cultured endothelial cells | ML analysis of CD31 / ZO-1 cellular junction morphology | ML on images in lipoedema research | Microscopy of cultured cells, not clinical ultrasound |
| Matei et al. (2025), *Biomedicines* | Systematic review, 9 studies, > 1000 patients | AI in venous pathology; accuracy > 90% | Evidence AI works in **venous** ultrasound | Lipoedema is named only as a future application |
| Urooj et al. (2026), *Biomedical Journal* | Review | Lymphoedema imaging and AI | Review of the adjacent condition | Not lipoedema-specific primary evidence |

Per `imaging_ml_evidence.yaml § segmentation_is_not_diagnosis` and `§ adjacent_condition_substitution`, none of the above may be cited as evidence that lipoedema can be detected by AI from ultrasound. Nowak et al. is the one most often mis-cited this way: a Dice score of 0.989 is a measurement result, not diagnostic accuracy.

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
| Date of search | 2026-08-18 |
| Sources searched | scite.ai literature index (approx. 210M records, including full-text and Smart Citation excerpts); general web search |
| Terms | `lipedema`/`lipoedema` crossed with `ultrasound`, `ultrasonography`, `sonograph*`, `machine learning`, `deep learning`, `artificial intelligence`, `radiomics`, `neural network`, `convolutional`, `texture analysis`, `classifier`, `echogenicity`, `echotexture`, `computer-aided`; both UK and US spellings throughout |
| Access limitations | Direct PubMed, PMC, Europe PMC, doi.org and ClinicalTrials.gov queries were **blocked by the executing environment's network egress policy**. Coverage therefore rests on the scite index plus web search. A repeat search with direct database access is warranted before treating this negative as settled. |
| Not systematically covered | Non-English literature, conference abstracts, dissertations, preprint servers |

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
3. **Device control** — internally referenced features (ratios) rather than absolute echogenicity; locked gain and depth; device held out at validation.
4. **Sample size** — the largest ultrasound series identified here is 102 subjects. This is well below what a convolutional model on raw images requires; a feature-based classifier over the Amato/Barros standardised points plus the Iker subcutaneous echogenicity measures is the proportionate starting design.
5. **Threshold provenance and external validation** — pre-specified thresholds, and at minimum single-centre external validation, before any confidence above "uncertain" is permitted.
6. **Reporting** — TRIPOD+AI and STARD; calibration reported alongside discrimination, per `§ calibration`.

The proportionate honest claim such a study could make, if successful, is *adjunctive discrimination*, not diagnosis.

---

## References

*Note on author lists: the indexing source used for this review returns the first three authors per record. Entries below therefore list up to three named authors and may omit further co-authors. Verify the full author list against the publisher record before reusing these citations in a manuscript.*

Amato, A. C. M., Saucedo, D. Z., Santos, K. da S., & Benitti, D. A. (2021). Ultrasound criteria for lipedema diagnosis. *Phlebology: The Journal of Venous Disease*. https://doi.org/10.1177/02683555211002340

Barros, F. S., Tavares, I. R., & Frasson, P. H. L. (2026). Ultrasound criteria for upper extremity lipedema diagnosis. *Phlebology: The Journal of Venous Disease*. https://doi.org/10.1177/02683555261475099

Iker, E., Mayfield, C. K., & Gould, D. J. (2019). Characterizing lower extremity lymphedema and lipedema with cutaneous ultrasonography and an objective computer-assisted measurement of dermal echogenicity. *Lymphatic Research and Biology, 17*(5), 525-530. https://doi.org/10.1089/lrb.2017.0090

Intagliata, D., & Garo, M. L. (2026). Lipedema in clinical practice: Longitudinal ultrasound monitoring and outcomes in a real-world cohort. *Journal of Aesthetic Medicine, 2*(3), 13. https://doi.org/10.3390/jaestheticmed2030013

Jeziorek, M., Wronowicz, J., & Janek, Ł. (2024). Development of new predictive equations for the resting metabolic rate (RMR) of women with lipedema. *Metabolites, 14*(4), 235. https://doi.org/10.3390/metabo14040235

Kempa, S., Tessmann, V., & Prantl, L. (2024). The value of sonographic microvascular imaging in the diagnosis of lipedema. *Clinical Hemorheology and Microcirculation*. https://doi.org/10.3233/ch-238103

Matei, S.-C., Olariu, S., & Ungureanu, A.-M. (2025). Does artificial intelligence bring new insights in diagnosing phlebological diseases?—A systematic review. *Biomedicines, 13*(4), 776. https://doi.org/10.3390/biomedicines13040776

Nowak, S., Henkel, A., & Theis, M. (2022). Deep learning for standardized, MRI-based quantification of subcutaneous and subfascial tissue volume for patients with lipedema and lymphedema. *European Radiology, 33*(2), 884-892. https://doi.org/10.1007/s00330-022-09047-0

Straub, L. G., Funcke, J.-B., & Joffin, N. (2025). Defining lipedema's molecular hallmarks by multi-omics approach for disease prediction in women. *Metabolism, 168*, 156191. https://doi.org/10.1016/j.metabol.2025.156191

Strohmeier, K., Hofmann, M., & Jacak, J. (2022). Multi-level analysis of adipose tissue reveals the relevance of perivascular subpopulations and an increased endothelial permeability in early-stage lipedema. *Biomedicines, 10*(5), 1163. https://doi.org/10.3390/biomedicines10051163

Urooj, B., Ali, S., & Xiao, F. (2026). Lymphedema imaging and AI: A review of diagnostic modalities, biomarkers, and clinical integration. *Biomedical Journal, 49*(3), 100932. https://doi.org/10.1016/j.bj.2025.100932
