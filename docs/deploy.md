# Deploy the AMIS Claim Calculator

The scorer is FastAPI. It needs a host that can accept a pasted abstract or an uploaded PDF. GitHub Pages can only serve the static landing in `site/`.

## One-click (Render, free plan)

Sign in with GitHub, then open:

**https://render.com/deploy?repo=https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-)

The Blueprint (`render.yaml`) created the free Python web service `amis-claim-calculator`. The public citeable URL is live:

**https://amis-claim-calculator.onrender.com**

Open that URL. The **Access** bar has a **Calculator** tab and an **Onboarding** tab
([/onboarding](https://amis-claim-calculator.onrender.com/onboarding)). Load an example or
upload a PDF, and cite the scorer in the letter. Free instances sleep after about 15 minutes
idle; the first request after sleep is slow.

How to use and how to read a score: [docs/calculator_onboarding.md](calculator_onboarding.md).

Manual path if the button is not used:

1. [render.com](https://render.com) → Sign in with GitHub.
2. New → Blueprint → this repository. Or New → Web Service → this repository.
3. Use `render.yaml` (native Python, `$PORT`, health check `/api/health`). Free plan is enough.
4. Do not override `PORT`. Render sets it.

Free instances sleep after about 15 minutes idle. The first request after sleep is slow; that is expected.

## Docker (optional)

```bash
docker build -t amis-calculator .
docker run --rm -p 8765:8765 amis-calculator
```

`Dockerfile` remains the local / CI image. Render no longer builds it.

## Source

https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-

Local run: `python3 -m implementation.web.app`
