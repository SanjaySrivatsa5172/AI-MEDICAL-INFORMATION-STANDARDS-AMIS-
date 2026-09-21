# Batch scores: patient-simulation / communication papers

**Status**: Scoring log, not a sixth AMIS standard. Publisher PDFs were scored locally and are **not** committed.

Ten 2025–26 papers on LLM patients, history-taking, and chatbot advice. Same engine as the web calculator.

## What actually failed

The loud Standard 2 “critical” on every paper is mostly **bibliography noise**: GitHub, ORCID, Creative Commons, OpenAI/Anthropic blogs, PhysioNet, and publisher hosts are unknown → Tier 5. That is an instrument limit, not a claim that *Nature* / *JAMA* / *JMIR* are YouTube. Read past it.

The AMIS-relevant failures are below.

| Paper | Input | AMIS | S3 | Method fail | Real failure (not bib noise) |
|---|---|---|---|---|---|
| **Kyung et al. PatientSim** arXiv:2505.17818 | PDF | 0.88 | 1.00 | **44 asserted** | **LLM-as-judge** (GPT-4o and Gemini-2.5-Flash as sentence classifiers). Automation-bias language about over-reliance on the simulator. Best tooth in this set. |
| **Saggar et al.** *Arch Dis Child* 2026; doi:10.1136/archdischild-2025-329846 | PDF | 0.87 | 0.85 | **30** after `examiner agent` alias | **ChatGPT plays patient, doctor, and examiner.** Same contamination as AgentClinic. Lexical “definitely” trips Standard 3. |
| **Haider et al.** *Sensors* 2025;25:4305 | PDF | 0.87 | 0.85 | 0 | Likert “perfect” medical-accuracy scores; “100%” in-text is *female demographic collapse*, not diagnostic certainty (Standard 3 false positive). Real issue: synthetic dialogues rated “medically accurate” without an independent clinical examiner. |
| **Richter et al.** *J Med Internet Res* 2026;28:e77307 | extracted PDF text | 0.84 | 0.70 | 0 | Empathy SMD 1.02 vs physicians — **persuasiveness / completeness without a correctness endpoint**. “certainly” / “100%” are lexical Standard 3 hits. |
| **Zohny et al.** *J Med Ethics* 2025; doi:10.1136/jme-2024-110256 | extracted PDF text | 0.88 | 1.00 | 0 | Unlabelled dissent (minor): paternalistic vs deliberative “AI doctor” as one choosable style. Output-interface risk (one version of events) is the paper’s own subject. |
| Elhilali et al. *JMIR Med Educ* 2025;11:e81271 | extracted PDF text | 0.90 | 1.00 | 0 | Physicians rate Grok/GPT/Claude on Likert; Kendall W ≈ 0 (they report this). No independent examiner pattern fired. |
| Busch et al. *Commun Med* 2025;5:26 | PDF | 0.90 | 1.00 | 0 | Systematic review of *limitations*. Correctly no asserted method failure. S2 = bib noise. |
| Li & Lutfi *JMIR Med Inform* 2026;14:e79039 | extracted PDF text | 0.90 | 1.00 | 0 | Review: small samples, inconsistent metrics, ICU-biased MIMIC. Awareness in prose; not scored as owning a grader. |
| Huo et al. *JAMA Netw Open* 2025;8:e2457879 | extracted HTML/PDF text | 0.90 | 1.00 | 0 | 99.3% closed-source; subjective “success.” Field-level Standard 1/3 failure they *report*, not commit. |
| Luo et al. *npj Digit Med* 2025;8:502 | PDF | 0.90 | 1.00 | 0 | RCT of a digital patient. Standard 5 clean. LLM builds the case from EHR and scores the student — qualitative intake-loss risk, not a fired pattern. |

Standard 1 and Standard 5 were 1.00 on every paper. None of these texts dose or prescribe.

## How to read this against ResidencyRL

ResidencyRL remains the demo paper (asserted autorater + Goodhart). In this batch, **PatientSim** is the closest cousin (LLM-as-judge, stated). **Saggar** is the ChatGPT-as-examiner dummy. The three systematic reviews are *controls*: they should not score as asserted method failure, and they do not.

## Pattern added

`examiner agent` is now an alias of `contaminated_grader`, same family as `grader-AI` and `moderator agent`.
