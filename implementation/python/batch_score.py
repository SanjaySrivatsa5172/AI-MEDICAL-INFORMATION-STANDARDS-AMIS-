"""
Thin AMIS batch scorer.

Reuses AMISCalculator. No second schema, no sixth standard, no
engine changes. Classes expose static functions so a directory of
abstracts or locally downloaded PDFs can be scored into one table.

    PYTHONPATH=. python -m implementation.python.batch_score \
        examples/calculator/patient_sim_2025/manifest.json

PDFs are never written into the repository. Point --input-dir at a
local download folder, or score the committed public excerpts.

Author: S. Sanjay Srivatsa, MD
License: MIT
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from implementation.python.calculator import AMISCalculator, CalculatorResult


class BatchRow:
    """One paper's calculator payload flattened for a comparison table."""

    COLUMNS = (
        "id",
        "short_title",
        "access",
        "overall",
        "conformance",
        "compliant",
        "std1",
        "std2",
        "std3",
        "std4",
        "std5",
        "uncertainty",
        "certainty_excess",
        "method_failure",
        "method_awareness",
        "claim_count",
        "source_url",
    )

    @staticmethod
    def from_result(
        result: CalculatorResult,
        *,
        paper_id: str,
        short_title: str,
        access: str,
        source_url: str,
    ) -> Dict[str, Any]:
        payload = result.to_dict()
        scores = payload.get("standards_scores") or {}
        axes = payload.get("axes") or {}
        overall = payload.get("overall") or {}
        return {
            "id": paper_id,
            "short_title": short_title,
            "access": access,
            "overall": overall.get("score"),
            "conformance": overall.get("conformance_level"),
            "compliant": overall.get("compliant"),
            "std1": scores.get("standard_1_literature_review"),
            "std2": scores.get("standard_2_source_hierarchy"),
            "std3": scores.get("standard_3_uncertainty_disclosure"),
            "std4": scores.get("standard_4_dissent_labeling"),
            "std5": scores.get("standard_5_therapeutic_scope"),
            "uncertainty": (axes.get("uncertainty_calibration") or {}).get("score"),
            "certainty_excess": (axes.get("certainty_excess") or {}).get("score"),
            "method_failure": (axes.get("methodological_failure") or {}).get("score"),
            "method_awareness": (axes.get("methodological_awareness") or {}).get("score"),
            "claim_count": len(payload.get("claims") or []),
            "source_url": source_url,
            "payload": payload,
        }

    @staticmethod
    def markdown_table(rows: List[Dict[str, Any]]) -> str:
        header = (
            "| Paper | Overall | Std1 | Std2 | Std3 | Std4 | Std5 | "
            "Uncertainty | Certainty excess | Method failure | Claims | ACCESS | Source |"
        )
        sep = "|---|---|---|---|---|---|---|---|---|---|---|---|---|"
        lines = [header, sep]
        for row in rows:
            lines.append(
                "| {short} | {overall:.2f} | {s1:.2f} | {s2:.2f} | {s3:.2f} | {s4:.2f} | {s5:.2f} | "
                "{unc:.0f} | {exc:.0f} | {fail:.0f} | {claims} | {access} | {url} |".format(
                    short=row["short_title"],
                    overall=float(row["overall"] or 0),
                    s1=float(row["std1"] or 0),
                    s2=float(row["std2"] or 0),
                    s3=float(row["std3"] or 0),
                    s4=float(row["std4"] or 0),
                    s5=float(row["std5"] or 0),
                    unc=float(row["uncertainty"] or 0),
                    exc=float(row["certainty_excess"] or 0),
                    fail=float(row["method_failure"] or 0),
                    claims=row["claim_count"],
                    access=row["access"],
                    url=row["source_url"],
                )
            )
        return "\n".join(lines)


class BatchScorer:
    """Score a manifest of papers with the existing calculator."""

    @staticmethod
    def load_manifest(path: Path) -> Dict[str, Any]:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if "papers" not in data:
            raise ValueError("Manifest must contain a 'papers' list.")
        return data

    @staticmethod
    def resolve_input(paper: Dict[str, Any], input_dir: Optional[Path]) -> Optional[Path]:
        """Prefer a local download (PDF/text); fall back to committed excerpt."""
        candidates: List[Path] = []
        local_name = paper.get("local_filename")
        excerpt = paper.get("excerpt")
        if input_dir and local_name:
            candidates.append(Path(input_dir) / local_name)
        if excerpt:
            excerpt_path = Path(excerpt)
            if not excerpt_path.is_absolute():
                excerpt_path = Path.cwd() / excerpt_path
            candidates.append(excerpt_path)
        for path in candidates:
            if path.exists():
                return path
        return None

    @staticmethod
    def score_paper(
        calculator: AMISCalculator,
        paper: Dict[str, Any],
        input_dir: Optional[Path],
    ) -> Dict[str, Any]:
        path = BatchScorer.resolve_input(paper, input_dir)
        if path is None:
            raise FileNotFoundError(
                f"No local file for {paper.get('id')}. "
                "Download the open PDF into --input-dir or keep the excerpt."
            )
        access = paper.get("access", "unknown")
        if path.suffix.lower() == ".pdf":
            access = paper.get("fulltext_access", access)
        elif access == "unknown":
            access = "excerpt"
        result = calculator.score_path(path)
        return BatchRow.from_result(
            result,
            paper_id=paper.get("id", path.stem),
            short_title=paper.get("short_title", path.stem),
            access=access,
            source_url=paper.get("source_url", ""),
        )

    @staticmethod
    def score_manifest(
        manifest_path: Path,
        input_dir: Optional[Path] = None,
    ) -> List[Dict[str, Any]]:
        manifest = BatchScorer.load_manifest(manifest_path)
        calculator = AMISCalculator()
        rows = []
        for paper in manifest["papers"]:
            rows.append(BatchScorer.score_paper(calculator, paper, input_dir))
        return rows

    @staticmethod
    def public_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Drop the bulky payload before writing JSON."""
        return [{k: v for k, v in row.items() if k != "payload"} for row in rows]


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Batch-score papers with the AMIS calculator.")
    parser.add_argument("manifest", help="JSON manifest with a papers list")
    parser.add_argument(
        "--input-dir",
        default=None,
        help="Local folder of downloaded PDFs/text (not committed).",
    )
    parser.add_argument("--json-out", default=None, help="Write flattened rows as JSON.")
    parser.add_argument("--table-only", action="store_true", help="Print only the markdown table.")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    rows = BatchScorer.score_manifest(Path(args.manifest), Path(args.input_dir) if args.input_dir else None)
    table = BatchRow.markdown_table(rows)
    if not args.table_only:
        print(table)
        print()
        for row in rows:
            print(f"## {row['short_title']}")
            print(
                f"overall={row['overall']:.3f} uncertainty={row['uncertainty']:.1f} "
                f"certainty_excess={row['certainty_excess']:.1f} "
                f"method_failure={row['method_failure']:.1f} claims={row['claim_count']} "
                f"ACCESS={row['access']}"
            )
            print()
    else:
        print(table)

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(BatchScorer.public_rows(rows), indent=2),
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
