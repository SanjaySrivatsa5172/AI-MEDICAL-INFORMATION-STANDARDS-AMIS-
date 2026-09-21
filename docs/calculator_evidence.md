# Evidence base for the AMIS Claim Calculator

**Status**: Methods appendix for academic review  
**Calculator version**: 1.0.0 (AMIS specification 1.0.0)  
**Last updated**: 2026-09-21

This note states *why* the five AMIS standards exist, what empirical literature warrants each
score the calculator reports, and which newer criteria we **discuss but do not silently add**
as a sixth standard. The calculator is an inspectable heuristic instrument. It is **not** a
psychometrically validated scale, a systematic review, or a substitute for clinician appraisal.

---

## 1. How the five AMIS criteria were chosen

AMIS was written for a specific failure class: **AI-generated medical information**
(chat summaries, LLM answers, paper claims about clinical AI) whose apparent confidence
outruns its warrant. The five standards are constitutive, not a convenience sample.
They come from three sources, in order:

1. **Documented output failures** — the January 2026 *Guardian* investigation of AI health
   summaries (YouTube outranking journals; decontextualised laboratory ranges; dietary advice
   opposite to oncology guidance). These map one-to-one onto Standards 2, 3, and 5.
2. **Evidence-based medicine infrastructure that already exists** — GRADE, Cochrane, NICE/WHO
   guideline methodology, and the EQUATOR reporting family. AMIS does not invent a new
   evidence pyramid; it requires AI systems to *use* the one medicine already agreed.
3. **Empirical work on automation bias and productive uncertainty** — including the owner’s
   JVS–Vascular Insights analysis and the independent literature it cites.

| AMIS standard | Construct | Primary warrant | What the calculator measures |
|---|---|---|---|
| 1 Literature review paradigm | Evidence must be appraised, not popularity-ranked | Cochrane Handbook; GRADE; AMIS spec §3 | Presence of graded sources and appraisal language |
| 2 Source quality hierarchy | Five-tier source classification; Tier 5 excluded | GRADE / guideline bodies; *Guardian* YouTube finding | URL/DOI/named-source tier via `SourceClassifier` |
| 3 Mandatory uncertainty disclosure | Confidence ≤ epistemic warrant | Simpkin & Schwartzstein 2016; Croskerry 2003; Guo et al. calibration | Overconfident vs qualified language; Standard 3 score |
| 4 Dissent labelling without false certainty | No dogma and no false equivalence | AMIS spec §6; history of reversed consensus | Dogmatic phrasing; labelled vs unlabelled controversy |
| 5 Therapeutic advice requires a physician | AI informs; physicians prescribe | Medical practice acts; FDA CDS distinction; AMIS spec §7 | Dosing / implementation language; physician-referral |

The two owner-requested **axes** are aggregates, not new standards:

- **Uncertainty vs certainty** = Standard 3 + Standard 4 + humility/overconfidence markers
  from `standards/uncertainty_calibration.yaml`.
- **Methodological failure** = evaluation integrity (who graded the claim, whether the grader
  trained the system, Goodhart risk, shortcut learning, fabricated reasoning). This is the
  one net-new *primitive*. It does not fork the AMIS YAML schema.

---

## 2. Objective evidence, by construct

### 2.1 Uncertainty, calibration, automation bias

- Simpkin AL, Schwartzstein RM. Toleration of uncertainty: the next medical revolution?
  *N Engl J Med.* 2016;375:1713-1715.
- Croskerry P. The importance of cognitive errors in diagnosis and strategies to minimize them.
  *Acad Med.* 2003;78:775-780.
- Goddard K, Roudsari A, Wyatt JC. Automation bias: a systematic review.
  *J Am Med Inform Assoc.* 2012;19:121-127.
- Parasuraman R, Manzey DH. Complacency and bias in human use of automation.
  *Hum Factors.* 2010;52:381-410.
- Guo C, Pleiss G, Sun Y, Weinberger KQ. On calibration of modern neural networks.
  *Proc ICML.* 2017.
- Yang A, Ghassemi M, Doshi-Velez F. The effect of AI explanations on medical diagnostic
  decisions. arXiv:2101.07769.
- Jabbour S, et al. Measuring the impact of AI in the diagnosis of hospitalized patients.
  *JAMA.* 2023;330:2275-2284. (Explanation did not repair accuracy loss from biased AI.)
- Srivatsa SS. The epistemic risk of AI over-reliance in clinical medicine: why productive
  uncertainty matters. *JVS Vasc Insights.* 2026;4:100492.

### 2.2 Source hierarchy and appraisal

- Guyatt G, et al. GRADE: an emerging consensus on rating quality of evidence.
  *BMJ.* 2008;336:924-926.
- Higgins JPT, Thomas J, eds. *Cochrane Handbook for Systematic Reviews of Interventions.*
- National Institute for Health and Care Excellence. *Developing NICE guidelines: the manual.*

### 2.3 Methodological failure (evaluation contamination)

These are the constructs Sanjay’s ResidencyRL letter asked the calculator to score explicitly.
They are not AMIS inventions; they are named in the target paper and in the judge-bias literature.

- **Goodhart’s law** — when a measure becomes a target, it ceases to be a good measure.
  Liévin et al. state that in-domain results “primarily validate that the agent successfully
  learns to optimize its training signals.” That is the authors’ own Goodhart disclosure.
- **LLM judges prefer their own lineage** — Panickssery A, Bowman SR, Feng S. LLM evaluators
  recognize and favor their own generations. arXiv:2404.13076. 2024.
- **Persuasiveness ≠ correctness** — Wen J, et al. Language models learn to mislead humans
  via RLHF. arXiv:2409.12822. 2024. Physician preference for completeness is not diagnostic
  gain (Liévin et al., 90.7% completeness preference; no independent accuracy delta on that
  comparison).
- **Shortcut learning / fabricated rationale** — Geirhos R, et al. Shortcut learning in
  deep neural networks. *Nat Mach Intell.* 2020;2:665-673. Gu Y, et al. The illusion of
  readiness: stress testing large frontier models on multimodal medical benchmarks.
  arXiv:2509.18234. 2025.
- **Deskilling after routine AI exposure** — Budzyń K, et al. Endoscopist deskilling risk
  after exposure to artificial intelligence in colonoscopy. *Lancet Gastroenterol Hepatol.*
  2025;10:896-903.
- **Independent examiner** — ACGME milestones and board certification exist precisely so
  the teacher is not the sole summative examiner. The calculator treats an in-family
  autorater as the computational analogue of that structural failure.
- **Conversational evaluation still needs an independent examiner** — Johri et al.
  (CRAFT-MD, *Nat Med* 2025;31:77–86; doi:10.1038/s41591-024-03328-5) replace static
  vignettes with multi-turn dialogue and show every tested model drops; their grader-AI
  plus patient-AI is the same contamination class as an autorater, even when experts
  later audit a sample. Schmidgall et al. (AgentClinic, *npj Digit Med* 2026;9:499;
  doi:10.1038/s41746-026-02674-7; PMID 42045532) show MedQA-in-dialogue can fall to
  about one-tenth of static accuracy and use an LLM moderator (an LLM judge) to score
  the doctor agent. The *slide* (vignette → conversation; static QA → tool-use
  dialogue) is what the papers measure. The *tooth* is that the examiner is still in
  the same agent family. No sixth AMIS standard is added; `grader-AI` and
  `moderator agent` are aliases of the existing contaminated-grader pattern.

### 2.4 Therapeutic scope

- U.S. Food and Drug Administration. Clinical Decision Support Software guidance.
- AMIS Standard 5 is a *constitutive* boundary: the calculator itself issues no dose,
  no start/stop, and no “you should take.”

---

## 3. Newer criteria in the literature — discuss, then (selectively) incorporate

A reviewer will ask why AMIS is not simply TRIPOD-LLM. The honest answer: **different object.**

| Instrument | Object | Year | Relationship to AMIS |
|---|---|---|---|
| TRIPOD+AI | Prediction-model *reporting* | 2024 (*BMJ*) | Complementary. Use when the artefact is a prognostic/diagnostic model paper. |
| TRIPOD-LLM | Healthcare LLM *reporting* (19 items) | 2025 (*Nat Med*) | Closest cousin. Human oversight, assessor procedure, and task-specific metrics map onto our methodological-failure axis. |
| STARD-AI | AI diagnostic-accuracy *reporting* | 2025 (*Nat Med*) | Use for diagnostic accuracy studies. Risk-of-bias / index-test independence ≈ contaminated grader. |
| CONSORT-AI / SPIRIT-AI | Trials of AI interventions | 2020; use with CONSORT 2025 | Required if anyone claims clinical utility in patients. ResidencyRL correctly says prospective validation remains necessary. |
| DECIDE-AI | Early live clinical evaluation | 2022 (*Nat Med*) | Next step after simulation. Not yet applicable to ResidencyRL. |
| FUTURE-AI | Lifecycle trustworthiness (fairness, robustness, …) | 2024+ | Broader than AMIS. We do **not** collapse fairness/robustness into a sixth AMIS number. |

**Incorporated now (axis, not a sixth standard):** independent examiner, in-family LLM judge,
Goodhart/in-domain reward, persuasiveness without correctness, shortcut / fabricated reasoning.
These are the TRIPOD-LLM / STARD-AI assessment-integrity items that AMIS was missing as an
explicit score.

**Not incorporated as new AMIS standards** (needs owner sign-off and a spec revision):

- Fairness / subgroup calibration (FUTURE-AI, TRIPOD-LLM).
- Dataset leakage / train–test contamination beyond grader contamination.
- Environmental / compute reporting.
- Patient-reported outcome endpoints.

If those are added later, they should land in `SPECIFICATION.md` first, then in code.

---

## 4. What a ResidencyRL score is allowed to mean

A high methodological-failure score on Liévin et al. means: the paper *describes and uses*
an autorater from the same model family as the policy and the patient simulator, reports
in-domain gains on the training rubric, and treats clinician preference as validation.
It does **not** mean the work is without value, that out-of-domain benchmarks are false,
or that the calculator has “refuted” the paper. The authors already wrote the Goodhart
sentence. AMIS makes that sentence numerically visible.

### 4.1 What a CRAFT-MD or AgentClinic score is allowed to mean

These two papers are *tooth* fixtures: they are the runnable process (CRAFT-MD) and
tool-use (AgentClinic) analogues of ResidencyRL’s contaminated examiner.

| Paper | What they showed (the slide) | What AMIS flags (the tooth) |
|---|---|---|
| Johri et al., CRAFT-MD, *Nat Med* 2025 | Every model drops from vignette → conversation; o1-preview leads multi-turn FRQ on the public leaderboard. Code: `github.com/rajpurkarlab/craft-md`. | Asserted **grader-AI** + **patient-AI**. Expert audit of the grader is awareness, not independence of the examiner. |
| Schmidgall et al., AgentClinic, *npj Digit Med* 2026 | MedQA-in-dialogue can fall to ~1/10 of static accuracy; Claude 3.5 best backbone; Llama-3 + notebook tool +92% relative. Code (MIT): `github.com/SamuelSchmidgall/AgentClinic`. | Asserted **moderator agent** / **LLM judge**, with GPT-4 as the patient for consistency. The authors’ own limitation paragraph is awareness credit. |

A high methodological-failure score here means the paper *uses* a language-model
examiner (grader-AI or moderator) to score the system under test. It does **not**
mean the vignette→conversation drop is false, that Claude 3.5 is not the strongest
backbone they measured, or that conversational benchmarks should be abandoned.
The drop is why static USMLE-style numbers cannot be believed at face value. The
grader is why the conversational number still needs an examiner who did not play
the patient.

Do not commit the publisher PDFs. Score the public excerpts in
`examples/calculator/craftmd_excerpt.txt` and `agentclinic_excerpt.txt`.

**Standard 2 bibliography noise (not a YouTube-tier failure).** Full-text PDFs
and author lines routinely contain GitHub, ORCID, Hugging Face, Zenodo, and
similar hosts. Those URLs are **Tier 4 reproducibility / identity hosts**: they
are not medical evidence (they cannot raise Standard 2) and they are **not**
Tier 5 excluded platforms. YouTube, TikTok, and social media remain the
YouTube-class failures. A *Nature* / *npj* article stays Tier 2 via DOI
`10.1038/` even when the bibliography also lists `github.com/…` or
`huggingface.co/…`. The calculator surfaces this as a source note so a reviewer
does not read a GitHub link as a Standard 2 critical hit.

The calculator must remain conservative about source tiers: conference PDFs (NeurIPS,
OpenReview) are Tier 4, not Tier 5. A DOI is not “unknown social media.” arXiv remains
Tier 4 (preprint), including `10.48550/arXiv…`.

---

## 5. Limitations of the instrument (state these in any letter)

- Deterministic lexical patterns, not an LLM judge (by design: the judge must not grade itself).
- English-centric.
- Abstracts without a reference list will fail Standard 1 even when the full paper would pass.
- Bibliography hosts (GitHub, ORCID, Hugging Face) are Tier 4 noise, not Tier 5. Reviewers
  should not treat those links as YouTube-class Standard 2 failures.
- “100%” inside a methods table can trip Standard 3; reviewers should read the violation, not
  only the headline number.
- No claim of inter-rater reliability against a human AMIS panel has been published yet.

---

*Maintainer: S. Sanjay Srivatsa, MD. License: CC BY 4.0 for the standards; MIT for the code.*
