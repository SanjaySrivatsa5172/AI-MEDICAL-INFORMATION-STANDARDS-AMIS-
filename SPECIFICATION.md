# AI Medical Information Standards (AMIS) Specification

**Version**: 1.0.0  
**Status**: Draft  
**Last Updated**: January 2026

---

## 1. Overview

### 1.1 Purpose

This specification defines five foundational standards for artificial intelligence systems that generate medical or health-related information. The standards are designed to prevent documented failure modes and ensure that AI-generated health information meets minimum epistemic and safety requirements.

### 1.2 Scope

These standards apply to any AI system that:
- Responds to health-related queries from users
- Generates medical information for display or consumption
- Synthesizes content from medical or health sources
- Provides guidance that could influence health decisions

### 1.3 Normative Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

---

## 2. Definitions

**AI Medical Information System (AMIS)**: Any artificial intelligence system that generates, synthesizes, or presents medical or health-related information to users.

**Epistemic Warrant**: The degree of justification or evidential support for a claim. A claim has high epistemic warrant when supported by multiple high-quality, independent sources using rigorous methodology.

**Therapeutic Intent**: A query or context implying the user seeks guidance for implementing a health intervention, including medication changes, treatment modifications, dietary interventions for medical conditions, or supplement regimens.

**Source Tier**: A classification level (1-5) indicating the reliability and appropriateness of an information source for medical claims.

**Harm Cascade**: The propagation of potential negative effects from an information output across direct, indirect, epistemic, and systemic dimensions.

---

## 3. Standard 1: Literature Review Paradigm

### 3.1 Requirement

Health-related queries MUST be treated with the same methodological rigour as formal systematic literature reviews.

### 3.2 Specifications

3.2.1 Every source used to generate medical information MUST be graded by:
  - Quality of information (accuracy, completeness, currency)
  - Quality of cited evidence (study design, sample size, bias risk)

3.2.2 Systems MUST NOT aggregate health information results by:
  - Popularity metrics
  - Recency alone (without quality assessment)
  - Search engine optimisation signals

3.2.3 Systems MUST apply systematic evidence appraisal methodology, including:
  - Assessment of study design hierarchy
  - Evaluation of potential biases
  - Consideration of consistency across sources
  - Assessment of directness of evidence

### 3.3 Rationale

The casual aggregation approach appropriate for general web queries is categorically inappropriate for health information, where epistemic errors propagate through human bodies with potentially irreversible consequences.

### 3.4 Compliance Criteria

| Criterion | Compliant | Non-Compliant |
|-----------|-----------|---------------|
| Source grading | Each source assigned quality score | Sources used without evaluation |
| Methodology | Systematic appraisal documented | Ad hoc selection |
| Ranking | Evidence quality drives prominence | Popularity/SEO drives prominence |

---

## 4. Standard 2: Source Quality Hierarchy

### 4.1 Requirement

Only trusted, peer-reviewed, reputable sources SHALL be used to generate medical opinions. Sources MUST be classified according to a five-tier hierarchy.

### 4.2 Tier Definitions

#### Tier 1: Primary Authority
**Sources**: Cochrane systematic reviews, WHO recommendations, NICE guidelines, peer-reviewed systematic reviews and meta-analyses published in indexed journals.

**Usage**: MUST receive primary weight. Definitive statements ("X is established") are permitted when Tier 1 sources demonstrate consensus.

**Rationale**: These sources employ rigorous methodology, systematic search strategies, and formal quality assessment.

#### Tier 2: High-Quality Primary Evidence
**Sources**: Randomised controlled trials in major peer-reviewed journals (NEJM, Lancet, JAMA, BMJ, Annals of Internal Medicine, and specialty equivalents), institutional clinical guidelines from recognised medical bodies.

**Usage**: MAY supplement Tier 1 consensus. Qualified definitive statements are permitted.

**Rationale**: Peer review and editorial standards provide quality assurance, though individual studies may have limitations.

#### Tier 3: Supporting Evidence
**Sources**: Observational studies in peer-reviewed journals, established medical databases (UpToDate, MedlinePlus, DynaMed), academic medical institution websites (.edu domains with medical school affiliation).

**Usage**: MAY provide context. MUST NOT contradict Tier 1-2 consensus without explicit flagging.

**Rationale**: Useful for prevalence data, natural history, and areas where RCTs are impractical, but subject to confounding and bias.

#### Tier 4: Expert Opinion
**Sources**: Expert opinion from credentialed professionals, professional society position statements, medical textbooks, clinical experience reports.

**Usage**: MAY provide narrative framing. MUST NOT serve as sole basis for medical claims.

**Rationale**: Valuable for emerging areas and clinical nuance, but subject to individual bias and may not reflect evidence synthesis.

#### Tier 5: Excluded Sources
**Sources**: YouTube, TikTok, Reddit, social media platforms, forums, blogs without institutional affiliation, news aggregators, content farms.

**Usage**: MUST NOT be used as basis for medical claims under any circumstances.

**Rationale**: Platform architecture provides no mechanism for quality control, peer review, or accountability for harm. Individual creator credentials do not mitigate platform-level deficiencies.

### 4.3 Source Classification Requirements

4.3.1 Systems MUST maintain a source classification database or algorithm capable of assigning tier levels.

4.3.2 Tier classification MUST be based on platform/publication characteristics, not individual content creator credentials.

4.3.3 When a source's tier is ambiguous, systems MUST default to the lower (more restrictive) tier.

4.3.4 Source tier SHOULD be made available to users upon request.

### 4.4 Compliance Criteria

| Criterion | Compliant | Non-Compliant |
|-----------|-----------|---------------|
| Tier 5 usage | Never cited for medical claims | YouTube/social media cited |
| Tier weighting | Tier 1-2 receive primary weight | All sources weighted equally |
| Classification | Systematic tier assignment | No source classification |

---

## 5. Standard 3: Mandatory Uncertainty Disclosure

### 5.1 Requirement

The apparent confidence of any medical statement MUST NOT exceed its epistemic warrant. Uncertain, disputed, or speculative information MUST include explicit warnings.

### 5.2 Confidence Calibration

#### 5.2.1 Definitive Statements
**Form**: "X is established", "Evidence demonstrates", "It is known that"

**Permitted when**:
- Tier 1-2 source support exists
- Broad expert consensus (>90% agreement in guidelines)
- No significant methodological disputes

#### 5.2.2 Qualified Statements
**Form**: "Evidence suggests", "Studies indicate", "Current understanding holds"

**Required when**:
- Tier 2-3 source support
- Some expert disagreement exists
- Methodological limitations present
- Evidence is observational rather than experimental

#### 5.2.3 Uncertain Statements
**Form**: "This is not well established", "Evidence is limited", "Findings are preliminary"

**Required when**:
- Tier 3-4 source support only
- Significant conflicting evidence
- Limited sample sizes
- Emerging or rapidly evolving area

#### 5.2.4 Speculative Statements
**Form**: "This is speculative", "No reliable evidence exists", "Claims are unverified"

**Required when**:
- Tier 4 support only
- Claims contradict Tier 1-2 consensus
- No peer-reviewed evidence available

### 5.3 Mandatory Warning Requirement

5.3.1 When presenting uncertain, disputed, or speculative medical information, systems MUST include an explicit warning that:
  - Adoption of unverified advice could lead to detrimental health outcomes
  - Qualified physician guidance must be sought before acting on such information

5.3.2 This warning requirement is NOT OPTIONAL. It is a prerequisite for any system that interacts with human health decisions.

5.3.3 Warnings MUST be proximate to the uncertain content, not relegated to generic disclaimers.

### 5.4 Compliance Criteria

| Criterion | Compliant | Non-Compliant |
|-----------|-----------|---------------|
| Confidence calibration | Matches epistemic warrant | Overconfident relative to evidence |
| Uncertainty labelling | Explicit qualifiers used | Uncertain claims stated definitively |
| Warnings | Included for uncertain content | No warnings or generic only |

---

## 6. Standard 4: Dissent Labelling Without False Certainty

### 6.1 Requirement

Positions that dissent from prevailing medical consensus MUST be explicitly labelled as such. Neither prevailing opinion nor dissenting views SHALL be presented as dogma where legitimate scientific doubt exists.

### 6.2 Specifications

6.2.1 When presenting dissenting positions, systems MUST:
  - Explicitly identify the view as dissenting from consensus
  - State what the prevailing consensus holds
  - Describe what dissenting positions argue
  - Characterize the quality of evidence supporting each position
  - Acknowledge when the question remains unsettled

6.2.2 Systems MUST NOT:
  - Present consensus positions as infallible dogma
  - Present dissenting positions as equally supported when evidence is asymmetric
  - Suppress legitimate scientific controversy
  - Create false equivalence between well-supported and poorly-supported positions

6.2.3 Medical knowledge evolves. Systems MUST communicate epistemic humility regarding:
  - Historical revisions of consensus positions
  - Ongoing research that may alter understanding
  - Areas of genuine scientific uncertainty

### 6.3 Controversy Presentation Format

When genuine scientific controversy exists, systems SHOULD present:

```
CONSENSUS POSITION: [Statement of majority view]
Evidence basis: [Tier level and key sources]

DISSENTING POSITION(S): [Statement of minority view(s)]
Evidence basis: [Tier level and key sources]

STATUS: [Settled / Active debate / Emerging evidence]

Note: This question remains [settled with minority dissent / actively debated / 
under investigation]. Consult a healthcare provider for guidance specific to 
your situation.
```

### 6.4 Compliance Criteria

| Criterion | Compliant | Non-Compliant |
|-----------|-----------|---------------|
| Dissent labelling | Explicitly marked | Presented without context |
| Consensus treatment | Presented with appropriate confidence | Treated as infallible |
| Evidence comparison | Quality characterized for each position | False equivalence |

---

## 7. Standard 5: Therapeutic Advice Requires Physician Evaluation

### 7.1 Requirement

No advice that is therapeutic in nature SHALL be offered for implementation without explicit direction to obtain prior evaluation by a qualified physician.

### 7.2 Scope Definition

7.2.1 **Therapeutic advice** includes:
  - Medication recommendations (starting, stopping, changing doses)
  - Treatment protocol suggestions
  - Dietary interventions for medical conditions
  - Supplement regimens for health conditions
  - Exercise prescriptions for medical rehabilitation
  - Decisions about when to seek or defer medical care

7.2.2 **Informational content** (permitted without physician referral):
  - General explanations of conditions, mechanisms, or treatments
  - Descriptions of what treatments exist for a condition
  - Explanations of how medications work
  - General health education

### 7.3 Therapeutic Intent Detection

7.3.1 Systems MUST identify queries with therapeutic intent, including:
  - Explicit requests: "Should I take X for my Y?"
  - Implicit intent: "What can I do about my [condition]?"
  - Implementation queries: "How much X should I take?"
  - Decision queries: "Should I stop taking my medication?"

7.3.2 When therapeutic intent is detected, systems MUST:
  - Provide general information if appropriate
  - Explicitly direct the user to physician consultation before implementation
  - NOT provide specific dosing, timing, or implementation guidance

### 7.4 Physician Referral Language

Systems MUST include language such as:

> "This information is for educational purposes. Before making any changes to your treatment, medications, or health regimen, please consult with a qualified healthcare provider who can evaluate your specific situation."

### 7.5 Compliance Criteria

| Criterion | Compliant | Non-Compliant |
|-----------|-----------|---------------|
| Therapeutic detection | Intent identified and flagged | Therapeutic queries treated as informational |
| Physician referral | Explicit direction to consult | No referral or buried in disclaimer |
| Implementation guidance | Withheld pending physician input | Specific implementation provided |

---

## 8. Harm Cascade Analysis

### 8.1 Requirement

Before generating medical information outputs, systems SHOULD trace potential harm cascades across four dimensions.

### 8.2 Harm Dimensions

#### 8.2.1 Direct Harm
**Question**: Could this information cause physical harm if acted upon?

**Examples**:
- Incorrect dosing information
- Dangerous drug interactions not mentioned
- Contraindicated treatments recommended

**Severity**: Critical — immediate physical danger

#### 8.2.2 Indirect Harm
**Question**: Could this information lead to harmful decisions such as delaying necessary care?

**Examples**:
- False reassurance discouraging follow-up
- Minimizing symptoms that require evaluation
- Suggesting watchful waiting when urgency exists

**Severity**: High — delayed intervention may worsen outcomes

#### 8.2.3 Epistemic Harm
**Question**: Could this information distort understanding in compounding ways?

**Examples**:
- Laboratory values without context (e.g., "normal" ranges without age/sex/ethnicity variation)
- Partial information creating false confidence
- Misconceptions that affect future health decisions

**Severity**: Medium-High — errors compound over time

#### 8.2.4 Systemic Harm
**Question**: Could this information, at scale, degrade public health understanding?

**Examples**:
- Vaccine misinformation reaching millions
- Normalized distrust of medical institutions
- Propagation of ineffective treatments

**Severity**: Variable — population-level effects

### 8.3 Analysis Process

```
FOR each potential output:
  1. Assess DIRECT harm potential (0-10)
  2. Assess INDIRECT harm potential (0-10)
  3. Assess EPISTEMIC harm potential (0-10)
  4. Assess SYSTEMIC harm potential (0-10)
  
  IF any dimension >= 7:
    BLOCK output or require explicit physician referral
  ELSE IF any dimension >= 4:
    ADD appropriate warnings and uncertainty markers
  ELSE:
    PROCEED with standard confidence calibration
```

---

## 9. Implementation Requirements

### 9.1 Traceability

9.1.1 All medical claims MUST be traceable to specific sources.

9.1.2 Source tier classification MUST be available to users upon request.

9.1.3 Systems SHOULD maintain auditable logs enabling reconstruction of reasoning chains.

### 9.2 Accountability

9.2.1 Documented harms MUST trigger mandatory review and system modification.

9.2.2 Systems SHOULD facilitate third-party audit by qualified medical professionals.

9.2.3 Operators MUST maintain incident reporting mechanisms.

### 9.3 Transparency

9.3.1 Systems MUST disclose that information is AI-generated.

9.3.2 Limitations of AI medical information MUST be communicated to users.

9.3.3 The standards framework in use SHOULD be publicly documented.

---

## 10. Conformance

### 10.1 Conformance Levels

**Level 1 — Partial Conformance**: Implements Standards 2, 3, and 5 (source hierarchy, uncertainty disclosure, physician referral).

**Level 2 — Substantial Conformance**: Implements all five standards with documented processes.

**Level 3 — Full Conformance**: Implements all standards plus harm cascade analysis, full traceability, and third-party audit capability.

### 10.2 Conformance Statement

Systems claiming conformance to this specification SHOULD publish a conformance statement indicating:
- Conformance level claimed
- Any standards not implemented or partially implemented
- Date of last conformance assessment

---

## Appendix A: Reference to Machine-Readable Specifications

- Source hierarchy: `standards/source_hierarchy.yaml`
- Uncertainty calibration: `standards/uncertainty_calibration.yaml`
- Harm cascade decision tree: `standards/harm_cascade.json`
- Validation schema: `standards/validation_schema.json`

## Appendix B: Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01 | Initial specification |

---

*This specification is licensed under CC BY 4.0. Attribution to S. Sanjay Srivatsa, MD.*
