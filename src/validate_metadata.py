"""Validate the project's planning metadata without claiming data collection is complete."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    with (ROOT / "data" / "metadata" / name).open(newline="") as stream:
        return list(csv.DictReader(stream))

def main():
    dictionary = read("data_dictionary.csv")
    names = [row["variable_name"] for row in dictionary]
    assert len(names) == len(set(names)), "Duplicate dictionary variable"
    assert all(row[key] for row in dictionary for key in ("variable_name", "description", "unit", "source"))
    tracker = read("project_tracker.csv")
    assert {row["Variable"] for row in tracker} == set(names), "Tracker/dictionary mismatch"
    assert all(row["Status"] in {"Not Started", "In Progress", "Review", "Done", "Blocked"} for row in tracker)
    markets = read("markets.csv")
    allowed = {"columbus", "cleveland", "cincinnati", "dayton", "toledo"}
    assert {row["market_id"] for row in markets} == allowed and len(markets) == 5
    crosswalk = read("county_crosswalk.csv")
    keys = []
    for row in crosswalk:
        assert row["market_id"] in allowed
        assert row["state_fips"] == "39" and row["county_fips"].startswith("39")
        assert len(row["county_fips"]) == 5 and row["county_fips"].isdigit()
        assert row["boundary_vintage"] and row["source_url"]
        keys.append(row["county_fips"])
    assert len(keys) == len(set(keys)), "County mapped more than once"
    print(f"Planning metadata valid: {len(dictionary)} variables, {len(markets)} markets.")
    if not crosswalk:
        print("PENDING: county crosswalk is empty; geography has not been validated.")
    if not read("source_manifest.csv"):
        print("PENDING: source manifest is empty; no downloaded data claimed.")

if __name__ == "__main__":
    main()
