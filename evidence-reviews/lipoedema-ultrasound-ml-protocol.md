# Draft Protocol: Standardised Research Ultrasound Acquisition and Machine-Learning Tissue Characterisation of Subcutaneous Fat in Lipoedema

### Quantifying the "sparkling" appearance of lipoedematous fat

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

**H1 (primary).** The characteristic **sparkling appearance** of lipoedematous subcutaneous fat (§3A) is a reproducible, quantifiable acoustic phenomenon that distinguishes affected fat from that patient's own unaffected trunk fat, independent of layer thickness.

**H2.** That signature distinguishes lipoedema from BMI-matched controls, from cellulite without lipoedema, and from lymphoedema.

**H3.** The signature correlates with histological adipose tissue remodelling — adipocyte diameter, septal fibrosis, inflammatory infiltrate, interstitial fluid — in tissue biopsied from the scanned site.

**H4.** Quantitative features outperform blinded expert visual grading (SEG/SEF and echotexture/fibrosis/oedema) of the same images.

**Biological rationale.** Lipoedema histology describes adipocyte hypertrophy, interstitial fluid accumulation, septal fibrosis and altered microvasculature. Each has a predicted acoustic consequence: larger scatterers alter backscatter magnitude and envelope statistics; interstitial fluid creates anechoic clefts, raising heterogeneity and echo-free space; fibrotic septa raise stromal echogenicity and structural anisotropy. These are directional predictions, not a blind feature dump.

---

## 3A. The index phenomenon: the "sparkling" appearance

The clinical observation driving this study is that lipoedematous fat has a **characteristic sparkling appearance recognisable casually, at a glance, on general settings**. This is the phenomenon to quantify. Naming it precisely matters more than any modelling choice, because it converts a gestalt into a measurand.

### 3A.1 What "sparkly" is, acoustically

Sparkle is the visual impression of **numerous discrete, bright, punctate echoes scattered through an otherwise hypoechoic background**. In scattering terms this is a departure from *fully developed speckle*.

When a resolution cell contains many small, randomly positioned scatterers of similar strength, the echo envelope follows a **Rayleigh** distribution — smooth, featureless speckle. Adding a population of **discrete, high-amplitude, coherent reflectors** shifts the envelope into the **post-Rayleigh (Rician)** regime. That shift *is* sparkle.

This is not a novel idea requiring invention; it is exactly what envelope statistics were developed to measure:

| Parameter | Behaviour | Interpretation |
|---|---|---|
| **Nakagami *m*** | *m* < 1 pre-Rayleigh; *m* = 1 Rayleigh; ***m* > 1 post-Rayleigh** | The classical single-parameter sparkle index |
| **Homodyned-K *k*** (coherent-to-diffuse ratio) | Rises with coherent component | The principled decomposition — separates the "sparkle" from the diffuse background explicitly |

**The clinician's eye and the estimator are measuring the same physics.** That alignment is the strongest asset this study has.

### 3A.2 The quantification ladder — most interpretable first

1. **Bright-spot density** — count of local intensity maxima exceeding a phantom-normalised threshold, per mm² of subcutaneous ROI, with multi-scale blob detection (Laplacian-of-Gaussian) to capture sparkle size. This is the most literal translation of what the eye sees, is trivially explainable to a clinician, and should be reported whatever else is used.
2. **Envelope statistics** — Nakagami *m*, homodyned-K *k*.
3. **Intensity distribution shape** — skewness and kurtosis of the envelope histogram; ratio of the 95th–99th percentile to the median ("how bright are the bright bits relative to background"). Sparkle predicts a heavy right tail.
4. **Scatterer spacing** — cepstral or autocorrelation analysis, testing whether sparkles are quasi-regularly spaced, as lobular architecture would predict.
5. **Generic texture** — GLCM contrast, entropy, run-length. Included as a comparator, but expected to be a blunter instrument than the targeted parameters above.

### 3A.3 Recovering envelope statistics without RF

Envelope statistics are classically computed on the **uncompressed envelope**. B-mode display data is **log-compressed and post-processed**, which distorts the distribution.

This is recoverable, and it is the specific reason the §4.2 settings lock matters:

- With **dynamic range (Compress) and grey map fixed and known**, the log compression can be inverted to approximate the linear envelope before fitting.
- The mapping must be **characterised once against the reference phantom** at the study settings, and that characterisation applied identically to every image.
- GE's TruScan raw-data archive (§4.9.4) helps, provided every study is exported through one fixed configuration.

Without locked compression settings, envelope-statistic estimates are uninterpretable. The acquisition standard is not hygiene — it is what makes the primary measurand recoverable.

### 3A.4 Predicted histological substrate

Leading hypothesis, testable directly in the liposuction sub-study (§6.5): sparkle reflects **increased density and impedance contrast of septal and interstitial interfaces, set against an anechoic background of interstitial fluid**. Fibrotic and thickened septa supply the bright discrete reflectors; interstitial fluid supplies the dark background that makes them conspicuous. This predicts that bright-spot density correlates with septal fibrosis grade, and that the *contrast* between spots and background correlates with interstitial fluid.

The related descriptors already in circulation — "snowstorm", "starry sky", "pebbles in cotton wool" — are almost certainly describing the same phenomenon, and none has been quantified.

### 3A.5 The confound that will be attacked first, and the defence

**Sparkle is exquisitely sensitive to gain, dynamic range, focus position and depth.** Raise the gain or narrow the dynamic range and everything looks sparklier. This is the first objection any reviewer will raise, and it would be fatal if unaddressed.

Three defences, all built into this protocol:

1. **Locked gain, compression and grey map** (§4.2) — sparkle cannot be manufactured by console adjustment if the console cannot be adjusted.
2. **The within-subject abdominal control** (§6.4) — sparkle present in limb fat but absent in trunk fat *of the same patient, in the same session, at identical settings* cannot be a gain artifact. This is the decisive argument and the reason S4 is the primary comparator.
3. **Standardised analysis depth and fixed focal zone** — sparkle appearance varies with depth through attenuation and with distance from focus through resolution. ROIs are taken at a fixed depth below the dermis, with focus fixed at that depth.

### 3A.6 What this changes about the study

If the phenomenon is visible casually, the effect size is probably large, which is good news for feasibility. Two consequences:

- **The pilot must first establish that the visual phenomenon is real and reproducible between observers.** Two or more clinicians, blinded, grade "sparkle present / absent / equivocal" on de-identified single frames. Report the agreement statistic. For calibration, the closest published comparator — clinical versus ultrasound classification of cellulite — achieved only moderate agreement (Gwet's AC1 = 0.444). If blinded sparkle grading beats that, the phenomenon is robust and the quantification programme is justified.
- **The paper's narrative becomes clean and strong**: clinicians recognise a characteristic sparkling appearance of lipoedematous fat; we define it physically, quantify it under a standardised acquisition protocol, show it has a histological substrate, and show it discriminates independently of tissue thickness.

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

| View | Purpose | Frequency mode | Depth | Focus |
|---|---|---|---|---|
| **Survey (low magnification)** | Structural measurement: skin surface → subcutaneous/muscle fascial boundary; layer identification; site documentation | Lowest available on the probe (penetration mode) | Sufficient to include deep fascia | Mid-subcutaneous |
| **Characterisation (high magnification)** | Texture analysis of the subcutaneous layer | Highest available on the probe (resolution mode) | 2–3 cm | Mid-subcutaneous layer |

The survey view supplies the thickness covariate and the anatomical context. The characterisation view supplies the tissue signature. They are separate acquisitions with separate presets, not the same image at two zooms.

Absolute frequencies are set by the available probe — see §4.9, which is binding for this study.

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

### 4.9 Platform-specific implementation: GE Vivid 6 / Vivid 7 with 12L-RS

This is the hardware actually available, and it constrains the study in ways that must be designed around rather than discovered during analysis.

**Probe — confirmed specification.** GE 12L-RS wideband linear array:

| Spec | Value |
|---|---|
| Frequency bandwidth | **5.0 – 13.0 MHz** |
| Field of view | 38 – 39 mm |
| Footprint | ~42 × 7 mm (housing ~47 × 14 mm) |
| Modes | 2D, colour Doppler, PW Doppler, harmonics, **SRI** |

The small footprint is an advantage for the malleolar and foot-dorsum contours in S1. The 38–39 mm field of view constrains ROI width and requires generous frame overlap on the long sweeps (S2, S5).

#### 4.9.1 Three consequences that change the study

**(a) Dermal texture analysis is out of reach — scope honestly to subcutaneous fat.**
The cellulite structural work that provides our closest precedent used a **20 MHz** probe. At a ceiling near 13 MHz, axial resolution is roughly 0.2–0.3 mm against a dermal thickness of 1–3 mm, so the dermis spans only a few resolution cells. That is enough to *measure* dermal thickness; it is not enough to characterise dermal texture.

The study should therefore be titled and framed around **subcutaneous adipose tissue**, not skin. This is not fatal — the lymphoedema histological work (Piyaman et al.) used 6–18 MHz conventional HFUS and successfully graded subcutaneous echogenicity and echo-free space, which is precisely our target. If dermal characterisation becomes a priority later, it requires a higher-frequency probe (a hockey-stick or small-parts linear in the 15–20+ MHz class); check with GE which high-frequency `-RS` transducers are compatible with your consoles before assuming availability.

**(b) Deep fascia in the thigh: probably reachable, but verify in the pilot.**
Reported medial proximal thigh subcutaneous thickness in this population reaches ~48 mm. In **resolution mode near 13 MHz this will not penetrate**, but the confirmed 5 MHz lower bound is genuinely useful: a dedicated survey preset at the bottom of the band should reach 5–6 cm and visualise the deep fascia in most participants.

- Use a **survey preset at the lowest available frequency** (penetration mode), separate from the characterisation preset
- **Verify in the pilot on the thickest participants specifically** — do not assume, and do not discover this at analysis
- Where the fascial boundary still cannot be resolved, record it as a **pre-specified missing-data category** rather than forcing a measurement
- Only if the pilot shows systematic failure is a curvilinear or lower-frequency probe needed, and then for the survey view alone — characterisation stays on the 12L-RS

**(c) Two consoles means a cross-device study from day one.**
Vivid 6 and Vivid 7 are different machines with different processing. This is not a defect — handled properly it strengthens generalisability, which most single-centre radiomics papers lack. It makes three things mandatory:
- The **reference phantom (§4.3) is compulsory, not optional** — it is the only way to harmonise the two consoles
- **Console identity is recorded per acquisition** and entered as a covariate, with device held out at validation
- **Scan a subset of participants on both consoles in the same session.** This yields a direct cross-device transferability measurement — cheap to collect, and a publishable methodological result in its own right

#### 4.9.2 GE-specific control names to lock

The generic table in §4.2 maps onto the Vivid console as follows. Save as named presets and photograph the control panel.

| Generic parameter | GE Vivid control | Required setting |
|---|---|---|
| Speckle reduction | **SRI** (Speckle Reduction Imaging) | **OFF / level 0** — this is the single most important switch; SRI destroys the texture signal |
| Spatial compounding | **CrossXBeam / CRI** | **OFF** |
| Tissue harmonics | **Octave / Harmonics** | **OFF** (or fixed ON for every acquisition — do not mix) |
| Frequency selection | **Pen / Gen / Res** | **Res** for characterisation; **Pen** for deep survey. Record which |
| Dynamic range | **Compress / DR** | Fixed numeric value |
| Grey map | **Map** (named curve) | Fixed named map |
| Edge enhancement | **Edge Enhance** | Fixed, minimum |
| Frame averaging | **Frame Average / Persistence** | Fixed, minimum |
| Overall gain | **2D Gain** (numeric readout) | Fixed numeric value, never adjusted per patient |
| Depth-dependent gain | **TGC sliders** | All at centre detent; photograph the slider bank each session |
| Depth | **Depth** | Fixed per site |
| Focus | **Focus** | Single zone, fixed depth |

#### 4.9.3 Resolution cell and minimum ROI size — derived for this probe

Sparkle quantification and envelope-statistic fitting both require an ROI containing enough **independent speckle cells** for a stable estimate. Nakagami *m* is generally considered to need on the order of 100+ independent samples.

Taking c = 1540 m/s, axial resolution ≈ 2λ and lateral resolution ≈ 6λ (F-number ~3):

| Frequency | λ (mm) | Axial res (mm) | Approx. lateral res (mm) |
|---|---|---|---|
| 5 MHz | 0.308 | 0.62 | 1.85 |
| 9 MHz | 0.171 | 0.34 | 1.03 |
| 13 MHz | 0.118 | **0.24** | **0.71** |

At 13 MHz the speckle cell is roughly 0.24 × 0.71 mm ≈ **0.17 mm²**, giving:

| ROI | Area | Independent speckle cells |
|---|---|---|
| 5 × 5 mm | 25 mm² | ~150 |
| **10 × 10 mm** | 100 mm² | **~590** |
| 15 × 15 mm | 225 mm² | ~1340 |

**Specification: minimum ROI 5 × 5 mm; preferred 10 × 10 mm.** A 10 mm box fits comfortably within the 38 mm field of view and within the subcutaneous layer at most sites, while giving ample samples for stable envelope-statistic estimation.

Two corollaries:
- **Texture kernels must be defined in millimetres and must exceed the speckle cell size**; a kernel smaller than ~0.7 mm laterally at 13 MHz is measuring the point spread function, not the tissue.
- **Sparkle features are frequency-dependent.** Because resolution changes across the band, all characterisation acquisitions must use the **same** frequency setting. Comparing sparkle between a 9 MHz and a 13 MHz image is not valid.

#### 4.9.4 Raw data — what is and is not available

**Do not assume RF or IQ export.** GE's **TruScan Architecture with Raw Data** is a proprietary archive format that preserves pre-processing data so an archived study can be re-opened and re-processed with different scan controls. It is genuinely useful here, but it is **not calibrated radiofrequency data** and does not by itself enable spectral QUS.

Two practical implications:

- **Enable TruScan raw-data archiving**, and export every study for analysis through a **single fixed post-processing configuration**. The ability to re-apply controls post-hoc is a benefit only if it is used to enforce uniformity; if different operators re-export with different maps or gain, it becomes another source of drift.
- **Ask GE directly whether an RF or IQ research export exists for your Vivid consoles**, ideally under a research agreement. If it does, the spectral QUS parameters in §7.1 (backscatter coefficient, attenuation coefficient, effective scatterer size) become available and the study's ceiling rises substantially. If it does not — the likely answer for this platform — the study proceeds on phantom-calibrated B-mode, which is exactly what the lymphoedema precedent used.

Assume no RF until GE confirms otherwise, and design the primary analysis so it does not depend on it.

### 4.10 Probe inventory and assignment — and one rule that must not be broken

Three transducers are available. Only one can carry the primary measurement.

| Probe | Type | Band | Role in this study |
|---|---|---|---|
| **12L-RS** | Linear array, 38–39 mm FOV | 5–13 MHz | **All characterisation (sparkle) acquisitions. All limb and abdominal texture analysis.** Survey views at the low end of the band. |
| **C1-6 class** | Curvilinear/convex | 1–6 MHz | Deep abdominal **thickness only**, where the linear probe cannot penetrate. Excluded from all texture analysis. Connector compatibility unconfirmed (§4.10.4). |
| **3S-RS** | Phased array sector, 90°, 19.3 × 27.6 mm | 1.5–4.0 MHz | **No role in the primary study.** Fallback for deep abdominal thickness only if no compatible curvilinear exists (§4.10.5). |

#### 4.10.0 Speckle cell across the available hardware

Sparkle is a fine-scale phenomenon, so resolution is the binding constraint. Independent speckle cells available in a 10 × 10 mm ROI, against the ~100-sample minimum for a stable Nakagami fit:

| Probe / setting | Speckle cell | Cells in 10×10 mm ROI | Adequate for envelope statistics? |
|---|---|---|---|
| **12L-RS @ 13 MHz** | **0.17 mm²** | **~594** | **Yes — the reference configuration** |
| 12L-RS @ 7 MHz | 0.58 mm² | ~172 | Marginal |
| C1-6 @ 6 MHz | 0.79 mm² | ~126 | Marginal, and geometry disqualifies it |
| 12L-RS @ 5 MHz | 1.14 mm² | ~88 | **No** |
| 3S-RS @ 4 MHz | 1.78 mm² | ~56 | **No** |
| 3S-RS @ 1.5 MHz | 12.65 mm² | ~8 | **No** |

**A trap this table exposes.** The penetration-mode survey preset recommended in §4.9.1(b) sits near 5 MHz and yields only ~88 independent cells — **inadequate for envelope statistics**. Survey-preset images are for **thickness measurement and anatomy only**. Envelope statistics, bright-spot density and texture features must **never** be computed on survey acquisitions. This is a protocol-level exclusion, not a caution.

---

A curvilinear abdominal transducer (GE C1-6 class, **1–6 MHz**, up to 35 cm depth) and a phased array cardiac probe are also available. Both have limited roles, and **neither touches the primary measurement**.

#### 4.10.1 The rule

> **All characterisation (sparkle) acquisitions — limb and abdomen alike — are made with the 12L-RS at one fixed frequency setting.**

The within-subject affected-versus-spared contrast (§6.4) is the primary endpoint and the decisive defence against the gain-artifact objection (§3A.5). That defence only works if both sides of the comparison are acquired **identically**. Measuring limb sparkle on a linear probe and trunk "control" sparkle on a curvilinear would confound the primary endpoint with probe geometry and destroy the argument. The abdominal characterisation view (S4) is therefore a **12L-RS acquisition**, using the same preset as the limbs.

#### 4.10.2 Why the curvilinear cannot carry sparkle

**Resolution.** Sparkle is a fine-scale phenomenon. Discrete reflectors smaller than the resolution cell merge into the diffuse background — the sparkle is literally averaged away:

| Probe / setting | Axial (mm) | Lateral (mm) | Speckle cell |
|---|---|---|---|
| 12L-RS @ 13 MHz | 0.24 | 0.71 | **0.17 mm²** |
| 12L-RS @ 7 MHz | 0.44 | 1.32 | 0.58 mm² |
| C1-6 @ 6 MHz | 0.51 | 1.54 | 0.79 mm² |
| C1-6 @ 3 MHz | 1.03 | 3.08 | 3.16 mm² |

The resolution cell is **~4.7× larger** at 6 MHz curvilinear than at 13 MHz linear, and ~19× larger at 3 MHz.

**Non-comparable statistics.** Nakagami *m*, bright-spot density and every texture descriptor depend on the point spread function. Values from a 13 MHz linear and a 6 MHz curvilinear acquisition are **different measurands**, not the same measurand with more noise. They must never be pooled or compared.

**Convex geometry.** On a curvilinear array the beam lines diverge, so lateral resolution degrades with depth and the scan-converted image has a spatially varying relationship between pixels and beam lines. Texture features computed on scan-converted convex images are therefore **position-dependent** in a way linear-array images are not. This is an under-appreciated confounder in texture work and a further reason to keep the primary measurement on the linear probe.

#### 4.10.3 What the curvilinear is genuinely useful for

- **Deep abdominal survey.** Where subcutaneous fat at the midline exceeds what the 12L-RS can penetrate even in penetration mode, the C1-6 reliably resolves the full layer to the rectus sheath. This supplies the thickness covariate in participants where the linear probe cannot.
- **Anatomical context and site documentation** at S4.
- **Confirming layer identification** at depth before placing the linear-probe characterisation ROI.

Record probe identity on every acquisition. Curvilinear images enter thickness and anatomical analyses only, and are **excluded by protocol** from all sparkle, envelope-statistic and texture analyses.

#### 4.10.4 Connector compatibility — verify before purchase or planning

As you have already noted, the **C1-6-D / C1-6VN-D are D-port transducers** intended for GE's newer digital architecture (Vivid E95 / S70, LOGIQ E9) rather than legacy Vivid consoles. Before the protocol depends on it, **confirm which curvilinear actually connects to your Vivid 6 and 7** — on the `-RS` connector family this is typically a 4C-RS-class convex probe rather than a C1-6-D.

If no compatible curvilinear exists on these consoles, the protocol is unaffected in its primary endpoint: only the deep abdominal thickness covariate is lost, and that is recorded as missing data (§4.9.1b).

#### 4.10.5 The 3S-RS phased array — why it has no role here

Specification: phased array sector, **1.5–4.0 MHz**, 90° field of view, 30 cm depth, footprint 19.3 × 27.6 mm. Confirmed compatible with Vivid 6 and the `-RS` connector family.

It is a **cardiac probe**, and for subcutaneous tissue characterisation it is the least suitable of the three, for four independent reasons:

1. **Resolution.** At 4 MHz the speckle cell is ~1.78 mm² — **10.6× larger** than the 12L-RS at 13 MHz; at 1.5 MHz it is ~75× larger. A 10 × 10 mm ROI yields ~56 independent cells at 4 MHz and ~8 at 1.5 MHz, both far below what a stable envelope-statistic fit requires. Sparkle would be entirely averaged away.
2. **The near field is the region of interest.** Subcutaneous fat sits at roughly 0–5 cm. A phased array with a ~20 × 28 mm footprint is designed to image the heart at 8–20 cm through an intercostal window. At 1–3 cm the beam is poorly formed, the aperture is small relative to depth, and lens and matching-layer reverberation contaminate exactly the depths being measured.
3. **Sector geometry is worse than convex.** Scan lines radiate from a virtual apex effectively at the probe face, so at shallow depth adjacent lines are very closely spaced while the actual beam remains wide. The result is dense but **highly correlated** sampling: the pixel count grossly overstates the number of independent observations, which silently invalidates Nakagami and homodyned-K estimation. Scan-conversion interpolation then dominates any texture measure.
4. **Cardiac presets** apply aggressive adaptive and temporal processing and default to harmonics — the opposite of what §4.2 requires.

**Permitted use.** One only: if no `-RS`-compatible curvilinear can be sourced (§4.10.4), the 3S-RS may substitute as the **deep abdominal thickness** probe in participants whose midline fat exceeds 12L-RS penetration. Thickness measurement is a boundary-detection task and tolerates poor speckle statistics. Even then it is excluded from every texture, sparkle and envelope analysis.

**A useful incidental.** The 3S-RS being confirmed on Vivid 6 establishes the `-RS` connector family for these consoles, which supports sourcing a **4C-RS-class convex** probe rather than the D-port C1-6-D discussed in §4.10.4.

#### 4.10.6 Optional sub-study: frequency dependence of sparkle

This costs only extra presets and could be genuinely informative. Scattering behaviour depends on scatterer size relative to wavelength, so measuring how sparkle metrics change across the **12L-RS band alone** (e.g. 7, 10 and 13 MHz on the same marked ROI, back to back) constrains the effective size of the structures producing it.

- Rigorous effective-scatterer-size estimation needs RF and the reference phantom, so treat this as **exploratory** unless GE confirms an RF export (§4.9.4).
- Even without RF, a reproducible frequency trend in bright-spot density and Nakagami *m* is a mechanistic clue and strengthens the histological correlation in §6.5.
- Strictly within one probe. This sub-study is **not** an argument for comparing linear against curvilinear.

---

## 5. Scan protocol — anatomical sites

Five regions, each with survey and characterisation views. Sweeps are recorded as cine; static frames are captured at defined landmarks within each sweep.

| # | Region | Path | Rationale |
|---|---|---|---|
| S1 | **Distal leg / ankle transition** | Continuous sweep, medial aspect: mid-calf → over medial malleolus → onto dorsum of foot | Captures the affected-to-spared transition where it exists. Foot dorsum acts as a **distal internal control**. |
| S2 | **Medial thigh** | Sweep, knee → inguinal region along the medial aspect ("trouser crease") | Principal affected territory across nearly all variants. |
| S3 | **Distal third of thigh** | Focused static acquisitions, survey + characterisation | Where lipoedema is most obvious morphologically; highest expected signal. |
| S4 | **Abdominal midline, sagittal** | 6 inches below umbilicus → 6 inches above | **Primary internal control** — see §6.4. Trunk fat is typically spared. Characterisation view **must** be 12L-RS at the same preset as the limbs (§4.10.1); curvilinear used only for deep thickness if the linear probe cannot penetrate. |
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

Ordered for **this platform**, where RF export should be assumed unavailable (§4.9.4). The sparkle parameters (§3A.2) are primary, not exploratory.

1. **Sparkle quantification — PRIMARY.** Bright-spot density per mm² by multi-scale local-maximum / Laplacian-of-Gaussian detection at a phantom-normalised threshold, with spot size distribution and spot-to-background contrast. Directly operationalises the index phenomenon and is interpretable to a clinician without translation.
2. **Envelope statistics — PRIMARY.** Nakagami *m* and homodyned-K *k*, fitted after inverting the known log compression (§3A.3). *m* > 1 is the formal signature of the coherent scattering that produces sparkle.
3. **Intensity distribution shape.** Skewness, kurtosis, and high-percentile-to-median ratios of the envelope histogram.
4. **Calibrated B-mode intensity and echo-free space.** Phantom-normalised mean echogenicity, and an **echo-free space fraction** quantifying Piyaman's SEF — the dark background against which sparkle is conspicuous.
5. **Structural.** Septal density, thickness and orientation anisotropy; dermal–subcutaneous interface regularity.
6. **Generic texture.** GLCM, run-length, LBP, wavelet energies — computed only after resampling to common physical resolution (§4.5), with kernels in millimetres exceeding the speckle cell (§4.9.3). Included as a comparator; expected to be blunter than 1–2.
7. **Spectral QUS — conditional.** Backscatter coefficient, attenuation coefficient (dB/cm/MHz), effective scatterer diameter. Available **only if** GE confirms an RF/IQ research export. If obtainable, these are the most defensible parameters in the whole study and should be promoted to primary.
8. **Deep features.** CNN embeddings on calibrated, resolution-normalised patches — reported alongside, never instead of, the interpretable parameters. A model that beats bright-spot density but cannot say why is a weaker paper, not a stronger one.

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
