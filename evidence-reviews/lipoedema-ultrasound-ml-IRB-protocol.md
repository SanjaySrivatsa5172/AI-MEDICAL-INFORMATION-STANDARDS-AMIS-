# Full Research Protocol for IRB Submission

## Quantitative Ultrasound Tissue Characterisation and Machine Learning for the Identification of Lipoedema: The Sparkle Study

**Status: draft for institutional review. Not yet submitted, not yet approved. Placeholders marked `[...]` must be completed by the investigator before submission. Statistical sections require sign-off by a named statistician; the power calculations herein are computed and reproducible but are not a substitute for that review.**

| Field | Entry |
|---|---|
| Protocol title | Quantitative Ultrasound Tissue Characterisation and Machine Learning for the Identification of Lipoedema (The Sparkle Study) |
| Short title | The Sparkle Study |
| Protocol version | 1.0 |
| Date | 2026-08-19 |
| Principal Investigator | `[Name, degrees, department, institution]` |
| Co-investigators | `[Sonographer(s), statistician, pathologist, surgeon]` |
| Sponsor | `[Institution / investigator-initiated]` |
| Funding | `[Source or "unfunded / departmental"]` |
| Design | Prospective, cross-sectional, case–control diagnostic accuracy study with a nested within-subject paired comparison, an embedded histological correlation sub-study, and a separate prospective validation cohort |
| Population | Adults with clinically diagnosed lipoedema and four comparison groups |
| Sample size | 391 development cohort (5 arms) + 90 independent test cohort + 30 histology sub-study participants (nested) |
| Duration | `[24–36 months anticipated]` |
| Risk classification | **Minimal risk** for the imaging protocol. The nested histology sub-study uses tissue already being removed during clinically indicated surgery and adds no incision, anaesthesia or operative time |
| Companion document | [lipoedema-ultrasound-ml-protocol.md](lipoedema-ultrasound-ml-protocol.md) — the technical acquisition standard, incorporated here by reference |

---

# 1. Introduction and Background

## 1.1 The clinical problem

Lipoedema is a chronic, progressive disorder of subcutaneous adipose tissue that affects women almost exclusively. It is characterised by disproportionate, symmetrical accumulation of subcutaneous fat in the limbs, with pain, tenderness, easy bruising and a tendency to orthostatic oedema. It is distinct from obesity and from lymphoedema, but is routinely mistaken for both.

The central clinical failure is **diagnostic delay and misattribution**. Patients are commonly told that their limb enlargement is simple obesity and that they should lose weight — advice that does not address the condition and that many patients experience as dismissive. Years frequently pass before a correct diagnosis is made. The consequences are not merely administrative: they include progression to later stages, secondary lymphatic dysfunction, mobility loss, and documented psychosocial harm including depression, disordered eating and social withdrawal.

There is at present **no biomarker and no histological gold standard** for lipoedema. Diagnosis rests on clinical assessment by an experienced clinician. Where such expertise is unavailable — which is most places — patients are not diagnosed.

## 1.2 What imaging currently offers, and why it is insufficient

A structured appraisal of the published evidence was conducted for this programme (companion document, [lipoedema-ultrasound-ml.md](lipoedema-ultrasound-ml.md)). Its findings define the gap this study addresses.

**Ultrasound criteria for lipoedema exist, but they are morphometric and modest.** Published work measures the *thickness* of dermis and subcutaneous tissue at standardised anatomical points and derives diagnostic cut-offs. In the largest published series (102 women, 51 with lipoedema and 51 matched controls), the best-performing site achieved an area under the ROC curve of 0.74, with sensitivity 82.4% against specificity 51.9%. A specificity near 50% has little capacity to rule the condition in. Independent work in the lower limb reached similar conclusions. Both derived their thresholds within the same cohort used to evaluate them, so those thresholds remain externally unvalidated.

**Two measures of tissue *appearance* have been tested and have failed.** The dermal-to-subcutaneous echogenicity ratio, frequently cited as distinguishing lipoedema, in fact separates *lymphoedema* from the other groups; lipoedema and control values are closely similar at every anatomical site (1.36 vs 1.26 at ankle; 1.58 vs 1.54 at calf; 1.54 vs 1.56 at thigh). Shear-wave elastography likewise shows **no significant difference in elastic modulus between lipoedema patients and healthy subjects** within BMI strata; the published work concludes that pain characteristics are more distinctive than the elastic properties of the tissue.

**Machine learning has not been applied to ultrasound in this condition.** A direct search of PubMed returned exactly one record at the intersection of lipoedema, ultrasound and machine-learning terms, and that record is a magnetic resonance segmentation study that matched only through MeSH expansion. Deep learning in lipoedema exists only for MRI tissue-volume quantification; other machine-learning work in the condition uses serum multi-omics or metabolic data, not imaging. The published artificial-intelligence literature in lipoedema is otherwise dominated by large language models and generative imagery, neither of which is diagnostic.

## 1.3 The observation motivating this study

Experienced clinicians report that lipoedematous subcutaneous fat has a **characteristic "sparkling" appearance on B-mode ultrasound**, recognisable casually and at a glance, on standard machine settings. This observation has never been formally defined, quantified, validated against tissue, or tested as a diagnostic feature.

The descriptors already circulating in clinical practice — "snowstorm", "starry sky", "pebbles in cotton wool" — almost certainly refer to the same phenomenon.

## 1.4 Why this is tractable: the phenomenon has a known physical basis

The sparkling appearance is not an impressionistic notion. It corresponds to a well-characterised departure from *fully developed speckle*.

When an ultrasound resolution cell contains many small, randomly positioned scatterers of comparable strength, the echo envelope follows a **Rayleigh** distribution, seen as smooth, featureless speckle. When a population of **discrete, high-amplitude, coherent reflectors** is added, the envelope shifts into the **post-Rayleigh (Rician)** regime. That shift is what the eye perceives as sparkle.

This regime shift is precisely what envelope statistics were developed to measure. The **Nakagami parameter *m*** (with *m* > 1 indicating post-Rayleigh behaviour) and the **homodyned-K coherent-to-diffuse ratio** are established estimators with a mature theoretical literature. The clinician's visual impression and the quantitative estimator are measuring the same underlying physics.

**Predicted tissue substrate.** Lipoedema histology describes adipocyte hypertrophy, interstitial fluid accumulation, septal fibrosis and altered microvasculature. Fibrotic and thickened interlobular septa supply discrete bright reflectors; interstitial fluid supplies the anechoic background against which those reflectors become conspicuous. The prediction is therefore specific and falsifiable: **bright-spot density should correlate with septal fibrosis, and spot-to-background contrast with interstitial fluid**.

## 1.5 Precedents supporting feasibility

Three separate literatures make this programme credible rather than speculative.

**Quantitative ultrasound is mature — in the liver.** Attenuation coefficient, backscatter coefficient, fat-fraction and entropy-based tissue characterisation are established for hepatic steatosis, with commercial implementations and settled estimator theory. This study transfers established methods to a new tissue; it does not invent methodology.

**Structural ultrasound phenotyping of subcutaneous fat has a direct precedent — in cellulite.** A 2025 observational cohort of 150 women used 20 MHz high-frequency ultrasound to subclassify stage III cellulite by echotexture, fibrosis and oedema, identifying a third phenotype that clinical inspection does not recognise. Clinical and ultrasound classification disagreed in 33.3% of cases, with only moderate agreement (Gwet's AC1 = 0.444). Subcutaneous fat *does* carry structurally meaningful ultrasound information, and visual inspection alone captures it poorly.

**Ultrasound appearance has been tied to histology — in lymphoedema.** A 2025 study graded subcutaneous echogenicity and subcutaneous echo-free space on conventional 6–18 MHz ultrasound in 22 patients, biopsying 46 surgical sites during lymphaticovenular anastomosis. Adipose tissue remodelling — adipocyte hypertrophy, inflammatory infiltration, fibrosis — tracked those ultrasound grades. Sensitivity was high; specificity was insufficient.

**The gap this study fills.** The estimator theory is solved elsewhere. The appearance-phenotyping premise is established in the same tissue and the same demographic. The histological validation template exists in the adjacent condition. Lipoedema offers the identical tissue-access opportunity through liposuction — and no one has taken it.

---

# 2. Objectives and Hypotheses

## 2.1 Primary objective

To determine whether the sparkling appearance of lipoedematous subcutaneous fat is a reproducible, quantifiable acoustic phenomenon that distinguishes affected tissue from unaffected tissue **within the same participant**, independent of tissue thickness.

## 2.2 Secondary objectives

1. To determine whether quantitative sparkle parameters distinguish lipoedema from BMI-matched controls, from obesity without lipoedema, from cellulite without lipoedema, and from lymphoedema.
2. To determine whether these parameters correlate with histological features of adipose tissue remodelling in tissue biopsied from the scanned site.
3. To develop and then prospectively validate a machine-learning model that classifies participants from standardised ultrasound images, and to determine whether it outperforms simple interpretable baselines.
4. To establish and publish the **reproducibility** (inter- and intra-operator) of every candidate parameter under a standardised acquisition protocol.

## 2.3 Hypotheses

| ID | Hypothesis |
|---|---|
| **H1 (primary)** | Quantitative sparkle metrics differ significantly between an affected limb site and the participant's own upper abdominal subcutaneous fat, in participants with lipoedema, and this difference is not present in controls |
| **H2** | Sparkle metrics discriminate lipoedema from each comparison arm, independent of subcutaneous thickness |
| **H3** | Sparkle metrics correlate with histological septal fibrosis, adipocyte diameter, inflammatory infiltrate and interstitial fluid in tissue biopsied from the scanned site |
| **H4** | A machine-learning model trained against expert clinical classification of the **subject** outperforms thickness-alone and bright-spot-density-alone baselines on an independent, never-iterated test cohort |

**Labelling principle.** Human experts classify **participants** as lipoedema or non-lipoedema on clinical grounds. Humans do **not** grade ultrasound appearance, and there is no human image-reading comparator. This avoids the circularity of asking readers to grade the same images the model analyses, and makes the algorithm responsible for discovering the image signature rather than reproducing a human reading of it.

---

# 3. Study Design

Prospective, cross-sectional, multi-arm case–control diagnostic accuracy study, comprising:

1. A **development cohort** (5 arms) for parameter estimation, reproducibility assessment and model development.
2. A nested **within-subject paired comparison** (affected site vs the participant's own upper abdomen) serving the primary endpoint.
3. A nested **histological correlation sub-study** in participants proceeding to clinically indicated liposuction.
4. A separate, later-recruited **independent test cohort** for single-shot evaluation of the frozen model.

## 3.1 Study arms

| Arm | Description | n (development) |
|---|---|---|
| A | **Lipoedema** — clinically diagnosed, stratified by distribution variant | 68 |
| B | **Healthy controls**, BMI-matched to Arm A | 68 |
| C | **Obesity without lipoedema**, BMI-matched | 68 |
| D | **Cellulite without lipoedema** | 68 |
| E | **Lymphoedema** | 68 |

**Why Arms C, D and E are scientifically necessary.** Arm C addresses the actual diagnostic dilemma — patients told they are simply obese. Arm D is essential because cellulite affects the same body regions in the same demographic and has its own documented ultrasound structural phenotypes; without this arm, any signature we identify could be attributed to cellulite and the study would be uninterpretable. Arm E tests specificity against the other condition characterised by adipose tissue remodelling.

## 3.2 Distribution-variant stratification

Lipoedema occurs in variants confined to the hips, extending from hips to knee, and extending from hips to ankle, with upper-limb involvement in a substantial minority. Arm A recruitment is stratified across these variants, and **the primary hypothesis is tested within every variant stratum**. A signature present only in distally extensive disease would fail the clinical requirement that motivates this study.

---

# 4. Participants

## 4.1 Inclusion criteria — all arms

- Age 18–70 years inclusive
- Able to give written informed consent
- Able to lie supine for approximately 30 minutes

## 4.2 Arm-specific inclusion criteria

**Arm A (lipoedema):** Clinical diagnosis of lipoedema established independently by two study clinicians per §5.1, with recorded stage (I–III) and distribution variant.

**Arm B (healthy control):** No clinical evidence of lipoedema, lymphoedema or clinically significant cellulite; BMI matched to an Arm A participant within ±2 kg/m².

**Arm C (obesity without lipoedema):** BMI ≥ 30 kg/m² without clinical features of lipoedema; matched to an Arm A participant within ±2 kg/m².

**Arm D (cellulite without lipoedema):** Clinically graded cellulite (Nürnberger–Müller scale) without features of lipoedema.

**Arm E (lymphoedema):** Clinically diagnosed lymphoedema with recorded ISL stage.

## 4.3 Exclusion criteria — all arms

- Pregnancy or breastfeeding (self-reported; pregnancy testing not required as ultrasound is non-teratogenic, but excluded to remove fluid-status confounding)
- Prior liposuction, lipectomy or other surgery **at any planned scan site**
- Active cellulitis, erysipelas, dermatitis, open wound, ulceration or rash at any planned scan site
- Known malignancy under active treatment
- Renal failure, decompensated cardiac failure or hepatic failure — each causes oedema that would confound fluid-sensitive parameters
- Current diuretic therapy, or initiation/dose change of any medication with significant fluid effects (including calcium channel blockers, corticosteroids, gabapentinoids) within 4 weeks
- Initiation or change of systemic hormonal therapy within 3 months
- Weight change exceeding 5% of body weight within 3 months
- Any implanted device or dressing preventing probe contact at a scan site
- Inability to comply with the pre-scan preparation requirements in §6.2

## 4.4 Sub-study inclusion (histological correlation)

Arm A participants already scheduled for **clinically indicated** liposuction, who consent separately to the sub-study. Enrolment in the sub-study is **not** a condition of participation in the main study, and the decision to undergo liposuction is made independently of this research, on clinical grounds, by the treating surgeon.

## 4.5 Sex distribution

Lipoedema affects women almost exclusively. Recruitment is therefore expected to be overwhelmingly or entirely female across Arms A–D. This reflects the disease epidemiology and is not an exclusion. Men meeting criteria will be enrolled if identified and analysed descriptively. Arm E may include men.

## 4.6 Vulnerable populations

No vulnerable population is targeted. Participants under 18, adults lacking capacity to consent, prisoners and institutionalised individuals are not enrolled. Patients of the investigators may be enrolled, with the safeguards in §11.3 to protect against perceived coercion.

---

# 5. Reference Standard

## 5.1 Establishing the diagnostic label

The label against which the model is trained is **expert clinical classification of the participant**, performed by **a single expert clinician (the Principal Investigator)**, **before any study imaging is performed**.

### 5.1.1 The procedure

1. The PI examines the participant and classifies them as **lipoedema** or **non-lipoedema control**, using the pre-specified written criterion set in Appendix A.
2. **The classification is recorded, timestamped and locked in the study database BEFORE the participant proceeds to ultrasound.** Once locked it cannot be edited; any correction is appended as a new, separately timestamped entry with a documented reason, and both entries are retained and reported.
3. The participant then proceeds to imaging, performed by a technician **blinded to the classification** (§6.6).
4. The PI takes **no part** in acquiring, viewing, interpreting or analysing study ultrasound images.

### 5.1.2 Why pre-imaging locking is the load-bearing safeguard

Because the label for each participant is fixed and locked **before that participant's images exist**, the label cannot have been influenced by those images. This is what makes a single-adjudicator design scientifically defensible, and it must be enforced technically — by database locking — rather than by intention.

### 5.1.3 The circularity hazard, stated plainly

**This is the single most important methodological question in the study.**

The phenomenon under investigation is an ultrasound appearance. The PI is an experienced ultrasound practitioner. If ultrasound appearance forms any part of the PI's clinical diagnostic reasoning, then the labels would be partly derived from the very signal the model is being asked to discover, and the study would be circular.

**Required mitigations:**

- **The criterion set in Appendix A must contain no ultrasound-derived criterion.** Classification rests on history and physical examination only — disproportionate symmetrical limb fat, tenderness on pressure, easy bruising, Stemmer sign, foot sparing, resistance to caloric restriction, family history. This must be explicit in the criterion document.
- **The PI must not have performed or reviewed any prior ultrasound of the participant** for diagnostic purposes before locking the classification. Where a participant has had prior imaging, this is recorded, and a sensitivity analysis excluding those participants is pre-specified.
- **A declaration is required in the protocol and the publication** stating whether ultrasound appearance contributes to the PI's routine clinical diagnosis of lipoedema, and confirming its exclusion from the study criterion set.

Residual limitation, which cannot be eliminated and will be stated in the publication: the PI's general diagnostic gestalt has been formed over a career that includes ultrasound exposure. Per-participant pre-imaging locking prevents contamination of individual labels; it does not undo the expert's accumulated experience. This is a limitation, not a fatal flaw, and honest disclosure is the appropriate response.

### 5.1.4 Compensating safeguards for a single adjudicator

A single rater means **inter-rater kappa cannot be computed**. Because label reliability bounds the meaning of any model performance figure, three substitutes are required:

**(a) Intra-rater reliability.** The PI re-classifies a random **20% subsample** from the recorded clinical documentation, **at least 3 months later**, blinded to the original classification. Intra-rater kappa is computed and reported. This measures the consistency of the criterion set in the hands of its user.

**(b) Independent external audit — strongly recommended.** An external clinician experienced in lipoedema, **independent of the study and blinded to the PI's calls and to all imaging**, independently classifies a random **20% subsample** from the recorded clinical documentation and photographs. Agreement with the PI is reported. This does not require the external clinician to examine every participant, making it practical, while providing the external check that a single-adjudicator design otherwise lacks. **Without this, reviewers will treat the labels as unverified.**

**(c) Structured, auditable documentation.** For every participant, each Appendix A criterion is recorded as present/absent/not assessable, with the classification derivable from the recorded criteria rather than resting on unrecorded impression. This makes the judgement reconstructible by a third party.

### 5.1.5 Declared limitation

The protocol states, and the publication will state, that **all labels derive from a single expert**, that the study therefore measures **concordance with one expert's clinical classification** rather than with a consensus or an independent gold standard, and that generalisation to other clinicians' diagnostic practice is unestablished. Multi-rater or multicentre labelling is identified as required future work.

### 5.1.6 Conflict of interest

The PI is both the sole adjudicator of the labels and an investigator with an interest in the study's success. This is declared to the IRB and in publication. The pre-imaging database lock (§5.1.1), the blinding of technicians (§6.6), the image-only export to the modelling pipeline (§7.1A), and the external audit sample (§5.1.4b) together constitute the structural mitigation.

---

# 6. Study Procedures

## 6.1 Visit schedule

Single study visit per participant, approximately **45–60 minutes**. A random 20% subsample is invited to a **second visit** within 2–6 weeks for test–retest reproducibility. Sub-study participants have tissue collected during their already-scheduled operation, requiring no additional visit.

| Activity | Duration |
|---|---|
| Consent, eligibility, demographics, medication and menstrual/hormonal history | 15 min |
| Supine rest (mandatory, see §6.2) | 15 min |
| Ultrasound acquisition, 5 regions | 25–30 min |
| Total | 55–60 min |

## 6.2 Participant preparation

Required to control physiological variation in tissue fluid:

- **Supine rest 15 minutes** before scanning. Orthostatic oedema is intrinsic to lipoedema and varies with time spent upright.
- **Scans conducted within a fixed time-of-day window** (08:00–11:00) to control diurnal fluid shift.
- **No compression garments for ≥ 12 hours** beforehand; adherence recorded.
- No vigorous exercise for 12 hours; no alcohol for 24 hours.
- Menstrual cycle day and hormonal status recorded.
- Room temperature maintained at `[22 ± 2 °C]`, recorded.

## 6.3 Imaging equipment

GE Vivid 6 and Vivid 7 consoles. **GE 12L-RS** linear array (5–13 MHz, 38–39 mm field of view) for **all** characterisation and texture acquisitions. A curvilinear probe is used **only** for deep abdominal thickness where the linear probe cannot penetrate, and a phased array only as a further fallback for the same purpose; neither contributes to any texture or envelope-statistic analysis. Full technical rationale is in the companion acquisition standard.

## 6.4 Acquisition standard — summary

All console settings are locked in named presets and photographed each session. Speckle reduction (SRI), spatial compounding (CrossXBeam), harmonics and edge enhancement are **switched off**, because speckle is the signal being measured. Gain is fixed numerically and never adjusted per participant; time-gain compensation sliders are set to centre detent. Dynamic range, grey map, depth, focus, frequency, persistence and acoustic output are fixed.

A **tissue-mimicking reference phantom** with known attenuation and backscatter is scanned at the start and end of every session, enabling session normalisation, cross-console harmonisation and daily quality assurance. Phantom parameter drift beyond a pre-set tolerance halts scanning until service.

Images are exported as **uncompressed DICOM**; lossy compression is specifically destructive to speckle texture.

## 6.5 Anatomical sites

| Site | Region | Path |
|---|---|---|
| S1 | Distal leg / ankle transition | Mid-calf → medial malleolus → dorsum of foot |
| S2 | Medial thigh | Knee → inguinal region |
| S3 | Distal third of thigh | Focused acquisitions |
| **S4a** | **Upper abdomen, midline sagittal** | **Umbilicus → xiphisternum — PRIMARY INTERNAL CONTROL** |
| S4b | Lower abdomen | Umbilicus → suprapubic (secondary) |
| S5 | Posterior arm | Elbow → shoulder |

**Why the upper abdomen is the control.** Lipoedema is a gynoid-pattern disorder; infraumbilical fat is gynoid-adjacent and more likely involved, while epigastric fat is android-pattern and the cleanest available unaffected reference in the same participant. It also avoids the dependent panniculus, uses two fixed bony landmarks that scale with body size, and is thin enough for the linear probe to resolve fully. Regions of interest lie superficial to the linea alba; preperitoneal and visceral fat are excluded by definition. Characterisation frames are acquired at suspended end-expiration.

## 6.6 Operators, separation of duties, and blinding

**Three trained sonographic technicians** perform all acquisitions, scanning **both lipoedema and control participants**, following the identical standardised protocol.

### 6.6.1 Separation of duties

| Role | Personnel | Access |
|---|---|---|
| Image acquisition | 3 technicians | Standardised protocol only. **Blinded to clinical classification.** |
| Clinical classification | **Single expert (PI)** | Clinical examination only, **locked before imaging**. Takes no part in acquisition, interpretation or analysis (§5.1). |
| Image analysis / modelling | Analysis team | **De-identified images only** — no reports, no clinical data (§7.4) |

**The technicians take no part in adjudication, classification, image interpretation or analysis.** This is a firm separation, not a preference. It removes the principal route by which a diagnosis could influence how an image is captured, or an image could influence how a diagnosis is made.

### 6.6.2 Operator as a study variable

Three operators is a **strength** for generalisability — a model cannot overfit to one person's scanning style — provided operator is handled explicitly rather than ignored:

- **Operator identity is recorded on every acquisition.**
- All data splits are **stratified by operator** in addition to diagnosis, variant, BMI band and console.
- A **leave-one-operator-out sensitivity analysis** is pre-specified: the model is retrained excluding each operator's data in turn and evaluated on it, testing whether performance depends on who held the probe.
- **Inter-operator reproducibility** is measured directly: in the 20% duplicate subsample, the repeat acquisition is performed by a *different* technician, yielding inter-operator ICCs alongside the intra-operator values.

### 6.6.3 Operator training and drift control

- All three technicians complete a **common training and certification** exercise before enrolment begins, scanning the phantom and a set of volunteers until measurements agree within pre-specified tolerance.
- **Periodic re-certification** against the phantom every `[3 months]`, with results logged. Operator drift over a multi-year study is a real and under-reported source of variance.
- Sweep speed, probe pressure technique and probe angulation are covered explicitly in training, as these remain operator-dependent despite protocol instruction.

### 6.6.4 Scheduling: interleaving is mandatory

**This is a critical anti-confounding requirement.** Lipoedema and control participants **must be interleaved** across operators, consoles, sessions, days and calendar periods.

If cases are scanned predominantly by one technician, on one console, or during one calendar period, and controls in another, then operator, console or session becomes **perfectly confounded with diagnosis**. A model would learn that artefact and report excellent, entirely spurious accuracy.

Concretely:
- Scanning is **not** organised as a case phase followed by a control phase
- Console assignment is **randomised** per participant
- Operator assignment is **randomised** or balanced across arms
- Recruitment logs record operator, console, date and time for every participant, and **balance across arms is monitored monthly**, with corrective allocation if imbalance emerges

## 6.7 Histological sub-study procedure

For consenting Arm A participants undergoing clinically indicated liposuction:

1. **Pre-operatively**, a defined site is scanned with the full protocol and marked on the skin.
2. **Intra-operatively**, tissue is collected from that marked site as part of the liposuction that is being performed anyway. **No additional incision, no additional anaesthesia, no additional operative time.**
3. Specimens are analysed by a pathologist blinded to ultrasound findings for adipocyte diameter distribution, septal fibrosis grade, inflammatory infiltrate and interstitial fluid.

---

# 7. Data Management

## 7.1 De-identification

DICOM files contain protected health information in header fields and sometimes burned into pixel data. Before any analysis:

- All DICOM headers are stripped of identifiers using a validated anonymisation tool, retaining only acquisition parameters required for analysis
- Any burned-in text is masked
- Each participant is assigned a **study ID**; the linking key is held separately in an encrypted file accessible only to the PI and study coordinator

## 7.1A What the machine-learning pipeline receives — images only

**Only de-identified images are exported to the analysis pipeline. No clinical reports, no clinical data, no free text.**

This is a deliberate design decision with real scientific force: it guarantees that the model is learning **image content** and cannot be quietly exploiting a clinical covariate or a phrase in a report. Any performance the model achieves is attributable to the ultrasound signal.

### What is exported

| Exported to the ML pipeline | Withheld from the ML pipeline |
|---|---|
| De-identified pixel data | Clinical reports of any kind |
| Acquisition parameters needed for calibration (frequency, depth, gain, dynamic range, focus, mm/pixel, phantom reference) | Age, BMI, weight, medication, symptoms, history |
| Study ID | Name, MRN, date of birth, any identifier |
| Site code (S1–S5) and operator/console codes, held for stratification | Diagnosis narrative or clinician reasoning |
| Class label, supplied in a **separate keyed file** | Anything not required to compute a feature |

### Burned-in annotation must be removed

DICOM images from clinical consoles routinely carry **burned-in text in the pixel data** — institution name, patient name, date, operator initials, exam description, preset name. Any of these can leak class information into an image-only pipeline.

- Every image is passed through **automated burned-in-text masking**, with the masked region fixed and identical for all images so masking itself does not encode class
- A **manual audit of a random 10% sample** verifies masking before analysis begins
- **The site/exam label baked in by the console is a specific hazard.** If, for example, the operator types a different exam description for cases than controls, that text is class information sitting in the pixel array. Exam descriptions are standardised across arms, and masked regardless

### Labels are supplied separately

Class labels are held in a separate file keyed by study ID, containing **only** study ID and class. Clinical variables required for the statistical analyses (thickness covariate for H2, variant stratification, histology for H3) are held by the statistical team and are **never joined to the image set that the model sees**.

## 7.2 Storage and retention

De-identified images and analysis data are stored on `[institutional secure server / encrypted institutional storage]`, access-controlled and audit-logged. No participant data is stored on personal devices, portable media or non-institutional cloud services. Data are retained for `[7 years / per institutional policy]` after publication, then destroyed per institutional procedure.

## 7.3 Data sharing

De-identified derived parameters and analysis code will be made available on publication in a public repository. **Image sharing** will be offered only where the consent form explicitly permits it and institutional policy allows, given that medical images carry re-identification considerations. Participants may consent to the study while declining image sharing (§10).

---

# 8. Statistical Analysis and Power

**All calculations below are reproducible and were computed for this protocol. They require review and sign-off by the study statistician before submission.**

## 8.1 Analysis sequence

Analyses proceed in a fixed, pre-specified order. Later steps are not performed if earlier ones fail.

**Step 1 — Reproducibility screening (gatekeeper).** Intraclass correlation coefficients are computed for every candidate parameter from the duplicate-acquisition and test–retest subsamples. **Parameters with ICC below 0.75 are discarded before any hypothesis is tested.** This reproducibility table is a deliverable in its own right and will be published irrespective of downstream results, as no such table exists for subcutaneous adipose tissue quantitative ultrasound.

**Step 2 — H1, primary endpoint.** Paired comparison of each surviving sparkle metric between the affected limb site and the participant's own upper abdominal fat (S4a), within Arm A. Paired *t*-test where distributional assumptions hold, otherwise Wilcoxon signed-rank. The identical paired contrast is computed in Arms B–E; the hypothesis requires the contrast to be present in Arm A and absent or substantially smaller in controls, formally tested as an arm × site interaction in a mixed-effects model with participant as random effect.

**Step 3 — H2.** Between-arm discrimination, with **subcutaneous thickness entered as a covariate** to demonstrate that any signature is not a proxy for thickness. Reported as AUC with 95% confidence intervals.

**Step 4 — H3.** Correlation of ultrasound parameters with histological variables (Pearson or Spearman as appropriate).

**Step 5 — H4.** Frozen model evaluated once on the independent test cohort, against thickness-alone and bright-spot-density-alone baselines.

## 8.2 Handling of clustering

Each participant contributes multiple regions of interest, multiple sites and bilateral limbs. **All analyses use mixed-effects models with participant as a random effect.** Treating regions of interest as independent observations would inflate the effective sample size several-fold and is explicitly prohibited by this protocol.

## 8.3 Multiplicity

Multiple sparkle metrics are evaluated. **A maximum of five co-primary metrics is pre-specified** (bright-spot density, Nakagami *m*, homodyned-K *k*, echo-free space fraction, high-percentile-to-median intensity ratio), with **Bonferroni correction to α = 0.01 two-sided** for the primary endpoint. All other parameters are exploratory, reported with false discovery rate control, and explicitly labelled as hypothesis-generating.

## 8.4 Power calculations

### H1 — primary endpoint (paired, within-subject)

Effect expressed as Cohen's *d_z*. Two-sided α, Bonferroni-corrected to 0.01 for five co-primary metrics.

| Effect *d_z* | 80% power (α = 0.05) | 90% power (α = 0.05) | **90% power (α = 0.01)** |
|---|---|---|---|
| 0.4 | 50 | 66 | 93 |
| **0.5** | 32 | 43 | **60** |
| 0.6 | 22 | 30 | 42 |
| 0.8 | 13 | 17 | 24 |
| 1.0 | 8 | 11 | 15 |

**Assumption and justification.** A phenomenon described as recognisable casually and at a glance implies a large effect, plausibly *d_z* > 0.8. Powering at *d_z* = 0.5 (moderate) is deliberately conservative and provides headroom should the effect prove smaller than clinical impression suggests. **Requirement: 60 Arm A participants** for 90% power at the corrected α. Non-parametric fallback inflates this by approximately 5%.

### H2 — between-arm discrimination

Hanley–McNeil, balanced groups. Sample size per arm for a given AUC and confidence-interval half-width:

| True AUC | ± 0.075 | ± 0.05 |
|---|---|---|
| 0.75 | 82 | 182 |
| **0.80** | **68** | 151 |
| 0.85 | 53 | 117 |
| 0.90 | 36 | 79 |

Power to reject AUC = 0.5 at 90% power, one-sided α = 0.05: 34 per arm at true AUC 0.70; 21 at 0.75; 14 at 0.80.

**Requirement: 68 per arm**, giving AUC estimated to ± 0.075 — precise enough to distinguish clinically useful from marginal discrimination, which the existing literature (51 per group, CI spanning roughly 0.64–0.84) cannot.

### H3 — histological correlation

Detecting a Pearson correlation at 80% power, two-sided α = 0.05: r = 0.4 requires 47 pairs; **r = 0.5 requires 30 pairs**; r = 0.6 requires 20 pairs.

**Requirement: 30 biopsy–scan pairs.**

### H4 — independent test cohort

Precision of the frozen-model AUC:

| True AUC | ± 0.075 | ± 0.10 |
|---|---|---|
| 0.80 | 68/class (136) | **39/class (78)** |
| 0.85 | 53/class (106) | 30/class (60) |

**Requirement: 78 participants** (39 per class), giving the headline AUC to ± 0.10.

### Recruitment roll-up

| Component | n | With 15% attrition |
|---|---|---|
| Development cohort, 5 arms × 68 | 340 | **391** |
| Independent test cohort | 78 | **90** |
| Histology sub-study (nested within Arm A) | 30 | 35 |
| **Total to recruit** | | **~481** |

The binding constraint is H2 at 68 per arm; this comfortably exceeds the 60 required for H1.

## 8.5 Machine learning methodology — data partitions and model weights

This section is deliberately prescriptive. The commonest reason clinical machine-learning results fail to replicate is not a poor algorithm; it is undisciplined handling of partitions and weights.

### 8.5.1 Definitions

**"Weights"** in this protocol means **the complete set of learned parameters required to turn a new image into a prediction**, not merely the coefficients of the classifier. Specifically, the frozen model artefact comprises **all** of the following:

| Component | Examples | Fitted on |
|---|---|---|
| **Preprocessing parameters** | log-compression inversion constants; phantom normalisation factors; resampling target resolution; ROI extraction rules | **Training set only** |
| **Feature scaling parameters** | per-feature mean and standard deviation, or min/max, used for standardisation | **Training set only** |
| **Feature selection** | which features are retained after ICC screening and after any embedded selection | **Training set only** |
| **Classifier parameters** | regression coefficients and intercept; tree structures and split values; neural network weights and biases | **Training set only** |
| **Hyperparameters** | regularisation strength, tree depth, learning rate, architecture | Selected on **tuning set** |
| **Aggregation rule** | how frame-level or ROI-level predictions combine into one participant-level prediction | **Training set only**, rule selected on tuning |
| **Decision threshold** | the probability cut-off defining a positive call | **Tuning set only — never the test set** |
| **Calibration mapping** | Platt scaling / isotonic parameters, if used | **Training set only**, assessed on tuning |

### 8.5.2 The leakage rule that is most often broken

> **Every parameter that is estimated from data — including means, standard deviations, normalisation constants and thresholds — must be computed on the TRAINING set alone and then applied unchanged to the tuning and test sets.**

Computing a feature scaler across the whole development cohort before splitting, or selecting features using all the data, leaks information from tuning into training and inflates apparent performance. This is subtle, extremely common, and invalidates results. In practice this means **the entire pipeline is fitted inside the cross-validation loop**, never before it.

### 8.5.3 Partition specification with numbers

Analysed development cohort ≈ 340 participants (68 per arm × 5 arms; 391 recruited to allow 15% attrition). Classification task: **lipoedema (Arm A) vs non-lipoedema (Arms B–E pooled)**.

| Partition | Arm A | Arms B–E | Total | Purpose |
|---|---|---|---|---|
| **Training** (70%) | 48 | 190 | **238** | Fit all parameters in §8.5.1 |
| **Tuning / validation** (30%) | 20 | 82 | **102** | Hyperparameters, model selection, threshold, iteration |
| **TEST (independent cohort)** | 39 | 39 | **78** | Single evaluation of frozen weights |

**Class imbalance in development (1:4) must be handled and reported.** Options pre-specified: class-weighted loss, or balanced resampling within the training folds only. Because the development cohort is imbalanced while the test cohort is balanced, **precision–recall AUC and calibration are reported alongside ROC-AUC**, and the prevalence of each partition is stated explicitly wherever a predictive value is quoted.

**Prevalence differs between development and test by design.** The decision threshold fixed on the tuning set is carried unchanged to the test set. **Post-hoc recalibration on the test set is prohibited** — it would convert the test set into a tuning set. Any miscalibration observed on test is *reported as a finding*, not corrected.

### 8.5.4 Splitting rules

1. **Participant-level splitting, always, at every stage.** A single participant contributes 6 sites, bilateral limbs, and many frames per cine sweep — plausibly several hundred images. Frames from one sweep are near-duplicates. Any image-level split places the same participant on both sides and produces spectacular, meaningless accuracy. **No participant appears in more than one partition, ever.**
2. **Stratification variables:** diagnosis, distribution variant, BMI band, **console**, **operator**.
3. **The split is generated once, from a recorded random seed, and frozen.** The participant-to-partition assignment is written to a file, hashed, and never regenerated. Re-drawing a split after seeing results is a form of tuning on the outcome.
4. **Model selection uses repeated stratified k-fold cross-validation *within the 238-participant training set***, with folds also split by participant. The 102-participant tuning set is reserved for final model comparison, threshold setting and the iteration loop — not consumed by routine hyperparameter search.

### 8.5.5 The iteration loop, and its limits

The permitted development cycle is:

1. Fit candidate pipeline on training set
2. Evaluate on tuning set
3. Human adjudication of performance; revise features, model class or hyperparameters
4. Return to step 1

**Governance of this loop:**

- A **maximum of `[10]` cycles is pre-specified**; the actual number executed is recorded and reported in the publication.
- Every cycle is logged with: date, cycle number, what was changed and why, tuning-set performance, and the operator making the change.
- **Tuning-set performance is never reported as the study result.** It appears in the publication only as "development performance", explicitly labelled optimistically biased.
- If the cycle limit is reached without acceptable tuning performance, the study reports that outcome. Extending the limit after seeing results is prohibited.

### 8.5.6 Weight freezing — the procedural gate

Before **any** test-cohort image is analysed:

1. The complete model artefact (all components in §8.5.1) is **serialised to a single file**, together with the exact preprocessing code and library versions.
2. The file is **cryptographically hashed (SHA-256)** and the hash recorded with a timestamp.
3. The hash is **deposited externally** — in the trial registry record, a timestamped repository commit, or with an independent third party — so the freeze date is independently verifiable.
4. The frozen artefact is **placed in the custody of a team member who is not performing the modelling**, ideally the statistician.
5. **A written declaration** is signed stating that the model is frozen and that no further modification will occur.

Test-set analysis begins only after all five steps are complete. **The hash reported in the publication must match the artefact used to produce the test result.**

### 8.5.7 Test-set discipline

- **The test cohort is analysed exactly once.**
- Test images are held by the custodian and released to the analysis pipeline only after freezing.
- **No modification of any kind** — not features, not thresholds, not calibration, not aggregation — is permitted after test-set exposure.
- If test performance is disappointing, that is the result. **Returning to development and re-testing on the same cohort is prohibited**; doing so converts it into a second tuning set and would require an entirely new cohort for an unbiased estimate. Any such subsequent work is reported explicitly as a **new development phase requiring fresh prospective validation**.
- The test cohort is recruited **later in time**, and where practical uses different operator–console combinations, so it tests transportability rather than a re-draw of identical conditions.

### 8.5.8 Confound-specific sensitivity analyses (pre-specified)

Run on the frozen model, reported alongside the primary result:

| Analysis | Question it answers |
|---|---|
| **Leave-one-console-out** | Has the model learned the machine? |
| **Leave-one-operator-out** | Has the model learned a technician's scanning style? |
| **Site-restricted models** (each of S1, S2, S3, S5 alone) | Is the signature present across territories, or driven by one site? |
| **Variant-stratified performance** | Does it hold in hip-confined disease, not only distally extensive disease? |
| **Thickness-matched subgroup** | Is the model a covert thickness detector? |
| **Internal-reference-normalised vs raw features** | How much of the performance survives per-participant normalisation to S4a? |

### 8.5.9 Model class, proportionate to sample size

- **Primary:** penalised logistic regression or gradient boosting over the interpretable parameters of §7.1 (companion document). With ~238 training participants and a modest feature count, this is the defensible choice.
- **Secondary:** deep models on calibrated, resolution-normalised image patches, with multiple-instance learning over frames, the participant being the labelled unit.
- A deep model is reported **only alongside** the interpretable model and the simple baselines. A complex model that cannot beat bright-spot density alone has not earned its complexity, and the protocol commits in advance to saying so.

### 8.5.10 Reproducibility artefacts published

- The frozen model file and its SHA-256 hash
- The participant-to-partition assignment (by study ID) and the random seed
- The full iteration log
- Preprocessing and analysis code, with pinned library versions
- The reproducibility (ICC) table

## 8.6 Pre-specified interpretation rules

- An AUC above 0.90 on first analysis **triggers a leakage audit** — most plausibly participant-level frame leakage or console confounding — before any positive interpretation.
- A model that fails to beat bright-spot density alone has not earned its complexity, and this will be reported plainly.
- If reproducibility screening (Step 1) eliminates the candidate parameters, the study reports that finding and stops. That is an informative result for the field.

## 8.7 Missing data

Where the deep fascial boundary cannot be resolved, thickness is recorded as **missing by pre-specified category**, not estimated. Missingness is reported by arm and site. Analyses use available-case methods with sensitivity analysis under multiple imputation where missingness exceeds 10%.

---

# 9. Risks and Absence of Harm to Participants

## 9.1 Overall risk determination

**The imaging protocol is minimal risk.** It involves diagnostic B-mode ultrasound at standard diagnostic power settings, applied to the skin surface of the limbs and abdomen. It is the same modality, the same equipment and the same energy exposure as routine clinical ultrasound performed millions of times daily worldwide.

## 9.2 Specific risk analysis

**No ionising radiation.** Ultrasound uses mechanical sound waves. There is no radiation exposure and no cumulative dose consideration.

**No contrast agent.** No intravenous access, no injection, no contrast medium. No risk of allergy, nephrotoxicity or extravasation.

**No known bioeffects at diagnostic levels.** Diagnostic ultrasound at the acoustic output levels used has no established harmful biological effect in the tissues scanned. Acoustic output is **fixed at standard diagnostic levels and recorded**, and the study operates under the ALARA principle. Thermal and mechanical indices remain within FDA/IEC limits for the scanning of non-fetal soft tissue throughout. Scanning is superficial and of short duration at any one location.

**No pregnancy risk pathway.** Pregnancy is an exclusion criterion for fluid-status reasons rather than safety, and no obstetric or fetal scanning is performed.

**Physical discomfort — minimal and transient.** Contact gel is applied to the skin; it is at room temperature and may feel cool. The protocol specifies **minimal transducer pressure** with a standoff or generous gel, both because fat is compressible (a scientific requirement) and because this minimises any pressure sensation. Participants with lipoedema commonly have tender tissue; the sonographer is instructed to use the lightest contact that produces an adequate image, and any participant may ask for a pause or for a site to be skipped at any time without explanation.

**Positional discomfort.** Participants lie supine for approximately 30 minutes plus a 15-minute rest. Position changes, cushions and breaks are available on request.

**Skin reaction.** Ultrasound gel rarely causes local irritation. Gel is removed at the end of the examination. Participants with known gel or preservative sensitivity are asked at consent, and hypoallergenic gel is used where indicated.

**Privacy and dignity.** Scanning requires exposure of the limbs and abdomen. Participants are gowned and draped, examined in a private room, and may request a chaperone. Given that many participants have longstanding distress about their body shape, staff are briefed to conduct examinations without comment on appearance.

**No withholding of care.** Participation does not alter, delay or substitute for any clinical care. No treatment is withheld, changed or offered as part of this study.

## 9.3 Risk of the histological sub-study

This is the only element beyond the imaging protocol, and it adds **no procedural risk**.

- Tissue is collected **during liposuction that is already scheduled on clinical grounds**, for reasons independent of this research.
- **No additional incision.** **No additional anaesthesia.** **No additional operative time** beyond the seconds required to retain a specimen from the marked site.
- The tissue collected would otherwise be **discarded as surgical waste**.
- The decision to undergo liposuction is made by the participant and treating surgeon on clinical grounds. **Declining the sub-study has no effect on surgical care, and enrolment in the sub-study does not influence whether surgery is offered or performed.** This separation is stated explicitly in the consent form.

## 9.4 Psychological and social risk

Some participants may find discussion of their diagnosis distressing, particularly given the frequency of prior dismissal by clinicians. Participants may decline any question, pause, or withdraw at any time. `[Local counselling/support pathway and patient support organisation details to be inserted.]`

## 9.5 Risk of loss of confidentiality — and mitigation

The principal residual risk in the study is confidentiality, not physical harm. Mitigations are described in §7: DICOM de-identification including burned-in text, separately held encrypted linking key, access-controlled institutional storage, and a separate consent option for image sharing.

## 9.6 Incidental findings

Scanning may reveal unexpected findings — for example a suspicious mass, deep venous thrombosis, hernia or significant lymphadenopathy.

**Policy.** Research scans are **not diagnostic examinations** and are not systematically reported. However, any finding the sonographer considers potentially clinically significant is escalated **the same day** to the study physician, who reviews it and, if warranted, informs the participant and their treating clinician and arranges appropriate clinical follow-up. This policy, including the limits of what the research scan can detect, is stated explicitly in the consent form so that participants do not mistake research participation for a health screen.

## 9.7 Benefits

**There is no direct medical benefit to individual participants.** Participants are told this plainly. Potential benefits are societal: if successful, this research may contribute to earlier and more objective identification of lipoedema for future patients. `[Reimbursement for travel and time, if offered: amount and basis.]`

## 9.8 Risk–benefit assessment

The imaging protocol presents no more than minimal risk, comparable to routine clinical ultrasound. The sub-study adds no procedural risk, using tissue that would otherwise be discarded. The principal risk is confidentiality, addressed by established de-identification and access-control measures. Set against the documented harm of diagnostic delay in a condition with no biomarker, **the risk–benefit balance strongly favours conducting the study**.

---

# 10. Informed Consent Document

> **Note to the IRB:** the following is the proposed participant-facing consent form. Institution-specific language, contact details, compensation, and injury-compensation provisions are marked `[...]` for completion. Target reading level is grade 8.

---

## CONSENT TO TAKE PART IN A RESEARCH STUDY

**Study title:** Using ultrasound and computer analysis to identify lipoedema
**Principal Investigator:** `[Name]` · **Telephone:** `[number]` · **Institution:** `[name]`

### An invitation

You are being invited to take part in a research study. Before you decide, it is important that you understand why the research is being done and what it would involve for you. Please take your time. Ask us anything you like. You may discuss it with family, friends or your own doctor.

**Taking part is entirely voluntary.** If you decide not to take part, or if you start and then change your mind, your medical care will not be affected in any way.

### Why is this study being done?

Lipoedema is a condition that causes fat to build up in the legs, hips and sometimes the arms. It can be painful and tender. It is often mistaken for ordinary weight gain, and many people wait years before anyone gives them the right diagnosis. There is currently no blood test or scan that can identify it reliably.

Doctors who see many patients with lipoedema have noticed that the fat often has a particular "sparkling" look on an ultrasound picture. Nobody has ever measured this properly.

We want to find out two things:
1. Can this sparkling appearance be measured accurately using ultrasound?
2. Can a computer program learn to recognise it?

If it works, it might one day help people get a correct diagnosis sooner.

### Why have I been invited?

You are being invited because you `[have been diagnosed with lipoedema / have lymphoedema / have cellulite / are a volunteer without these conditions]`. We need to compare ultrasound pictures from people with different conditions to find out what is specific to lipoedema.

We are looking for about **481 people** in total.

### What will happen if I take part?

You would come for **one visit lasting about one hour**.

**Before your visit, we would ask you to:**
- Not wear compression garments for 12 hours beforehand
- Avoid hard exercise for 12 hours and alcohol for 24 hours
- Come in the morning, between 8am and 11am

**During your visit:**
1. We will ask about your medical history and the medicines you take, and measure your height and weight.
2. A doctor will examine you. This is a normal physical examination. This happens **before** your scan.
3. You will rest lying down for 15 minutes.
4. We will do an **ultrasound scan** of your lower legs, thighs, tummy and the back of your arms. This takes about 25–30 minutes.

**About the ultrasound scan:** This is the same kind of scan used to look at babies in pregnancy and at blood vessels. A small amount of cool gel is put on your skin and a smooth handheld probe is moved gently over it. **There are no X-rays and no injections.** It does not hurt. We press only very lightly — this matters both for your comfort and for the quality of our measurements. If any area is tender, tell us and we will be gentle, pause, or skip it altogether.

You will need to uncover your legs, tummy and arms. You will be given a gown and covered with sheets, in a private room. You may ask for a chaperone.

**Some people will be asked to come back once more**, 2 to 6 weeks later, for the same scan. This helps us check that our measurements are consistent. This is optional.

### The tissue part of the study (only for some people)

**This part only applies if you are already having liposuction surgery for your lipoedema, planned by your surgeon for your own medical reasons.**

If so, we would ask permission to keep a small piece of the fat that is removed during that operation, and to look at it under a microscope. This helps us understand what causes the sparkling appearance.

Please note:
- **This does not change your operation in any way.** No extra cut, no extra anaesthetic, no extra time.
- The tissue we would keep is tissue that would otherwise be **thrown away**.
- **Your operation does not depend on this study.** Saying no makes no difference to your surgery or your care.

You can take part in the main study and say no to this part.

### What are the possible risks or disadvantages?

The scan itself is very safe. Ultrasound has been used in medicine for decades and is not known to cause harm at the settings we use.

The main things to be aware of:
- **The gel may feel cold.**
- **Lying still for about half an hour** may be uncomfortable. You can move, take a break, or ask for a cushion at any time.
- **Your skin will be uncovered** during the scan. We know this can feel uncomfortable, especially if you have had difficult experiences with doctors about your body. We will keep you covered as much as possible and treat you with respect.
- Rarely, ultrasound gel can irritate the skin. Tell us if you have had a reaction to gel before.
- Some people find talking about their diagnosis upsetting. You do not have to answer any question.

### Will the scan tell me if something is wrong?

**This is a research scan, not a medical check-up.** It is not designed to find other health problems, and it should not be relied on as a health check.

However, if we happen to see something that looks like it might matter for your health, we will tell you and your doctor, and help you arrange proper follow-up.

### Will I benefit from taking part?

**No — we do not expect this study to help you personally.** We are being honest about that. What we learn may help other people with lipoedema get diagnosed sooner in the future.

`[Reimbursement details, if any, to be inserted here.]`

### Do I have to take part?

No. Taking part is completely voluntary.

**You may stop at any time, for any reason, without giving one.** Your medical care, and your relationship with your doctors, will not be affected in any way.

If you withdraw, you can ask us to delete the information collected about you. We will do so unless it has already been combined into analysis results that cannot be separated out — we will explain clearly if that is the case.

### How will my information be kept private?

- Your name and other identifying details are **removed** from all scan pictures and data.
- You are given a **study number** instead. The list linking your number to your name is kept separately, encrypted, and only the study leader and coordinator can see it.
- Data is stored on secure `[institution]` computers, not on personal devices or laptops.
- When we publish results, **no individual can be identified.**
- Data will be kept for `[X]` years and then destroyed.

### Will my scan pictures be shared with other researchers?

Sharing anonymous scan pictures helps other scientists check and build on our work. **You can take part in this study without agreeing to this.** Please indicate your preference below.

### Who has reviewed this study?

This study has been reviewed and approved by `[IRB / Research Ethics Committee name and reference number]`.

### Who do I contact?

- **Questions about the study:** `[PI name, telephone, email]`
- **Questions about your rights as a research participant, or a concern or complaint:** `[IRB office contact — independent of the research team]`
- **In case of research-related injury:** `[institutional provision]`

---

### CONSENT

Please initial each box:

| | Statement |
|---|---|
| ☐ | I have read and understood the information sheet dated `[date]`, version `[x]`. I have had the chance to ask questions and they have been answered. |
| ☐ | I understand that taking part is **voluntary** and that I may stop at any time, without giving a reason, **without my medical care being affected**. |
| ☐ | I understand this is a **research scan and not a medical check-up**, and that it is not designed to find other health problems. |
| ☐ | I agree that if something possibly important for my health is seen, I and my doctor may be told. |
| ☐ | I understand that my anonymised data may be looked at by regulatory authorities and by people responsible for checking the research is done properly. |
| ☐ | **I agree to take part in this study.** |

**Optional — please tick to agree, or leave blank to decline. Either choice is fine.**

| | Statement |
|---|---|
| ☐ | I agree to be invited back for **one repeat scan** 2–6 weeks later. |
| ☐ | I agree that my **anonymised scan pictures** may be shared with other researchers. |
| ☐ | **Only if you are already having liposuction:** I agree that a small piece of the fat removed during my planned operation may be kept and examined for this research. I understand this **does not change my operation** and that my surgery does not depend on it. |
| ☐ | I agree to be contacted about **future related research**. This does not commit me to anything. |

<br>

| | | |
|---|---|---|
| Participant name | Signature | Date |
| Person taking consent | Signature | Date |

*One copy for the participant, one for the研究 file, one for the medical record.*

---

# 11. Ethical Considerations

## 11.1 Governing principles

The study is conducted per the **Declaration of Helsinki**, ICH Good Clinical Practice, and `[45 CFR 46 / local governing regulation]`. No participant is enrolled before written informed consent and IRB approval.

## 11.2 Justice and participant selection

Participants are selected on scientific grounds. Recruitment is expected to be predominantly female because lipoedema is predominantly a disease of women; this reflects disease epidemiology, not exclusion. `[Recruitment materials should be reviewed to ensure access across socioeconomic and ethnic groups within the catchment population, and interpretation provided where needed.]`

## 11.3 Avoiding coercion

Participants may be patients of the investigators, creating potential for perceived pressure. Safeguards:

- Consent is sought by a team member **not directly responsible for the participant's clinical care** wherever practical
- The consent discussion states explicitly and in writing that **declining will not affect care**
- Adequate time is given; consent is not sought immediately before a clinical procedure
- **For the sub-study specifically**, the independence of the surgical decision from the research decision is stated in both the protocol and the consent form, and consent for tissue is sought separately from consent for surgery

## 11.4 Consent capacity and withdrawal

Only adults able to give informed consent are enrolled. Participants may withdraw at any time; data collected up to withdrawal is deleted on request unless already irreversibly incorporated into aggregate analysis, which is explained at consent.

## 11.5 Use of human tissue

Tissue is collected only from clinically indicated procedures, is surgical waste, and is used only for the purposes described. Storage, retention and disposal follow `[institutional human tissue policy / applicable Human Tissue Act provisions]`. Tissue is not used for genetic analysis, not commercialised, and not transferred to third parties without further specific approval.

## 11.6 Data protection

Processing complies with `[GDPR / HIPAA / local data protection law]`. The lawful basis is `[consent / public task — to be specified]`. A data protection impact assessment `[has been / will be]` completed. Participants have the rights of access, rectification and erasure as described at consent.

## 11.7 Conflicts of interest

`[Declare all: equipment manufacturer relationships, clinic ownership, any commercial interest in a diagnostic test for lipoedema, patent intentions.]` Any intention to seek intellectual property protection over the resulting algorithm **must be declared here and disclosed to participants at consent**, as this materially affects the terms on which people contribute their data.

## 11.8 Publication and reporting integrity

- The study will be **registered on a public trials registry before recruitment begins**.
- The protocol, including the statistical analysis plan and the frozen-model hash, is deposited before the test cohort is analysed.
- Results will be published **irrespective of outcome**, including a null result.
- Reporting follows **STARD** for diagnostic accuracy, **TRIPOD+AI** for the model, and the **CLAIM** checklist for artificial intelligence in medical imaging.
- Any dissemination will state operating characteristics alongside any headline metric. Lipoedema patients are an actively marketed-to population, and overstated diagnostic claims are readily repurposed as clinic advertising. The investigators accept a specific responsibility not to create that material.

---

# 12. Expected Outcomes

## 12.1 Primary anticipated result

The sparkling appearance is expected to be quantifiable, with sparkle metrics — most likely bright-spot density and Nakagami *m* — significantly elevated in lipoedema-affected sites relative to the participant's own upper abdominal fat, and this within-subject contrast substantially larger in Arm A than in control arms.

## 12.2 Realistic performance expectations

**A modest, well-calibrated, reproducible result is the success case.** The existing single-site morphometric benchmark is AUC 0.74. A plausible successful outcome is an AUC in the high 0.70s to mid 0.80s on the independent test cohort. An AUC above 0.90 would trigger a leakage audit before any positive interpretation.

## 12.3 Deliverables regardless of outcome

1. **A published reproducibility table** for quantitative ultrasound parameters of subcutaneous adipose tissue — which does not currently exist for this tissue, and is reusable by any group working on subcutaneous ultrasound.
2. **A standardised, fully specified acquisition protocol** for research ultrasound of skin and subcutaneous fat, transferable to other conditions.
3. **Histological correlation data** for ultrasound appearance in lipoedema, currently absent.

## 12.4 Possible negative outcomes, and their value

- **Parameters prove insufficiently reproducible.** This would indicate that B-mode texture of subcutaneous fat is not a viable biomarker without radiofrequency-based quantitative ultrasound. Publishable and useful.
- **Sparkle proves non-specific** — present also in cellulite or lymphoedema. This defines the limits of the sign and prevents others pursuing it naively. Precisely why Arms D and E are included.
- **Upper abdominal fat proves abnormal** in lipoedema, invalidating the internal control. This would itself be a novel finding about disease distribution.

All negative results will be published.

---

# 13. Significance of the Research

## 13.1 If the study succeeds

**For patients.** The central harm in lipoedema is not the fat; it is the years of being told the problem is self-inflicted. An objective, quantitative tissue marker that does not depend on the rare availability of an expert examiner would shorten diagnostic delay and change the terms of the clinical conversation. A patient with a measurable tissue abnormality is in a different position from one with a contested clinical impression.

**For clinical practice.** Diagnosis currently rests on expert pattern recognition concentrated in a small number of specialist centres. A standardised protocol running on **general vascular ultrasound equipment already present in most departments** could extend objective assessment far beyond those centres — a deliberate design choice of this study.

**For the science of the disease.** Linking a specific acoustic signature to specific histological features would provide a non-invasive window onto adipose tissue remodelling in lipoedema, with potential application to staging, to monitoring conservative and surgical treatment, and as an endpoint in future therapeutic trials.

**For methodology.** The acquisition standard and reproducibility data are transferable to any research requiring quantitative ultrasound of subcutaneous tissue — cellulite, lymphoedema, scleroderma, diabetic skin disease, wound healing. This broadens the contribution well beyond one condition.

## 13.2 The narrative this study would establish

Clinicians recognise a characteristic sparkling appearance of lipoedematous fat. This study defines that appearance physically, quantifies it under a fully standardised and reproducible acquisition protocol, demonstrates a histological substrate for it, shows it discriminates independently of tissue thickness, and validates a machine-learning model prospectively on subjects never used in development.

## 13.3 What the study will not claim

Even if entirely successful, this study will support **adjunctive concordance with a single expert's clinical assessment**, in the population studied, on the equipment studied. It will not support the claim that ultrasound artificial intelligence diagnoses lipoedema. A single-centre study with internal validation permits only cautious language; multicentre prospective evaluation would be required before stronger claims are appropriate. This limitation is stated in the protocol so that it appears in the publication rather than being extracted by a reviewer.

---

# 13A. Declared Limitations

Stated here so they appear in the protocol and the publication rather than being extracted by a reviewer.

1. **Single-expert reference standard.** All labels derive from one clinician. The study measures concordance with one expert's clinical classification, not with a consensus or an independent gold standard. Mitigated by pre-imaging database locking, intra-rater kappa, and an independent external audit of a 20% subsample (§5.1).
2. **No histological gold standard for the disease itself.** Lipoedema has no diagnostic biopsy. The histology sub-study correlates ultrasound with tissue features; it does not establish a gold-standard diagnosis.
3. **Single centre, two consoles, three operators.** Generalisation to other equipment, settings and operators is unestablished. Mitigated by leave-one-console-out and leave-one-operator-out analyses, but not eliminated.
4. **Dermal characterisation is out of reach.** The available probe ceiling (13 MHz) does not resolve dermal texture. The study is scoped to subcutaneous fat.
5. **Radiofrequency data is likely unavailable** on this platform, restricting the study to phantom-calibrated B-mode rather than full spectral quantitative ultrasound.
6. **The internal control assumes upper abdominal sparing**, which is a clinical generalisation. The Phase 1 pilot tests this; if it fails, the primary endpoint requires redesign.
7. **Cross-sectional design.** No inference about progression, staging or treatment response is supported.

---

# 14. Study Timeline

| Phase | Duration | Activity |
|---|---|---|
| 0 | 3 months | IRB approval, registry registration, phantom procurement, preset creation and validation, sonographer training |
| 1 | 3 months | **Pilot (n ≈ 20–30)**: verify deep fascia visualisation in the thickest participants; verify upper abdominal fat is not itself abnormal; estimate effect size and ICCs; finalise statistical analysis plan |
| 2 | 12–18 months | Development cohort recruitment and imaging (n ≈ 391) |
| 3 | 3 months | Reproducibility analysis, feature screening, model development, **weight freeze and hash** |
| 4 | 6–9 months | Independent test cohort recruitment and single-shot evaluation (n ≈ 90) |
| 5 | 3 months | Histology analysis, synthesis, manuscript preparation |

**The Phase 1 pilot is a gate, not a formality.** If upper abdominal fat proves abnormal in lipoedema, the primary endpoint requires redesign before the main study proceeds.

---

# 15. Appendices

- **Appendix A** — Clinical diagnostic criterion set for reference-standard classification `[to be finalised]`
- **Appendix B** — Console preset specification and settings photographs `[to be attached]`
- **Appendix C** — Phantom QA log template and tolerance thresholds `[numeric tolerances to be set during Phase 0]`
- **Appendix D** — Case report form
- **Appendix E** — Statistical analysis plan (full), for statistician sign-off
- **Appendix F** — Data management and de-identification standard operating procedure
- **Appendix G** — Technical acquisition standard — see companion document [lipoedema-ultrasound-ml-protocol.md](lipoedema-ultrasound-ml-protocol.md)

---

## References

Amato, A. C. M., Saucedo, D. Z., Santos, K. da S., & Benitti, D. A. (2021). Ultrasound criteria for lipedema diagnosis. *Phlebology*. https://doi.org/10.1177/02683555211002340

Barros, F. S., Tavares, I. R., & Frasson, P. H. L. (2026). Ultrasound criteria for upper extremity lipedema diagnosis. *Phlebology*. https://doi.org/10.1177/02683555261475099

Iker, E., Mayfield, C. K., & Gould, D. J. (2019). Characterizing lower extremity lymphedema and lipedema with cutaneous ultrasonography and an objective computer-assisted measurement of dermal echogenicity. *Lymphatic Research and Biology, 17*(5), 525–530. https://doi.org/10.1089/lrb.2017.0090

Intagliata, D., Priolo, M., & Molinari, P. (2025). High-frequency ultrasound imaging for stage III cellulite: A three-subtype structural classification from an observational cohort study. *Dermatology and Therapy, 15*(10), 2865–2878. https://doi.org/10.1007/s13555-025-01504-0

Nowak, S., Henkel, A., & Theis, M. (2022). Deep learning for standardized, MRI-based quantification of subcutaneous and subfascial tissue volume for patients with lipedema and lymphedema. *European Radiology, 33*(2), 884–892. https://doi.org/10.1007/s00330-022-09047-0

Ozturk, G., Kahraman, A. N., & Akpinar, P. (2025). Relationship of the tissue stiffness measured using shear wave elastography with the pain threshold and quality of life of patients with lipedema. *Phlebology, 40*(8), 627–637. https://doi.org/10.1177/02683555251357094

Piyaman, P., Sitthinamsuwan, P., & Apichonbancha, S. (2025). Assessing subcutaneous changes in lymphedema by subcutaneous tissue ultrasonography and pathological association. *Scientific Reports, 15*(1). https://doi.org/10.1038/s41598-025-00485-6

Quantitative ultrasound imaging of soft biological tissues: a primer for radiologists and medical physicists. (2021). *Insights into Imaging*. https://doi.org/10.1186/s13244-021-01071-w

Yaman, A., & Mansız-Kaplan, B. (2026). Assessment of the elasticity of lipedematous tissue and the examination of the relationship between pain and fibrosis in lipedema. *International Journal of Obesity, 50*(5), 1136–1141. https://doi.org/10.1038/s41366-026-02049-8

*Full evidence appraisal with search boundary and tier classification: [lipoedema-ultrasound-ml.md](lipoedema-ultrasound-ml.md)*
