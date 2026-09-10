"""Build unweighted monthly occupation/state network snapshots."""

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "Data" / "IPUM" / "transition_probe.sqlite"
OUTPUT_DIR = ROOT / "Data" / "IPUM" / "dynamic_networks"


VARIANTS = {
    "occupation_only": "occ != '0000'",
    "with_0000": "occ != ''",
}


def write_query(db: sqlite3.Connection, path: Path, query: str) -> int:
    cursor = db.execute(query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(columns)
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)

    for variant, condition in VARIANTS.items():
        nodes_query = f"""
            WITH selected AS (
                SELECT year, month, occ
                FROM observations
                WHERE {condition}
            ), counts AS (
                SELECT year, month, occ, COUNT(*) AS node_count
                FROM selected
                GROUP BY year, month, occ
            ), totals AS (
                SELECT year, month, SUM(node_count) AS month_total
                FROM counts
                GROUP BY year, month
            )
            SELECT c.year, c.month, c.occ, c.node_count,
                   t.month_total,
                   CAST(c.node_count AS REAL) / t.month_total AS node_share
            FROM counts AS c
            JOIN totals AS t USING (year, month)
            ORDER BY c.year, c.month, c.occ
        """
        edges_query = f"""
            WITH links AS (
                SELECT a.year AS origin_year, a.month AS origin_month,
                       b.year AS destination_year, b.month AS destination_month,
                       a.occ AS origin_occ, b.occ AS destination_occ
                FROM observations AS a
                JOIN observations AS b
                  ON a.pid = b.pid
                 AND (b.year * 12 + b.month) = (a.year * 12 + a.month) + 1
                WHERE a.occ != '' AND b.occ != ''
                  AND a.occ IN (SELECT occ FROM observations WHERE {condition})
                  AND b.occ IN (SELECT occ FROM observations WHERE {condition})
            ), counts AS (
                SELECT origin_year, origin_month, destination_year,
                       destination_month, origin_occ, destination_occ,
                       COUNT(*) AS transition_count
                FROM links
                GROUP BY origin_year, origin_month, destination_year,
                         destination_month, origin_occ, destination_occ
            ), totals AS (
                SELECT origin_year, origin_month, origin_occ,
                       SUM(transition_count) AS origin_total
                FROM counts
                GROUP BY origin_year, origin_month, origin_occ
            )
            SELECT c.origin_year, c.origin_month,
                   c.destination_year, c.destination_month,
                   c.origin_occ, c.destination_occ, c.transition_count,
                   t.origin_total,
                   CAST(c.transition_count AS REAL) / t.origin_total
                       AS transition_probability
            FROM counts AS c
            JOIN totals AS t USING (origin_year, origin_month, origin_occ)
            ORDER BY c.origin_year, c.origin_month, c.origin_occ,
                     c.destination_occ
        """
        node_count = write_query(
            db, OUTPUT_DIR / f"{variant}_nodes.csv", nodes_query
        )
        edge_count = write_query(
            db, OUTPUT_DIR / f"{variant}_edges.csv", edges_query
        )
        print(f"{variant}: nodes={node_count}, edges={edge_count}")

    db.close()


if __name__ == "__main__":
    main()
