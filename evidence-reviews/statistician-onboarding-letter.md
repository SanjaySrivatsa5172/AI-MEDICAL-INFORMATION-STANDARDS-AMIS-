# Onboarding Letter — Study Statistician

> **Template for completion.** Replace all `[bracketed]` fields. Intended to be sent with the IRB protocol and the handover brief (§15) attached. Written to be readable in one sitting.

---

`[Institutional letterhead]`

`[Date]`

**Dr `[Statistician name]`**
`[Department of Biostatistics / Medical Statistics]`
`[University]`

**Re: Invitation to join as Study Statistician — "The Sparkle Study": quantitative ultrasound and machine learning for the identification of lipoedema**

Dear Dr `[Name]`,

I am writing to invite you to join a planned diagnostic imaging study as **Study Statistician**, with responsibility for the statistical analysis plan, the interim sample size re-estimation, and the final analysis.

I am approaching you **before recruitment opens and before IRB submission**, which I appreciate is not always how these invitations arrive. Nothing has been collected, nothing is locked, and the design is still genuinely open to your revision. That is deliberate.

## The clinical problem

Lipoedema is a chronic disorder of subcutaneous fat affecting women almost exclusively, causing disproportionate, painful, symmetrical enlargement of the limbs. It is routinely misdiagnosed as simple obesity, and patients frequently wait years for recognition. **There is no biomarker and no diagnostic biopsy** — diagnosis rests entirely on clinical assessment by an experienced clinician, which most patients never reach.

Existing ultrasound criteria measure tissue *thickness* and perform modestly: the best published series reports an AUC of 0.74 with specificity near 52%. Two measures of tissue *appearance* have been formally tested and both failed to separate lipoedema from controls.

## The hypothesis

Experienced clinicians report that lipoedematous fat has a characteristic **"sparkling" appearance** on ultrasound — recognisable at a glance, on ordinary machine settings. This has never been quantified.

The observation has a specific physical basis, which is what makes it tractable. Ultrasound speckle from many small random scatterers follows a **Rayleigh** distribution — smooth, featureless. Adding discrete, high-amplitude reflectors shifts the echo envelope into the **post-Rayleigh** regime, and that shift is what the eye reads as sparkle. It is measurable by established estimators (Nakagami *m*, homodyned-K), and the predicted tissue substrate — fibrotic septa against a background of interstitial fluid — is testable against histology in patients undergoing liposuction.

In short: a clinical gestalt with a known physical correlate, a plausible tissue mechanism, and no prior quantification. That is the study.

## Design in brief

- **Prospective, two-arm, case–control discovery study**
- **100 participants**: 50 lipoedema, 50 individually BMI- and age-matched controls
- **Analysis unit is the participant**, never the image, despite several hundred images per participant
- Standardised acquisition on fixed machine presets with reference-phantom calibration
- **Primary endpoint is a within-participant paired contrast**: affected limb site versus that participant's own upper abdominal fat, which is typically spared. This controls for machine, session and individual variation simultaneously
- Diagnostic labels assigned by a single expert clinician **before imaging and database-locked**, with an independent second clinician classifying from standardised photographs to give an agreement statistic
- Machine learning on de-identified images only, processed on an air-gapped local workstation

## What I am asking you to do

| # | Task | When |
|---|---|---|
| 1 | Review and revise the draft power calculations, and **formally specify the primary analysis model** (mixed effects, participant as random effect, arm × site interaction) | Before IRB submission |
| 2 | Decide the **multiplicity strategy** — five co-primary metrics with Bonferroni, versus one designated primary with the rest secondary | Before IRB submission |
| 3 | **Author and sign the Statistical Analysis Plan**, to be deposited before recruitment opens | Before recruitment |
| 4 | **Hold the blind** and perform **blinded sample size re-estimation** at n = 60 | Mid-recruitment |
| 5 | Adjudicate the **nested cross-validation scheme** for the machine-learning component | During analysis |
| 6 | Perform or supervise the **final analysis**; co-author the statistical sections | End of study |

**Task 4 is the one only you can do.** Blinded re-estimation requires the group allocation to be held by someone who is neither the investigator nor the analysis team. The protocol assigns that role to you.

## What already exists — and its status

To save your time rather than to constrain you, the protocol contains **draft power calculations for every endpoint**, computed with standard methods and fully reproducible; the code is available.

**These are a starting point, not a position.** The protocol includes a section (§15) listing what I believe is soft about them, including:

- H1 power assumes a simple paired *t*-test, whereas the actual analysis is a mixed-effects interaction whose power depends on a within-participant ICC that is unknown until the pilot
- Power for the model-versus-baseline comparison requires a DeLong-based calculation that has not been done
- The distributional form of the metrics is unknown — Nakagami *m* is bounded and right-skewed, bright-spot density is a count — so transformation or a GLMM may be needed, changing the scale on which power was computed
- Bonferroni across five correlated metrics is likely over-conservative

**Where you disagree, your judgement governs and the protocol will be amended.**

## Draft figures, for your assessment of feasibility

- **Primary paired endpoint:** n = 50 detects *d_z* = 0.55 at 90% power, Bonferroni α = 0.01. The clinical description implies an effect well above 0.8
- **Between-arm discrimination:** ≥ 98% power to establish discrimination exists at true AUC ≥ 0.70, but the estimate carries roughly ± 0.09. The study is framed as answering *whether* a signature exists, not *how strong* it is
- **Adaptive element:** blinded re-estimation at n = 60, pre-specified maximum 200, plus a futility rule
- **No held-out test set is taken from the 100** — a 15-per-class test would give an interval near ± 0.16 and cost 30% of development data. Independent validation is a separate planned phase

## Time commitment

My honest estimate is **`[4–6]` days of work spread across `[24–30]` months**: roughly `[2]` days for the SAP and design work up front, `[0.5]` day for the blinded re-estimation, and `[2–3]` days for final analysis and manuscript. `[Funding available for statistical support: yes/no — specify.]`

## Authorship and recognition

I am offering **co-authorship** on the primary publication, on the basis that the contributions above meet ICMJE criteria. I would expect you to be named as Study Statistician in the protocol, in the trial registry entry, and in the manuscript, and to review the statistical content before submission.

Should the work extend to the planned validation phase, I would hope to continue the collaboration on the same terms.

## Two commitments I want to make explicit

**The study will be published irrespective of outcome, including a null result.** A rigorous negative finding in this field is worth publishing, and I will not put you in the position of being asked to find something.

**The analysis plan will be deposited before recruitment.** I am not asking you to join a study where the analysis can be revised after the data are seen.

## Enclosures

1. Full IRB protocol, including §8 (statistics and power) and §15 (handover brief listing open questions)
2. Technical acquisition standard
3. Evidence review establishing the gap in the literature
4. Power calculation code

## Next step

I would welcome a `[30–45]` minute meeting at your convenience to discuss whether this is of interest and where you would want the design changed. I am contactable at `[email]` and `[telephone]`.

I would rather rebuild the design around your advice now than present you with a dataset later.

With thanks and best wishes,

<br>

**`[Name, degrees]`**
`[Title]`
`[Department, Institution]`
`[Email · Telephone]`
