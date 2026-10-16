#!/usr/bin/env node
/**
 * Builds the reference-library outputs from library.json:
 *   1. dashboard.html — self-contained dashboard (template + inlined data)
 *   2. obsidian/PATIENT FACING AI TRIAGE SAFETY/ — one Obsidian note per
 *      reference plus an index note. The folder is a generated mirror and is
 *      wiped and rewritten on every build.
 *
 * Usage: node reference-library/build.js
 */
const fs = require("fs");
const path = require("path");

const ROOT = __dirname;
const VAULT_DIR = path.join(ROOT, "obsidian", "PATIENT FACING AI TRIAGE SAFETY");

const lib = JSON.parse(fs.readFileSync(path.join(ROOT, "library.json"), "utf8"));
const { meta, references } = lib;

/* ---------- 1. Dashboard ---------- */
const template = fs.readFileSync(path.join(ROOT, "dashboard-template.html"), "utf8");
const marker = "/*__LIBRARY_JSON__*/ null";
if (!template.includes(marker)) {
  console.error("build.js: data marker not found in dashboard-template.html");
  process.exit(1);
}
const inlined = JSON.stringify(lib).replace(/</g, "\\u003c");
fs.writeFileSync(path.join(ROOT, "dashboard.html"), template.replace(marker, inlined));
console.log(`dashboard.html written (${references.length} references)`);

/* ---------- 2. Obsidian vault mirror ---------- */
const TOPIC_LABELS = {
  "emergency-triage-ai": "Emergency triage AI",
  "patient-facing-ai": "Patient-facing AI",
  "physician-evaluation": "Physician evaluation",
  "benchmark-methodology": "Benchmark methodology",
  "ai-safety-failure-modes": "AI safety failure modes",
  "triage-standards": "Triage standards",
  "policy-regulation": "Policy & regulation",
  "medical-education-assessment": "Assessment methodology",
};

const sanitize = (s) =>
  s
    .replace(/[\\/:*?"<>|#^\[\]]/g, "")
    .replace(/\s+/g, " ")
    .trim();

const firstAuthorLast = (authors) => {
  const first = (authors || "Unknown").split(",")[0].trim();
  const parts = first.split(/\s+/);
  // "Ayers JW" style → "Ayers"; "J. W. Ayers" style → last token
  return /^[A-Z][a-z]/.test(parts[0]) && parts.length <= 3 ? parts[0] : parts[parts.length - 1];
};

const noteName = (r) => {
  let t = sanitize(r.title);
  if (t.length > 70) t = t.slice(0, 70).replace(/\s\S*$/, "") + "…";
  return sanitize(`${firstAuthorLast(r.authors)} ${r.year} — ${t}`) + ".md";
};

const yq = (s) => `"${String(s ?? "").replace(/"/g, '\\"')}"`;

fs.rmSync(VAULT_DIR, { recursive: true, force: true });
fs.mkdirSync(VAULT_DIR, { recursive: true });

const INDEX_NAME = "00 INDEX — Patient-Facing AI Triage Safety.md";
const nameOf = new Map();
for (const r of references) {
  let n = noteName(r);
  // guarantee uniqueness
  let i = 2;
  while ([...nameOf.values()].includes(n)) n = n.replace(/\.md$/, ` (${i++}).md`);
  nameOf.set(r, n);

  const tags = [...r.topics, r.tier, ...(r.design_overlap ? ["design-overlap", "critical"] : [])];
  const fm = [
    "---",
    `title: ${yq(r.title)}`,
    `authors: ${yq(r.authors)}`,
    `journal: ${yq(r.journal)}`,
    `year: ${r.year}`,
    `doi: ${yq(r.doi || "")}`,
    `pmid: ${yq(r.pmid || "")}`,
    `url: ${yq(r.url)}`,
    `type: ${yq(r.type)}`,
    `tier: ${yq(r.tier)}`,
    `design-overlap: ${!!r.design_overlap}`,
    `date-added: ${r.date_added}`,
    `source: ${yq(r.source)}`,
    `tags: [${tags.join(", ")}]`,
    "---",
  ].join("\n");

  const body = [
    "",
    `# ${r.title}`,
    "",
    `**${r.authors}** — *${r.journal}* (${r.year})`,
    "",
    ...(r.design_overlap
      ? ["> [!warning] Critical — design overlap", "> This work overlaps the study design of the Cedars-Sinai protocol. Reference explicitly in methods differentiation.", ""]
      : []),
    `> [!note] Clinical relevance`,
    `> ${r.relevance || "—"}`,
    "",
    `**Link:** ${r.url}`,
    ...(r.doi ? [`**DOI:** \`${r.doi}\``] : []),
    ...(r.pmid ? [`**PMID:** \`${r.pmid}\``] : []),
    "",
    `Topics: ${r.topics.map((t) => TOPIC_LABELS[t] || t).join(" · ")}`,
    "",
    `Index: [[${INDEX_NAME.replace(/\.md$/, "")}]]`,
    "",
  ].join("\n");

  fs.writeFileSync(path.join(VAULT_DIR, n), fm + body);
}

/* Index note */
const link = (r) => `[[${nameOf.get(r).replace(/\.md$/, "")}]]`;
const overlap = references.filter((r) => r.design_overlap).sort((a, b) => b.year - a.year);
const byTopic = {};
for (const r of references) for (const t of r.topics) (byTopic[t] ||= []).push(r);

const indexLines = [
  "---",
  `title: "Patient-Facing AI Triage Safety — Reference Index"`,
  `last-updated: ${meta.last_updated}`,
  `total-references: ${references.length}`,
  "tags: [reference-index, ai-triage-safety]",
  "---",
  "",
  "# Patient-Facing AI Triage Safety — Reference Index",
  "",
  `Supporting the Cedars-Sinai protocol **${meta.project}** (PI: ${meta.pi}).`,
  "",
  `> Core question: *${meta.core_question}*`,
  "",
  `Updated daily by automated scan. Last scan: **${meta.last_updated}** · ${references.length} references.`,
  meta.dashboard_url ? `\nLive dashboard: ${meta.dashboard_url}` : "",
  "",
  "> [!info] Generated folder",
  "> This folder is regenerated on every scan. Keep personal annotations in separate notes that link here, not inside these files.",
  "",
  ...((meta.alerts || []).filter((a) => !a.resolved).length
    ? [
        "## 🚨 Active urgent alerts",
        "",
        ...(meta.alerts || [])
          .filter((a) => !a.resolved)
          .map((a) => `- **${a.date} — ${a.headline}** — ${a.detail}${a.url ? ` (${a.url})` : ""}`),
        "",
      ]
    : []),
  "## ⚠ Critical — design overlap",
  "",
  ...(overlap.length ? overlap.map((r) => `- ${link(r)} — *${r.journal}* ${r.year}`) : ["- (none flagged)"]),
  "",
];
for (const t of Object.keys(TOPIC_LABELS)) {
  const rows = (byTopic[t] || []).sort((a, b) => b.year - a.year);
  if (!rows.length) continue;
  indexLines.push(`## ${TOPIC_LABELS[t]}`, "");
  for (const r of rows) indexLines.push(`- ${link(r)} (${r.year})${r.tier === "core" ? " — **core**" : ""}`);
  indexLines.push("");
}
fs.writeFileSync(path.join(VAULT_DIR, INDEX_NAME), indexLines.join("\n"));
console.log(`Obsidian mirror written: ${references.length} notes + index in "${path.relative(process.cwd(), VAULT_DIR)}"`);
