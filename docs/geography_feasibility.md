# Geography crosswalk and source feasibility (Issue #01 / #07)

Status: **county list verified; source decisions pending team review**. Owner: Member 4.

Verified on 2026-10-01 against the official Census file `list1_2023.xlsx` (July 2023 delineation, SHA-256 `c04b5668d42d5f8893ae740835d3c36bd01656a2bdc27a626f368f80d99d4eda`). Filter: State Name = Ohio and CBSA Code in {17140, 17410, 18140, 19430, 45780}. Result: 27 rows. All county FIPS, names and CBSA codes match `county_crosswalk.csv`, with 0 missing and 0 extra. The same file confirms that Ottawa County (39123) now belongs to Sandusky, OH (41780), not Toledo. `cbsa_history.csv` rows for 2013 and 2018/2020 are still inferred and should be checked against those years' list1 files.

## 1. Proposed frozen geography

**Vintage: OMB July 2023 delineation (Bulletin 23-01), Ohio counties only. 27 counties.**

| market_id | CBSA (2023) | Ohio counties (FIPS) | n |
|---|---|---|---|
| columbus | 18140 Columbus, OH | Delaware 39041, Fairfield 39045, Franklin 39049, Hocking 39073, Licking 39089, Madison 39097, Morrow 39117, Perry 39127, Pickaway 39129, Union 39159 | 10 |
| cleveland | 17410 Cleveland, OH | Ashtabula 39007, Cuyahoga 39035, Geauga 39055, Lake 39085, Lorain 39093, Medina 39103 | 6 |
| cincinnati | 17140 Cincinnati, OH-KY-IN (**Ohio part only**) | Brown 39015, Butler 39017, Clermont 39025, Hamilton 39061, Warren 39165 | 5 |
| dayton | 19430 Dayton-Kettering-Beavercreek, OH | Greene 39057, Miami 39109, Montgomery 39113 | 3 |
| toledo | 45780 Toledo, OH | Fulton 39051, Lucas 39095, Wood 39173 | 3 |

Why 2023:
- It is the current delineation.
- FHFA's metro HPI is already published on it, back-cast to 1975.
- ACS 2023 and later use it.
- It drops Ottawa County from Toledo, which removes Toledo's mid-period anomaly.

Files: [`county_crosswalk.csv`](../data/metadata/county_crosswalk.csv), [`cbsa_history.csv`](../data/metadata/cbsa_history.csv), [`source_geography_map.csv`](../data/metadata/source_geography_map.csv).

## 2. Boundary changes in 2015–2025

| Market | 2013 delineation (ACS 2015–18) | 2018/2020 (ACS 2019–22) | 2023 (ACS 2023–) | Effect |
|---|---|---|---|---|
| Columbus | 10 counties | same | same | none |
| Cleveland | 17460 Cleveland-Elyria, 5 counties | same | **17410**, +Ashtabula | Code change. ACS for 2015–22 is missing from the repo pull |
| Cincinnati | 5 OH counties + KY/IN | same OH part | same OH part | Full CBSA is never Ohio-only |
| Dayton | 19380, 3 counties | 19430, same counties | same, renamed | Name/code only. Not an expansion |
| Toledo | 3 counties | **+Ottawa** | 3 counties | ACS population 603k → 642k (2019) → 600k (2023) |

## 3. Source-by-source verdict

| Source | Columbus | Cleveland | Cincinnati | Dayton | Toledo |
|---|---|---|---|---|---|
| FHFA metro HPI | OK | OK (17410) | **Blocked** (full MSA) | OK | OK |
| Zillow metro ZHVI | Provisional | Provisional | **Blocked** (full MSA) | **Missing** from raw file | Provisional |
| Zillow metro ZORI | Provisional | Provisional | **Blocked** | Provisional | Provisional |
| ACS 1-yr MSA | OK | **Rework**: 2015–22 missing; 2015–22 excludes Ashtabula | **Rework**: use Ohio-part geography | OK (map 19380 + 19430) | **Flag**: 2019–22 includes Ottawa |
| BLS LAUS county sums | OK | OK | OK | OK | OK |
| FRED (national) | n/a | n/a | n/a | n/a | n/a |

"Provisional" means Zillow does not document which CBSA vintage its metro regions use, and a Zillow RegionID is not a CBSA code.

## 4. Issues found in uploaded data (as of 2026-10-01)

1. **`all_acs.csv`, Cincinnati.** This is the full OH-KY-IN MSA, so it can't be labeled `cincinnati`. Candidate replacement: ACS 1-year "Cincinnati, OH-KY-IN Metro Area (part); Ohio" (state-MSA part, summary level 320). Member 2 should confirm it is published every year.
2. **`all_acs.csv`, Cleveland 2015–2022.** These rows are absent because the CBSA code was 17460 before 2023. Pull 17460.
3. **`all_acs.csv`, Toledo 2019–2022.** These years include Ottawa County, so they are not comparable with the frozen geography.
4. **`all_acs.csv`, MOE sentinel.** `-555555555` is a Census annotation meaning the estimate is controlled and has no sampling MOE. It is not a numeric MOE. Convert it to null with reason `controlled_estimate`.
5. **`all_acs.csv`, column names.** Variable names are mixed (`B25002_003M`, `vacant_housing_units MoE`), and `vacant_housing_units estimate` seems to be missing from the long table. Align them with the data dictionary.
6. **`metro_data` branch, Zillow outputs.** These include **Akron**, which is out of scope, and omit **Dayton** ZHVI. They also use the full Cincinnati metro.
7. **Zillow and FHFA Cincinnati series.** These are full-MSA values and must not enter the panel as `cincinnati`.

## 5. Options for Cincinnati (team decision needed)

| Option | Housing (ZHVI/ZORI/HPI) | ACS | Trade-off |
|---|---|---|---|
| A. Custom county proxy | Weighted mean of 5 county series (weights such as ACS housing units, fixed base year) | Ohio-part ACS geography | Stays in scope. The housing measure is a documented proxy, not an official index. ZORI may be missing for small counties (Brown) |
| B. Drop Cincinnati housing measures | Missing with reason `incompatible_geography` | Ohio-part ACS | Scope kept. Loses 11 of 55 rows for housing targets |
| C. Full MSA | Full-MSA series | Full MSA | **Violates agreed scope.** Listed only for completeness |

Recommendation: **A** for ZHVI and HPI if all 5 county series exist for all years. Otherwise **B**. Use a sensitivity check against the full-MSA series only as a diagnostic, never as a panel value.

## 6. Options for ACS boundary breaks (Cleveland 2015–22, Toledo 2019–22)

- **Counts** (population, housing units, vacancy): these can be rebuilt by summing ACS 1-year county estimates, but only where every county has a 1-year estimate (population of 65k or more). Ottawa (Toledo) has no 1-year estimate, so Toledo 2019–22 can't be corrected this way.
- **Median income** can't be rebuilt from county medians.
- Proposal: keep published MSA values, add `acs_geo_matches_frozen` (bool) and `acs_geo_note` columns, and exclude flagged rows from the main analysis. ACS 5-year values must not be spliced in.

## 7. Requests to data owners

- **Member 1 (Zillow/FHFA)**
  - Remove Akron.
  - Add Dayton ZHVI (RegionID 845158).
  - Find out which CBSA vintage Zillow metro definitions use.
  - Check county ZHVI/ZORI coverage for the 5 Cincinnati Ohio counties.
  - Check FHFA county annual HPI for the same 5 counties.
- **Member 2 (ACS)**
  - Pull Cleveland 17460 for 2015–2022.
  - Pull the Cincinnati Ohio-part geography.
  - List which crosswalk counties have 1-year estimates each year.
  - Handle the `-555555555` MOE sentinel.
- **Member 3 (BLS)**
  - Collect LAUS at county level for the 27 counties in `county_crosswalk.csv` (series `LAUCN{county_fips}0000000003/4/5/6`).
  - Sum counts to market level, then compute the rate from the sums.

## Sources

- [Census delineation files](https://www.census.gov/geographies/reference-files/time-series/demo/metro-micro/delineation-files.html), list1_2023.xlsx
- [Ohio statistical areas (2023 county membership summary)](https://en.wikipedia.org/wiki/Ohio_statistical_areas)
- [BLS QCEW county-MSA-CSA crosswalk](https://www.bls.gov/cew/classifications/areas/county-msa-csa-crosswalk.htm)
- Repo evidence: `data/raw/hpi_at_metro.csv` (CBSA codes), `data/raw/acs20*.csv` (MSA codes and populations by year)
