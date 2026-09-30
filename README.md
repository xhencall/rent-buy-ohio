# Rent or Buy? A Data-Driven Analysis of Ohio Housing Markets

A five-person PhD Data Science Bootcamp project studying housing-market dynamics and their implications for renting versus buying.

## Research questions

**When does it make more financial sense to rent or buy a home in Ohio, and how does the answer vary across housing markets and over time?**

We will collect housing, demographic, and economic data, assess statistical learnability, and model price and rent dynamics. Rent-versus-buy scenarios are the final application. They will incorporate model uncertainty and explicit household assumptions, rather than treating a price-to-rent ratio as a decision rule.

Optional extension: Which markets appear relatively over- or undervalued compared with local economic fundamentals? Model residuals will be described as relative deviations, not proof of mispricing or future returns.

## Scope

- Markets: **Columbus, Cleveland, Cincinnati, Dayton, Toledo only**.
- Geography: **Ohio counties only** within a documented, fixed metropolitan delineation. Cincinnati is an Ohio-only subset, not the full OH–KY–IN MSA. No out-of-state housing observations enter the analytical panel.
- Unit: market × calendar year. Frequency: annual. Target: 2015–2025, subject to compatible data coverage.
- Maximum panel size: 55 rows before missing observations, growth rates, lags, and future targets.
- National FRED series are shared macroeconomic covariates, not additional geographic observations.

The Ohio-only boundary is a collection feasibility gate. Full-MSA indicators cannot be relabeled as Ohio-only values. Source-native monthly, quarterly, or weekly files may be retained unchanged; only annual observations enter the analytical panel. See [data contract](docs/data_contract.md).

## Current stage

**Checkpoint 1: problem definition, data gathering, data assessment, learnability assessment, and KPI definition.** This repository contains the project scaffold and collection plan. No housing dataset has yet been collected or model fitted. Coverage, licensing, and geographic compatibility must be verified before data are marked complete.

## Planned sources

| Source | Measures | Collection considerations |
|---|---|---|
| [Zillow Research](https://www.zillow.com/research/data/) | ZHVI home values, ZORI monthly asking-rent measure | Select consistent property types and seasonal adjustment. Verify county/subregion support and full-year coverage. |
| [FHFA HPI](https://www.fhfa.gov/data/hpi/datasets) | House Price Index | Record product, base, frequency and geography. An index is not a dollar price. |
| [Census ACS](https://www.census.gov/programs-surveys/acs/data.html) | Population, household income, housing units, vacancy | Preserve estimate/MOE pairs. Standard 2020 one-year estimates are unavailable. |
| [FRED](https://fred.stlouisfed.org/) | MORTGAGE30US, CPIAUCSL, FEDFUNDS | National series annualized consistently; source release dates and revisions documented. |
| [BLS LAUS](https://www.bls.gov/lau/) | Resident employment, unemployment, labor force | Use compatible county or area definitions; avoid mixing workplace jobs with resident employment. |

## Repository structure

```text
rent-buy-ohio/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   ├── checkpoint1.md
│   ├── data_contract.md
│   ├── decisions.md
│   └── issues/                 # Versioned issue specifications
├── data/
│   ├── raw/                    # Immutable downloads, ignored by Git
│   ├── processed/              # Reproducible annual outputs, ignored by Git
│   └── metadata/               # Dictionary, manifest, geography and tracker seed
├── notebooks/                  # Ordered exploratory work
├── src/                        # Reusable data processing code
├── figures/
├── requirements.txt
└── .gitignore
```

## Team workflow

[Open the Google Sheets project tracker](https://docs.google.com/spreadsheets/d/1rilH7LUtxTCM9mm-4_Ky26AgNipGnTNG8dwc90tSSN0/edit). It contains 23 planned variables, owner/status dropdowns and color-coded statuses. Access is managed in Google Drive; repository visibility does not grant sheet access.

| Role | Responsibility | Suggested branch |
|---|---|---|
| Member 1 | Zillow and FHFA | `housing-data` |
| Member 2 | ACS | `demographics-data` |
| Member 3 | FRED and BLS | `economy-data` |
| Member 4 | Geography, cleaning, merges, dictionary | `data-cleaning` |
| Member 5 | Coordination, reports, baseline plan | `documentation` |

GitHub Issues own task scope, dependencies and acceptance criteria. Google Sheets owns variable-level collection status. Slack supports discussion and blockers; record durable decisions in `docs/decisions.md` and link the relevant issue. Use a brief weekly check-in and one independent reviewer per PR. Replace role placeholders with names/usernames before assigning issues or inviting collaborators. Public visibility does not grant write access.

## GitHub Flow

Never push work directly to `main`. Create a short-lived feature branch, commit a coherent change, open a PR linked to an issue, obtain review, and squash-merge after checks pass. Delete merged branches and start subsequent tasks from updated `main`.

```bash
git clone https://github.com/xhencall/rent-buy-ohio.git
cd rent-buy-ohio
git switch main
git pull --ff-only
git switch -c housing-data
# Edit, validate, then stage explicit files.
git add src/ data/metadata/
git commit -m "Document housing data sources and coverage"
git push -u origin housing-data
# Open a pull request targeting main.
```

Suggested branches describe workstreams, not permanent integration branches. Use issue suffixes for concurrent tasks. Repository creation may generate the initial README commit; all project changes after initialization go through PRs. Branch protection is a separate repository setting and must not be assumed active from this documentation.

## Local setup and standards

Use Python 3.11 or later in an isolated environment. Dependencies below are planning ranges, not a tested lockfile. Freeze an exact environment after the first reproducible pipeline succeeds.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/validate_metadata.py
```

Keep reusable transformations in `src/`, use snake_case, explicit units, relative paths, and English docstrings. Number notebooks by analysis order, clear outputs before review, and avoid hidden execution state. Never commit credentials or source downloads. Follow [contribution guidance](CONTRIBUTING.md).

## Data management

Never edit an original download. Store it under `data/raw/<source>/<retrieved_date>/` with its original filename. Record URL, retrieval time, SHA-256, coverage and license in `data/metadata/source_manifest.csv`. Keep raw and processed files locally; use an access-controlled shared data location and reproducible download instructions as needed. A public code repository does not automatically authorize redistribution of third-party data.

Cleaned outputs belong in `data/processed/`. Join on stable market identifiers and year, never fuzzy metro names. Document all variables in `data/metadata/data_dictionary.csv`. Missing observations remain missing with reasons; do not manufacture a balanced panel. The tracker seed has no downloaded-file claims.

## Planned milestones

| Milestone | Deliverable | Exit criterion |
|---|---|---|
| CP1-A | Scope and geography decision | County membership, vintage and source feasibility reviewed |
| CP1-B | Source inventory and raw snapshots | Each source has manifest, dictionary and observed coverage |
| CP1-C | Annual merged panel and assessment | Unique keys, missingness report and reproducible run |
| CP1-D | Checkpoint 1 report | Actual KPI results and justified modeling go/no-go |
| Later | Baselines and time-based evaluation | Compare against simple forecasts using held-out years |
| Later | Rent-versus-buy scenarios | Transparent assumptions and sensitivity analysis |
| Optional | Relative valuation | Only if sample size and model stability support interpretation |

Dates will be set by the team. See [Checkpoint 1](docs/checkpoint1.md) for the current plan and acceptance criteria.
