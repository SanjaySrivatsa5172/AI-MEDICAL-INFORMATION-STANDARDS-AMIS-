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
| Design | Prospective, cross-sectional, two-arm case–control **discovery / proof-of-concept** study, with a nested within-subject paired comparison and an embedded histological correlation sub-study. Independent validation is a planned subsequent phase, not part of this protocol |
| Population | Adult women with clinically diagnosed lipoedema and BMI-matched controls without lipoedema |
| Sample size | **100 participants (50 lipoedema, 50 BMI-matched controls), with pre-planned blinded sample size re-estimation at n = 60 and a pre-specified maximum of 200 (§8.4A).** Analysis unit is the **participant**, not the image. Histology sub-study nested within the lipoedema arm |
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

**Two arms, 100 participants total.**

| Arm | Description | n |
|---|---|---|
| **A** | **Lipoedema** — clinically diagnosed, stratified by distribution variant | **50** |
| **B** | **Non-lipoedema controls**, individually **BMI-matched** to Arm A participants (± 2 kg/m²) | **50** |

### 3.1.1 Why BMI matching is non-negotiable

If controls are not BMI-matched, any model will separate the groups on **adiposity** and the study will have demonstrated nothing about lipoedema. Matching is performed **individually**, participant to participant, and match quality is reported.

### 3.1.2 Cellulite is handled as a covariate, not a separate arm

Cellulite is common in BMI-matched women and affects the same body regions; a dedicated cellulite arm is not affordable at this sample size, and would in any case be partly redundant because many Arm B participants will have cellulite.

**Cellulite is therefore graded in every participant in both arms** (Nürnberger–Müller scale) and:

- entered as a **covariate** in the between-arm analysis
- used in a pre-specified **sensitivity analysis restricted to cellulite-matched pairs**
- reported by arm, so that any imbalance is visible

This is more statistically efficient than a separate arm and directly answers the reviewer objection that the signature is merely cellulite.

### 3.1.3 What this sample size defers

Dedicated **lymphoedema** and **obesity-without-lipoedema** comparison arms are **not included** at n=100 and are identified as **planned future work**. Their absence is a declared limitation (§14): this study establishes whether a signature exists against BMI-matched controls; it does not establish specificity against lymphoedema.

Where a small convenience sample of lymphoedema participants is available, they may be imaged as an **exploratory descriptive addition**, reported separately and explicitly under-powered, with no formal hypothesis attached.

## 3.2 Distribution-variant stratification

Lipoedema occurs in variants confined to the hips, extending from hips to knee, and extending from hips to ankle, with upper-limb involvement in a substantial minority. Arm A recruitment is stratified across these variants, and the primary hypothesis is examined within variant strata. **At n = 50, individual variant strata are small and these analyses are exploratory**, powered to describe rather than to confirm. A signature apparently present only in distally extensive disease would be a flag for the validation phase, not a conclusion.

---

# 4. Participants

## 4.1 Inclusion criteria — all arms

- Age 18–70 years inclusive
- Able to give written informed consent
- Able to lie supine for approximately 30 minutes

## 4.2 Arm-specific inclusion criteria

**Arm A (lipoedema), n = 50:** Clinical diagnosis of lipoedema established by the PI per §5.1, with recorded stage (I–III) and distribution variant.

**Arm B (BMI-matched control), n = 50:** No clinical features of lipoedema or lymphoedema; **individually BMI-matched** to a specific Arm A participant within ± 2 kg/m², and additionally matched on **age band (± 10 years)** and **sex**. Cellulite is permitted and graded, not excluded (§3.1.2).

**Matching procedure.** Each Arm B participant is recruited against a named Arm A participant. Matching quality — mean and maximum absolute BMI difference, age difference — is reported in the participant flow table.

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

Lipoedema affects women almost exclusively. Recruitment is therefore expected to be overwhelmingly or entirely female in both arms. This reflects the disease epidemiology and is not an exclusion. Men meeting criteria will be enrolled if identified and analysed descriptively. 

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

### 5.1.4 Independent photographic adjudication by a second clinician

A single adjudicator means inter-rater kappa cannot be computed from the primary examination. This is addressed by an **independent second clinician who classifies every participant from standardised clinical photographs**, blinded to the PI's classification and to all ultrasound.

This is a stronger safeguard than auditing the PI's own written documentation, because the second clinician assesses **primary visual data** rather than re-reading the first adjudicator's reasoning.

**Procedure**

1. Standardised photographs are taken of every participant at the study visit (§6.5A), before or independently of imaging.
2. A second clinician experienced in lipoedema, **independent of the study team's imaging and analysis work**, classifies each participant as lipoedema or non-lipoedema from the photographs alone.
3. The second clinician is blinded to: the PI's classification, all ultrasound data and images, and the participant's arm allocation.
4. **Agreement between the two adjudicators is a reported study outcome**, not an internal check.

**Statistics of agreement.** Because the development cohort is imbalanced (approximately 1:4), and kappa is prevalence-sensitive, the following are reported together: **Cohen's kappa**, **Gwet's AC1**, **prevalence-adjusted bias-adjusted kappa (PABAK)**, and **raw percentage agreement**, each with confidence intervals. Reporting AC1 alongside kappa follows the precedent set in the comparable cellulite phenotyping literature.

**Pre-specified interpretation and action.**

| Agreement | Interpretation | Pre-specified action |
|---|---|---|
| AC1 ≥ 0.80 | Strong | Proceed; labels well supported |
| AC1 0.60–0.79 | Moderate | Proceed, with the **concordant-subset sensitivity analysis** (below) elevated to a co-primary report |
| AC1 < 0.60 | Weak | **Model performance figures must be interpreted as bounded by label uncertainty.** The publication leads with this limitation. Additional adjudicators are sought before any diagnostic claim |

**Concordant-subset sensitivity analysis (pre-specified).** The model is additionally trained and evaluated on the subset of participants where **both adjudicators agree**. This is the highest-label-confidence subset. Performance in the concordant subset versus the full cohort quantifies how much label noise is costing the model — a genuinely informative analysis that few diagnostic-AI studies perform.

### 5.1.4A An important interpretive caveat about photograph-based agreement

**Photographic classification is a harder task than in-person examination, and disagreement will partly reflect that rather than unreliability of either clinician.**

Lipoedema assessment normally uses **palpation** — tissue texture, tenderness on pressure, the character of the fat, Stemmer sign. None of this is available from a photograph. The second clinician is therefore working from a **strictly reduced information set**.

Consequences that must be stated in the publication:

- Agreement between the two adjudicators is a **conservative lower bound** on the reliability of the PI's classification. It confounds inter-rater disagreement with the information difference between examination and photograph.
- A moderate agreement statistic does **not** by itself establish that the PI's labels are unreliable.
- Conversely, **high** agreement despite the reduced information set would be strong evidence that the classification is robust and largely visually determined.
- To make this interpretable, the second clinician records **confidence (high / moderate / low / cannot assess)** for each case, and agreement is reported both overall and restricted to high-confidence calls.

### 5.1.4B Intra-rater reliability

Additionally, the PI re-classifies a random **20% subsample** from the recorded clinical documentation at least **3 months** later, blinded to the original classification. Intra-rater kappa is reported. This measures the consistency of the criterion set in the hands of its user, independent of the photographic comparison.

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

## 7.1B Computing environment — local, air-gapped processing

All image processing, feature extraction and model training are performed **locally on a dedicated NVIDIA DGX Spark workstation held within the institution**. `[Exact model, unified memory capacity and storage to be recorded.]`

### 7.1B.1 No internet egress

**No image, derived feature, or participant datum leaves the institutional environment at any point.**

- The analysis workstation operates **without internet connectivity** for study processing; network isolation is enforced `[by air-gap / by firewall rule restricting all outbound traffic — specify]`
- **No cloud computing, no third-party processing, no external application programming interfaces.** This includes an explicit prohibition on submitting any study image or derived data to any external artificial-intelligence, machine-learning or large-language-model service, whether commercial or academic
- Software dependencies are obtained and installed during a controlled provisioning step, with library versions pinned and recorded; the machine is then isolated for study processing
- **Model training occurs entirely on local hardware.** No federated, hosted or remote training is used

This eliminates the largest category of data-protection risk in imaging research — transmission to and storage on third-party infrastructure — and is a material factor in the risk assessment at §9.5.

### 7.1B.2 Pseudonymisation workflow

1. Images are exported from the ultrasound console.
2. **De-identification is performed first**: DICOM headers stripped of identifiers, burned-in pixel text masked (§7.1A).
3. Each participant is then assigned a **unique study label identifier**, which is the only identifier present in the analysis dataset.
4. The **linking key** mapping study identifier to participant identity is held **separately**, encrypted, on institutional storage distinct from the analysis workstation, accessible only to the PI and study coordinator.
5. **The analysis workstation never holds the linking key.** A compromise of the analysis machine therefore does not permit re-identification.

### 7.1B.3 Physical and logical security

- The workstation is located in `[secure, access-controlled room]`
- Full-disk encryption at rest; unique named user accounts, no shared credentials; multi-factor authentication where supported
- Access limited to named analysis personnel listed in the protocol; access log maintained
- **Backups** are held on encrypted institutional storage within the same security boundary — never on portable media, personal devices or consumer cloud services
- On study completion, storage is **securely sanitised** per institutional policy, with a certificate of destruction retained

### 7.1B.4 A caution: compute is not the limiting factor

Dedicated GPU hardware makes deep learning technically straightforward, and that creates a temptation the protocol explicitly resists.

**The binding constraint on model complexity is sample size, not compute.** With approximately 238 training participants, penalised regression or gradient boosting over interpretable parameters remains the *primary* model (§8.5.9). A high-capacity convolutional network trained on a few hundred participants will fit confounders — console, operator, session — more readily than disease, and the availability of hardware to train it is not an argument for doing so.

Local compute does confer three genuine advantages, and these are the ones to exploit:
- **Uncompressed DICOM and full cine sweeps can be retained and processed** without upload or storage-cost constraints, preserving the speckle information that lossy compression destroys
- **Radiofrequency or IQ data can be handled** at volume if a research export is obtained, which is otherwise impractical
- **The full pre-specified sensitivity analysis programme** (§8.5.8) — leave-one-console-out, leave-one-operator-out, site-restricted, variant-stratified, thickness-matched — can be run exhaustively rather than sampled

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

## 8.4 Power and precision at n = 50 + 50

**The honest framing: this sample is well powered to establish whether a signal exists, and imprecise about how strong it is.** That is the correct trade-off for a discovery study, and it is stated as such rather than disguised.

### H1 — primary endpoint (paired, within-subject, n = 50 lipoedema)

Smallest detectable paired effect (Cohen's *d_z*):

| α | 80% power | 90% power |
|---|---|---|
| 0.05 | *d_z* = 0.40 | *d_z* = 0.46 |
| **0.01** (Bonferroni, 5 co-primary metrics) | *d_z* = 0.48 | **_d_z_ = 0.55** |

**Verdict: comfortably powered.** A phenomenon described as recognisable casually and at a glance implies *d_z* well above 0.8. Detecting *d_z* = 0.55 at 90% power under a corrected α leaves substantial margin, and would still detect an effect roughly half the size clinical impression suggests.

### H2 — between-arm discrimination (50 vs 50)

**Power to detect that discrimination exists** (reject AUC = 0.5, one-sided α = 0.05):

| True AUC | Power |
|---|---|
| 0.65 | 84% |
| 0.70 | 98% |
| 0.75 | 100% |
| 0.80 | 100% |

**Precision of the AUC estimate** (Hanley–McNeil, 50 vs 50):

| True AUC | 95% CI | Half-width |
|---|---|---|
| 0.70 | 0.60 – 0.80 | ± 0.102 |
| 0.75 | 0.65 – 0.85 | ± 0.096 |
| 0.80 | 0.71 – 0.89 | ± 0.087 |
| 0.85 | 0.77 – 0.93 | ± 0.077 |

**Interpretation, stated in advance.** The study can answer *"is there a detectable signature?"* with high confidence. It **cannot** answer *"is the AUC 0.78 or 0.86?"* — the interval is roughly ± 0.09 wide. Any published AUC will be reported with its confidence interval and described as an **imprecise first estimate requiring confirmation**, not as an established operating characteristic. Estimating an AUC of 0.80 to ± 0.05 would require approximately 151 per arm and is deferred to the validation phase.

### H3 — histological correlation

30 biopsy–scan pairs detect r = 0.5 at 80% power (α = 0.05, two-sided); 47 pairs detect r = 0.4. **Target: 30 pairs nested within the 50 lipoedema participants.** If fewer are obtainable, the analysis is reported as exploratory with its achieved precision stated.

### Recruitment

| Component | n | With 15% attrition |
|---|---|---|
| Arm A (lipoedema) | 50 | 58 |
| Arm B (BMI-matched controls) | 50 | 58 |
| **Total** | **100** | **~116 to recruit** |
| Histology sub-study (nested in Arm A) | 30 | 35 |

## 8.4A Adaptive sample size: pre-planned expansion from 100

The investigator's intention to increase recruitment if the effect proves smaller than anticipated is **methodologically sound and recommended** — provided it is pre-specified here rather than decided later. Formalising it now is what separates a legitimate adaptive design from data-dredging.

### 8.4A.1 The trap being avoided

**Informally looking at the group difference, finding it non-significant, recruiting more, and looking again inflates the false-positive rate severely.** Testing repeatedly at a nominal α = 0.05:

| Number of looks | True Type I error |
|---|---|
| 1 | 0.050 |
| 2 | 0.083 |
| 3 | 0.107 |
| 5 | 0.142 |
| 10 | 0.193 |

With unbounded looking, the false-positive rate approaches certainty. **"Recruit until significant" is not an acceptable design and would be identified by any competent reviewer.** The remedy is not to avoid expanding — it is to pre-specify how.

### 8.4A.2 Primary mechanism: blinded sample size re-estimation (recommended)

**Blinded sample size re-estimation carries no Type I error penalty and requires no α adjustment**, because the group difference is never examined.

**Procedure.** At **n = 60 (30 per arm)**, the study statistician computes the **pooled variance** of each co-primary sparkle metric **without unblinding to arm**, and re-estimates the required sample size using that observed variance and the originally specified target effect size. The PI and analysis team are not informed of any group difference, because none is computed.

This is the right mechanism here because **the dominant uncertainty is the variance of novel metrics** — no published data exists on the standard deviation of Nakagami *m* or bright-spot density in subcutaneous fat. It is uncertainty about the measurement, not about the disease.

**Illustrative re-estimated requirements** (90% power, Bonferroni α = 0.01):

| If true *d_z* is | Required lipoedema n | Total |
|---|---|---|
| 0.80 | 24 | 48 |
| 0.65 | 36 | 72 |
| **0.55** | **50** | **100 — the planned design** |
| 0.45 | 74 | 148 |
| 0.40 | 93 | 186 |

### 8.4A.3 Pre-specified maximum

**Maximum recruitment is capped at 200 participants (100 per arm).** Declaring a ceiling in advance is what makes the design adaptive rather than open-ended. If blinded re-estimation indicates a requirement beyond 200, the study reports that the effect is smaller than the design could address and that a larger multicentre study is required — it does not quietly continue.

**What the ceiling buys** (AUC precision, true AUC 0.80):

| Per arm | Total | 95% CI half-width |
|---|---|---|
| 50 | 100 | ± 0.087 |
| 75 | 150 | ± 0.071 |
| **100** | **200** | **± 0.061** |
| 151 | 302 | ± 0.050 |

Note the diminishing return: doubling from 100 to 200 participants narrows the interval from ± 0.087 to ± 0.061. It does not transform an imprecise estimate into a definitive one. **Precision at the ± 0.05 level requires roughly 300 participants and belongs to the validation phase**, not this study.

### 8.4A.4 If an unblinded interim look is wanted

Should the investigator wish to examine actual discrimination at an interim point — for example to stop early for futility — this requires a **formal group-sequential design with α spending**, pre-specified here:

| Approach | Interim α | Final α | Comment |
|---|---|---|---|
| **O'Brien–Fleming** (recommended) | 0.0031 | 0.0490 | Conservative early; final analysis barely penalised |
| Pocock | 0.0294 | 0.0294 | Easier to stop early; substantial final-analysis cost |

**O'Brien–Fleming with a single interim at 50% information is recommended** if an unblinded look is required, because it preserves almost all final-analysis power.

**A futility rule is also pre-specified**, and is the more valuable use of an interim look: if at n = 100 the observed discrimination is **below AUC 0.60** with the confidence interval excluding 0.75, recruitment stops and the study reports a negative result. This protects against expending resources on a signal that is not there, and a well-conducted negative result in this field is publishable.

### 8.4A.5 Governance

- The interim analysis is performed by the **study statistician**, not the PI.
- The PI, technicians and analysis team **remain blinded to any group comparison** throughout blinded re-estimation.
- Any sample size change, its trigger, its date and its justification are **logged and reported in the publication**.
- **This section is written before recruitment begins and is not modified afterwards.** Any amendment requires IRB approval and is disclosed.

### 8.4A.6 Recommendation

**Begin at 100 as planned.** The primary endpoint (H1) is comfortably powered at that size for any effect resembling the clinical description, and 100 is a defensible discovery-scale cohort. Add blinded re-estimation at n = 60 and a cap of 200. This gives exactly the flexibility the investigator wants, costs nothing in statistical validity, and is straightforwardly defensible to both an IRB and a journal.

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

### 8.5.3 Partition strategy at n = 100 — why there is no carved-out test set

**A held-out test set must not be taken from these 100 participants.** A 70/30 split would leave roughly 15 per class for testing, giving:

| True AUC | 95% CI on a 15 v 15 test set |
|---|---|
| 0.75 | 0.57 – 0.93 (± 0.18) |
| 0.80 | 0.64 – 0.96 (± 0.16) |
| 0.85 | 0.71 – 0.99 (± 0.14) |

An interval that wide is uninformative — it would neither confirm nor refute anything, while simultaneously removing 30% of the data from development. **Carving out a test set here costs precision twice and buys nothing.**

**Adopted strategy.**

| Stage | Data | Method |
|---|---|---|
| **Development** | All 100 participants | **Repeated stratified nested cross-validation** (e.g. 5×5 repeats), all folds split **by participant** |
| **Final evaluation** | **A separate cohort recruited later** | Single-shot evaluation of frozen weights — a **subsequent protocol phase**, not part of this submission |

**Nested cross-validation** is used specifically because the inner loop performs model and hyperparameter selection while the outer loop provides the performance estimate, so selection does not contaminate the reported figure. Every element of the pipeline in §8.5.1 — scalers, feature selection, thresholds, calibration — is fitted **inside the inner loop only**.

**What this study reports.** Cross-validated performance on the development cohort, explicitly labelled as **development performance requiring independent validation**. This protocol does **not** report a held-out test result, and does not claim one.

**Weight freezing still applies (§8.5.6).** At the end of development the model is frozen and hashed. That frozen artefact is what the subsequent validation phase will evaluate — which is precisely the design intent of "test on new subjects."

### 8.5.3A Per-participant analysis — the aggregation rule

**The unit of analysis is the participant, never the image.** Each participant contributes six sites, bilateral limbs, and many frames per cine sweep — plausibly several hundred images. Treating images as independent observations would imply a sample of many thousands and inflate every statistic catastrophically.

**Aggregation is pre-specified:**

1. Features are computed per **region of interest**.
2. ROI-level values are aggregated to a **site-level** value per participant (median across ROIs, which is robust to occasional artefactual ROIs).
3. Site-level values are combined into a **single participant-level prediction**.
4. The combination rule (mean of site probabilities, median, or attention-weighted multiple-instance learning) is **selected within the inner cross-validation loop** and reported.

**Every reported statistic — AUC, sensitivity, specificity, ICC — is computed over 100 participant-level observations.** Any figure implying a larger denominator is an error and will not be reported.

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

The principal residual risk in the study is confidentiality, not physical harm. Mitigations are described in §7: DICOM de-identification including burned-in text, separately held encrypted linking key, access-controlled institutional storage, and a separate consent option for image sharing. **Critically, all processing is performed on an isolated local workstation with no internet egress and no third-party or cloud service involvement (§7.1B)**, removing the largest category of data-protection risk in imaging research. The analysis machine does not hold the linking key, so its compromise would not permit re-identification.

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
- **The computer analysis is done entirely on a machine inside the hospital, with no internet connection.** Your scan pictures are never sent to any outside company, cloud service or website.
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

*One copy for the participant, one for the study file, one for the medical record.*

---

# 11. Ethical Considerations

## 11.1 Governing principles

The study is conducted per the **Declaration of Helsinki**, ICH Good Clinical Practice, and `[45 CFR 46 / local governing regulation]`. No participant is enrolled before written informed consent and IRB approval.

## 11.2 Justice and participant selection

Participants are selected on scientific grounds; controls are individually BMI- and age-matched to cases. Recruitment is expected to be female because lipoedema is overwhelmingly a disease of women; this reflects disease epidemiology, not exclusion. `[Recruitment materials should be reviewed to ensure access across socioeconomic and ethnic groups within the catchment population, and interpretation provided where needed.]`

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

Even if entirely successful, this study is a **discovery / proof-of-concept study**. It will support the claim that a quantifiable ultrasound tissue signature exists and is associated with a single expert's clinical classification, in the population and on the equipment studied, with an imprecise effect estimate. It will **not** support a diagnostic-accuracy claim, and independent prospective validation is required before one is made. It will not support the claim that ultrasound artificial intelligence diagnoses lipoedema. A single-centre study with internal validation permits only cautious language; multicentre prospective evaluation would be required before stronger claims are appropriate. This limitation is stated in the protocol so that it appears in the publication rather than being extracted by a reviewer.

---

# 14. Declared Limitations

Stated here so they appear in the protocol and the publication rather than being extracted by a reviewer.

1. **Single-expert reference standard.** All labels derive from one clinician. The study measures concordance with one expert's clinical classification, not with a consensus or an independent gold standard. Mitigated by pre-imaging database locking, intra-rater kappa, and an independent external audit of a 20% subsample (§5.1).
2. **No histological gold standard for the disease itself.** Lipoedema has no diagnostic biopsy. The histology sub-study correlates ultrasound with tissue features; it does not establish a gold-standard diagnosis.
3. **Discovery-scale sample (n = 100, expandable to a pre-specified maximum of 200).** Well powered to detect whether a signature exists; imprecise about its magnitude (AUC interval approximately ± 0.09). No held-out test set is taken from this cohort, because a 15-per-class test would be uninformative; cross-validated development performance is reported and independent validation deferred to a subsequent phase.
4. **No lymphoedema or obesity-without-lipoedema arm.** Specificity against those conditions is not established here. Cellulite is controlled as a covariate rather than an arm.
5. **Single centre, two consoles, three operators.** Generalisation to other equipment, settings and operators is unestablished. Mitigated by leave-one-console-out and leave-one-operator-out analyses, but not eliminated.
6. **Dermal characterisation is out of reach.** The available probe ceiling (13 MHz) does not resolve dermal texture. The study is scoped to subcutaneous fat.
7. **Radiofrequency data is likely unavailable** on this platform, restricting the study to phantom-calibrated B-mode rather than full spectral quantitative ultrasound.
8. **The internal control assumes upper abdominal sparing**, which is a clinical generalisation. The Phase 1 pilot tests this; if it fails, the primary endpoint requires redesign.
9. **Cross-sectional design.** No inference about progression, staging or treatment response is supported.

---

# 15. Handover Brief for the Study Statistician

The calculations in §8 are computed and reproducible, not estimated, and the code is available. They are intended to give the statistician a working draft to check and correct in an hour rather than derive from scratch. **They are not a substitute for statistical sign-off, and the following are open questions where the statistician's judgement should override this document.**

## 15.1 Known limitations of the calculations as presented

| Issue | Why it matters |
|---|---|
| **H1 power assumes a simple paired *t*-test** | The actual primary analysis is a mixed-effects **arm × site interaction** with participant as a random effect. Effective power depends on the within-participant intraclass correlation across ROIs and sites, which is **unknown until the pilot**. The paired-*t* figure is an approximation and is likely optimistic or pessimistic depending on that ICC |
| **Hanley–McNeil is for a single AUC** | Comparing the model against thickness-alone and bright-spot-density-alone uses **correlated** AUCs on the same participants. Power for that comparison requires a **DeLong-based calculation**, which is not presented here |
| **Distributional form of the metrics is unknown** | Nakagami *m* is bounded below at zero and typically right-skewed; bright-spot density is a count per unit area and may be better modelled as Poisson or negative binomial. **Transformation or a generalised linear mixed model may be required**, which changes the effect-size scale on which power was computed |
| **Bonferroni across 5 co-primary metrics is conservative** | The metrics are correlated — they measure related aspects of the same phenomenon. A **hierarchical or gatekeeping procedure**, or a single pre-specified primary metric with the others as secondary, may preserve more power. This is a real decision to make |
| **"Independent speckle cells" is a rule of thumb** | The ~100-sample minimum for a stable Nakagami fit, and the ~0.17 mm² speckle cell derived from axial ≈ 2λ and lateral ≈ 6λ, are engineering approximations. Actual lateral resolution depends on aperture and depth |
| **Attrition assumed at 15%** | Not evidence-based; a placeholder |
| **Group-sequential boundaries quoted from standard tables** | If an unblinded interim is adopted, boundaries should be computed for the actual design and information fractions |

## 15.2 Specific decisions requested from the statistician

1. **Specify the primary analysis model formally** — the mixed-effects structure, the random-effects specification, and the exact form of the arm × site interaction test.
2. **Choose the multiplicity strategy**: five co-primary metrics with Bonferroni, versus one designated primary metric with the rest secondary. The latter would materially increase power and may be preferable.
3. **Rule on transformations** for each metric, ideally after the pilot provides distributional data.
4. **Compute DeLong-based power** for the model-versus-baseline comparison.
5. **Confirm or revise the blinded re-estimation trigger** (currently n = 60) and the re-estimation formula.
6. **Adjudicate the nested cross-validation scheme** — repeats, folds, and whether the outer-loop estimate is reported with a proper confidence interval given fold dependence.
7. **Set the ICC threshold** for the reproducibility gate (currently 0.75, a convention rather than a derivation).
8. **Own the blind.** Blinded sample size re-estimation requires someone who is not the PI and not the analysis team to hold the group allocation. **This must be the statistician**, and the protocol assigns it to them (§8.4A.5).
9. **Sign the Statistical Analysis Plan** (Appendix E) before recruitment opens.

## 15.3 What is deliberately fixed and should not be relaxed

These are design commitments rather than statistical preferences, and changing them would undermine the study's defensibility:

- **Participant-level analysis and participant-level splitting**, never image-level
- **All data-estimated parameters fitted inside the cross-validation loop**, including scalers and thresholds
- **Pre-specification before recruitment**, with the SAP deposited
- **No held-out test set carved from n = 100** — validation is a separate phase
- **Publication irrespective of outcome**

# 16. Study Timeline

| Phase | Duration | Activity |
|---|---|---|
| 0 | 3 months | IRB approval, registry registration, phantom procurement, preset creation and validation, sonographer training |
| 1 | 3 months | **Pilot (n ≈ 20–30)**: verify deep fascia visualisation in the thickest participants; verify upper abdominal fat is not itself abnormal; estimate effect size and ICCs; finalise statistical analysis plan |
| 2 | 12–18 months | Cohort recruitment and imaging (n = 100; ~116 recruited for attrition) |
| 3 | 3 months | Reproducibility analysis, feature screening, nested cross-validated model development, **weight freeze and hash** |
| 4 | — | **Independent validation is a separate subsequent protocol**, not part of this submission. The frozen model from Phase 3 is its input |
| 5 | 3 months | Histology analysis, synthesis, manuscript preparation |

**The Phase 1 pilot is a gate, not a formality.** If upper abdominal fat proves abnormal in lipoedema, the primary endpoint requires redesign before the main study proceeds.

---

# 17. Appendices

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
