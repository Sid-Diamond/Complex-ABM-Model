"""Inspect an IPUMS-CPS extract and count linked monthly occupation changes."""

from __future__ import annotations

import gzip
import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "Data" / "IPUM"
DDI_PATH = DATA_DIR / "cps_00001.xml"
DAT_PATH = DATA_DIR / "cps_00001.dat.gz"
DB_PATH = DATA_DIR / "transition_probe.sqlite"


def get_locations() -> dict[str, tuple[int, int]]:
    root = ET.parse(DDI_PATH).getroot()
    ns = {"d": "ddi:codebook:2_5"}
    wanted = {"YEAR", "MONTH", "CPSIDP", "OCC", "ASECFLAG"}
    return {
        var.attrib["name"]: (
            int(var.find("d:location", ns).attrib["StartPos"]),
            int(var.find("d:location", ns).attrib["EndPos"]),
        )
        for var in root.findall(".//d:var", ns)
        if var.attrib.get("name") in wanted
    }


def main() -> None:
    locations = get_locations()
    required = {"YEAR", "MONTH", "CPSIDP", "OCC", "ASECFLAG"}
    missing = required - locations.keys()
    if missing:
        raise RuntimeError(f"Missing required variables: {sorted(missing)}")

    def field(line: str, name: str) -> str:
        start, end = locations[name]
        return line[start - 1 : end].strip()

    db = sqlite3.connect(DB_PATH)
    db.execute("DROP TABLE IF EXISTS source_observations")
    db.execute("DROP TABLE IF EXISTS observations")
    db.execute(
        "CREATE TABLE source_observations ("
        "pid TEXT, year INTEGER, month INTEGER, occ TEXT, source TEXT, "
        "PRIMARY KEY (pid, year, month, occ, source))"
    )

    rows = 0
    months: set[tuple[int, int]] = set()
    batch: list[tuple[str, int, int, str, str]] = []
    with gzip.open(DAT_PATH, "rt", encoding="utf-8") as raw_file:
        for line in raw_file:
            year = int(field(line, "YEAR"))
            month = int(field(line, "MONTH"))
            source_label = {"1": "ASEC", "2": "March Basic"}.get(
                field(line, "ASECFLAG"), "Unknown"
            )
            batch.append(
                (field(line, "CPSIDP"), year, month, field(line, "OCC"), source_label)
            )
            months.add((year, month))
            rows += 1
            if len(batch) >= 20_000:
                db.executemany(
                    "INSERT OR IGNORE INTO source_observations VALUES (?, ?, ?, ?, ?)",
                    batch,
                )
                batch.clear()
    if batch:
        db.executemany(
            "INSERT OR IGNORE INTO source_observations VALUES (?, ?, ?, ?, ?)", batch
        )
    db.commit()
    db.execute(
        "CREATE TABLE observations AS "
        "SELECT pid, year, month, occ, MIN(source) AS source "
        "FROM source_observations GROUP BY pid, year, month, occ"
    )
    db.execute("CREATE INDEX observations_pid_time ON observations(pid, year, month)")
    db.commit()

    source_rows = db.execute("SELECT COUNT(*) FROM source_observations").fetchone()[0]
    unique_rows = db.execute("SELECT COUNT(*) FROM observations").fetchone()[0]
    overlap_keys = db.execute(
        "SELECT COUNT(*) FROM ("
        "SELECT pid, year, month, occ FROM source_observations "
        "GROUP BY pid, year, month, occ HAVING COUNT(DISTINCT source) > 1)"
    ).fetchone()[0]

    join = """
        FROM observations AS a
        JOIN observations AS b
          ON a.pid = b.pid
         AND (b.year * 12 + b.month) = (a.year * 12 + a.month) + 1
        WHERE a.occ != '0000' AND b.occ != '0000'
    """
    total = db.execute(f"SELECT COUNT(*) {join}").fetchone()[0]
    changed = db.execute(f"SELECT COUNT(*) {join} AND a.occ != b.occ").fetchone()[0]
    self_edge_types = db.execute(
        f"SELECT COUNT(DISTINCT a.occ || ':' || b.occ) {join} AND a.occ = b.occ"
    ).fetchone()[0]
    changed_edge_types = db.execute(
        f"SELECT COUNT(DISTINCT a.occ || ':' || b.occ) {join} AND a.occ != b.occ"
    ).fetchone()[0]
    if total != (total - changed) + changed:
        raise RuntimeError("Transition arithmetic failed")

    print(f"rows={rows}")
    print(f"source_rows={source_rows}")
    print(f"unique_observations={unique_rows}")
    print(f"rows_removed_by_exact_key={rows - unique_rows}")
    print(f"source_overlap_keys={overlap_keys}")
    print("source_counts=")
    for source, count in db.execute(
        "SELECT source, COUNT(*) FROM source_observations GROUP BY source ORDER BY source"
    ):
        print(f"  {source}: {count}")
    print(f"unique_months={len(months)}")
    print(f"unique_ids={db.execute('SELECT COUNT(DISTINCT pid) FROM observations').fetchone()[0]}")
    print(f"valid_adjacent_month_transitions={total}")
    print(f"occupation_changes={changed}")
    print(f"same_occupation={total - changed}")
    print(f"self_loop_edge_types={self_edge_types}")
    print(f"changed_edge_types={changed_edge_types}")
    print(f"local_intermediate={DB_PATH}")
    db.close()


if __name__ == "__main__":
    main()
