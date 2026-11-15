"""
AMIS document ingest — paste, plain text, and PDF.

Author: S. Sanjay Srivatsa, MD
License: MIT
"""

from __future__ import annotations

import io
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

from implementation.python.source_classifier import SourceClassifier


@dataclass
class IngestedDocument:
    """Normalized text plus extracted citation candidates."""

    text: str
    filename: Optional[str]
    source_kind: str  # paste | txt | pdf
    char_count: int
    sources: List[Dict] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "filename": self.filename,
            "source_kind": self.source_kind,
            "char_count": self.char_count,
            "sources": self.sources,
            "notes": list(self.notes),
        }


class DocumentIngest:
    """Load abstracts and papers into plain text."""

    MAX_CHARS = 80_000
    MAX_BYTES = 8 * 1024 * 1024
    MAX_PDF_PAGES = 16
    MAX_PDF_SECONDS = 10.0

    @staticmethod
    def from_text(
        text: str,
        filename: Optional[str] = None,
        source_kind: str = "paste",
        notes: Optional[List[str]] = None,
    ) -> IngestedDocument:
        cleaned = DocumentIngest._normalize(text or "")
        extra = list(notes or [])
        if len(cleaned) > DocumentIngest.MAX_CHARS:
            cleaned = cleaned[: DocumentIngest.MAX_CHARS]
            extra.append(
                f"Scored the first {DocumentIngest.MAX_CHARS:,} characters so the free host can finish."
            )
        sources = CitationExtractor.extract(cleaned)
        return IngestedDocument(
            text=cleaned,
            filename=filename,
            source_kind=source_kind,
            char_count=len(cleaned),
            sources=sources,
            notes=extra,
        )

    @staticmethod
    def from_bytes(data: bytes, filename: str) -> IngestedDocument:
        if data is None:
            raise ValueError("Empty upload.")
        if len(data) > DocumentIngest.MAX_BYTES:
            raise ValueError("File exceeds the 8 MB upload limit.")
        name = filename or "upload"
        suffix = Path(name).suffix.lower()
        notes: List[str] = []
        if suffix == ".pdf" or data[:5] == b"%PDF-":
            text, notes = DocumentIngest._pdf_to_text(data)
            kind = "pdf"
        elif suffix in {".txt", ".md", ".text", ""}:
            text = DocumentIngest._decode(data)
            kind = "txt"
        else:
            text = DocumentIngest._decode(data)
            kind = "txt"
        if not text.strip():
            raise ValueError("No extractable text was found in the upload.")
        return DocumentIngest.from_text(text, filename=name, source_kind=kind, notes=notes)

    @staticmethod
    def from_path(path: Path) -> IngestedDocument:
        data = Path(path).read_bytes()
        return DocumentIngest.from_bytes(data, Path(path).name)

    @staticmethod
    def _pdf_to_text(data: bytes) -> Tuple[str, List[str]]:
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise ValueError("PDF support requires the pypdf package.") from exc
        try:
            reader = PdfReader(io.BytesIO(data), strict=False)
        except Exception as exc:
            raise ValueError(f"Could not read that PDF ({exc}). Try a text export or the example excerpt.") from exc
        if getattr(reader, "is_encrypted", False):
            raise ValueError("This PDF is encrypted. Export an unlocked copy or paste the abstract.")
        total = len(reader.pages)
        limit = min(total, DocumentIngest.MAX_PDF_PAGES)
        deadline = time.monotonic() + DocumentIngest.MAX_PDF_SECONDS
        pages: List[str] = []
        notes: List[str] = []
        for index in range(limit):
            if time.monotonic() > deadline:
                notes.append(
                    f"Stopped PDF extract after {index} of {total} pages so the free host can finish."
                )
                break
            try:
                pages.append(reader.pages[index].extract_text() or "")
            except Exception:
                pages.append("")
        else:
            if total > DocumentIngest.MAX_PDF_PAGES:
                notes.append(
                    f"Scored the first {DocumentIngest.MAX_PDF_PAGES} of {total} pages "
                    "(abstract, methods, and early results). Later pages are skipped on the free host."
                )
        text = "\n".join(pages)
        if not text.strip() and total:
            raise ValueError(
                "This PDF has no extractable text (likely a scan). Use a text PDF or paste the abstract."
            )
        return text, notes

    @staticmethod
    def _decode(data: bytes) -> str:
        for encoding in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
            try:
                return data.decode(encoding)
            except UnicodeDecodeError:
                continue
        return data.decode("utf-8", errors="replace")

    @staticmethod
    def _normalize(text: str) -> str:
        replacements = {
            "\u2018": "'",
            "\u2019": "'",
            "\u201c": '"',
            "\u201d": '"',
            "\u2013": "-",
            "\u2014": "-",
            "\u00a0": " ",
        }
        for src, dst in replacements.items():
            text = text.replace(src, dst)
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        return text.strip()


class CitationExtractor:
    """Pull URLs and named medical sources for SourceClassifier."""

    MAX_SOURCES = 40
    URL_RE = re.compile(r"https?://[^\s\]\)<>\"']+", re.IGNORECASE)
    DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)

    NAMED_SOURCES = {
        "cochrane": ("https://www.cochranelibrary.com/", "Cochrane"),
        "world health organization": ("https://www.who.int/", "WHO"),
        "nice guideline": ("https://www.nice.org.uk/", "NICE"),
        "new england journal": ("https://www.nejm.org/", "NEJM"),
        "nejm": ("https://www.nejm.org/", "NEJM"),
        "the lancet": ("https://www.thelancet.com/", "The Lancet"),
        "lancet": ("https://www.thelancet.com/", "The Lancet"),
        "jama": ("https://jamanetwork.com/", "JAMA"),
        "bmj": ("https://www.bmj.com/", "BMJ"),
        "nature": ("https://www.nature.com/", "Nature"),
        "science": ("https://www.science.org/", "Science"),
        "pubmed": ("https://pubmed.ncbi.nlm.nih.gov/", "PubMed"),
        "cdc": ("https://www.cdc.gov/", "CDC"),
        "arxiv": ("https://arxiv.org/", "arXiv preprint"),
        "youtube": ("https://www.youtube.com/", "YouTube"),
        "tiktok": ("https://www.tiktok.com/", "TikTok"),
        "reddit": ("https://www.reddit.com/", "Reddit"),
    }

    @staticmethod
    def extract(text: str) -> List[Dict]:
        classifier = SourceClassifier()
        found: List[Dict] = []
        seen = set()

        for match in CitationExtractor.URL_RE.finditer(text or ""):
            if len(found) >= CitationExtractor.MAX_SOURCES:
                break
            url = match.group(0).rstrip(".,;:)")
            CitationExtractor._add(found, seen, classifier, url, url)

        for match in CitationExtractor.DOI_RE.finditer(text or ""):
            if len(found) >= CitationExtractor.MAX_SOURCES:
                break
            doi = match.group(0).rstrip(".,;:)")
            url = f"https://doi.org/{doi}"
            CitationExtractor._add(found, seen, classifier, url, f"DOI {doi}")

        lowered = (text or "").lower()
        for name, (url, title) in CitationExtractor.NAMED_SOURCES.items():
            if name in lowered:
                CitationExtractor._add(found, seen, classifier, url, title)

        return found

    @staticmethod
    def _add(found: List[Dict], seen: set, classifier: SourceClassifier, url: str, title: str) -> None:
        key = CitationExtractor._host(url) + "|" + title.lower()
        if key in seen:
            return
        seen.add(key)
        classification = classifier.classify(url, context=title)
        found.append(
            {
                "url": url,
                "title": title,
                "tier": classification.level,
                "tier_justification": classification.justification,
            }
        )

    @staticmethod
    def _host(url: str) -> str:
        try:
            return urlparse(url).netloc.replace("www.", "")
        except Exception:
            return url
