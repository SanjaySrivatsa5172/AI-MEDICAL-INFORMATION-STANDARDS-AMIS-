const form = document.getElementById("score-form");
const textarea = document.getElementById("source-text");
const fileInput = document.getElementById("source-file");
const fileName = document.getElementById("file-name");
const scoreBtn = document.getElementById("score-btn");
const clearBtn = document.getElementById("clear-btn");
const formError = document.getElementById("form-error");
const results = document.getElementById("results");
const exampleRow = document.getElementById("example-row");

function showError(message) {
  formError.hidden = !message;
  formError.textContent = message || "";
}

function pct(value, max = 1) {
  const n = Number(value) || 0;
  return Math.round((n / max) * 100);
}

function toneClass(score, max = 100) {
  const p = score / max;
  if (p >= 0.75) return "good";
  if (p >= 0.5) return "mid";
  return "bad";
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

async function loadExamples() {
  const response = await fetch("/api/examples");
  if (!response.ok) return;
  const data = await response.json();
  data.examples.forEach((example) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "example-btn";
    button.textContent = example.title;
    button.title = example.blurb;
    button.addEventListener("click", async () => {
      const detail = await fetch(`/api/examples/${example.slug}`);
      if (!detail.ok) {
        showError("Could not load the example.");
        return;
      }
      const body = await detail.json();
      textarea.value = body.text;
      fileInput.value = "";
      fileName.textContent = body.filename;
      showError("");
    });
    exampleRow.appendChild(button);
  });
}

function renderStandards(standards) {
  const list = document.getElementById("standards-list");
  list.innerHTML = standards.map((item) => {
    const width = pct(item.score, 1);
    return `
      <li>
        <div class="std-num">${item.number}</div>
        <div>
          <strong>${escapeHtml(item.name)}</strong>
          <div class="std-bar" aria-hidden="true"><span style="width:${width}%"></span></div>
        </div>
        <div class="std-score">${item.score.toFixed(2)}</div>
      </li>
    `;
  }).join("");
}

function renderAxes(axes) {
  const grid = document.getElementById("axes-grid");
  const cards = [
    axes.uncertainty_calibration,
    axes.certainty_excess,
    axes.methodological_failure,
    axes.methodological_awareness,
  ];
  grid.innerHTML = cards.map((axis) => `
    <article class="axis-card">
      <h3>${escapeHtml(axis.name)}</h3>
      <div class="axis-score">${axis.score.toFixed(0)} <span class="chip">${escapeHtml(axis.label)}</span></div>
      <p>${escapeHtml(axis.detail)}</p>
    </article>
  `).join("");
}

function renderClaims(claims) {
  const root = document.getElementById("claims-list");
  if (!claims.length) {
    root.innerHTML = "<p>No AI-specific medical claims were extracted. The document-level AMIS scores above still apply.</p>";
    return;
  }
  root.innerHTML = claims.map((item) => {
    const method = (item.method_findings || [])
      .map((finding) => `<span class="chip">${escapeHtml(finding.title)} · ${escapeHtml(finding.polarity)}</span>`)
      .join(" ");
    return `
      <article>
        <div class="claim-kind">${escapeHtml(item.claim.kind)}</div>
        <p class="claim-text">${escapeHtml(item.claim.claim_text)}</p>
        <div class="mini-scores">
          <span class="chip">AMIS ${item.overall_score.toFixed(2)}</span>
          <span class="chip">Uncertainty ${item.uncertainty_score.toFixed(0)}</span>
          <span class="chip">Method failure ${item.method_failure_score.toFixed(0)}</span>
          ${method}
        </div>
      </article>
    `;
  }).join("");
}

function renderList(id, items, mapper) {
  const node = document.getElementById(id);
  if (!items.length) {
    node.innerHTML = "<li>None detected.</li>";
    return;
  }
  node.innerHTML = items.map(mapper).join("");
}

function render(result) {
  results.hidden = false;
  const overall = Math.round((result.overall.score || 0) * 100);
  const dial = document.getElementById("overall-dial");
  document.getElementById("overall-score").textContent = overall;
  dial.classList.remove("good", "mid", "bad");
  dial.classList.add(toneClass(overall));
  document.getElementById("conformance-line").textContent =
    `Conformance: ${result.overall.conformance_level} · compliant=${result.overall.compliant}`;
  document.getElementById("doc-meta").textContent =
    `${result.document.source_kind} · ${result.document.char_count} characters · ${result.claims.length} AI claims`;
  document.getElementById("hero-disclaimer").textContent = result.calculator_disclaimer;
  renderStandards(result.standards);
  renderAxes(result.axes);
  renderClaims(result.claims);
  renderList("violations-list", result.violations, (item) =>
    `<li class="sev-${escapeHtml(item.severity)}"><strong>${escapeHtml(item.standard)}</strong> — ${escapeHtml(item.description)}</li>`
  );
  renderList("recommendations-list", result.recommendations, (item) =>
    `<li>${escapeHtml(item)}</li>`
  );
  renderList("sources-list", result.sources, (item) =>
    `<li>Tier ${item.tier}: ${escapeHtml(item.title || item.url)} — ${escapeHtml(item.tier_justification)}</li>`
  );
  const harm = result.harm || {};
  const harmItems = ["direct", "indirect", "epistemic", "systemic"]
    .filter((key) => harm[key])
    .map((key) => ({
      key,
      score: harm[key].score,
      level: harm[key].risk_level,
      explanation: harm[key].explanation,
    }));
  renderList("harm-list", harmItems, (item) =>
    `<li><strong>${escapeHtml(item.key)}</strong> ${item.score} (${escapeHtml(item.level)}) — ${escapeHtml(item.explanation)}</li>`
  );
  results.scrollIntoView({ behavior: "smooth", block: "start" });
}

fileInput.addEventListener("change", () => {
  fileName.textContent = fileInput.files[0] ? fileInput.files[0].name : "No file selected";
});

clearBtn.addEventListener("click", () => {
  form.reset();
  fileName.textContent = "No file selected";
  results.hidden = true;
  showError("");
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  showError("");
  const text = textarea.value.trim();
  const file = fileInput.files[0];
  if (!text && !file) {
    showError("Paste an abstract or upload a PDF/text file.");
    return;
  }
  const body = new FormData();
  if (text) body.append("text", text);
  if (file) body.append("file", file);
  scoreBtn.disabled = true;
  scoreBtn.textContent = "Scoring…";
  try {
    const response = await fetch("/api/score", { method: "POST", body });
    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload.detail || "Scoring failed.");
    }
    render(payload);
  } catch (error) {
    showError(error.message);
  } finally {
    scoreBtn.disabled = false;
    scoreBtn.textContent = "Score claims";
  }
});

loadExamples().catch(() => {});
