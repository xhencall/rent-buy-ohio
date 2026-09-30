# Annual panel data contract

## Geography and identifiers

Use `market_id` in {columbus, cleveland, cincinnati, dayton, toledo} and integer `year` in 2015–2025. Retain a canonical display name separately. The primary key is `(market_id, year)`.

The approved scope excludes all counties outside Ohio. Select and version one Census/OMB delineation, then freeze county membership across the study period. Verify state FIPS 39 and five-digit county FIPS. Store the source geography IDs and boundary vintage in the crosswalk before downloading or merging. The initially empty county crosswalk is a collection deliverable, not a verified geography table.

Official CBSA codes can identify the source regions but are not identifiers for custom Ohio-only subsets. Zillow RegionID is not a CBSA code. Do not infer geographic equivalence from matching names. Cincinnati's full MSA includes non-Ohio counties. Check all five regions against the selected vintage.

Counts can be summed across nonoverlapping counties. Compute rates from summed numerators and denominators. County medians cannot be summed or averaged to obtain a regional median. A weighted aggregation of county ZHVI/ZORI series would be a custom proxy requiring documented weights, coverage, and sensitivity analysis; it is not an official metro index. Do not silently replace missing Ohio-only indicators with full-MSA values. If a compatible annual income or housing measure is infeasible, record the gap, narrow the feature set, and obtain a documented team decision on any proxy. Do not expand geography.

## Annualization

| Measure | Rule | Required coverage |
|---|---|---|
| ZHVI, ZORI | Arithmetic mean of monthly levels | 12 distinct months |
| FHFA HPI | Prefer consistent annual product; otherwise mean of quarterly levels | 4 quarters |
| ACS | Published one-year estimate for reference year | One compatible estimate with MOE |
| BLS LAUS | Published annual averages; otherwise annualize compatible monthly counts | 12 months |
| CPIAUCSL, FEDFUNDS | Mean of monthly values | 12 months |
| MORTGAGE30US | Mean of weekly observations dated in year | Compare against expected source calendar; record count |

Keep source frequency, aggregation rule, number of periods, geographic coverage and missingness flags in intermediate audits. Partial-year means are not full-year observations. Never sum index levels, monthly stocks, or rates across time. If county BLS values are aggregated, unemployment rate equals summed unemployed / summed labor force × 100.

Annual means are descriptive annual measures, not beginning-of-year investment prices. Later purchase scenarios must state their observation timing and avoid assuming the annual mean was known at the beginning of the year.

## ACS policy

Use one-year estimates where geographic availability supports them. Preserve estimate and MOE fields and convert Census missing/suppression sentinels to missing values with reasons. Standard 2020 ACS one-year estimates were not released. Keep that gap explicit. Do not splice experimental 2020 estimates or five-year estimates into a one-year series. Five-year releases describe overlapping 60-month windows and do not satisfy the current annual point-in-time interpretation. Small-county availability and regional median income reconstruction are feasibility risks for the Ohio-only design.

Candidate ACS tables: B01003 population, B19013 median household income, B25001 housing units, and B25002 occupied/vacant housing units. Confirm variable IDs, universes and availability for each release. General vacancy is vacant units / total housing units; it differs from rental or homeowner vacancy rates.

## Features, units and missingness

- Store monetary levels in nominal USD, rent in USD/month, and rates in percentage points (5 means 5%). Record CPI base in metadata. Real-dollar outputs must specify a base year and use one consistent deflator.
- `price_to_income = home_value_usd / household_income_usd`.
- `price_to_rent = home_value_usd / (12 * rent_usd_month)`.
- Growth = `100 * (level_t / level_t_minus_1 - 1)`, within market, only for consecutive years and positive denominators. First available growth is missing. No interpolation across gaps.
- Housing units are a stock proxy for supply, not annual construction or listings.
- Price/rent comparisons must disclose property-type and tenant/owner composition differences.
- Source-specific null reasons: not released, suppressed, missing period, incompatible geography, unavailable series. Zero is not a missing-value code.

## Merge and provenance

Start with the five-market × approved-year skeleton. Validate one record per market-year in each annual source, then left-join one-to-one. National macro series join many-to-one on year. Report unmatched keys and row counts after every join. Retain a missingness matrix and a separate complete-case view instead of silently inner-joining away missing observations.

Record original filename, source URL, series/table ID, retrieval UTC timestamp, SHA-256, release/vintage, license, geography, period coverage and annualization rule in the source manifest. Store new source revisions in a new dated directory. All transformations must read raw snapshots and write only processed outputs.

## Authoritative references

- [Census delineation files](https://www.census.gov/programs-surveys/metro-micro/about/delineation-files.html)
- [2020 ACS experimental release and standard-release gap](https://www.census.gov/programs-surveys/acs/data/experimental-data.html)
- [Zillow housing data](https://www.zillow.com/research/data/)
- [FHFA datasets](https://www.fhfa.gov/data/hpi/datasets)
- [BLS LAUS](https://www.bls.gov/lau/)
- [Mortgage rate](https://fred.stlouisfed.org/series/MORTGAGE30US), [CPI](https://fred.stlouisfed.org/series/CPIAUCSL), [Federal funds rate](https://fred.stlouisfed.org/series/FEDFUNDS)
