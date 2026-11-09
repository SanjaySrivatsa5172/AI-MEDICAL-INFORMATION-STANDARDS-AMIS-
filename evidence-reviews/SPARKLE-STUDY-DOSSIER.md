# The Sparkle Study — Master Dossier

> **Purpose of this file.** Single-page recall document for the whole programme. If you are an
> assistant, collaborator or the investigator returning to this work after a gap, read this first:
> it carries the decisions *and the reasons for them*, so that settled questions are not reopened
> and rejected approaches are not silently reintroduced.
>
> **Status:** design complete, IRB-ready, nothing collected. Branch
> `claude/ml-ultrasound-lipoedema-detection-ih91mf`, PR #4 (draft).

---

## 0. Names this programme goes by

| Name | Notes |
|---|---|
| **The Sparkle Study** | The canonical name. From the index phenomenon (§3). |
| "SPARQL study" | A recurring **transcription artefact** of "Sparkle Study" — dictation and autocorrect both produce it. It has nothing to do with the RDF query language. Treat as the same study. |
| "The lipoedema ultrasound machine-learning study" | Descriptive long form. |
| "The ML ultrasound lipoedema detection study" | Matches the branch name. |

---

## 1. Where this started, and what the answer was

**The original question.** *Is there a published study applying machine-learning criteria to
ultrasound detection of lipoedema, or identifying lipoedema from ultrasound characteristics and
appearance?*

**The answer: no.** Confirmed directly against PubMed. The intersection query
(lipoedema/lipedema × ultrasonography × machine learning / AI / radiomics / texture analysis)
returns exactly **one** record, and that record is an **MRI segmentation** study that matches only
through MeSH term expansion — not an ultrasound study, and not a diagnostic-classification study.

The gap is real, it is specific, and it is documented with its search boundaries in
`lipoedema-ultrasound-ml.md`. Everything downstream exists to fill it.

**Two corrections to the received literature were established along the way:**

1. **The Iker dermal echogenicity ratio does not separate lipoedema from controls.** It separates
   *lymphoedema*. The actual lipoedema-vs-control values are near-identical —
   ankle 1.36 / 1.26, calf 1.58 / 1.54, thigh 1.54 / 1.56. This result is widely mis-cited as a
   lipoedema finding; it is not one.
2. **Elastography is negative.** Ozturk found no significant lipoedema-vs-control difference
   within BMI strata.

So of all published ultrasound *appearance* measures, **two have been formally tested and both
failed.** Only **thickness** has ever passed a case–control test, and it performs modestly:
best published AUC ≈ 0.74, specificity ≈ 52%. In Bayesian terms LR+ 1.71 and LR− 0.34 — a 10%
pre-test probability moves to only 16% on a positive result. That is not a diagnostic test.

---

## 2. The constraint that shaped everything: no morphometry

The investigator **explicitly rejected** thickness, size and disproportion as the basis of the
study. The reasoning is theirs and it is correct, so it must not be quietly undone:

> Lipoedema has **distribution variants** — hip-confined, hip-to-knee, hip-to-ankle. Any feature
> built on how far the disease extends distally is **variant-specific by construction**, and will
> fail precisely on the patients whose disease does not reach the site being measured.

**Consequence:** the study is about **tissue characteristics**, not geometry. Thickness is retained
only as a covariate and for anatomy, never as a discriminative feature.

**Do not reintroduce ratio-based, thickness-based or distribution-based primary features.** A v1.0
draft was built on the disproportion hypothesis and was rejected outright. It is dead.

---

## 3. The index phenomenon — "sparkle"

The investigator's own observation, in their words:

> *"I can tell you that I can pick out 'the sparkly typical appearance of lipedema fat' by looking
> at an image casually."*

This is the whole study. A clinical gestalt, reported as reliable and effortless, that **has never
been quantified**.

**Why it is tractable rather than merely anecdotal.** It maps onto established scattering physics:

- Speckle from many small random sub-resolution scatterers → **Rayleigh** envelope statistics
  (smooth, featureless).
- Add **discrete, high-amplitude, coherent reflectors** → envelope shifts **post-Rayleigh** (Rician).
- *That shift is what the eye reads as sparkle.*

It is therefore measurable with established estimators:

| Estimator | Reads |
|---|---|
| **Nakagami *m*** | m < 1 pre-Rayleigh · m = 1 Rayleigh · **m > 1 post-Rayleigh** |
| **Homodyned-K** coherent-to-diffuse ratio | Coherent component against diffuse background |
| **Bright-spot density** | Leads the quantification ladder — closest to what the eye does |
| Echo-free space fraction | The dark interstitial counterpart |
| High-percentile-to-median intensity ratio | Simple, robust, log-domain |

**Predicted tissue substrate:** fibrotic septa against a background of interstitial fluid — testable
against histology in patients coming to liposuction (see §7, the specimen requirement).

---

## 4. Hardware — the investigator's actual equipment

| Probe | Spec | Role |
|---|---|---|
| **GE 12L-RS** linear | 5.0–13.0 MHz, FOV 38–39 mm, footprint ≈ 42 × 7 mm; 2D, colour, PW, harmonics, SRI | **All** sparkle / envelope / texture acquisitions, at **one fixed frequency** |
| **GE C1-6** curvilinear | 1–6 MHz | Deep abdominal thickness covariate **only**. Caveat: C1-6-D / C1-6VN-D are D-port/digital-architecture probes and may not mate with a legacy Vivid 6 |
| **GE 3S-RS** phased array | 1.5–4.0 MHz, 90° FOV, 30 cm depth, footprint 19.3 × 27.6 mm | **Excluded from all tissue characterisation** |

Consoles: **GE Vivid 6 and Vivid 7.**

### 4.1 The speckle-cell calculation that drives probe assignment

Speckle cell ≈ 2λ axial × 6λ lateral. Stable Nakagami fitting needs **≥ ~100 independent samples**.
In a 10 × 10 mm ROI:

| Probe / setting | Speckle cell | Cells in ROI | Verdict |
|---|---|---|---|
| **12L-RS @ 13 MHz** | 0.17 mm² | **~594** | Ample |
| 12L-RS @ 5 MHz | 1.14 mm² | ~88 | **Inadequate** |
| C1-6 @ 6 MHz | 0.79 mm² | ~126 | Marginal |
| 3S-RS @ 4 MHz | 1.78 mm² | ~56 | **Inadequate** |
| 3S-RS @ 1.5 MHz | 12.65 mm² | ~8 | **Hopeless** |

**This is a protocol-level exclusion, derived from first principles for this specific hardware.**
The 5 MHz survey preset yields only ~88 cells — survey images are therefore usable for thickness and
anatomy **only**, never for envelope statistics. This trap was caught during design; do not
re-open it.

### 4.2 The abdominal control must also be 12L-RS

Measuring limb sparkle on a linear probe and trunk "control" sparkle on a curvilinear would confound
the primary comparison with probe geometry and destroy the entire gain-artefact defence. The
abdominal characterisation view is a **12L-RS acquisition on the same preset as the limbs**.

---

## 5. The acquisition standard — the thing the investigator actually asked for

> *"Remember I am looking for standardized research ultrasound settings for quantitating and doing
> AI machine learning analysis on skin fat."*

Core requirements, all in `lipoedema-ultrasound-ml-protocol.md` §4:

- **Locked settings table** — frequency, depth, focus, gain, TGC detents, dynamic range, grey map.
- **Speckle reduction (SRI) OFF · spatial compounding (CrossXBeam/CRI) OFF.** Both destroy exactly
  the envelope statistics being measured.
- **Reference-phantom method** for machine independence and cross-console comparability.
- **The magnification trap (§4.5):** texture descriptors are *pixel-scale dependent*. Images must be
  resampled to a common mm/pixel before any texture feature is computed, or magnification alone
  produces a spurious group difference.
- **Log-compression inversion:** envelope statistics are recoverable from B-mode **only** if dynamic
  range and grey map are locked and characterised.
- TruScan raw data is a proprietary re-processing archive — **not** calibrated RF. Do not treat it
  as RF.

### 5.1 The gain confound, and the defence against it

The obvious objection to any brightness-derived measure is that gain settings drive it. The defence
is **within-subject**: affected-site fat and spared trunk fat are acquired **in the same patient, in
the same session, on the same machine, at identical locked settings**, so any residual console drift
is common to both and cancels in the contrast.

### 5.2 Why the control site is the upper abdomen

Investigator's proposal, adopted: **umbilicus to xiphisternum**. Upper abdominal fat is typically
spared in lipoedema. The lower abdomen (S4b) is retained but **demoted** — informative about
distribution, explicitly *not* the control, and must never be substituted for S4a.

---

## 6. Design as it now stands

- **Prospective, two-arm, case–control discovery study.**
- **100 participants: 50 lipoedema, 50 individually BMI- and age-matched controls.**
- **The analysis unit is the participant, never the image** — several hundred images per person.
- Labels assigned by a single expert clinician **before imaging and database-locked**.
- **Second independent clinician** classifies from standardised photographs (AP, lateral, posterior;
  shorts, abdomen/legs/arms exposed) → an agreement statistic. Gwet's AC1 alongside Cohen's κ and
  PABAK, because κ is prevalence-sensitive.
- ML on **de-identified images only, on an air-gapped local workstation**.
- Training scheme per the investigator: 70% train / 30% test, human adjudication of performance,
  retrain and optimise, then a **new** cohort to test the optimised weights.

### 6.1 THE PRIMARY TEST — the single most load-bearing point in the protocol

> **The primary test is the arm × site interaction. It is NOT the within-Arm-A paired contrast.**

Each participant contributes a within-participant contrast: affected limb site versus their own upper
abdominal fat. The hypothesis is that **this contrast is larger in lipoedema than in matched
controls** — the *difference of differences*.

**Why this matters and why it keeps getting lost.** Limb and abdominal subcutaneous fat differ
anatomically **in everyone** — different depth, different attenuation path, different septal
architecture, different position relative to the probe's fixed elevational focus, different curvature
and coupling. A non-zero within-participant limb-versus-abdomen contrast is therefore *expected in
controls too*, and on its own demonstrates nothing.

Modelled as **mixed effects with participant as a random effect**.

This correction was made late (commit `997ee5f`) and stale "within-participant is primary" phrasing
had to be chased through four documents afterwards. **If you edit these documents, check this
statement has not regressed.**

### 6.2 Multiplicity and power

- **Five co-primary metrics** pre-specified: bright-spot density, Nakagami *m*, homodyned-K *k*,
  echo-free space fraction, high-percentile-to-median intensity ratio. **Bonferroni → α = 0.01
  two-sided.** Everything else is exploratory with FDR control and labelled hypothesis-generating.
- **Draft power (paired-contrast approximation):** n = 50 detects *d_z* = 0.55 at 90% power,
  α = 0.01. The clinical description implies an effect well above 0.8.
  **This is an approximation to the interaction actually specified, and the interaction costs more.**
- **Between-arm discrimination:** ≥ 98% power to establish that discrimination *exists* at true
  AUC ≥ 0.70, but the estimate carries roughly **± 0.09**. The study answers *whether* a signature
  exists, not *how strong* it is. It is framed as discovery-scale and says so.
- **No held-out test set is taken from the 100.** A 15-per-class test gives an interval near
  **± 0.16** — uninformative — and costs 30% of development data. Independent validation is a
  separate planned phase.
- **Adaptive recruitment:** **blinded** sample size re-estimation at n = 60, pre-specified maximum
  200, plus a futility rule. Blinded re-estimation costs **zero α** — this is what lets the
  investigator "increase the numbers as we go if power is not met at 100" without penalty.
- Nested cross-validation; patient-level splitting; multiple-instance learning for the
  many-images-one-label structure.

---

## 7. The histology requirement — the most serious defect caught in audit

**Routine liposuction aspirate cannot support the histological hypothesis.** Three independent
reasons:

1. **Tumescent infiltration destroys one of the endpoints outright.** Interstitial fluid is one of
   the four histological variables H3 correlates against — and tumescent fluid *is* injected
   interstitial fluid.
2. **Aspirate is emulsified and pooled.** Septal thickness, lobule size and architectural
   organisation are mechanically destroyed by cannula work.
3. **Co-registration is lost.** There is no way to tie aspirate back to the imaged ROI.

**Requirement (§6.4A):** an **intact, oriented skin-and-subcutaneous-fat core or excision, taken
from the ultrasound-marked ROI, at the start of the case, BEFORE tumescent infiltration and before
any cannula pass** — orientation-sutured and fixed intact.

Without this the histology sub-study is void. This is a requirement, not a detail.

---

## 8. Statistician involvement

The investigator has an independent university statistician. The position taken — and it is the
right one — is that this **strengthens** the study, and the approach is early, honest and
non-defensive: the letter states plainly that the draft calculations are *"a starting point, not a
position"*, and that **where the statistician disagrees, their judgement governs**.

Six itemised tasks. **Task 4 — hold the blind and perform blinded re-estimation at n = 60 — is
flagged as the one only they can do**, because it requires someone who is neither the investigator
nor the analysis team.

Declared soft spots, listed rather than hidden:

- H1 power assumes a paired *t*-test; the real analysis is a mixed-effects interaction whose power
  depends on a within-participant ICC **unknown until the pilot**.
- The model-vs-baseline AUC comparison needs a **DeLong**-based calculation that **has not been
  done**.
- Distributional form is unknown — Nakagami *m* is bounded and right-skewed, bright-spot density is
  a count — so transformation or a GLMM may be needed, changing the scale power was computed on.
- Bonferroni across five correlated metrics is likely over-conservative.

Two commitments made explicitly in the letter: **publication irrespective of outcome including a
null result**, and **the analysis plan deposited before recruitment**.

---

## 9. File map

| File | What it is |
|---|---|
| `evidence-reviews/lipoedema-ultrasound-ml-IRB-protocol.md` | **The main deliverable.** ~45pp, 17 sections: intro/background, objectives, design, participants, reference standard, procedures, data management, statistics and power, absence of harm, consent form, ethics, expected outcomes, significance, declared limitations, statistician handover brief, timeline, appendices |
| `evidence-reviews/lipoedema-ultrasound-ml-protocol.md` | Technical acquisition standard, ~23pp. The settings lock, the physics, the probe assignment, the speckle-cell arithmetic |
| `evidence-reviews/lipoedema-ultrasound-ml.md` | Evidence review, ~17pp. Establishes the gap; contains the Iker and elastography corrections and the Bayes arithmetic |
| `evidence-reviews/statistician-onboarding-letter.md` | Sendable invitation template, ~5pp |
| `standards/imaging_ml_evidence.yaml` | v1.1.0 machine-readable appraisal standard for diagnostic-imaging ML claims. Extends AMIS Standards 2 and 3 |
| `deliverables/` | PDF + Word of all four documents, plus `print.css` and `Sparkle-Study-power-calculations.py` |
| `make-deliverables.sh` | Regenerates every deliverable. **Markdown is the single source of truth** — never hand-edit a PDF or docx |

### 9.1 Why `imaging_ml_evidence.yaml` exists

Source tiering does not catch how diagnostic-model claims fail — a weak ML paper and a strong one
share a journal tier. The standard adds: claim types (**segmentation ≠ diagnosis**), validation-design
confidence ceilings, eight required disclosures each with its failure mode, interpretation rules
(**AUC 0.70–0.80 is adjunctive**; sensitivity is never reported without paired specificity; registry
entries are not results), absence-of-evidence warrant requirements, and harm triggers.

---

## 10. Open placeholders — all `[bracketed]` fields need the investigator

- PI name, degrees, title, department, institution, contact details
- IRB name and reference number
- **Appendix A — the clinical criterion set.** Load-bearing: it **must contain no ultrasound-derived
  criterion**, or the study is circular
- Appendix C — numeric phantom tolerances
- Contact-force acceptance window
- Reimbursement, funding, investigator financial interests
- Statistician name and department; time commitment and funding line

---

## 11. Standing working notes

- **Regenerate deliverables after any markdown edit** — `./make-deliverables.sh`.
- **The PR body goes stale.** It has repeatedly drifted from the documents, and once was
  *substantively wrong* about the study design (said "within-participant" after the interaction
  correction). Re-read it whenever a commit lands.
- Toolchain: `pypandoc-binary` (pandoc 3.9) → docx and HTML; Chromium headless `--print-to-pdf` with
  custom print CSS → PDF. LaTeX is unavailable and LibreOffice cannot open pandoc's docx in this
  environment; `pypdf` is broken (missing `_cffi_backend`), so PDFs are verified by structure, page
  count and EOF marker.
- A multi-agent audit of the protocol **failed procedurally** — every agent hit its retry cap without
  reading the file, and the synthesis was written blind. Its findings were re-verified by hand; two
  were real (the histology specimen defect, a stale arm reference) and were fixed. Do not treat that
  audit as evidence of anything.
