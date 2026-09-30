# Checkpoint 1 — Project plan and data assessment

Status: planning scaffold. No source observations collected, no model trained, and no data-quality KPI measured yet. Replace pending fields with evidence and links before submission.

## 1. Problem definition

Research question: When does it make more financial sense to rent or buy in the five selected Ohio housing markets, and how does this change over time?

Modeling objective: estimate annual housing-market dynamics from historical housing, demographic and economic data. Proposed primary target is next-year home-value growth; rent growth is secondary if compatible coverage permits. Renting/buying is a scenario application of those estimates, not a supervised binary label.

Scope: Ohio-only county subsets of Columbus, Cleveland, Cincinnati, Dayton and Toledo; annual market-year observations; approximately 2015–2025. National macroeconomic controls are allowed. No additional markets or out-of-state housing observations are included.

## 2. Data gathering

Members 1–3 collect source snapshots and write provenance. Member 4 approves geography and schema, then builds the panel. Member 5 coordinates the report and methodological decisions. See the README role table, metadata dictionary, tracker seed, and issue specifications.

First dependency: verify that Zillow, FHFA, ACS and BLS can support the same Ohio-only geography. Record infeasible features explicitly. ACS regional median income cannot be reconstructed by averaging county medians. Download source-native files unchanged and aggregate only in processing scripts.

For each source deliver: original file; series/table identifier; UTC retrieval timestamp; checksum; release vintage; license; source-to-project geographic crosswalk; actual first/last available year per market; annualization rule; missingness reason; reviewer sign-off.

## 3. Data assessment

| Assessment | Required evidence | Current result |
|---|---|---|
| Geography | Ohio-only county membership and compatible source mapping | Pending |
| Coverage | Market × year × variable availability matrix | Pending |
| Keys | Duplicate and unmatched-key counts per source | Pending |
| Missingness | Counts and reasons, including ACS 2020 gap | Pending |
| Units | Dollar/index/rate checks and dictionary review | Pending |
| Quality | Range checks, abrupt changes, MOEs and source revisions | Pending |
| Reproducibility | Fresh-environment rebuild and input hashes | Pending |

Do not interpret a planned 55-row skeleton as 55 observed samples. Separate observed, missing, excluded and derived values. Examine revisions, changing boundaries, seasonal adjustment, property-type mismatch and the representativeness of asking rents. Record outliers before deciding whether any adjustment is justified.

## 4. Learnability assessment

Maximum unlagged sample: 5 × 11 = 55 rows. Adjacent years within a market and national economic shocks across markets are correlated. Growth and next-year targets reduce usable observations further, and national predictors have only about 11 unique annual values.

Proposed progression after CP1: historical-mean and last-observed-growth baselines, then a parsimonious pooled linear or ridge model with few prespecified lagged predictors. Deep learning and extensive hyperparameter searches are not justified by this design. Do not promise a complex ML model before measuring coverage.

Use rolling-origin evaluation with whole years held out across all five markets. Fit scaling, imputation and feature selection on training folds only. Reserve the most recent one or two usable years for final evaluation if enough earlier years remain; freeze exact splits after coverage review. A leave-one-market-out sensitivity check is optional and does not replace future-year evaluation. Avoid random row splitting.

For target growth in year t+1, use only information available at the forecast origin. Release delays may require additional predictor lags. Current revised historical downloads do not establish real-time backtest validity; document this limitation or use vintage data. Avoid simultaneously including a target level and deterministic ratios that encode it. National rates cannot be separately identified from unrestricted year fixed effects.

Go/no-go: proceed with prediction only if aligned training and evaluation years support baseline comparison without leaking future information. If not, deliver a descriptive panel analysis and assumption-based scenarios, explicitly labeled as such. Use uncertainty and sensitivity analysis. With five clusters, conventional cluster-robust inference is fragile.

Optional valuation extension: fundamentals-based price residuals, preferably evaluated out of sample. Positive residuals indicate prices above model-implied values, not proven overvaluation. Defer if coefficients or rankings are unstable.

## 5. KPIs

| KPI | Definition | CP1 target / policy | Actual |
|---|---|---|---|
| Scope integrity | Share of analytical rows with approved Ohio-only geography | 100% | Pending |
| Key integrity | Duplicate market-year keys in final panel | 0 | Pending |
| Provenance | Downloaded files with all required manifest fields / downloaded files | 100%; undefined before downloads | Pending |
| Dictionary completeness | Analytical columns with definition, unit, source and transformation / all analytical columns | 100% | Pending |
| Coverage | Observed core-variable cells / expected cells in frozen window | Report by variable and market; no invented threshold | Pending |
| Annual completeness | Accepted annual aggregates satisfying source-period requirements / accepted aggregates | 100% | Pending |
| Merge accountability | Unmatched source keys without documented disposition | 0 | Pending |
| Reproducibility | Independent reviewer rebuilds outputs from recorded inputs | Required before CP1 sign-off | Pending |

Later predictive KPIs: MAE and RMSE of annual growth in percentage points, reported by fold and market; skill = 1 − model MAE / baseline MAE when baseline MAE > 0. Also report prediction-interval coverage and width where supportable. No accuracy claim is made at CP1.

Later decision KPIs: buy-minus-rent discounted cost or terminal net wealth at stated horizons, break-even holding period, and recommendation sensitivity. Include down payment, financing and amortization, taxes, insurance, maintenance, HOA where relevant, purchase/sale costs, rent growth and the renter's investment opportunity cost. Avoid double-counting principal as both an expense and lost equity. These inputs are future assumptions/data requirements, not collected CP1 features.

## 6. Submission checklist

- [ ] Geographic crosswalk and source feasibility approved.
- [ ] Planned sources collected or limitations documented.
- [ ] Manifest, data dictionary and tracker updated.
- [ ] Annual panel and missingness report reproducible.
- [ ] Assessment table and KPI actuals completed.
- [ ] Modeling target, evaluation design and go/no-go justified.
- [ ] Independent review completed and report PR merged.
