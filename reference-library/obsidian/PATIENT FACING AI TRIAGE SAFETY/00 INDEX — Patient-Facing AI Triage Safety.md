---
title: "Patient-Facing AI Triage Safety — Reference Index"
last-updated: 2026-08-07
total-references: 135
tags: [reference-index, ai-triage-safety]
---

# Patient-Facing AI Triage Safety — Reference Index

Supporting the Cedars-Sinai protocol **Physician-Authored Evaluation of Patient-Facing Artificial Intelligence in Emergency Triage** (PI: S. Sanjay Srivatsa, MD).

> Core question: *Can AI systems safely recognize when symptoms described in everyday language require emergency care?*

Updated daily by automated scan. Last scan: **2026-08-07** · 135 references.

Live dashboard: https://claude.ai/code/artifact/528465e1-0a3b-40aa-81ab-00373aaa2461

> [!info] Generated folder
> This folder is regenerated on every scan. Keep personal annotations in separate notes that link here, not inside these files.

## 🚨 Active urgent alerts

- **2026-08-03 — Preprint challenges Ramaswamy ChatGPT Health undertriage finding: forced-choice exam format, not model capability, drives failure** — Fraile Navarro, Magrabi & Coiera (Macquarie University, arXiv 2603.11413) partially replicated the Nature Medicine ChatGPT Health stress test (Ramaswamy et al., the subject of this library's standing urgent alert) on 5 frontier LLMs (GPT-5.2, Claude Sonnet 4.6, Claude Opus 4.6, Gemini 3 Flash, Gemini 3.1 Pro) across 17 scenarios under two conditions: constrained exam-style forced-choice (A/B/C/D, 1,275 trials) vs naturalistic patient-style free-text messaging (850 trials). Naturalistic interaction improved triage accuracy by 6.4 percentage points (p=0.015); three models scored as low as 0-24% under forced choice but 100% on matched scenarios in free text. This directly bears on the primary endpoint's interpretation: it suggests undertriage/critical-miss rates measured under a forced-choice evaluation format may substantially overstate real-world model failure, and that naturalistic, everyday-language presentation format is itself a major determinant of triage accuracy -- the core dual-register design question this protocol is built around. TWO CAVEATS temper the critique (verified against the Ramaswamy full text): (1) MODEL CONFOUND -- Fraile Navarro tested newer, larger frontier models via API, whereas Ramaswamy tested the actual ChatGPT Health product (gpt-5-mini backbone), so the accuracy gain conflates evaluation format with model capability and is not a clean format-only comparison of the same system; (2) Ramaswamy pre-empted the objection, arguing vignettes are a CONSERVATIVE test because real consumers under-report symptoms and misapply advice, which would compound errors. The two critiques address different axes -- output format vs input quality -- and can both hold, leaving the net real-world effect unresolved. Not yet peer-reviewed (arXiv preprint). (https://arxiv.org/abs/2603.11413)
- **2026-08-05 — NOHARM benchmark (ARISE / Stanford & Harvard): physician-authored, harm-weighted evaluation finds up to 22.2% severe-harm potential across 31 LLMs -- closely matches this protocol's own evaluation architecture** — 'First, do NOHARM: towards clinically safe large language models' (Wu, Nateghi Haredasht, ... Goh; ARISE clinical-AI research network, Stanford & Harvard Medical School physicians; arXiv 2512.01241, posted Dec 2025, PMID 41532042) is a physician-authored, harm-weighted clinical-AI safety benchmark. Per the PubMed-indexed record: 100 real primary-care-to-specialist consultation cases across 10 specialties, with 12,747 expert annotations of 4,249 candidate management options by a 29-physician panel. Across 31 LLMs, direct application of AI-generated recommendations carried potential for SEVERE harm in up to 22.2% of cases (95% CI 21.6-22.8%), with errors of omission accounting for 76.6% of errors. Crucially, safety correlated only moderately (r=0.61-0.64) with existing accuracy/knowledge benchmarks -- a model can score well on standard evaluations yet be unsafe -- and the best models slightly exceeded generalist physicians on safety (+9.7%). RELEVANCE: NOHARM's architecture -- physician-authored clinical scenarios with expert-panel, action-level, harm-weighted scoring -- closely parallels this protocol's own physician-authored, harm-weighted evaluation methodology, and its central thesis (clinical safety is a distinct axis from accuracy, requiring explicit measurement) directly supports the protocol's rationale; recommend PI review of the NOHARM harm-scoring rubric for methodological cross-reference. CONTEXT/CAVEAT: the work reached the press only this week via a July 29 2026 Fortune report on an industry dispute (OpenEvidence vs Doximity Ask) over a later, expanded arXiv version that adds a randomized physician-AI teaming study and tests commercial RAG tools; widely-circulated news figures (e.g. '45 LLMs and 4 clinical AI systems', '24.6% severe harm', '>80% omission') come from that secondary coverage/expanded version and differ from the PubMed-indexed abstract cited above -- treat them as unverified pending the specific arXiv version. arXiv preprint (not peer-reviewed); does not resolve either standing alert. UPDATE 2026-08-05 (main session): RESOLVED CAVEAT -- the expanded arXiv version ('...a medical safety benchmark and randomized study of physician and AI teaming on clinical consultations') has now been verified directly from the PI-supplied full PDF: 45 LLMs evaluated (20 notable + 4 clinical RAG tools in primary analyses), severe-harm range 2.9-24.6%, omission >80% of severe errors, 101-physician randomized crossover (AI-assisted 47.3% vs 42.2% conventional; as-treated 52.0%), autograder kappa 0.804 vs inter-physician 0.784, severity weights 1:8:24, 'Do Nothing' floor 37%. Both versions' figures are citable with the version named. Methodological disposition (judging-architecture adoptions) documented in docs/cedars_ramaswamy_nm2026_redraft_plan.md Sec 2.7/3.5. (https://arxiv.org/abs/2512.01241)
- **2026-08-06 — New arXiv benchmark (Weilnhammer et al., Microsoft Research/Oxford) tests 15 frontier AI chatbots on one-shot emergency psychiatric triage -- closely parallels this protocol's critical-miss-rate design** — One-shot emergency psychiatric triage across 15 frontier AI chatbots (arXiv 2604.25415, posted 2026-04-28) tested 112 clinical vignettes as realistic single-message disclosures against a 4-level urgency benchmark (A routine / B within-1-week / C within-24-48h / D emergency-now) across 15 frontier chatbots. Emergency under-triage occurred in 5.6% (23/410) of level-D (emergency) trials -- every under-triaged case was reassigned to the next-lower urgency tier (C), a pattern structurally similar to the anchoring-toward-less-urgent-care finding in the standing Ramaswamy Nature Medicine alert. Overall accuracy ranged 42.0-71.8% across models and was lowest for level-B (routine-but-soon) vignettes (19.7%), highest for level-D emergencies (94.3%) -- an inverse U/step pattern distinct from Ramaswamy's inverted-U (which found emergencies and non-urgent cases both as failure extremes). RELEVANCE: this is a new, independently-constructed critical-miss-rate benchmark using single-message (everyday-language-adjacent) disclosures across 15 frontier models -- closely matching this protocol's own primary-endpoint architecture (undertriage/critical-miss rate) and single-message presentation format. Domain is psychiatric emergency triage specifically (not general ED triage), so findings should be read as a parallel/comparator design rather than a direct replication. Not yet peer-reviewed (arXiv preprint); does not resolve any standing alert. (https://arxiv.org/abs/2604.25415)

## ⚠ Critical — design overlap

- [[Soskin 2026 — HealthBench Professional Evaluating Large Language Models on Real…]] — *arXiv* 2026
- [[Nedos 2026 — Is Artificial Intelligence Ready for Emergency Department Triage A…]] — *Journal of Clinical Medicine* 2026
- [[Draelos 2026 — Large language models provide unsafe answers to patient-posed medical…]] — *npj Digital Medicine* 2026
- [[Benning 2026 — Performance evaluation and benchmarking across 16 large language…]] — *medRxiv* 2026
- [[Harada 2026 — Safety Audit of a Large Language Model for Lay Self-Triage Using…]] — *Cureus* 2026
- [[Nourbakhsh 2026 — Skyer a novel benchmark for evaluating the effectiveness of large…]] — *CJEM* 2026
- [[Shamsabadi 2026 — Comparing the text-based diagnostic reasoning performance of…]] — *International Journal of Emergency Medicine* 2026
- [[Ramaswamy 2026 — ChatGPT Health performance in a structured test of triage…]] — *Nature Medicine* 2026
- [[Brodeur 2026 — A prospective clinical feasibility study of a conversational…]] — *arXiv* 2026
- [[Fraile 2026 — Evaluation format, not model capability, drives triage failure in the…]] — *arXiv (preprint)* 2026
- [[Feng 2026 — Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical…]] — *arXiv (preprint)* 2026
- [[Brooks 2026 — Assessment of Physician Preferences for Large Language…]] — *JMIR Formative Research* 2026
- [[Jia 2026 — OpenEvidence errs on the safe side in a structured test of triage…]] — *medRxiv* 2026
- [[Aygun 2026 — Should we leave paediatric emergency triage to artificial…]] — *Frontiers in Pediatrics* 2026
- [[Chen 2026 — Independent and collaborative performance of large language models…]] — *npj Digital Medicine* 2026
- [[Tyagi 2026 — Conversational multi-turn interaction does not ensure…]] — *openRxiv* 2026
- [[Auger 2026 — Medical errors in large language models revealed using 1,000…]] — *openRxiv* 2026
- [[Reis 2026 — Reduced symptom reporting quality during human–chatbot versus…]] — *Nature Health* 2026
- [[Weilnhammer 2026 — One-shot emergency psychiatric triage across 15 frontier AI chatbots]] — *arXiv preprint* 2026
- [[Reis 2026 — Disclaimers and Referral Patterns for Medical Advice Across Urgency…]] — *Journal of Medical Internet Research* 2026
- [[Rodman 2026 — Performance of a large language model on the reasoning tasks of a…]] — *Science* 2026
- [[Johri 2025 — An evaluation framework for clinical use of large language models in…]] — *Nature Medicine* 2025
- [[Gaber 2025 — Evaluating large language model workflows in clinical decision…]] — *npj Digital Medicine* 2025
- [[Livingston 2025 — Reproducible generative artificial intelligence evaluation for health…]] — *JAMIA Open* 2025
- [[Zaboli 2025 — Chat-GPT in triage Still far from surpassing human expertise - An…]] — *The American Journal of Emergency Medicine* 2025
- [[Xu 2025 — Diagnosis and Triage Performance of Contemporary Large Language…]] — *Journal of Medical Systems* 2025
- [[Brown 2025 — Evaluation of Artificial Intelligence for Patient Self-Triage…]] — *Cureus* 2025
- [[Ho 2025 — Evaluation of Generative Artificial Intelligence Models in Predicting…]] — *Pediatric Emergency Care* 2025
- [[Arora 2025 — HealthBench Evaluating Large Language Models Towards Improved Human…]] — *arXiv* 2025
- [[Wang 2025 — Patient Triage and Guidance in Emergency Departments Using Large…]] — *Journal of Medical Internet Research* 2025
- [[Tu 2025 — Towards conversational diagnostic artificial intelligence]] — *Nature* 2025
- [[Lee 2025 — Performance of ChatGPT, Gemini and DeepSeek for non-critical triage…]] — *BMC Emergency Medicine* 2025
- [[Wu 2025 — First, do NOHARM towards clinically safe large language models]] — *arXiv (preprint)* 2025
- [[Pasli 2024 — Assessing the precision of artificial intelligence in ED triage…]] — *The American Journal of Emergency Medicine* 2024
- [[Arslan 2024 — Evaluating LLM-based generative AI tools in emergency triage A…]] — *The American Journal of Emergency Medicine* 2024
- [[Kopka 2024 — Evaluating self-triage accuracy of laypeople, symptom-assessment…]] — *medRxiv* 2024
- [[Zaboli 2024 — Human intelligence versus Chat-GPT who performs better in correctly…]] — *The American Journal of Emergency Medicine* 2024
- [[Franc 2024 — Repeatability, reproducibility, and diagnostic accuracy of a…]] — *CJEM* 2024
- [[Williams 2024 — Use of a Large Language Model to Assess Clinical Acuity of Adults in…]] — *JAMA Network Open* 2024
- [[Sarbay 2023 — Performance of emergency triage prediction of an open access natural…]] — *Turkish Journal of Emergency Medicine* 2023

## Emergency triage AI

- [[Gao 2026 — Accuracy of the large language model ChatGPT in adult emergency…]] (2026)
- [[Cui 2026 — Diagnostic accuracy of large language models for emergency department…]] (2026)
- [[Aljohani 2026 — Domain-Adapted Small Language Models for Reliable Clinical Triage]] (2026)
- [[Nedos 2026 — Is Artificial Intelligence Ready for Emergency Department Triage A…]] (2026)
- [[Benning 2026 — Performance evaluation and benchmarking across 16 large language…]] (2026)
- [[MY 2026 — Prompt Framing Modulates Safety in Shoulder and Elbow Red-Flag…]] (2026)
- [[Harada 2026 — Safety Audit of a Large Language Model for Lay Self-Triage Using…]] (2026)
- [[Nourbakhsh 2026 — Skyer a novel benchmark for evaluating the effectiveness of large…]] (2026)
- [[Shamsabadi 2026 — Comparing the text-based diagnostic reasoning performance of…]] (2026)
- [[Kukreti 2026 — Can ChatGPT match physicians in the diagnosis, triage, management and…]] (2026)
- [[Ramaswamy 2026 — ChatGPT Health performance in a structured test of triage…]] (2026)
- [[staff 2026 — ChatGPT Health triage advice falls short in key cases]] (2026)
- [[Lansiaux 2026 — Artificial Intelligence Models for Predicting Triage in Emergency…]] (2026)
- [[Fraile 2026 — Evaluation format, not model capability, drives triage failure in the…]] (2026)
- [[Naderi 2026 — The role of large language models in emergency care a comprehensive…]] (2026)
- [[Lee 2026 — From Promising Capabilities to Pervasive Bias Assessing Large…]] (2026)
- [[Alamoudi 2026 — AI Triage in Primary Care Building Safer and More Equitable…]] (2026)
- [[Lee 2026 — Performance and safety of a fine-tuned small language model for…]] (2026)
- [[Mittal 2026 — Evaluation of Large Language Models in the Diagnosis, Urgency Triage,…]] (2026)
- [[Jia 2026 — OpenEvidence errs on the safe side in a structured test of triage…]] (2026)
- [[Aygun 2026 — Should we leave paediatric emergency triage to artificial…]] (2026)
- [[Chen 2026 — Independent and collaborative performance of large language models…]] (2026)
- [[Wang 2026 — Large language models for acute coronary syndrome triage at first…]] (2026)
- [[Tyagi 2026 — Conversational multi-turn interaction does not ensure…]] (2026)
- [[Joy 2026 — MedPRESS A Multi-turn Benchmark for Patient-Pressure-Induced Medical…]] (2026)
- [[Weilnhammer 2026 — One-shot emergency psychiatric triage across 15 frontier AI chatbots]] (2026)
- [[Cotte 2026 — From Advice to Action Real-World Behavior of Patients Using an…]] (2026)
- [[Liaw 2026 — Maturity, Safety, and Equity of AI-Enabled Systems and Triage in…]] (2026)
- [[Young 2026 — EQUITRIAGE A Fairness Audit of Gender Bias in LLM-Based Emergency…]] (2026)
- [[Zhou 2026 — Few-Shot Large Language Models for Actionable Triage Categorization…]] (2026)
- [[Reis 2026 — Disclaimers and Referral Patterns for Medical Advice Across Urgency…]] (2026)
- [[Gaber 2025 — Evaluating large language model workflows in clinical decision…]] (2025) — **core**
- [[Guerra-Adames 2025 — A Counterfactual LLM Framework for Detecting Human Biases A Case…]] (2025)
- [[Kopka 2025 — Accuracy of online symptom assessment applications, large language…]] (2025)
- [[Zaboli 2025 — Chat-GPT in triage Still far from surpassing human expertise - An…]] (2025)
- [[Shan 2025 — Comparing Diagnostic Accuracy of Clinical Professionals and Large…]] (2025)
- [[Xu 2025 — Diagnosis and Triage Performance of Contemporary Large Language…]] (2025)
- [[Brown 2025 — Evaluation of Artificial Intelligence for Patient Self-Triage…]] (2025)
- [[Ho 2025 — Evaluation of Generative Artificial Intelligence Models in Predicting…]] (2025)
- [[Schmieding 2025 — Impact of a Symptom Checker App on Patient-Physician Interaction…]] (2025)
- [[Wang 2025 — Patient Triage and Guidance in Emergency Departments Using Large…]] (2025)
- [[Gourabathina 2025 — The Medium is the Message How Non-Clinical Information Shapes…]] (2025)
- [[Lee 2025 — Performance of ChatGPT, Gemini and DeepSeek for non-critical triage…]] (2025)
- [[Pasli 2024 — Assessing the precision of artificial intelligence in ED triage…]] (2024) — **core**
- [[Yazaki 2024 — Emergency Patient Triage Improvement through a Retrieval-Augmented…]] (2024)
- [[Arslan 2024 — Evaluating LLM-based generative AI tools in emergency triage A…]] (2024)
- [[Zaboli 2024 — Human intelligence versus Chat-GPT who performs better in correctly…]] (2024)
- [[Tang 2024 — Real-World Performance of Large Language Models in Emergency…]] (2024)
- [[Franc 2024 — Repeatability, reproducibility, and diagnostic accuracy of a…]] (2024)
- [[Williams 2024 — Use of a Large Language Model to Assess Clinical Acuity of Adults in…]] (2024)
- [[Sarbay 2023 — Performance of emergency triage prediction of an open access natural…]] (2023)

## Patient-facing AI

- [[Saab 2026 — Advancing conversational diagnostic AI with multimodal reasoning]] (2026)
- [[Hazare 2026 — Evaluating Sycophancy in Frontier Models Using Persona-Driven…]] (2026)
- [[Kopka 2026 — Increasing Large Language Model Accuracy for Care-Seeking Advice…]] (2026)
- [[Draelos 2026 — Large language models provide unsafe answers to patient-posed medical…]] (2026)
- [[Zuo 2026 — Patient Cognitive Bias in Large Language Model-Supported Health…]] (2026)
- [[Harada 2026 — Safety Audit of a Large Language Model for Lay Self-Triage Using…]] (2026)
- [[Lievin 2026 — Towards conversational artificial intelligence for disease management]] (2026)
- [[Kukreti 2026 — Can ChatGPT match physicians in the diagnosis, triage, management and…]] (2026)
- [[Ramaswamy 2026 — ChatGPT Health performance in a structured test of triage…]] (2026)
- [[staff 2026 — ChatGPT Health triage advice falls short in key cases]] (2026)
- [[Hussain 2026 — Toward trustworthy chatbots a protocol for red teaming for health…]] (2026)
- [[Brodeur 2026 — A prospective clinical feasibility study of a conversational…]] (2026)
- [[Fraile 2026 — Evaluation format, not model capability, drives triage failure in the…]] (2026)
- [[Feng 2026 — Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical…]] (2026)
- [[Brooks 2026 — Assessment of Physician Preferences for Large Language…]] (2026)
- [[Tiller 2026 — Generative artificial intelligence-driven chatbots and medical…]] (2026)
- [[Jia 2026 — OpenEvidence errs on the safe side in a structured test of triage…]] (2026)
- [[Aygun 2026 — Should we leave paediatric emergency triage to artificial…]] (2026)
- [[Tyagi 2026 — Conversational multi-turn interaction does not ensure…]] (2026)
- [[Auger 2026 — Medical errors in large language models revealed using 1,000…]] (2026)
- [[Sukhera 2026 — Structured Red Teaming Improves Safety of a Clinical AI Multi-Agent…]] (2026)
- [[Barnhart 2026 — Solidarity or Segregation ChatGPT Health and US Health Care…]] (2026)
- [[Reis 2026 — Reduced symptom reporting quality during human–chatbot versus…]] (2026)
- [[Costa-Gomes 2026 — Public use of a generalist LLM chatbot for health queries]] (2026)
- [[Reis 2026 — Disclaimers and Referral Patterns for Medical Advice Across Urgency…]] (2026)
- [[Ping 2026 — Why LLMs Give In Conversational Factors and Reasoning Behind Medical…]] (2026)
- [[Johri 2025 — An evaluation framework for clinical use of large language models in…]] (2025) — **core**
- [[Kopka 2025 — Accuracy of online symptom assessment applications, large language…]] (2025)
- [[Chang 2025 — Evaluating the Impact of Authoritative and Subjective Cues on Large…]] (2025)
- [[Sutaria 2025 — Evaluating the use of red flags by online symptom checkers]] (2025)
- [[Brown 2025 — Evaluation of Artificial Intelligence for Patient Self-Triage…]] (2025)
- [[Shumate 2025 — Governing AI in Mental Health 50-State Legislative Review]] (2025)
- [[Arora 2025 — HealthBench Evaluating Large Language Models Towards Improved Human…]] (2025)
- [[Schmieding 2025 — Impact of a Symptom Checker App on Patient-Physician Interaction…]] (2025)
- [[Wang 2025 — Patient Triage and Guidance in Emergency Departments Using Large…]] (2025)
- [[Gourabathina 2025 — The Medium is the Message How Non-Clinical Information Shapes…]] (2025)
- [[Rosen 2025 — The perils of politeness how large language models may amplify…]] (2025)
- [[McDuff 2025 — Towards accurate differential diagnosis with large language models]] (2025)
- [[Tu 2025 — Towards conversational diagnostic artificial intelligence]] (2025)
- [[Chen 2025 — When helpfulness backfires LLMs and the risk of false medical…]] (2025)
- [[Wu 2025 — First, do NOHARM towards clinically safe large language models]] (2025)
- [[Garcia 2024 — Artificial Intelligence-Generated Draft Replies to Patient Inbox…]] (2024)
- [[Knitza 2024 — Comparison of Two Symptom Checkers (Ada and Symptoma) in the…]] (2024)
- [[Kopka 2024 — Evaluating self-triage accuracy of laypeople, symptom-assessment…]] (2024)
- [[Ayers 2023 — Comparing Physician and Artificial Intelligence Chatbot Responses to…]] (2023)
- [[Gilbert 2023 — Large language model AI chatbots require approval as medical devices]] (2023)
- [[Mesko 2023 — The imperative for regulatory oversight of large language models (or…]] (2023)
- [[Riboli-Sasco 2023 — Triage and Diagnostic Accuracy of Online Symptom Checkers Systematic…]] (2023)
- [[Wallace 2022 — The diagnostic and triage accuracy of digital and online symptom…]] (2022)
- [[Kopka 2022 — The Triage Capability of Laypersons Retrospective Exploratory Analysis]] (2022)
- [[Ceney 2021 — Accuracy of online symptom checkers and the potential impact on…]] (2021)
- [[Chambers 2019 — Digital and online symptom checkers and health assessmenttriage…]] (2019)
- [[Millenson 2018 — Beyond Dr. Google the evidence on consumer-facing digital tools for…]] (2018)
- [[Semigran 2015 — Evaluation of symptom checkers for self diagnosis and triage audit…]] (2015)

## Physician evaluation

- [[Saab 2026 — Advancing conversational diagnostic AI with multimodal reasoning]] (2026)
- [[Soskin 2026 — HealthBench Professional Evaluating Large Language Models on Real…]] (2026)
- [[Draelos 2026 — Large language models provide unsafe answers to patient-posed medical…]] (2026)
- [[Lievin 2026 — Towards conversational artificial intelligence for disease management]] (2026)
- [[Shamsabadi 2026 — Comparing the text-based diagnostic reasoning performance of…]] (2026)
- [[Brodeur 2026 — A prospective clinical feasibility study of a conversational…]] (2026)
- [[Feng 2026 — Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical…]] (2026)
- [[Brooks 2026 — Assessment of Physician Preferences for Large Language…]] (2026)
- [[Chen 2026 — Independent and collaborative performance of large language models…]] (2026)
- [[Reis 2026 — Reduced symptom reporting quality during human–chatbot versus…]] (2026)
- [[Rao 2026 — Large Language Model Performance and Clinical Reasoning Tasks]] (2026)
- [[Rodman 2026 — Performance of a large language model on the reasoning tasks of a…]] (2026)
- [[Johri 2025 — An evaluation framework for clinical use of large language models in…]] (2025) — **core**
- [[Livingston 2025 — Reproducible generative artificial intelligence evaluation for health…]] (2025) — **core**
- [[Cilar 2025 — A Brief Review on Benchmarking for Large Language Models Evaluation…]] (2025)
- [[Zhou 2025 — Automating expert-level medical reasoning evaluation of large…]] (2025)
- [[Shan 2025 — Comparing Diagnostic Accuracy of Clinical Professionals and Large…]] (2025)
- [[Liu 2025 — HealthBench Advancing AI evaluation in healthcare, but not yet…]] (2025)
- [[Arora 2025 — HealthBench Evaluating Large Language Models Towards Improved Human…]] (2025)
- [[Chang 2025 — Red teaming ChatGPT in medicine to yield real-world insights on model…]] (2025)
- [[Bedi 2025 — Testing and Evaluation of Health Care Applications of Large Language…]] (2025)
- [[Singhal 2025 — Toward expert-level medical question answering with large language…]] (2025)
- [[McDuff 2025 — Towards accurate differential diagnosis with large language models]] (2025)
- [[Tu 2025 — Towards conversational diagnostic artificial intelligence]] (2025)
- [[Wu 2025 — First, do NOHARM towards clinically safe large language models]] (2025)
- [[Tam 2024 — A framework for human evaluation of large language models in…]] (2024)
- [[Goh 2024 — Large Language Model Influence on Diagnostic Reasoning A Randomized…]] (2024)
- [[Fleming 2024 — MedAlign A Clinician-Generated Dataset for Instruction Following with…]] (2024)
- [[Ayers 2023 — Comparing Physician and Artificial Intelligence Chatbot Responses to…]] (2023)
- [[Singhal 2023 — Large language models encode clinical knowledge]] (2023)

## Benchmark methodology

- [[Soskin 2026 — HealthBench Professional Evaluating Large Language Models on Real…]] (2026)
- [[Kopka 2026 — Increasing Large Language Model Accuracy for Care-Seeking Advice…]] (2026)
- [[Yan 2026 — LiveMedBench A Contamination-Free Medical Benchmark for LLMs with…]] (2026)
- [[Benning 2026 — Performance evaluation and benchmarking across 16 large language…]] (2026)
- [[Nourbakhsh 2026 — Skyer a novel benchmark for evaluating the effectiveness of large…]] (2026)
- [[Hussain 2026 — Toward trustworthy chatbots a protocol for red teaming for health…]] (2026)
- [[Lansiaux 2026 — Artificial Intelligence Models for Predicting Triage in Emergency…]] (2026)
- [[Ekram 2026 — Red-Teaming Medical AI Systematic Adversarial Evaluation of LLM…]] (2026)
- [[Fraile 2026 — Evaluation format, not model capability, drives triage failure in the…]] (2026)
- [[Naderi 2026 — The role of large language models in emergency care a comprehensive…]] (2026)
- [[Feng 2026 — Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical…]] (2026)
- [[Lee 2026 — Performance and safety of a fine-tuned small language model for…]] (2026)
- [[Chen 2026 — Independent and collaborative performance of large language models…]] (2026)
- [[Ding 2026 — Advancing medical AI through benchmarking and competition for…]] (2026)
- [[Auger 2026 — Medical errors in large language models revealed using 1,000…]] (2026)
- [[Joy 2026 — MedPRESS A Multi-turn Benchmark for Patient-Pressure-Induced Medical…]] (2026)
- [[Rao 2026 — Large Language Model Performance and Clinical Reasoning Tasks]] (2026)
- [[Zhou 2026 — Few-Shot Large Language Models for Actionable Triage Categorization…]] (2026)
- [[Rodman 2026 — Performance of a large language model on the reasoning tasks of a…]] (2026)
- [[Johri 2025 — An evaluation framework for clinical use of large language models in…]] (2025) — **core**
- [[Gaber 2025 — Evaluating large language model workflows in clinical decision…]] (2025) — **core**
- [[Zuo 2025 — MedXpertQA Benchmarking Expert-Level Medical Reasoning and…]] (2025) — **core**
- [[Livingston 2025 — Reproducible generative artificial intelligence evaluation for health…]] (2025) — **core**
- [[Sun 2025 — The Emperor's New Clothes in Benchmarking A Rigorous Examination of…]] (2025) — **core**
- [[Singh 2025 — The pitfalls of multiple-choice questions in generative AI and…]] (2025) — **core**
- [[Cilar 2025 — A Brief Review on Benchmarking for Large Language Models Evaluation…]] (2025)
- [[Zhou 2025 — Automating expert-level medical reasoning evaluation of large…]] (2025)
- [[Tang 2025 — ClinDEF A Dynamic Evaluation Framework for Large Language Models in…]] (2025)
- [[Arora 2025 — HealthBench Evaluating Large Language Models Towards Improved Human…]] (2025)
- [[Bedi 2025 — Testing and Evaluation of Health Care Applications of Large Language…]] (2025)
- [[Singhal 2025 — Toward expert-level medical question answering with large language…]] (2025)
- [[Tu 2025 — Towards conversational diagnostic artificial intelligence]] (2025)
- [[Wu 2025 — First, do NOHARM towards clinically safe large language models]] (2025)
- [[Tam 2024 — A framework for human evaluation of large language models in…]] (2024)
- [[Xie 2024 — A Preliminary Study of o1 in Medicine Are We Closer to an AI Doctor]] (2024)
- [[Kopka 2024 — Evaluating self-triage accuracy of laypeople, symptom-assessment…]] (2024)
- [[Schmidgall 2024 — Evaluation and mitigation of cognitive biases in medical language…]] (2024)
- [[Hager 2024 — Evaluation and mitigation of the limitations of large language models…]] (2024)
- [[Fleming 2024 — MedAlign A Clinician-Generated Dataset for Instruction Following with…]] (2024)
- [[Franc 2024 — Repeatability, reproducibility, and diagnostic accuracy of a…]] (2024)
- [[Kopka 2023 — How suitable are clinical vignettes for the evaluation of symptom…]] (2023)
- [[Singhal 2023 — Large language models encode clinical knowledge]] (2023)
- [[Kung 2023 — Performance of ChatGPT on USMLE Potential for AI-assisted medical…]] (2023)
- [[Pal 2022 — MedMCQA A Large-scale Multi-Subject Multi-Choice Dataset for Medical…]] (2022) — **core**
- [[Jin 2021 — What Disease Does This Patient Have A Large-Scale Open Domain…]] (2021) — **core**
- [[Bordage 2018 — The key-features approach to assess clinical decisions validity…]] (2018)
- [[Semigran 2015 — Evaluation of symptom checkers for self diagnosis and triage audit…]] (2015)
- [[Page 1995 — Developing key-feature problems and examinations to assess clinical…]] (1995) — **core**
- [[Page 1995 — The Medical Council of Canada's key features project a more valid…]] (1995) — **core**

## AI safety failure modes

- [[Hazare 2026 — Evaluating Sycophancy in Frontier Models Using Persona-Driven…]] (2026)
- [[Draelos 2026 — Large language models provide unsafe answers to patient-posed medical…]] (2026)
- [[Zuo 2026 — Patient Cognitive Bias in Large Language Model-Supported Health…]] (2026)
- [[MY 2026 — Prompt Framing Modulates Safety in Shoulder and Elbow Red-Flag…]] (2026)
- [[Harada 2026 — Safety Audit of a Large Language Model for Lay Self-Triage Using…]] (2026)
- [[Ramaswamy 2026 — ChatGPT Health performance in a structured test of triage…]] (2026)
- [[Hussain 2026 — Toward trustworthy chatbots a protocol for red teaming for health…]] (2026)
- [[Ekram 2026 — Red-Teaming Medical AI Systematic Adversarial Evaluation of LLM…]] (2026)
- [[Fraile 2026 — Evaluation format, not model capability, drives triage failure in the…]] (2026)
- [[Lee 2026 — From Promising Capabilities to Pervasive Bias Assessing Large…]] (2026)
- [[Jia 2026 — OpenEvidence errs on the safe side in a structured test of triage…]] (2026)
- [[Tyagi 2026 — Conversational multi-turn interaction does not ensure…]] (2026)
- [[Auger 2026 — Medical errors in large language models revealed using 1,000…]] (2026)
- [[Sukhera 2026 — Structured Red Teaming Improves Safety of a Clinical AI Multi-Agent…]] (2026)
- [[Young 2026 — EQUITRIAGE A Fairness Audit of Gender Bias in LLM-Based Emergency…]] (2026)
- [[Ping 2026 — Why LLMs Give In Conversational Factors and Reasoning Behind Medical…]] (2026)
- [[Guerra-Adames 2025 — A Counterfactual LLM Framework for Detecting Human Biases A Case…]] (2025)
- [[Zaboli 2025 — Chat-GPT in triage Still far from surpassing human expertise - An…]] (2025)
- [[Xu 2025 — Diagnosis and Triage Performance of Contemporary Large Language…]] (2025)
- [[Chang 2025 — Evaluating the Impact of Authoritative and Subjective Cues on Large…]] (2025)
- [[Sutaria 2025 — Evaluating the use of red flags by online symptom checkers]] (2025)
- [[Chang 2025 — Red teaming ChatGPT in medicine to yield real-world insights on model…]] (2025)
- [[Gourabathina 2025 — The Medium is the Message How Non-Clinical Information Shapes…]] (2025)
- [[Rosen 2025 — The perils of politeness how large language models may amplify…]] (2025)
- [[Chen 2025 — When helpfulness backfires LLMs and the risk of false medical…]] (2025)
- [[Wu 2025 — First, do NOHARM towards clinically safe large language models]] (2025)
- [[Knitza 2024 — Comparison of Two Symptom Checkers (Ada and Symptoma) in the…]] (2024)
- [[Schmidgall 2024 — Evaluation and mitigation of cognitive biases in medical language…]] (2024)
- [[Hager 2024 — Evaluation and mitigation of the limitations of large language models…]] (2024)
- [[Zaboli 2024 — Human intelligence versus Chat-GPT who performs better in correctly…]] (2024)
- [[Wallace 2022 — The diagnostic and triage accuracy of digital and online symptom…]] (2022)
- [[Ceney 2021 — Accuracy of online symptom checkers and the potential impact on…]] (2021)

## Triage standards

- [[Aljohani 2026 — Domain-Adapted Small Language Models for Reliable Clinical Triage]] (2026)
- [[Barnhart 2026 — Solidarity or Segregation ChatGPT Health and US Health Care…]] (2026)
- [[Young 2026 — EQUITRIAGE A Fairness Audit of Gender Bias in LLM-Based Emergency…]] (2026)
- [[Ho 2025 — Evaluation of Generative Artificial Intelligence Models in Predicting…]] (2025)
- [[Wandl 2025 — Diagnostic test accuracy of the Emergency Severity Index a systematic…]] (2025)
- [[Sax 2024 — Emergency Severity Index Version 4 and Triage of Pediatric Emergency…]] (2024)
- [[Sax 2023 — Evaluation of the Emergency Severity Index in US Emergency…]] (2023) — **core**
- [[Trauma 2022 — Resources for Optimal Care of the Injured Patient (undertriage 5%…]] (2022) — **core**
- [[Kopka 2022 — The Triage Capability of Laypersons Retrospective Exploratory Analysis]] (2022)
- [[Chambers 2019 — Digital and online symptom checkers and health assessmenttriage…]] (2019)
- [[Hinson 2019 — Triage Performance in Emergency Medicine A Systematic Review]] (2019)
- [[Mistry 2018 — Accuracy and Reliability of Emergency Department Triage Using the…]] (2018)
- [[Semigran 2015 — Evaluation of symptom checkers for self diagnosis and triage audit…]] (2015)
- [[Gilboy 2012 — Emergency Severity Index (ESI) A Triage Tool for Emergency Department…]] (2012) — **core**
- [[Travers 2009 — Reliability and Validity of the Emergency Severity Index for…]] (2009)
- [[Fernandes 2005 — Five-level triage a report from the ACEPENA Five-level Triage Task…]] (2005)
- [[Tanabe 2005 — Refining Emergency Severity Index triage criteria]] (2005)
- [[Eitel 2003 — The emergency severity index triage algorithm version 2 is reliable…]] (2003)
- [[Wuerz 2001 — Implementation and Refinement of the Emergency Severity Index]] (2001)
- [[Wuerz 2000 — Reliability and validity of a new five-level triage instrument]] (2000)

## Policy & regulation

- [[Alamoudi 2026 — AI Triage in Primary Care Building Safer and More Equitable…]] (2026)
- [[Tiller 2026 — Generative artificial intelligence-driven chatbots and medical…]] (2026)
- [[Liaw 2026 — Maturity, Safety, and Equity of AI-Enabled Systems and Triage in…]] (2026)
- [[Shumate 2025 — Governing AI in Mental Health 50-State Legislative Review]] (2025)
- [[Liu 2025 — HealthBench Advancing AI evaluation in healthcare, but not yet…]] (2025)
- [[Gilbert 2023 — Large language model AI chatbots require approval as medical devices]] (2023)
- [[Mesko 2023 — The imperative for regulatory oversight of large language models (or…]] (2023)

## Assessment methodology

- [[Zuo 2025 — MedXpertQA Benchmarking Expert-Level Medical Reasoning and…]] (2025) — **core**
- [[Singh 2025 — The pitfalls of multiple-choice questions in generative AI and…]] (2025) — **core**
- [[Xie 2024 — A Preliminary Study of o1 in Medicine Are We Closer to an AI Doctor]] (2024)
- [[Kung 2023 — Performance of ChatGPT on USMLE Potential for AI-assisted medical…]] (2023)
- [[Pal 2022 — MedMCQA A Large-scale Multi-Subject Multi-Choice Dataset for Medical…]] (2022) — **core**
- [[Jin 2021 — What Disease Does This Patient Have A Large-Scale Open Domain…]] (2021) — **core**
- [[Bordage 2018 — The key-features approach to assess clinical decisions validity…]] (2018)
- [[Page 1995 — Developing key-feature problems and examinations to assess clinical…]] (1995) — **core**
- [[Page 1995 — The Medical Council of Canada's key features project a more valid…]] (1995) — **core**
