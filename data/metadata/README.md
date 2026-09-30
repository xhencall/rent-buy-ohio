## Demographic Data Sources

### Data Source
The acs*.csv were downloaded from the US census (https://www.census.gov/programs-surveys/acs/data.html). The data were downloaded using the Census API with an API key. 

### Data Range & Missingness
Note that 2020 and 2025 are missing. There was no data available for 2020, and 2025 data has not yet been released (as of 9/30/2026).

### Metropolitan Statistical Areas (MSA)
The following MSAs were considered:
- Cincinnati, OH-KY-IN Metro Area
- Cleveland, OH Metro Area
- Columbus, OH Metro Area
- Dayton, OH Metro Area
- Dayton-Kettering-Beavercreek, OH Metro Area
- Toledo, OH Metro Area

For the years 2015-2019, the Dayton MSA was active. Beginning 2019, the Dayton MSA code was retired and replaced with Dayton-Kettering. In 2023, the Dayton-Kettering was expanded to Dayton-kettering-Beavercreek but the MSA code did not change.

Cleveland data were collected beginning 2023.

### Variables
For each MSA, the following estimates and measures of error were acquired:
- B01003: Total Population
- B19013: Median Household Income in the Past 12 Months (in Inflation-Adjusted Dollars)
= B25001: Number of Housing Units
- B25002_003: Occupancy Status - Number of Vacancies
- B25002_001: Occupancy Status - Total