"""
AMIS Claim Extractor

Pulls candidate AI-related medical claims from abstracts and papers.
Does not treat every sentence as a claim: the filter is performance,
safety, diagnostic/therapeutic, evaluation, and epistemic-risk language.

Author: S. Sanjay Srivatsa, MD
License: MIT
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class ExtractedClaim:
    """A candidate AI-related medical claim."""

    claim_text: str
    kind: str
    score: float
    start: int
    end: int
    uncertainty_markers: List[str] = field(default_factory=list)
    overconfident_markers: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "claim_text": self.claim_text,
            "kind": self.kind,
            "score": round(self.score, 3),
            "uncertainty_markers": self.uncertainty_markers,
            "overconfident_markers": self.overconfident_markers,
        }


class ClaimExtractor:
    """Extract AI medical claims using deterministic lexical rules."""

    AI_RE = re.compile(
        r"\b("
        r"ai|a\.i\.|artificial intelligence|machine learning|deep learning|"
        r"language model|large language|llm|foundation model|frontier model|"
        r"neural network|multimodal|chatbot|algorithm(?:ic)?|"
        r"computer[- ]?(?:aided|assisted)|cad system|autorater|"
        r"residencyrl|reinforcement learning|"
        r"model(?:s)?|agent(?:s)?|system(?:s)?"
        r")\b",
        re.IGNORECASE,
    )

    MEDICAL_AI_RE = re.compile(
        r"\b("
        r"ai[- ]assisted|ai[- ]generated|medical ai|clinical ai|"
        r"diagnostic (?:ai|model|algorithm)|therapeutic (?:ai|algorithm)|"
        r"health(?:care)? (?:chatbot|llm|model)"
        r")\b",
        re.IGNORECASE,
    )

    KIND_PATTERNS = {
        "performance": re.compile(
            r"\b(accurac\w*|auc|auroc|sensitivity|specificity|f1|"
            r"outperform\w*|benchmark|performance|state-of-the-art|"
            r"surpass\w*|detect(?:s|ed|ion)|predict\w*)\b",
            re.IGNORECASE,
        ),
        "safety": re.compile(
            r"\b(safe(?:ty)?|harm|adverse|patient safety|risk(?:s)?|"
            r"hallucin\w*|over-?relian\w*|automation bias|deskilling|"
            r"epistemic (?:risk|harm|vigilance|humility))\b",
            re.IGNORECASE,
        ),
        "diagnostic": re.compile(
            r"\b(diagnos\w*|triage|differential|radiolog\w*|"
            r"imaging|screening|lesion|patholog\w*)\b",
            re.IGNORECASE,
        ),
        "therapeutic": re.compile(
            r"\b(therapeut\w*|treatment|prescribe|dosing|medication|"
            r"regimen|intervention|should (?:take|stop|start))\b",
            re.IGNORECASE,
        ),
        "evaluation": re.compile(
            r"\b(evaluat\w*|grader|autorater|rubric|reward|"
            r"goodhart|contaminat\w*|independent examin|"
            r"in-domain|blinded|inter[- ]rater|kappa|intraclass)\b",
            re.IGNORECASE,
        ),
    }

    UNCERTAINTY_RE = re.compile(
        r"\b(may|might|could|suggests?|indicates?|preliminary|"
        r"limited evidence|not well established|uncertain|"
        r"mixed (?:evidence|results)|insufficient|"
        r"narrative analysis|limitations?|risks? creating|"
        r"paradox(?:ically)?|appears? to|often)\b",
        re.IGNORECASE,
    )

    OVERCONFIDENT_RE = re.compile(
        r"\b(definitely|certainly|proven to|guaranteed|always works|"
        r"100%|will cure|is known to cure|miracle|breakthrough|"
        r"eliminated completely|the only (?:correct )?(?:way|treatment))\b",
        re.IGNORECASE,
    )

    REFERENCE_LINE_RE = re.compile(
        r"^\s*\d+\.\s+[A-Z].{10,}\.\s+\d{4}",
    )

    MAX_CLAIMS = 20
    MIN_LEN = 40
    MAX_LEN = 520

    @staticmethod
    def extract(text: str, max_claims: Optional[int] = None) -> List[ExtractedClaim]:
        """Return ranked AI-related medical claims from `text`."""
        body = ClaimExtractor._strip_references(text or "")
        sentences = ClaimExtractor._split_sentences(body)
        ranked: List[ExtractedClaim] = []

        for sentence, start, end in sentences:
            claim = ClaimExtractor._score_sentence(sentence, start, end)
            if claim is not None:
                ranked.append(claim)

        ranked.sort(key=lambda c: c.score, reverse=True)
        limit = max_claims if max_claims is not None else ClaimExtractor.MAX_CLAIMS
        return ranked[:limit]

    @staticmethod
    def _strip_references(text: str) -> str:
        parts = re.split(r"\n\s*References\s*\n", text, maxsplit=1, flags=re.IGNORECASE)
        return parts[0]

    @staticmethod
    def _split_sentences(text: str) -> List[Tuple[str, int, int]]:
        """Split on sentence boundaries while keeping offsets."""
        pieces: List[Tuple[str, int, int]] = []
        # Also split on newlines that look like paragraph breaks.
        spans = re.split(r"(?<=[.!?])\s+|\n{2,}", text)
        cursor = 0
        for raw in spans:
            idx = text.find(raw, cursor)
            if idx < 0:
                idx = cursor
            cleaned = re.sub(r"\s+", " ", raw).strip()
            cursor = idx + len(raw)
            if not cleaned:
                continue
            if ClaimExtractor.REFERENCE_LINE_RE.match(cleaned):
                continue
            if len(cleaned) < ClaimExtractor.MIN_LEN:
                continue
            if len(cleaned) > ClaimExtractor.MAX_LEN:
                cleaned = cleaned[: ClaimExtractor.MAX_LEN].rsplit(" ", 1)[0] + "…"
            pieces.append((cleaned, idx, idx + len(raw)))
        return pieces

    @staticmethod
    def _score_sentence(sentence: str, start: int, end: int) -> Optional[ExtractedClaim]:
        ai_hits = ClaimExtractor.AI_RE.findall(sentence)
        medical_ai = bool(ClaimExtractor.MEDICAL_AI_RE.search(sentence))
        kinds = [
            name
            for name, pattern in ClaimExtractor.KIND_PATTERNS.items()
            if pattern.search(sentence)
        ]
        if not kinds:
            return None
        # Require an AI/system cue unless the sentence is explicitly "medical AI".
        weak_system_only = (
            ai_hits
            and all(h.lower() in {"model", "models", "system", "systems", "agent", "agents"} for h in ai_hits)
        )
        if not medical_ai and (not ai_hits or (weak_system_only and "evaluation" not in kinds and "performance" not in kinds)):
            if not medical_ai:
                # Keep sentences that pair a generic system word with a strong eval/performance claim
                # only when another AI cue or medical-AI phrase is present.
                if not ai_hits:
                    return None
                if weak_system_only and not any(k in kinds for k in ("performance", "evaluation", "safety")):
                    return None

        kind = kinds[0]
        score = 1.0 + 0.35 * len(kinds) + 0.15 * min(3, len(ai_hits))
        if medical_ai:
            score += 0.6
        if 80 <= len(sentence) <= 320:
            score += 0.25

        uncertainty = [m.group(0).lower() for m in ClaimExtractor.UNCERTAINTY_RE.finditer(sentence)]
        overconfident = [m.group(0).lower() for m in ClaimExtractor.OVERCONFIDENT_RE.finditer(sentence)]
        return ExtractedClaim(
            claim_text=sentence,
            kind=kind,
            score=score,
            start=start,
            end=end,
            uncertainty_markers=sorted(set(uncertainty)),
            overconfident_markers=sorted(set(overconfident)),
        )
