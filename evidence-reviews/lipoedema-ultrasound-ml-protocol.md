# Draft Protocol: Disproportion-Ratio Ultrasound Features for Lipoedema Discrimination

**Status: draft design document, derived from an evidence review. Not ethics-approved, not statistician-reviewed, not registered. It is a starting point for those conversations, not a substitute for them.**

| Field | Value |
|---|---|
| Derived from | [lipoedema-ultrasound-ml.md](lipoedema-ultrasound-ml.md) §10.5 |
| Document type | Study design proposal — **not** an AMIS evidence appraisal |
| Date | 2026-08-19 |
| Constraints honoured | `standards/imaging_ml_evidence.yaml` v1.1.0 required disclosures |

---

## 1. Why this protocol exists

The evidence review found no published machine-learning model for ultrasound detection of lipoedema, and — more usefully — found that the feature set available to one is far narrower than the literature implies. Of every ultrasound-derived measure put to a case-control test, only **tissue thickness** has separated cases from controls. Dermal echogenicity and shear-wave stiffness were each tested and each failed.

The review's §10.5 identified one untested direction with a principled rationale. This document works it up.

## 2. Hypothesis

Lipoedema's cardinal clinical sign is **disproportion**, not bulk: the abrupt supramalleolar demarcation with a spared foot, limb volume out of keeping with the trunk, and near-symmetry between sides. Every located ultrasound study measures **absolute** subcutaneous thickness at anatomical sites and derives per-site cut-offs.

> **H1.** Internally referenced *ratios* of subcutaneous thickness discriminate lipoedema from BMI-matched controls better than absolute thickness at any single site.

**Why ratios should work.** A ratio of two thicknesses from the same image and the same machine settings divides out the two confounders the review identified as most dangerous:

- **Body-mass scaling.** In simple obesity, limb and trunk subcutaneous fat scale together. In lipoedema the limb is disproportionate to the trunk. An absolute thickness cannot distinguish these; a limb-to-trunk ratio is constructed precisely to.
- **Device gain.** Both terms share acquisition settings, so vendor post-processing, gain and TGC cancel — the same design logic Iker et al. applied to echogenicity, transposed from intensity to geometry.

This is a hypothesis the review generated. It has never been tested.

## 3. Candidate ratio features

Each is derived from paired measurements at standardised points, computed per limb.

| # | Ratio | Clinical sign it encodes |
|---|---|---|
| R1 | Supramalleolar : dorsum of foot | The **cuff sign** — abrupt demarcation with foot sparing. The sharpest specific sign |
| R2 | Proximal thigh : supramalleolar | Proximal-to-distal gradient within the limb |
| R3 | Pre-tibial : suprailiac (trunk) | **Limb-to-trunk disproportion** — the obesity discriminator |
| R4 | Left : right at each matched site | Symmetry index; near 1.0 in lipoedema, departs in unilateral lymphoedema |

R3 is the feature that most directly addresses the diagnostic dilemma the condition actually presents — being told one is simply obese.

Absolute thicknesses at the Amato and Barros standardised points are retained as the **comparator**, not discarded. The hypothesis is explicitly that ratios beat them; that comparison must be made on the same subjects.

## 4. Design

Cross-sectional diagnostic accuracy study, prospective recruitment, **blinded reference standard**. Reported to STARD; any model reported to TRIPOD+AI.

**Arms**
- Lipoedema (index)
- **BMI-, age- and sex-matched controls without lipoedema** — the essential comparator, matched because unmatched controls let any model separate groups on body mass and call it disease
- Optional third arm: unilateral lymphoedema, to test R4 and to check that features are not inheriting a lymphoedema discriminator (the failure mode identified in review §3.1)

## 5. Reference standard — the single most important design decision

Lipoedema has no biomarker and no histological gold standard. A supervised model can at best reproduce expert clinical judgement (review §10.4). The protocol cannot remove that ceiling, but it can stop the ceiling being contaminated and can **measure** it:

1. Diagnosis by **two clinicians independent of image acquisition**, each **blinded to all ultrasound**, applying a pre-specified criterion set.
2. Disagreements adjudicated by a third blinded clinician.
3. **Inter-rater kappa reported.** This quantifies the ceiling: if expert agreement is κ = 0.70, no model built against these labels can meaningfully claim to exceed it, and any reported accuracy above that band should be read as suspicion of leakage rather than success.
4. Sonographers blinded to clinical diagnosis at acquisition.

Without (1) and (4), the study cannot distinguish a tissue signature from the clinician's own heuristic, since diagnosis rests partly on palpating the tissue being imaged.

## 6. Acquisition — locked and specified

Per `imaging_ml_evidence.yaml § acquisition_confounding` and `§ region_of_interest_specification`:

- Single transducer class and frequency band; **gain, depth and TGC locked** and recorded per image
- ROI specified by anatomical landmark, depth and dimensions — Simarro (2026) identifies under-specified ROI as an active defect in the lipoedema elastography literature
- Measurement from dermal–epidermal junction to deep fascia (Barros convention), standardised patient position, minimal transducer pressure with a standoff where compressible
- Duplicate acquisition in a random ~20% subsample by a second sonographer → **inter- and intra-operator reproducibility (ICC)** reported before any modelling
- Multi-device acquisition preferred, with **device held out at validation** to test for device-signature learning

A feature that is not reproducible between operators cannot support a model, and reproducibility should be established first.

## 7. Sample size

From the review's precision analysis (Hanley–McNeil, balanced groups):

| Target | Per group | Total | With 10% attrition |
|---|---|---|---|
| AUC 0.80 ± 0.05 | 151 | 302 | **~334 recruited** |
| AUC 0.78 ± 0.05 | 164 | 328 | ~362 recruited |

**Recruit ≥ 165 per arm.** For reference, the largest published lipoedema ultrasound series is 102 in total.

*These are precision calculations for estimating a single AUC. They are a floor. A formal prediction-model sample-size calculation (Riley et al.) and a DeLong-based power calculation for the ratio-vs-absolute comparison should be done by a statistician before recruitment, and will likely demand more.*

## 8. Analysis plan — pre-specified

1. **Reproducibility first.** ICCs for every candidate measurement. Features below a pre-set ICC threshold are dropped before any model is fitted.
2. **Primary comparison.** AUC of the best ratio feature set versus AUC of the best absolute-thickness feature set, on the same subjects, compared by DeLong. H1 is supported only if the ratio set is superior.
3. **Thresholds pre-specified**, not derived and evaluated in the same data (review §2.1 identifies this as a live defect in the existing cut-off literature).
4. **Calibration reported alongside discrimination** — calibration slope and intercept, not AUC alone.
5. **Model class proportionate to n.** With ~330 subjects and a handful of correlated features, penalised logistic regression is the appropriate primary model. A convolutional network on raw images is not supportable at this sample size and should not be attempted as the primary analysis.
6. **External validation** in an independent centre and device before any confidence claim above *uncertain* is permitted.

## 9. Pre-specified expectations, including the negative ones

Recording these in advance protects against post-hoc rationalisation:

- **Elastography and dermal echogenicity are exploratory only.** Ozturk et al. found no significant case–control difference in elastic modulus within BMI strata; Iker et al.'s dermal echogenicity ratio separates lymphoedema, not lipoedema. Including either as a primary feature would contradict the available evidence. They are measured to test the prior, not relied upon.
- **A modest result is the expected result.** The existing single-site benchmark is AUC 0.74. A plausible successful outcome is incremental — an AUC in the high 0.70s to mid 0.80s — not 0.95. An AUC above ~0.90 in this setting should trigger a leakage audit before celebration.
- **The realistic clinical role is rule-out and triage**, not confirmation. At the published operating point, LR+ is 1.71 and LR− is 0.34 (review §10.3).

## 10. The honest claim ceiling

The strongest conclusion this design can support is **adjunctive concordance with blinded expert assessment**, in the population studied, on the devices studied.

It cannot support "ultrasound AI diagnoses lipoedema." Per `imaging_ml_evidence.yaml § validation_design`, a single-centre internally validated study caps permitted language at *uncertain*; single-centre external validation raises it to *qualified*; only prospective multicentre evaluation against a blinded reference standard permits definitive phrasing.

Any dissemination must state the operating characteristics in the same sentence as any headline metric, per `§ commercial_capture`. Lipoedema patients are an actively marketed-to population, and an overstated diagnostic claim would be repurposed as clinic advertising within weeks.

## 11. What would falsify H1

Stated up front so the study can return a clean negative, which would itself be worth publishing:

- Ratio features fail to exceed absolute thickness on DeLong comparison, or
- Ratio features prove less reproducible between operators than absolute measurements (plausible — a ratio compounds the error of two measurements), or
- R3 (limb : trunk) fails to separate lipoedema from BMI-matched obesity, which would undercut the core rationale

A null result here is informative and should be reported. The field's current problem is not a shortage of optimistic claims.
