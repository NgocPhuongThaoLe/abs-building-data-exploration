## Initial Exploration Findings

The BA_SA2 sample was explored to understand its structure,
coverage and data quality before selecting a business question.

### Structure and coverage

| Item | Finding |
| --- | --- |
| Dataset version | BA_SA2 2.0.0 |
| Rows | 162 |
| Columns | 14 |
| Frequency | Monthly (M) |
| Time coverage | July–September 2023 |
| Measures | 2 codes: 1 and 2 |
| Sectors | 3 codes: 1, 5 and 9 |
| Work type | TOT only |
| Building type | TOT only |
| Region types | STE and AUS |
| Regions | 9 codes: 1–8 and AUS |
| Units | NUM and AUD |
| Unit multipliers | 0 and 3 |

These findings describe the extracted sample, not the complete dataset.
Dimension code meanings still require verification using BA_SA2 metadata.

### Geographic coverage

The sample contains REGION_TYPE codes STE and AUS.
No SA2-level observations are present in this extract.

Although the dataset is named BA_SA2, the current API filters
selected region codes 1–8 and AUS.

The Australia total should not be added to its component regions,
as this would double count observations.

### Grain and unique key

Each row represents one observation for a combination of:

- MEASURE
- SECTOR
- WORK_TYPE
- BUILDING_TYPE
- REGION_TYPE
- REGION
- FREQ
- TIME_PERIOD

The combination of these eight columns uniquely identifies
each observation in the current sample.

| Duplicate check | Result |
| --- | ---: |
| Fully duplicated rows | 0 |
| Duplicate observation keys | 0 |

This confirms uniqueness within the current extract.
The key should be checked again if the extraction scope changes.

### Missing values

| Column | Non-missing values | Missing values |
| --- | ---: | ---: |
| OBS_VALUE | 162 | 0 |
| OBS_STATUS | 0 | 162 |
| OBS_COMMENT | 0 | 162 |
| All other columns, individually | 162 | 0 |

All 162 observations contain numeric values.
No missing values were found in the dimension, time or unit columns.

OBS_STATUS and OBS_COMMENT are entirely empty.
These empty fields alone do not demonstrate a data error,
and a blank status does not establish that a value is final or unrevised.

### Data type observations

- OBS_VALUE is stored as float64.
- TIME_PERIOD is stored as text containing monthly period labels.
- MEASURE and SECTOR are stored as int64 but represent categorical codes.
- REGION is stored as text, accommodating both numeric-looking codes and AUS.
- UNIT_MULT is stored as int64 and describes the scaling of observation values.
- OBS_STATUS and OBS_COMMENT are inferred as float64 because both columns
  are entirely missing; this does not establish their intended semantic types.

OBS_VALUE contains 153 distinct values across 162 populated rows.
Repeated numeric values do not indicate duplicate observations:
different dimension combinations can have the same value.

### Implications for analysis

- Select a specific measure before analysing OBS_VALUE.
- Verify measure and sector code meanings using BA_SA2 metadata.
- Keep different units separate; monetary values and counts cannot be added.
- Confirm unit multipliers before interpreting values.
- Avoid adding a total sector to the sectors it includes.
- Avoid adding the Australia total to its component regions.
- The sample contains only three months, providing limited evidence
  for long-term trends or seasonality.

### Compatibility with BUILDING_ACTIVITY

BA_SA2 contains monthly observations, while BUILDING_ACTIVITY
contains quarterly observations.

The current BA_SA2 sample covers July–September 2023,
corresponding to 2023-Q3.

Before comparing the datasets:

- Align their geographic scope and sector coverage.
- Verify that the selected measures and building definitions are comparable.
- Confirm units and price basis.
- Choose a compatible adjustment basis where applicable.
- Determine whether the selected monthly measure can be summed into a quarter.

Building approvals and building activity describe different stages
of the construction process. Their values should not be treated
as interchangeable or expected to match directly.

