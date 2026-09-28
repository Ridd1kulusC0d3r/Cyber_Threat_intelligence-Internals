const state = { resources: [], stats: {} };

const $ = (id) => document.getElementById(id);
const norm = (value) => String(value ?? "").toLowerCase();

function unique(field) {
  return [...new Set(state.resources.map((r) => r[field]).filter(Boolean))].sort();
}

function fillSelect(id, values) {
  const select = $(id);
  for (const value of values) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.appendChild(option);
  }
}

function renderStats() {
  const stats = state.stats;
  const items = [
    ["Resources", stats.resources ?? state.resources.length],
    ["Categories", stats.categories ?? unique("category").length],
    ["Verified", stats.verified ?? 0],
    ["Active", stats.active ?? 0],
    ["Research", stats.research ?? 0],
    ["Watchlist", stats.watchlist ?? 0],
  ];
  $("stats").innerHTML = items.map(([label, value]) =>
    `<div class="stat"><strong>${value}</strong><span>${label}</span></div>`
  ).join("");
}

function matches(resource) {
  const q = norm($("search").value).trim();
  const haystack = [
    resource.name, resource.use, resource.owner, resource.category,
    resource.evidence_level, resource.verification, resource.lifecycle,
    ...(resource.tags || []), ...(resource.intelligence_levels || [])
  ].map(norm).join(" ");

  return (!q || haystack.includes(q))
    && (!$("category").value || resource.category === $("category").value)
    && (!$("sourceClass").value || resource.source_class === $("sourceClass").value)
    && (!$("evidence").value || resource.evidence_level === $("evidence").value)
    && (!$("lifecycle").value || resource.lifecycle === $("lifecycle").value)
    && (!$("verification").value || resource.verification === $("verification").value);
}

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[c]);
}

function card(resource) {
  const name = escapeHtml(resource.name);
  const title = resource.url
    ? `<a href="${escapeHtml(resource.url)}" target="_blank" rel="noopener noreferrer">${name}</a>`
    : name;
  const badges = [
    `Class ${resource.source_class}`,
    resource.category,
    resource.evidence_level,
    resource.lifecycle,
    resource.verification
  ].filter(Boolean).map((b) =>
    `<span class="badge ${escapeHtml(resource.verification)}">${escapeHtml(b)}</span>`
  ).join("");
  const tags = (resource.tags || []).map((t) =>
    `<span class="tag">${escapeHtml(t)}</span>`
  ).join("");

  return `<article class="card">
    <div class="card-head">
      <div>
        <h2>${title}</h2>
        <div class="meta">${badges}</div>
      </div>
      <span class="tag">${escapeHtml(resource.owner || "")}</span>
    </div>
    <p class="use">${escapeHtml(resource.use || "")}</p>
    <div class="tags">${tags}</div>
    ${resource.notes ? `<p class="notes">${escapeHtml(resource.notes)}</p>` : ""}
  </article>`;
}

function render() {
  const filtered = state.resources.filter(matches);
  $("resultCount").textContent = `${filtered.length} of ${state.resources.length} resources`;
  $("catalog").innerHTML = filtered.length
    ? filtered.map(card).join("")
    : '<div class="empty">No resources match these filters.</div>';
}

function reset() {
  $("search").value = "";
  ["category", "sourceClass", "evidence", "lifecycle", "verification"].forEach((id) => $(id).value = "");
  render();
}

async function init() {
  const [resourcesResponse, statsResponse] = await Promise.all([
    fetch("data/resources.json"),
    fetch("data/stats.json")
  ]);
  if (!resourcesResponse.ok) throw new Error("Unable to load catalog data.");
  state.resources = await resourcesResponse.json();
  state.stats = statsResponse.ok ? await statsResponse.json() : {};

  fillSelect("category", unique("category"));
  fillSelect("evidence", unique("evidence_level"));
  fillSelect("lifecycle", unique("lifecycle"));
  fillSelect("verification", unique("verification"));
  renderStats();
  render();

  $("search").addEventListener("input", render);
  ["category", "sourceClass", "evidence", "lifecycle", "verification"].forEach((id) =>
    $(id).addEventListener("change", render)
  );
  $("reset").addEventListener("click", reset);
}

init().catch((error) => {
  $("catalog").innerHTML = `<div class="empty">${escapeHtml(error.message)}</div>`;
});
