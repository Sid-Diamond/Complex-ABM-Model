"""Create dependency-free HTML/SVG animations for the temporal networks."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data" / "IPUM" / "dynamic_networks"
OUTPUT_DIR = DATA_DIR / "visualisations"
W, H, PAD = 1100, 760, 45


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Temporal occupation network</title>
<style>
  body { font-family: system-ui, sans-serif; margin: 20px; color: #172033; }
  .controls { display: flex; flex-wrap: wrap; gap: 16px; align-items: center; margin: 12px 0; }
  label { white-space: nowrap; }
  input[type=range] { vertical-align: middle; }
  button { padding: 5px 12px; }
  #status { font-family: ui-monospace, monospace; margin: 8px 0; }
  svg { border: 1px solid #ccd3df; background: #fbfcfe; max-width: 100%; }
  .edge { stroke: #718096; stroke-linecap: round; }
  .node { stroke: #172033; stroke-width: 0.7; fill: #3182ce; }
  .node.zero { fill: #d97706; }
  .legend { font-size: 13px; color: #4a5568; }
</style>
</head>
<body>
<h1>Time-evolving occupation network</h1>
<div class="controls">
  <button id="play">Play</button>
  <label>Month <input id="month" type="range" min="0" max="0" value="0"></label>
  <label>Edge threshold <input id="threshold" type="range" min="0" max="0.1" step="0.001" value="0.01"></label>
  <label>Network <select id="variant"><option value="occupation_only">Occupation only</option><option value="with_0000">Include 0000</option></select></label>
</div>
<div id="status"></div>
<div class="legend">Node size = observed share at the selected month. Edge opacity/width = empirical transition probability. Hover a node for its code and share.</div>
<svg id="chart" viewBox="0 0 1100 760" role="img" aria-label="Animated temporal occupation network"></svg>
<script>
const DATA = __DATA__;
const W = 1100, H = 760, PAD = 45;
const svg = document.getElementById('chart');
const monthInput = document.getElementById('month');
const thresholdInput = document.getElementById('threshold');
const variantInput = document.getElementById('variant');
const status = document.getElementById('status');
let playing = false, timer = null;

function position(code) {
  return DATA.positions[code];
}

function clearSvg() { while (svg.firstChild) svg.removeChild(svg.firstChild); }

function add(tag, attrs, parent = svg) {
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [key, value] of Object.entries(attrs)) el.setAttribute(key, value);
  parent.appendChild(el);
  return el;
}

function render() {
  const variant = variantInput.value;
  const frames = DATA[variant];
  const index = Number(monthInput.value);
  const frame = frames[index];
  const threshold = Number(thresholdInput.value);
  clearSvg();
  const defs = add('defs', {});
  const marker = add('marker', { id: 'arrow', markerWidth: 7, markerHeight: 7, refX: 6, refY: 3.5, orient: 'auto' }, defs);
  add('path', { d: 'M0,0 L7,3.5 L0,7 z', fill: '#718096' }, marker);
  const edgeGroup = add('g', {});
  let shownEdges = 0;
  for (const edge of frame.edges) {
    if (edge.p < threshold) continue;
    const a = position(edge.a), b = position(edge.b);
    if (!a || !b) continue;
    const line = add('line', { x1: a[0], y1: a[1], x2: b[0], y2: b[1], class: 'edge', 'stroke-width': String(0.5 + 5 * Math.min(edge.p, 0.2)), 'stroke-opacity': String(Math.min(0.85, 0.15 + 5 * edge.p)), 'marker-end': 'url(#arrow)' }, edgeGroup);
    const title = add('title', {}, line);
    title.textContent = `${edge.a} → ${edge.b}: ${edge.count} observations; p=${edge.p.toFixed(4)}`;
    shownEdges++;
  }
  const nodeGroup = add('g', {});
  for (const node of frame.nodes) {
    const p = position(node.code);
    if (!p) continue;
    const circle = add('circle', { cx: p[0], cy: p[1], r: String(3 + 25 * Math.sqrt(node.share)), class: node.code === '0000' ? 'node zero' : 'node' }, nodeGroup);
    const title = add('title', {}, circle);
    title.textContent = `${node.code}: ${node.count} observations; share=${node.share.toFixed(4)}`;
  }
  const edgeLabel = threshold > 0 ? `threshold=${threshold.toFixed(3)}` : 'all edges';
  status.textContent = `${variant} | ${frame.label} → ${frame.next || 'no next month'} | nodes=${frame.nodes.length} | shown edges=${shownEdges} | ${edgeLabel}`;
}

function setFrame(value) { monthInput.value = value; render(); }
function advance() { setFrame((Number(monthInput.value) + 1) % DATA[variantInput.value].length); }
document.getElementById('play').addEventListener('click', () => {
  playing = !playing;
  document.getElementById('play').textContent = playing ? 'Pause' : 'Play';
  if (playing) timer = setInterval(advance, 900); else clearInterval(timer);
});
monthInput.addEventListener('input', render);
thresholdInput.addEventListener('input', render);
variantInput.addEventListener('change', () => { monthInput.max = DATA[variantInput.value].length - 1; monthInput.value = 0; render(); });
monthInput.max = DATA[variantInput.value].length - 1;
render();
</script>
</body>
</html>
"""


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def build_variant(variant: str) -> list[dict[str, object]]:
    nodes = read_csv(DATA_DIR / f"{variant}_nodes.csv")
    edges = read_csv(DATA_DIR / f"{variant}_edges.csv")
    frames: dict[str, dict[str, object]] = {}
    for row in nodes:
        label = f"{row['year']}-{int(row['month']):02d}"
        frames.setdefault(label, {"label": label, "next": None, "nodes": [], "edges": []})
        frames[label]["nodes"].append({"code": row["occ"], "count": int(row["node_count"]), "share": float(row["node_share"])})
    for row in edges:
        label = f"{row['origin_year']}-{int(row['origin_month']):02d}"
        next_label = f"{row['destination_year']}-{int(row['destination_month']):02d}"
        frames.setdefault(label, {"label": label, "next": next_label, "nodes": [], "edges": []})
        frames[label]["next"] = next_label
        frames[label]["edges"].append({"a": row["origin_occ"], "b": row["destination_occ"], "count": int(row["transition_count"]), "p": float(row["transition_probability"])})
    return [frames[label] for label in sorted(frames)]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    codes = set()
    for variant in ("occupation_only", "with_0000"):
        for row in read_csv(DATA_DIR / f"{variant}_nodes.csv"):
            codes.add(row["occ"])
    ordered = sorted(codes)
    columns = 30
    rows = math.ceil(len(ordered) / columns)
    positions = {
        code: [PAD + (index % columns) * ((W - 2 * PAD) / max(columns - 1, 1)),
               PAD + (index // columns) * ((H - 2 * PAD) / max(rows - 1, 1))]
        for index, code in enumerate(ordered)
    }
    data = {"positions": positions, "occupation_only": build_variant("occupation_only"), "with_0000": build_variant("with_0000")}
    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(data, separators=(",", ":")))
    output = OUTPUT_DIR / "temporal_networks.html"
    output.write_text(html, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
