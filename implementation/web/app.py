"""
AMIS Claim Calculator — local web app.

Run from the repository root:

    pip install -r implementation/web/requirements.txt
    python -m implementation.web.app

Then open http://127.0.0.1:8765
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

# Allow `python implementation/web/app.py` as well as module invocation.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from implementation.python.calculator import AMISCalculator, EvidenceAppendix

WEB_DIR = Path(__file__).resolve().parent
STATIC_DIR = WEB_DIR / "static"
EXAMPLES_DIR = REPO_ROOT / "examples" / "calculator"

calculator = AMISCalculator()
app = FastAPI(
    title="AMIS Claim Calculator",
    description="Score AI medical claims against the five AMIS standards.",
    version="1.0.0",
)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class TextScoreRequest(BaseModel):
    text: str = Field(..., min_length=1)
    filename: Optional[str] = None


EXAMPLES = {
    "productive-uncertainty": {
        "title": "Srivatsa abstract — productive uncertainty",
        "file": "srivatsa_abstract.txt",
        "blurb": "Gold-reference tone: epistemic humility, narrative analysis, no prescription.",
    },
    "residencyrl-letter": {
        "title": "ResidencyRL letter — contaminated grading",
        "file": "residencyrl_letter.txt",
        "blurb": "Critiques self-grading, Goodhart, and persuasiveness without correctness.",
    },
    "overconfident-claims": {
        "title": "Overconfident AI claims (synthetic)",
        "file": "overconfident_ai_claims.txt",
        "blurb": "False certainty, Tier 5 citations, and therapeutic dosing — should fail.",
    },
}


@app.get("/")
def index() -> FileResponse:
    page = STATIC_DIR / "index.html"
    if not page.exists():
        raise HTTPException(status_code=500, detail="Calculator UI is missing.")
    return FileResponse(page)


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "service": "amis-claim-calculator"}


@app.get("/api/evidence")
def evidence() -> dict:
    return EvidenceAppendix.to_dict()


@app.get("/api/examples")
def list_examples() -> dict:
    return {
        "examples": [
            {"slug": slug, "title": meta["title"], "blurb": meta["blurb"]}
            for slug, meta in EXAMPLES.items()
        ]
    }


@app.get("/api/examples/{slug}")
def get_example(slug: str) -> dict:
    meta = EXAMPLES.get(slug)
    if not meta:
        raise HTTPException(status_code=404, detail="Unknown example.")
    path = EXAMPLES_DIR / meta["file"]
    if not path.exists():
        raise HTTPException(status_code=404, detail="Example file missing.")
    return {
        "slug": slug,
        "title": meta["title"],
        "blurb": meta["blurb"],
        "filename": meta["file"],
        "text": path.read_text(encoding="utf-8"),
    }


@app.post("/api/score")
async def score(
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
) -> dict:
    if file is not None and file.filename:
        data = await file.read()
        if data:
            try:
                result = calculator.score_upload(data, file.filename)
            except ValueError as exc:
                raise HTTPException(status_code=400, detail=str(exc)) from exc
            return result.to_dict()
    if text and text.strip():
        result = calculator.score_text(text, filename="paste")
        return result.to_dict()
    raise HTTPException(status_code=400, detail="Paste an abstract or upload a PDF/text file.")


@app.post("/api/score-json")
def score_json(payload: TextScoreRequest) -> dict:
    return calculator.score_text(payload.text, filename=payload.filename or "paste").to_dict()


def main() -> None:
    import uvicorn

    uvicorn.run(
        "implementation.web.app:app",
        host="127.0.0.1",
        port=8765,
        reload=False,
    )


if __name__ == "__main__":
    main()
