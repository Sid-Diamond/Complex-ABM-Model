"""Main entry point for exploratory occupation-network visualisation."""

from pathlib import Path

from network_visualisation import load_variant, save_pdfs, show_interactive, stable_layout


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data" / "IPUM" / "dynamic_networks"

# Edit this dictionary to control the run.
CONFIG = {
    "variant": "occupation_only",  # or: "with_0000"
    "edge_threshold": 0.05,
    "save": False,                  # False = interactive Matplotlib; True = PDFs only
    "output_dir": ROOT / "outputs" / "network_pdfs",
}


def main() -> None:
    variant = CONFIG["variant"]
    node_path = DATA_DIR / f"{variant}_nodes.csv"
    if not node_path.exists():
        raise FileNotFoundError(f"Missing {node_path}. Run scripts\\build_dynamic_networks.py first.")
    nodes, edges, codes = load_variant(DATA_DIR, variant)
    positions = stable_layout(edges, codes)
    if CONFIG["save"]:
        save_pdfs(nodes, edges, positions, CONFIG["edge_threshold"], variant, CONFIG["output_dir"])
        print(f"Saved PDFs to {CONFIG['output_dir']}")
    else:
        show_interactive(nodes, edges, positions, CONFIG["edge_threshold"], variant)


if __name__ == "__main__":
    main()
