# Draft Protocol: Standardised Research Ultrasound Acquisition and Machine-Learning Tissue Characterisation of Skin and Subcutaneous Fat in Lipoedema

**Status: draft design document. Not ethics-approved, not statistician-reviewed, not registered. A starting point for those conversations, not a substitute for them.**

| Field | Value |
|---|---|
| Derived from | [lipoedema-ultrasound-ml.md](lipoedema-ultrasound-ml.md) |
| Document type | Study design and acquisition standard — **not** an AMIS evidence appraisal |
| Version | 2.0 (2026-08-19) — supersedes v1.0, which was morphometric |
| Constraints honoured | `standards/imaging_ml_evidence.yaml` v1.1.0 |

---

## 1. What changed from v1.0, and why

Version 1.0 proposed disproportion **ratios** of subcutaneous thickness. That was rejected on clinical grounds, correctly:

> Lipoedema occurs in variants confined to the hips, extending hip-to-knee, and extending hip-to-ankle. Any feature built on distribution or proximal-to-distal disproportion is **variant-specific by construction** and will fail on precisely those patients whose disease does not extend distally.

A **tissue signature** should be present wherever the disease is present, whatever its distribution. This version therefore abandons morphometry as the primary target and reframes the study around the ultrasound **appearance and physical properties of the fat itself**.

Thickness is retained only as a covariate and as the legacy comparator the new features must beat.

---

## 2. State of the field, and where the contribution sits

### 2.1 What is developed

**Quantitative ultrasound (QUS) is mature — for liver.** Attenuation coefficient, backscatter, fat-fraction and entropy-based methods are established for hepatic steatosis, with commercial implementations. The physics and the estimator theory are settled and directly transferable; the methodological backbone is documented in a radiologist/physicist primer (Śmieja-type QUS primer, *Insights into Imaging* 2021, https://doi.org/10.1186/s13244-021-01071-w) and in spectral RF-versus-IQ processing comparisons (https://doi.org/10.1177/01617346231226224). QUS multi-parameter classifiers exist for breast masses (https://doi.org/10.1016/j.ultrasmedbio.2019.02.025) and repeatability methodology exists for high-frequency QUS of muscle (https://doi.org/10.1177/01617346231207404).

**Structural HFUS phenotyping of subcutaneous fat has a direct precedent — in cellulite.** Intagliata et al. (2025) used 20 MHz HFUS in 150 women (BMI 18–32) to subclassify stage III cellulite by **echotexture, fibrosis and oedema** in addition to fat thickness, deriving three phenotypes including one clinical inspection does not recognise. Clinical and ultrasound classification disagreed in 33.3% of cases, with only moderate agreement (Gwet's AC1 = 0.444). https://doi.org/10.1007/s13555-025-01504-0

**Ultrasound appearance has been tied to histology — in lymphoedema.** Piyaman et al. (2025) graded two named appearance parameters, **subcutaneous echogenicity (SEG)** and **subcutaneous echo-free space (SEF)**, on conventional 6–18 MHz HFUS, and biopsied 46 surgical sites during lymphaticovenular anastomosis. Adipose tissue remodelling — adipocyte hypertrophy, inflammatory infiltration, fibrosis — tracked SEG and SEF grade. Sensitivity was high; **specificity was insufficient**. https://doi.org/10.1038/s41598-025-00485-6

### 2.2 What is absent

No study applies quantitative ultrasound tissue characterisation, texture analysis, radiomics, or machine learning to the **subcutaneous fat of lipoedema**. The lipoedema ultrasound literature is morphometric (thickness cut-offs), and the two appearance-adjacent measures that have been tested — dermal echogenicity ratio and shear-wave stiffness — each failed to separate lipoedema from controls.

### 2.3 The contribution

Three things are simultaneously true and define a publishable niche:

1. The **estimator theory is solved** elsewhere (liver), so this is not methods invention — it is rigorous transfer.
2. The **appearance-phenotyping precedent exists** in the same tissue and same demographic (cellulite), so the premise is credible to reviewers.
3. The **histological validation template exists** in the adjacent condition (lymphoedema), and lipoedema offers the same tissue access via liposuction — which nobody has exploited.

The publishable claim is not "AI detects lipoedema." It is: *a standardised acquisition protocol yields quantitative tissue parameters of subcutaneous fat that distinguish lipoedema from BMI-matched, cellulite- and lymphoedema-controlled comparators, with a demonstrated histological substrate, outperforming expert visual grading.*

---

## 3. Hypotheses

**H1 (primary).** Lipoedematous subcutaneous fat carries a reproducible quantitative ultrasound signature distinguishable from that patient's own unaffected trunk fat, independent of layer thickness.

**H2.** That signature distinguishes lipoedema from BMI-matched controls, from cellulite without lipoedema, and from lymphoedema.

**H3.** The signature correlates with histological adipose tissue remodelling — adipocyte diameter, septal fibrosis, inflammatory infiltrate, interstitial fluid — in tissue biopsied from the scanned site.

**H4.** Quantitative features outperform blinded expert visual grading (SEG/SEF and echotexture/fibrosis/oedema) of the same images.

**Biological rationale.** Lipoedema histology describes adipocyte hypertrophy, interstitial fluid accumulation, septal fibrosis and altered microvasculature. Each has a predicted acoustic consequence: larger scatterers alter backscatter magnitude and envelope statistics; interstitial fluid creates anechoic clefts, raising heterogeneity and echo-free space; fibrotic septa raise stromal echogenicity and structural anisotropy. These are directional predictions, not a blind feature dump.

---

## 4. THE ACQUISITION STANDARD

This is the core of the protocol. Quantitative and machine-learning analysis of speckle is only valid if the machine is prevented from silently changing the thing being measured.

### 4.1 The governing principle

**B-mode grey level is not a physical quantity.** It is the output of a processing chain — gain, time-gain compensation, dynamic range, grey map, speckle reduction, compounding, harmonics — most of which is vendor-proprietary and adjustable. A model trained across uncontrolled settings learns the console, not the tissue.

Two independent defences are used, and both are required:

1. **Lock the chain** (§4.2) so settings cannot vary between patients or sessions.
2. **Reference every measurement internally** (§4.3, §6.4) so residual drift cancels.

### 4.2 Settings to lock, record, and never adjust per patient

Create a **named machine preset** ("LIPO-RESEARCH") and a second ("LIPO-RESEARCH-HF"). Presets are saved on the console, applied at the start of every study, and photographed for the study file.

| Parameter | Setting | Why it matters |
|---|---|---|
| **Speckle reduction / SRI** | **OFF** | Speckle *is* the texture signal. Adaptive despeckling destroys the measurand. Non-negotiable. |
| **Spatial compounding** | **OFF** | Averages angular views; suppresses speckle statistics and septal anisotropy. |
| **Harmonic imaging** | **OFF** (or fixed ON for all) | Alters speckle statistics and effective frequency. |
| **Edge enhancement / sharpening** | **OFF** | Synthesises texture that is not tissue. |
| **Gain** | **Fixed numeric value**, identical every patient | The single largest source of grey-level drift. Never "optimise the image." |
| **TGC** | All sliders at **centre detent**, photographed | Depth-dependent gain otherwise confounds depth-dependent attenuation — the parameter of interest. |
| **Dynamic range** | Fixed (dB), recorded | Compresses the grey histogram; changes every intensity feature. |
| **Grey map / post-processing curve** | Fixed named curve | Non-linear remap of intensities. |
| **Depth** | Fixed per anatomical site | Changes pixel scale and TGC behaviour. |
| **Focus** | **Single focal zone**, fixed depth at mid-subcutaneous layer | Multiple/auto foci alter lateral resolution with depth. |
| **Frequency / probe preset** | Fixed per view class (§4.4) | Determines speckle size and penetration. |
| **Persistence / frame averaging** | Fixed, preferably minimum | Temporal averaging smooths speckle. |
| **Acoustic output (MI/TI)** | Fixed | Affects backscatter amplitude. |
| **Zoom** | See §4.5 — a genuine trap | Read-zoom interpolates; changes mm/pixel. |

**Any deviation is a protocol violation, recorded as such, and that acquisition is excluded from primary analysis rather than silently included.**

### 4.3 Reference phantom — the calibration backbone

A tissue-mimicking reference phantom with **known attenuation and backscatter coefficients** is scanned at the start and end of every session, with the identical preset, at the same depth settings.

This enables:
- **Reference-phantom-method estimation** of attenuation coefficient and backscatter coefficient — converting arbitrary grey levels into physical, machine-independent parameters
- **Session-to-session normalisation** of B-mode grey level even when RF is unavailable
- **Daily QA**: phantom parameter drift beyond a pre-set tolerance halts scanning until service

Without a phantom, cross-session and cross-machine comparison is not defensible, and the study is confined to within-session analysis.

### 4.4 Two view classes per site

| View | Purpose | Frequency | Depth | Focus |
|---|---|---|---|---|
| **Survey (low magnification)** | Structural measurement: skin surface → subcutaneous/muscle fascial boundary; layer identification; site documentation | 10–15 MHz linear | Sufficient to include deep fascia (typically 4–6 cm) | Mid-subcutaneous |
| **Characterisation (high magnification)** | Texture and QUS analysis of the subcutaneous layer | 18–24 MHz linear | 2–3 cm | Mid-subcutaneous layer |

The survey view supplies the thickness covariate and the anatomical context. The characterisation view supplies the tissue signature. They are separate acquisitions with separate presets, not the same image at two zooms.

### 4.5 The magnification trap — read this before piloting

Most texture descriptors (GLCM, run-length, LBP, wavelet energies) are computed over **pixel** neighbourhoods and are therefore **scale-dependent**. If a low-magnification and a high-magnification image are analysed at native pixel resolution, the extracted features encode the zoom setting, not the tissue. This is a leading cause of irreproducible radiomics.

Mandatory mitigations:

- Record **mm/pixel calibration for every image** (from DICOM pixel spacing, verified against a phantom scale).
- **Resample all images to a single common physical resolution** before feature extraction.
- Define texture kernels in **millimetres**, then convert to pixels per image — never fix them in pixels.
- Prefer **acquisition (write) zoom** over post-hoc (read) zoom; read zoom interpolates and manufactures correlation between neighbouring pixels, systematically biasing texture features.

### 4.6 Coupling, pressure and probe angle

- **Generous gel or a fixed-thickness standoff pad.** Subcutaneous fat is compressible; transducer pressure deforms it and changes echotexture, layer thickness and stiffness simultaneously.
- **Minimal, standardised contact pressure.** A force-sensing standoff or a fixed-thickness gel pad with the probe just floating is strongly preferred to operator "light pressure", which is not reproducible.
- **Probe perpendicular to the skin.** Septa are specular reflectors; a few degrees of angulation changes their apparent echogenicity substantially. Angle is a major source of septal-feature variance.

### 4.7 Patient preparation — lipoedema-specific

- **Supine rest for 10–15 minutes** before limb scanning. Orthostatic oedema is intrinsic to lipoedema and will otherwise vary with how long the patient sat in the waiting room.
- **Standardised time-of-day window** (e.g. all scans 08:00–11:00). Diurnal fluid shift is a real effect in this population and a genuine confounder for any fluid-sensitive feature.
- **No compression garments for ≥ 12 hours** prior; record adherence.
- **Standardised position per site**, recorded — supine for abdomen and medial thigh; the limb position must be identical across visits.
- **Skin marking** of scan sites with anatomical measurement from a bony landmark, photographed, for repeat visits and for biopsy co-registration.

### 4.8 Data export

- **Uncompressed DICOM.** Never JPEG or lossy video. Lossy compression is specifically destructive to speckle texture and silently invalidates the measurand.
- **Cine loops** for sweeps, with frame-level metadata and full acquisition parameters embedded.
- **RF or IQ data if the platform provides a research export.** This is the single highest-value capability upgrade available: RF enables true spectral QUS — backscatter coefficient, attenuation coefficient, effective scatterer size, and envelope statistics (Nakagami, homodyned-K) — which are physical, machine-independent, and far more defensible than B-mode texture. If a research package can be obtained, obtain it before starting.

---

## 5. Scan protocol — anatomical sites

Five regions, each with survey and characterisation views. Sweeps are recorded as cine; static frames are captured at defined landmarks within each sweep.

| # | Region | Path | Rationale |
|---|---|---|---|
| S1 | **Distal leg / ankle transition** | Continuous sweep, medial aspect: mid-calf → over medial malleolus → onto dorsum of foot | Captures the affected-to-spared transition where it exists. Foot dorsum acts as a **distal internal control**. |
| S2 | **Medial thigh** | Sweep, knee → inguinal region along the medial aspect ("trouser crease") | Principal affected territory across nearly all variants. |
| S3 | **Distal third of thigh** | Focused static acquisitions, survey + characterisation | Where lipoedema is most obvious morphologically; highest expected signal. |
| S4 | **Abdominal midline, sagittal** | 6 inches below umbilicus → 6 inches above | **Primary internal control** — see §6.4. Trunk fat is typically spared. |
| S5 | **Posterior arm** | Sweep, elbow → shoulder, posterior aspect | Upper-limb involvement (Type IV); tests distribution-independence of the signature. |

At **every** site: the survey view is used to measure skin surface → subcutaneous/muscle fascial boundary, and the characterisation view is centred on the subcutaneous layer.

Sites are scanned in a fixed order, and the phantom is scanned before S1 and after S5.

---

## 6. Study design

### 6.1 Arms

| Arm | Purpose |
|---|---|
| **Lipoedema** | Index condition; stratified by distribution variant (hip-confined / hip-to-knee / hip-to-ankle / upper limb) |
| **Healthy controls, BMI-matched** | Baseline normal fat |
| **Obesity without lipoedema, BMI-matched** | The primary clinical confounder |
| **Cellulite without lipoedema** | **Essential.** Intagliata et al. show cellulite has its own HFUS structural phenotypes in the same regions and demographic. Omitting this arm invites the reviewer objection that the signature is cellulite. |
| **Lymphoedema** | SEG/SEF changes overlap (Piyaman et al.); tests specificity against the other adipose-remodelling condition |

### 6.2 Distribution-variant stratification

Recruitment is stratified across variants, and **H1 is tested within every variant stratum**. A signature that holds only in hip-to-ankle disease has failed the clinical requirement that motivated this design.

### 6.3 Reference standard

As in the review's §10.4 — blinded, independent, and measured:

- Two clinicians independent of image acquisition, **blinded to all ultrasound**, applying a pre-specified criterion set
- Blinded third-clinician adjudication of disagreements
- **Inter-rater kappa reported**, so the ceiling on achievable model performance is quantified rather than assumed
- Sonographers blinded to clinical diagnosis at acquisition

### 6.4 The within-subject paired design — the strongest feature of this protocol

The abdominal midline scan (S4) is not merely a sixth site. It is the **internal reference** that makes the whole study defensible, and it solves three problems at once:

1. **Device and session confounding.** Affected-site fat and spared trunk fat are acquired in the same patient, on the same machine, in the same session, at the same locked settings. Any residual console drift is common to both and cancels in the paired contrast.
2. **Between-subject variation.** Age, skin type, hydration and body composition are held constant within the pair.
3. **The distribution-variant problem.** Whatever the variant, an affected site and the spared trunk are both available. The primary contrast is therefore **variant-agnostic** — exactly what the clinical objection demanded.

**The primary endpoint is the within-subject affected-versus-spared tissue-signature contrast**, which is also statistically far more efficient than between-subject classification. Between-subject discrimination (H2) is secondary.

*Caveat requiring pilot confirmation: trunk sparing in lipoedema is a clinical generalisation, not an established histological fact. The pilot must verify that trunk fat in lipoedema patients is not itself abnormal — if it is, the internal reference is contaminated and S4 becomes a comparison site rather than a control. This is a genuine risk to the design and should be resolved before the main study.*

### 6.5 Histological sub-study — the element that lifts this above pattern-matching

Patients proceeding to **liposuction** provide the same tissue access that lymphaticovenular anastomosis gave Piyaman et al.

- Pre-operatively, scan and **skin-mark a defined site** with the full protocol
- Intra-operatively, biopsy **that marked site**
- Blinded histology: adipocyte diameter distribution, septal fibrosis grade, inflammatory infiltrate, interstitial fluid, microvascular density
- Correlate each quantitative ultrasound parameter with each histological variable

This converts the claim from "a model separates groups" to "a measurable acoustic parameter has an identified tissue substrate." No such correlation exists for lipoedema. It is the most publishable single component of this protocol, and it should be pursued even if the classification results are modest.

---

## 7. Feature extraction and modelling

### 7.1 Feature families, in order of defensibility

1. **Spectral QUS (requires RF/IQ):** backscatter coefficient, attenuation coefficient (dB/cm/MHz), effective scatterer diameter. Physical, machine-independent after phantom calibration. Highest publication value.
2. **Envelope statistics:** Nakagami *m*, homodyned-K parameters. Sensitive to scatterer density and regularity — the predicted correlate of adipocyte hypertrophy.
3. **Calibrated B-mode intensity:** phantom-normalised mean echogenicity, and the **echo-free space fraction** operationalising Piyaman's SEF quantitatively.
4. **Texture:** GLCM, run-length, LBP, wavelet energies — computed only after resampling to common physical resolution (§4.5), with kernels defined in millimetres.
5. **Structural:** septal density, thickness and orientation anisotropy; dermal–subcutaneous interface regularity.
6. **Deep features:** CNN embeddings on calibrated, resolution-normalised patches — reported alongside, not instead of, interpretable parameters.

### 7.2 Modelling constraints

- **Patient-level splits, always.** Frames from a cine sweep are near-duplicates; any frame from a patient in training must exclude that patient from test. This is the most common fatal leak in cine-based studies.
- **Multiple-instance learning** over frames within a site is the natural formulation: the label attaches to the patient/site, not the frame.
- **Site-specific and site-pooled models** reported separately.
- **Model class proportionate to n.** Penalised regression or gradient boosting over interpretable QUS/texture features is primary. A deep model on raw B-mode is secondary and only defensible with the larger sample and multi-device validation.
- **Device held out** at validation wherever multi-device data exists.

### 7.3 The human comparator (H4)

Two blinded readers grade every characterisation image for SEG and SEF (Piyaman) and echotexture, fibrosis and oedema (Intagliata). Inter-rater agreement is reported. The quantitative model must beat the human read on the same images.

Intagliata et al.'s Gwet's AC1 of 0.444 for clinical-versus-ultrasound classification suggests the visual bar is only moderate — which is itself the argument for quantitation, and a clean framing for the paper.

---

## 8. Analysis plan

1. **Phantom QA and reproducibility first.** ICCs for every candidate parameter from a duplicate-acquisition subsample (second sonographer, ~20% of participants, same session and a repeat visit). Parameters below a pre-specified ICC threshold are dropped before any modelling. Publish the reproducibility table regardless of outcome — it is a contribution in its own right, because no such table exists for subcutaneous fat QUS.
2. **H1**: paired within-subject contrast, affected site versus S4, per variant stratum.
3. **H2**: between-arm discrimination, with thickness entered as a covariate to demonstrate the signature is not a proxy for thickness.
4. **H3**: ultrasound–histology correlation in the liposuction sub-study.
5. **H4**: model versus blinded visual grading on identical images.
6. **Thresholds pre-specified**; **calibration reported alongside discrimination**; external validation on a second centre and device before any confidence claim above *uncertain*.

**Sample size.** A pilot of roughly 20–30 per arm is required first, to estimate the paired effect size and the ICCs; the main study is then powered on those. Publishing a between-subject AUC target now would be guesswork. The review's precision analysis gives the between-subject floor (~150/group for AUC 0.80 ± 0.05), but the paired primary endpoint should need materially fewer. A statistician must set the final number.

---

## 9. Pre-specified expectations, including the negatives

- **Shear-wave stiffness and dermal echogenicity ratio are exploratory only.** Both have been tested in lipoedema and neither separated cases from controls.
- **A modest, well-calibrated, reproducible result is the success case.** An AUC above ~0.90 on a first single-centre dataset should trigger a leakage audit — most plausibly patient-level frame leakage or device/session confounding — before any celebration.
- **Reproducibility may defeat the whole approach.** If ICCs for texture parameters are poor under realistic operator variation, that is the finding, and it should be published: it would tell the field that B-mode texture of subcutaneous fat is not a viable biomarker without RF-based QUS.
- **Trunk fat may not be normal in lipoedema** (§6.4), which would force redesign of the primary endpoint.

## 10. The honest claim ceiling

Single-centre with internal validation caps permitted language at *uncertain*; single-centre external validation permits *qualified*; only prospective multicentre evaluation against a blinded reference standard permits definitive phrasing. Any dissemination must state operating characteristics in the same sentence as any headline metric — lipoedema patients are an actively marketed-to population.

## 11. Why this is publishable

- **Genuinely first.** No quantitative ultrasound or machine-learning tissue characterisation of lipoedematous fat exists.
- **Mechanistically grounded**, not a radiomics fishing expedition — directional acoustic predictions from known histology, tested against biopsy.
- **Methodologically transferable.** The acquisition standard and the reproducibility table are reusable by anyone working on subcutaneous tissue, which broadens citation beyond the lipoedema community.
- **Clinically motivated.** It targets the actual diagnostic failure — being told one is simply obese — rather than re-deriving thickness cut-offs.
- **Publishable if negative.** A rigorous null with a reproducibility table is a real contribution to a field that currently has neither.
