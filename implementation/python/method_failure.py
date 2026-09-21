"""
AMIS Methodological Failure Analyzer

Detects evaluation and reasoning failure modes documented in AMIS
companion materials (productive-uncertainty manuscript; ResidencyRL
letter): shortcut learning, contaminated graders, Goodhart gaming,
fabricated chain-of-thought, automation bias, and related patterns.

This is the one net-new primitive. Existing validators score output
compliance, not whether a claimed AI result was produced by a
contaminated or gamed evaluation. Patterns are Python constants that
cite AMIS standards — not a parallel YAML schema.

Author: S. Sanjay Srivatsa, MD
License: MIT
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class FailurePattern:
    """One methodological failure mode."""

    code: str
    title: str
    regex: str
    severity: str  # minor | moderate | major | critical
    description: str
    standard: str
    polarity_hint: str  # asserted | critiqued | either
    compiled: re.Pattern = field(init=False, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "compiled", re.compile(self.regex, re.IGNORECASE))


@dataclass
class FailureFinding:
    """A matched methodological failure, with polarity."""

    code: str
    title: str
    severity: str
    description: str
    standard: str
    polarity: str  # asserted | critiqued
    evidence: str
    weight: float

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "title": self.title,
            "severity": self.severity,
            "description": self.description,
            "standard": self.standard,
            "polarity": self.polarity,
            "evidence": self.evidence,
            "weight": self.weight,
        }


@dataclass
class MethodFailureResult:
    """Aggregate methodological-failure axis."""

    failure_score: float  # 0-100; higher = more asserted failure
    awareness_score: float  # 0-100; higher = more critiqued / labelled failure
    findings: List[FailureFinding]

    def to_dict(self) -> dict:
        return {
            "failure_score": round(self.failure_score, 1),
            "awareness_score": round(self.awareness_score, 1),
            "findings": [f.to_dict() for f in self.findings],
        }


class MethodologicalFailureAnalyzer:
    """Score methodological failure vs critique of that failure."""

    SEVERITY_WEIGHT = {
        "minor": 8.0,
        "moderate": 14.0,
        "major": 22.0,
        "critical": 30.0,
    }

    CRITIQUE_RE = re.compile(
        r"\b("
        r"we argue|risk(?:s)?|concern|however|danger|undermin|"
        r"wrong reasons|not a residency|failure|erode|threaten|"
        r"paradox|illusion|should take from|must (?:not|never)|"
        r"contaminated|does not repair|without raising correctness|"
        r"masquerades|misleading|inherently unstable"
        r")\b",
        re.IGNORECASE,
    )

    ASSERT_RE = re.compile(
        r"\b("
        r"we (?:achieved|report|trained?|present|introduce|evaluate|train)|"
        r"our (?:model|agent|system|approach|findings)|"
        r"the residencyrl[- ]trained agent|"
        r"we introduce residencyrl"
        r")\b",
        re.IGNORECASE,
    )

    FIRST_PERSON_METHOD_RE = re.compile(
        r"\b("
        r"we (?:present|train|introduce|evaluate)|"
        r"our (?:model|agent|system|autorater|rubric)|"
        r"an llm autorater|structured autorater|"
        r"training reward|reward signal|"
        r"residencyrl[- ]trained"
        r")\b",
        re.IGNORECASE,
    )

    DISCLOSURE_RE = re.compile(
        r"\b("
        r"primarily validate|limitation|caveat|"
        r"prospective validation remains|"
        r"does not (?:establish|translate|model)|"
        r"share(?:s|d)? the underlying"
        r")\b",
        re.IGNORECASE,
    )

    LETTER_RE = re.compile(
        r"\b(to the editor|not a residency|we argue that|my article argued)\b",
        re.IGNORECASE,
    )

    PATTERNS: List[FailurePattern] = [
        FailurePattern(
            code="shortcut_learning",
            title="Shortcut learning / spurious cues",
            regex=r"shortcut(?: learning)?|spurious (?:cue|correlation|textual)|"
                  r"succeed(?:s|ed)? for fundamentally wrong reasons|"
                  r"dataset artifacts|wrong reasons",
            severity="major",
            description="High benchmark scores attributed to brittle shortcuts rather than clinical reasoning.",
            standard="standard_1_literature_review",
            polarity_hint="either",
        ),
        FailurePattern(
            code="fabricated_reasoning",
            title="Fabricated reasoning / hollow chain-of-thought",
            regex=r"fabricat\w* (?:reasoning|explanation|rational)|"
                  r"nonexistent (?:image )?features|"
                  r"confident(?:ly)? generat\w*.{0,40}(?:nonexistent|without)|"
                  r"explanations of nonexistent",
            severity="major",
            description="Confident explanations of findings that were not in the input (fabricated CoT).",
            standard="standard_3_uncertainty_disclosure",
            polarity_hint="either",
        ),
        FailurePattern(
            code="contaminated_grader",
            title="Contaminated or in-family grader",
            regex=r"autorater|self-grad\w*|same model family|"
                  r"llm(?:-as)?[- ]judge|llm judge|"
                  r"gemini 3\.\d.{0,40}(?:judge|evaluat|autorater)|"
                  r"who graded|grader trained it|"
                  r"generator and its reviewer|one model family wrote|"
                  r"played the patient.{0,40}graded|"
                  r"same automated rubric pipeline",
            severity="critical",
            description="Teacher, patient simulator, and examiner share a model family — measurement is contaminated.",
            standard="standard_1_literature_review",
            polarity_hint="either",
        ),
        FailurePattern(
            code="goodhart",
            title="Goodhart gaming of the metric",
            regex=r"goodhart|optimize(?:s|d)? its training signals|"
                  r"reward target|learns to optimize|"
                  r"optimize(?:s|d)? (?:the )?training signal",
            severity="major",
            description="The system is rewarded for optimizing the grader rather than independent clinical truth.",
            standard="standard_1_literature_review",
            polarity_hint="either",
        ),
        FailurePattern(
            code="automation_bias",
            title="Automation bias / over-reliance",
            regex=r"automation bias|over-relian\w*|decreased vigilance|"
                  r"inappropriate deference|negative synerg",
            severity="moderate",
            description="Human oversight degrades when algorithmic output looks confident.",
            standard="standard_3_uncertainty_disclosure",
            polarity_hint="either",
        ),
        FailurePattern(
            code="brittleness",
            title="Brittleness under perturbation",
            regex=r"brittl\w*|minor perturbation|answer choices are reordered|"
                  r"visual (?:elements|inputs) (?:are|were) (?:substituted|removed|replaced)",
            severity="moderate",
            description="Apparent competence collapses under small, clinically irrelevant changes.",
            standard="standard_1_literature_review",
            polarity_hint="either",
        ),
        FailurePattern(
            code="persuasiveness_not_correctness",
            title="Persuasiveness without correctness",
            regex=r"persuasiveness without.{0,40}correctness|"
                  r"no accuracy difference|"
                  r"preferred.{0,40}(completeness|overall clinical impression)|"
                  r"preferr\w+.{0,40}completeness|"
                  r"training against approval",
            severity="major",
            description="Preference or completeness scores rise while diagnostic accuracy does not.",
            standard="standard_3_uncertainty_disclosure",
            polarity_hint="either",
        ),
        FailurePattern(
            code="performative_humility",
            title="Rubric-scored / performative humility",
            regex=r"humility that is scored|deferral language is itself a reward|"
                  r"rubric (?:awards|item).{0,40}(?:humility|deferral)|"
                  r"appropriate deferral scored",
            severity="moderate",
            description="Epistemic humility is a reward target, so deferral language is performed rather than warranted.",
            standard="standard_3_uncertainty_disclosure",
            polarity_hint="either",
        ),
        FailurePattern(
            code="in_domain_validation",
            title="In-domain validation of the training signal",
            regex=r"in-domain results.{0,80}training signals|"
                  r"primarily validate that the agent",
            severity="moderate",
            description="Reported gains mainly show the agent learned its own reward, not external clinical validity.",
            standard="standard_1_literature_review",
            polarity_hint="either",
        ),
        FailurePattern(
            code="no_independent_examiner",
            title="No independent examiner",
            regex=r"no agreement coefficient|evaluator independent of teacher|"
                  r"one attending wrote the case|"
                  r"examiners did not train.{0,40}none",
            severity="major",
            description="Summative evaluation is not independent of the teacher — the milestone measures the attending.",
            standard="standard_2_source_hierarchy",
            polarity_hint="either",
        ),
        FailurePattern(
            code="self_preference_judge",
            title="LLM judges favoring their own lineage",
            regex=r"favor(?:ed|s)? (?:their|its) own (?:lineage|generations)|"
                  r"language-model judges favor|"
                  r"autorater favored the agent where physicians did not",
            severity="major",
            description="Language-model judges systematically prefer their own family's outputs.",
            standard="standard_2_source_hierarchy",
            polarity_hint="either",
        ),
    ]

    @staticmethod
    def analyze(text: str) -> MethodFailureResult:
        """Analyze `text` for asserted vs critiqued methodological failures."""
        findings: List[FailureFinding] = []
        if not text:
            return MethodFailureResult(0.0, 0.0, [])

        default_polarity = MethodologicalFailureAnalyzer._document_default_polarity(text)
        awareness_extra = 0.0
        for pattern in MethodologicalFailureAnalyzer.PATTERNS:
            match = pattern.compiled.search(text)
            if not match:
                continue
            window = MethodologicalFailureAnalyzer._window(text, match.start(), match.end())
            polarity = MethodologicalFailureAnalyzer._polarity(window, default_polarity)
            weight = MethodologicalFailureAnalyzer.SEVERITY_WEIGHT[pattern.severity]
            if polarity == "critiqued":
                weight *= 0.35
            elif MethodologicalFailureAnalyzer.DISCLOSURE_RE.search(window):
                awareness_extra += MethodologicalFailureAnalyzer.SEVERITY_WEIGHT[pattern.severity] * 0.45
            findings.append(
                FailureFinding(
                    code=pattern.code,
                    title=pattern.title,
                    severity=pattern.severity,
                    description=pattern.description,
                    standard=pattern.standard,
                    polarity=polarity,
                    evidence=window.strip(),
                    weight=weight,
                )
            )

        asserted = [f for f in findings if f.polarity == "asserted"]
        critiqued = [f for f in findings if f.polarity == "critiqued"]
        failure_score = min(100.0, sum(f.weight for f in asserted))
        awareness_score = min(
            100.0,
            sum(MethodologicalFailureAnalyzer.SEVERITY_WEIGHT[f.severity] * 0.9 for f in critiqued)
            + awareness_extra,
        )
        return MethodFailureResult(failure_score, awareness_score, findings)

    @staticmethod
    def _window(text: str, start: int, end: int, radius: int = 180) -> str:
        lo = max(0, start - radius)
        hi = min(len(text), end + radius)
        snippet = re.sub(r"\s+", " ", text[lo:hi])
        return snippet[:320]

    @staticmethod
    def _document_default_polarity(text: str) -> str:
        if MethodologicalFailureAnalyzer.LETTER_RE.search(text or ""):
            return "critiqued"
        if MethodologicalFailureAnalyzer.ASSERT_RE.search(text or ""):
            return "asserted"
        critique_n = len(MethodologicalFailureAnalyzer.CRITIQUE_RE.findall(text or ""))
        asserted_n = len(MethodologicalFailureAnalyzer.ASSERT_RE.findall(text or ""))
        return "critiqued" if critique_n >= max(1, asserted_n) else "asserted"

    @staticmethod
    def _polarity(window: str, default: str) -> str:
        first_person = bool(
            MethodologicalFailureAnalyzer.FIRST_PERSON_METHOD_RE.search(window)
            or MethodologicalFailureAnalyzer.ASSERT_RE.search(window)
        )
        critique = bool(MethodologicalFailureAnalyzer.CRITIQUE_RE.search(window))
        # Owning the method is an asserted use, even if a caveat sits nearby.
        if first_person:
            return "asserted"
        if critique:
            return "critiqued"
        return default
