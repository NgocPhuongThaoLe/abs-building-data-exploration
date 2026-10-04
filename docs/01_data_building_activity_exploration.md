## Building Activity — Initial Exploration Findings

The BUILDING_ACTIVITY sample was explored in
`notebooks/01_EDA_Building_activity.ipynb` to understand its structure,
coverage and data quality.

### Structure and coverage

| Item | Finding |
| --- | --- |
| Dataset version | BUILDING_ACTIVITY 1.0.0 |
| Rows | 552 |
| Columns | 15 |
| Frequency | Quarterly |
| Time coverage | 2023-Q2 to 2023-Q4 |
| Measures | 8 codes: M1–M8 |
| Regions | 9 codes, including AUS |
| Price adjustment | CVM and CUR |
| Work type | TOT |
| Ownership sector | 9 |
| Building type | TOT |
| Series adjustment | TSEST codes 10, 20 and 30 |
| Units | AUD and NUM |
| Unit multipliers | 3 and 0 |

These findings describe the extracted sample, not the entire dataset.
Code meanings and unit multipliers still require metadata verification.

### Grain and unique key

Each row represents one observation for a combination of:

- MEASURE
- REGION
- PRICE_ADJ
- BLD_WORK_TYPE
- SECTOR_OWN
- TYPE_BLDG
- TSEST
- FREQ
- TIME_PERIOD

The combination of these columns uniquely identifies each observation
in the sample.

- Fully duplicated rows: **0**
- Duplicate observation keys: **0**

### Missing values

| Column | Missing values |
| --- | ---: |
| OBS_VALUE | 48 |
| OBS_STATUS | 504 |
| OBS_COMMENT | 552 |
| All other columns | 0 |

Of the 552 observations, 504 contain numeric values and 48 are missing
(approximately 8.7%).

All 48 missing observation values have `OBS_STATUS = m`.
All 504 populated observation values have a blank status.

The displayed missing observations belong to `MEASURE = M3`,
`PRICE_ADJ = CVM` and `TSEST` codes 20 or 30.

The meaning of status `m` and the reason for missing values still need
to be verified using metadata. Missing values should not be
automatically replaced with zero.

### Data type observations

- OBS_VALUE is stored as float64.
- TIME_PERIOD is stored as text containing quarterly period labels.
- SECTOR_OWN and TSEST are stored as integers but represent categorical codes.
- OBS_COMMENT is entirely empty; its inferred float64 type does not mean
  that comments are numeric.

### Implications for analysis

- Select a specific measure before analysing observation values.
- Verify units and multipliers before interpreting values.
- Keep different price and series adjustment variants separate.
- Avoid adding Australia totals to their component regions.
- Check whether a measure can be summed across time.
- The three-quarter sample provides limited evidence for long-term trends.


**Status:** Initial structure and quality checks are complete for the
BUILDING_ACTIVITY sample. Metadata interpretation and valid series
selection are still in progress.