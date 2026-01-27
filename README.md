# AI Medical Information Standards (AMIS)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Standards Version](https://img.shields.io/badge/Standards-v1.0.0-blue.svg)](SPECIFICATION.md)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Five foundational standards for AI systems that generate medical information.**

> *"The apparent confidence of any medical statement should not exceed its epistemic warrant."*

---

## Background

In January 2026, a [Guardian investigation](https://www.theguardian.com/technology/2026/jan/02/google-ai-health-summaries-risk) documented systematic failures in AI-generated medical information: dietary advice for pancreatic cancer patients that was "the exact opposite of what should be recommended," laboratory reference ranges presented without critical context, and YouTube cited more frequently than peer-reviewed medical journals.

These failures are not bugs to be patched—they are architectural deficiencies requiring systematic remediation.

This repository provides **implementable standards** for AI medical information systems, grounded in evidence-based medicine principles and informed by a [dharmic philosophical framework](docs/dharmic_framework.md) that distinguishes *constitutive* safety (built into architecture) from *regulatory* safety (bolted on afterward).

---

## The Five Standards

| # | Standard | Core Principle |
|---|----------|----------------|
| 1 | **Literature Review Paradigm** | Treat health queries with systematic evidence appraisal rigour |
| 2 | **Source Quality Hierarchy** | Only peer-reviewed, reputable sources; 5-tier classification |
| 3 | **Mandatory Uncertainty Disclosure** | Confidence calibrated to epistemic warrant + explicit warnings |
| 4 | **Dissent Labelling Without False Certainty** | Label heterodox views; avoid dogma in either direction |
| 5 | **Therapeutic Advice Requires Physician Evaluation** | AI informs; physicians prescribe |

See [SPECIFICATION.md](SPECIFICATION.md) for formal definitions.

---

## Quick Start

### 1. Validate AI Output Against Standards

```python
from implementation.python.validator import AMISValidator

validator = AMISValidator()
result = validator.validate(ai_output, query_type="health")

if not result.compliant:
    print(f"Violations: {result.violations}")
    print(f"Recommendations: {result.recommendations}")
```

### 2. Classify Source Quality

```python
from implementation.python.source_classifier import SourceClassifier

classifier = SourceClassifier()
tier = classifier.classify("https://www.cochranelibrary.com/...")
# Returns: Tier(level=1, name="Systematic Reviews", usage="Primary weight")
```

### 3. Analyze Harm Cascade

```python
from implementation.python.harm_analyzer import HarmCascadeAnalyzer

analyzer = HarmCascadeAnalyzer()
risks = analyzer.analyze(
    content="For liver function, normal ALT is 7-56 U/L",
    context="Patient query about blood test results"
)
# Returns risk assessment across 4 dimensions
```

### 4. Implement via System Prompt

Copy [implementation/prompts/system_prompt_template.md](implementation/prompts/system_prompt_template.md) into your LLM system prompt.

---

## Repository Structure

```
ai-medical-information-standards/
├── README.md                          # This file
├── SPECIFICATION.md                   # Formal standards specification
├── LICENSE                            # CC-BY-4.0
│
├── standards/                         # Machine-readable specifications
│   ├── source_hierarchy.yaml          # 5-tier hierarchy
│   ├── uncertainty_calibration.yaml   # Confidence thresholds
│   ├── harm_cascade.json              # Decision tree
│   └── validation_schema.json         # JSON Schema for compliance
│
├── implementation/                    # Reference implementations
│   ├── python/
│   │   ├── validator.py               # Compliance checker
│   │   ├── source_classifier.py       # Tier classification
│   │   └── harm_analyzer.py           # Cascade analysis
│   └── prompts/
│       └── system_prompt_template.md  # LLM system prompt
│
├── docs/
│   ├── extended_rationale.md          # Full philosophical grounding
│   ├── dharmic_framework.md           # Constitutive vs regulatory
│   ├── implementation_guide.md        # Adoption guide
│   └── compliance_checklist.md        # Self-assessment
│
└── examples/
    ├── compliant_output.md            # What good looks like
    └── non_compliant_output.md        # Documented failures
```

---

## Key Concepts

### Constitutive vs Regulatory Safety

| Aspect | Regulatory (Bolt-on) | Constitutive (Built-in) |
|--------|---------------------|------------------------|
| **Mechanism** | Monitor outputs → filter violations | Harmful pathways absent from architecture |
| **Analogy** | Censorship | Grammar |
| **Question** | "How do we catch bad outputs?" | "Why would bad outputs arise?" |
| **Kill switch** | Required | Unnecessary |

This framework, derived from dharmic philosophy (*ahiṃsā*, *pramāṇa*, *viveka*), argues that the five standards represent **constitutive** safety measures—they don't filter harmful outputs but prevent harmful reasoning pathways from existing.

See [docs/dharmic_framework.md](docs/dharmic_framework.md) for full exposition.

### Harm Cascade Analysis

Before generating medical information, systems should trace potential harms across four dimensions:

1. **Direct harm**: Could this cause physical harm if acted upon?
2. **Indirect harm**: Could this lead to delayed necessary care?
3. **Epistemic harm**: Could this distort understanding in compounding ways?
4. **Systemic harm**: Could this degrade public health understanding at scale?

---

## Citation

If you use these standards in research or implementation, please cite:

```bibtex
@article{srivatsa2026standards,
  title={Standards for AI-generated medical information: lessons from documented failures},
  author={Srivatsa, S. Sanjay},
  journal={The Lancet Digital Health},
  year={2026},
  note={Comment}
}
```

---

## Contributing

We welcome contributions that:
- Extend machine-readable specifications
- Add implementations in other languages
- Provide additional compliant/non-compliant examples
- Translate documentation

Please open an issue before submitting significant changes.

---

## Related Work

- [EXSTO ERGO SUM: A Dharmic Framework for AI Alignment](https://github.com/placeholder) — The broader philosophical framework
- [Guardian Investigation (Jan 2026)](https://www.theguardian.com/technology/2026/jan/02/google-ai-health-summaries-risk) — Empirical foundation
- [GRADE Working Group](https://www.gradeworkinggroup.org/) — Evidence quality assessment
- [Cochrane Collaboration](https://www.cochranelibrary.com/) — Systematic review methodology

---

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt with attribution.

Code implementations are additionally available under [MIT License](LICENSE).

---

**Maintainer**: S. Sanjay Srivatsa, MD | Heart Artery and Vein Center, Fresno, California

*Accuracy and appropriate epistemic humility in health information are not optional design features—they are prerequisites for AI systems that interact with human health and lives.*
