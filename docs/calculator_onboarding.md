# AMIS Claim Calculator — onboarding

**Public scorer:** https://amis-claim-calculator.onrender.com  
**Onboarding (this page on the host):** https://amis-claim-calculator.onrender.com/onboarding  
**Source:** https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-

Maintainer: S. Sanjay Srivatsa, MD · Heart Artery and Vein Center, Fresno  
Instrument version: AMIS 1.0.0

This note tells a reader how to run the calculator and how to read a score. It is not a
second standards document. The specification remains `SPECIFICATION.md`. The methods
appendix remains `docs/calculator_evidence.md`.

---

## 1. What this instrument is

Paste an abstract or upload a PDF / text file. The calculator extracts AI-related medical
claims and returns:

1. **Five AMIS standards** (0–1 each, then a mean)
2. **Uncertainty calibration vs certainty excess**
3. **Methodological failure vs methodological awareness** (who graded the claim)

It is a deterministic heuristic. It is not a licensed psychometric scale, a systematic
review, or a diagnosis. It does **not** prescribe treatment (AMIS Standard 5).

---

## 2. First use (phone or desktop)

Open https://amis-claim-calculator.onrender.com

The top **Access** bar has two tabs: **Calculator** (the scorer) and **Onboarding** (this
guide). Use those tabs to move between them.

### Fastest path — load an example

1. Stay on **Calculator**.
2. Tap **CRAFT-MD — grader-AI + vignette drop** (first example).
3. Tap **Score claims**.
4. Scroll the result: five standards, two axes, per-claim findings.

Expected CRAFT-MD excerpt: five standards at 1.00 (full AMIS conformance) and
methodological failure about 30 because the paper *asserts* a grader-AI. That pairing is
correct. AMIS can be 1.00 while the method axis still flags a contaminated examiner.

### Paste text

1. Paste an abstract, letter, or excerpt into the box.
2. Tap **Score claims**.

### Upload a PDF (including iPhone)

1. Use the system **Choose File** control — not a hidden custom button.
2. Confirm the filename appears (not “No file selected”).
3. Tap **Score claims**.
4. Wait on **Reading PDF…** The free host may take 10–25 seconds, especially after sleep.

Do not add an `accept` filter in a fork if you care about iOS: Mobile Safari has treated
that as a pattern mismatch and blocked Score claims.

---

## 3. Free-host limits (read these before a publisher PDF)

The public Render instance is a free Python service.

| Limit | What you will see |
|---|---|
| First 16 pages / 80,000 characters | `pdf · 80000 characters` |
| At most 8 scored AI claims | `8 AI claims` even if the paper has more |
| Idle sleep (~15 minutes) | First request after sleep is slow |
| Client abort at 28 seconds | Error: try Score claims again, or use the excerpt |

A full publisher PDF and the built-in excerpt are **different documents**. The excerpt is
the clean fixture. The PDF includes methods, tables, and bibliography, then is cut at the
cap. A drop from 1.00 on the excerpt to ~0.85 / `conformance none` on the PDF usually
means a **critical** validator hit in that capped text, not that the site failed.

Do not commit publisher PDFs to the repository.

---

## 4. How to read a score

### Overall number (the dial)

The large number is the **five-standard mean × 100**. It is not an average of the two
axes.

**Conformance** is stricter than the mean:

| Conformance | Rule of thumb |
|---|---|
| `full` | Mean ≥ 0.9 and no major/critical violations |
| `substantial` | Mean ≥ 0.7, no critical, no major |
| `partial` | Major violation or mean 0.5–0.7 |
| `none` | **Critical** violation **or** mean < 0.5 |

`compliant=true` only for substantial or full, and only when harm is not high. A paper
can show **85** and still be `none / compliant=false` if one critical violation fired.

### Five AMIS standards (0–1)

| # | Standard | What a high score means |
|---|---|---|
| 1 | Literature review paradigm | Appraisal language and graded evidence, not popularity ranking |
| 2 | Source quality hierarchy | Peer-reviewed / guideline sources; Tier 5 (YouTube, TikTok, social) excluded |
| 3 | Mandatory uncertainty disclosure | Confidence does not outrun warrant |
| 4 | Dissent labelling without false certainty | Controversy labelled; no dogma |
| 5 | Therapeutic advice requires a physician | No dosing / implementation as if the model were the prescriber |

### Two axes (not a sixth standard)

- **Uncertainty calibration (high is better)** vs **certainty excess** (the inverse).
- **Methodological failure (high = worse examiner integrity)** vs **methodological awareness**
  (the paper *labels* the failure as a risk).

Methodological failure looks for contaminated or in-family graders (grader-AI, autorater,
moderator agent, LLM judge), Goodhart gaming, shortcut learning, and fabricated reasoning.
**Asserted** means the paper owns that method. **Critiqued** means it is discussed as a
risk rather than used as the result.

TRIPOD-LLM, STARD-AI, CONSORT-AI, and DECIDE-AI remain the correct *reporting* instruments.
AMIS does not silently add them as Standard 6.

### Per-claim chips

Only AI performance, safety, diagnostic/therapeutic, and evaluation sentences are
extracted — not every sentence. A claim can be AMIS 1.00 and still show
`Contaminated or in-family grader · asserted`.

### Source tiers

Nature / *npj* / DOI `10.1038/` stay **Tier 2**. GitHub, ORCID, Hugging Face, and Zenodo
in a bibliography are **Tier 4 reproducibility hosts**, not YouTube-class Tier 5 failures.
arXiv is Tier 4 (preprint). YouTube / TikTok / social media still fail Standard 2.

---

## 5. Built-in examples

| Example | Why it is there |
|---|---|
| CRAFT-MD | Johri et al., *Nat Med* 2025 — grader-AI + vignette→conversation drop |
| AgentClinic | Schmidgall et al., *npj Digit Med* 2026 — LLM moderator + MedQA-in-dialogue drop |
| Srivatsa abstract | Gold-reference tone: productive uncertainty, no prescription |
| ResidencyRL letter | Contaminated grading named as critique (awareness > failure) |
| Overconfident AI claims | Synthetic fail case: false certainty, Tier 5, therapeutic dosing |

---

## 6. What a score is allowed to mean

A high methodological-failure score on CRAFT-MD or AgentClinic means the paper *uses* a
language-model examiner. It does **not** mean the vignette→conversation drop is false, or
that conversational benchmarks should be abandoned.

The same rule applies to ResidencyRL (arXiv:2608.07418): the autorater and in-domain
Goodhart sentence are made numerically visible. The calculator has not “refuted” the paper.

---

## 7. Citation

Cite the hosted scorer:

https://amis-claim-calculator.onrender.com

Cite the source repository:

https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-

Local run (same engine):

```bash
python3 -m pip install -r implementation/web/requirements.txt
python3 -m implementation.web.app
```

Then open http://127.0.0.1:8765 and http://127.0.0.1:8765/onboarding

See `docs/deploy.md` if the free instance is asleep or you are standing up a new host.

---

*License: CC BY 4.0 for the standards; MIT for the code.*
