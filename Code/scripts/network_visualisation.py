"""Reusable NetworkX/Matplotlib views for monthly occupation networks."""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button, Slider


# Visual hyperparameters: adjust these before changing plotting logic.
NODE_SIZE_BASE = 3
NODE_SIZE_SCALE = 260
LABEL_COUNT = 15
LAYOUT_K = 0.55
LAYOUT_SCALE = 1.45
LAYOUT_LIMIT = 1.55


def load_variant(data_dir: Path, variant: str):
    nodes_by_month = defaultdict(list)
    edges_by_month = defaultdict(list)
    codes = set()
    with (data_dir / f"{variant}_nodes.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            month = f"{row['year']}-{int(row['month']):02d}"
            nodes_by_month[month].append({"code": row["occ"], "count": int(row["node_count"]), "share": float(row["node_share"])})
            codes.add(row["occ"])
    with (data_dir / f"{variant}_edges.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            month = f"{row['origin_year']}-{int(row['origin_month']):02d}"
            edges_by_month[month].append({"a": row["origin_occ"], "b": row["destination_occ"], "count": int(row["transition_count"]), "p": float(row["transition_probability"])})
            codes.update((row["origin_occ"], row["destination_occ"]))
    return nodes_by_month, edges_by_month, codes


def stable_layout(edges_by_month, codes):
    aggregate = nx.Graph()
    aggregate.add_nodes_from(codes)
    for edges in edges_by_month.values():
        for edge in edges:
            if edge["a"] != edge["b"]:
                old = aggregate.get_edge_data(edge["a"], edge["b"], {}).get("weight", 0)
                aggregate.add_edge(edge["a"], edge["b"], weight=old + math.log1p(edge["count"]))
    # Use the aggregate graph only to determine fixed positions. The monthly
    # frames then change edges and node sizes without the layout jumping.
    return nx.spring_layout(
        aggregate,
        seed=42,
        weight="weight",
        iterations=100,
        k=LAYOUT_K,
        scale=LAYOUT_SCALE,
    )


def draw_month(ax, month, nodes, edges, positions, threshold, variant):
    ax.clear()
    visible = [edge for edge in edges if edge["p"] >= threshold and edge["a"] != edge["b"]]
    graph = nx.DiGraph()
    graph.add_nodes_from(node["code"] for node in nodes)
    graph.add_edges_from((edge["a"], edge["b"]) for edge in visible)
    node_by_code = {node["code"]: node for node in nodes}
    segments = [[positions[e["a"]], positions[e["b"]]] for e in visible]
    if segments:
        from matplotlib.collections import LineCollection
        ax.add_collection(LineCollection(segments, colors="#64748b", alpha=0.35,
            linewidths=[0.5 + 7 * min(e["p"], 0.2) for e in visible]))
    for code in graph:
        x, y = positions[code]
        node = node_by_code.get(code, {"share": 0.0})
        ax.scatter(x, y, s=NODE_SIZE_BASE + NODE_SIZE_SCALE * math.sqrt(node["share"]),
                   c="#d97706" if code == "0000" else "#3182ce",
                   edgecolors="#172033", linewidths=0.4, alpha=0.86, zorder=2)
    for node in sorted(nodes, key=lambda item: item["share"], reverse=True)[:LABEL_COUNT]:
        x, y = positions[node["code"]]
        ax.text(x, y, node["code"], fontsize=7, ha="center", va="center", zorder=3)
    ax.set_title(f"{variant.replace('_', ' ').title()} | {month}\n"
                 f"edge threshold >= {threshold:.3f} | visible edges: {len(visible)} | nodes: {len(nodes)}",
                 fontsize=14, fontweight="bold")
    ax.text(0.01, 0.01, "Node area = monthly observed share | edge width = transition probability | labels = largest nodes",
            transform=ax.transAxes, fontsize=8, color="#475569")
    ax.axis("off")
    ax.set_xlim(-LAYOUT_LIMIT, LAYOUT_LIMIT)
    ax.set_ylim(-LAYOUT_LIMIT, LAYOUT_LIMIT)


def show_interactive(nodes_by_month, edges_by_month, positions, threshold, variant):
    months = sorted(nodes_by_month)
    fig, ax = plt.subplots(figsize=(12, 9))
    fig.subplots_adjust(bottom=0.16)
    draw_month(ax, months[0], nodes_by_month[months[0]], edges_by_month.get(months[0], []), positions, threshold, variant)
    slider_ax = fig.add_axes((0.18, 0.06, 0.62, 0.03))
    slider = Slider(slider_ax, "Month", 0, len(months) - 1, valinit=0, valstep=1)
    button_ax = fig.add_axes((0.83, 0.045, 0.10, 0.06))
    button = Button(button_ax, "Play")
    timer = fig.canvas.new_timer(interval=900)
    playing = {"value": False}

    def update(value):
        index = int(value)
        draw_month(ax, months[index], nodes_by_month[months[index]], edges_by_month.get(months[index], []), positions, threshold, variant)
        fig.canvas.draw_idle()

    def advance():
        slider.set_val((int(slider.val) + 1) % len(months))

    def toggle(_event):
        playing["value"] = not playing["value"]
        button.label.set_text("Pause" if playing["value"] else "Play")
        if playing["value"]:
            timer.start()
        else:
            timer.stop()

    slider.on_changed(update)
    timer.add_callback(advance)
    button.on_clicked(toggle)
    plt.show()


def save_pdfs(nodes_by_month, edges_by_month, positions, threshold, variant, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    for month in sorted(nodes_by_month):
        fig, ax = plt.subplots(figsize=(12, 9))
        draw_month(ax, month, nodes_by_month[month], edges_by_month.get(month, []), positions, threshold, variant)
        fig.savefig(output_dir / f"{variant}_{month}.pdf", bbox_inches="tight")
        plt.close(fig)
