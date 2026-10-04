# Dataset Overview

## Dataset 1:

### Building Activity — API and Metadata

- **Agency:** ABS
- **Dataset ID:** `BUILDING_ACTIVITY`
- **Version:** `1.0.0`
- **Description:** Estimates the value of building work and the number of dwellings commenced, completed, under construction and in the pipeline.
- **Measures:** Value of work done during the quarter, yet to be done, commenced, completed and under construction; dwelling units commenced, completed and under construction. These eight measures were verified against the API metadata.
- **Units:** Monetary values in Australian dollars (AUD) and dwelling unit counts. Scaling factors require verification in the extracted data.
- **Geography:** Australia and states/territories.
- **Frequency:** Quarterly.
- **Selected start period:** Q2 2023. Actual coverage requires verification for each selected series.
- **Dimensions:** Measure; State/territory; Price Adjustment; Type of Work; Sector of Ownership; Type of Building; Time Series Adjustment; Frequency; Time Period.
  
#### API URLs

**Data query:**
https://data.api.abs.gov.au/rest/data/ABS,BUILDING_ACTIVITY,1.0.0/...TOT.9.TOT..Q?startPeriod=2023-Q2&dimensionAtObservation=AllDimensions

**Structure query (metadata):**
https://data.api.abs.gov.au/rest/dataflow/ABS/BUILDING_ACTIVITY/1.0.0?detail=referencepartial&references=all


### Dimension Filters

The key `...TOT.9.TOT..Q` contains eight dimension positions separated by dots. Empty positions leave the corresponding dimension unrestricted.

| Position | Dimension ID | Description | Selected value |
|----------|--------------|-------------|----------------|
| 1 | MEASURE | Measure | All available |
| 2 | REGION | State or territory | All available |
| 3 | PRICE_ADJ | Price adjustment | All available |
| 4 | BLD_WORK_TYPE | Type of work | TOT — Total Work |
| 5 | SECTOR_OWN | Sector of ownership | 9 — Total Sectors |
| 6 | TYPE_BLDG | Type of building | TOT — All Buildings |
| 7 | TSEST | Time series adjustment | All available |
| 8 | FREQ | Frequency | Q — Quarterly |

### Query Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| startPeriod | 2023-Q2 | Request data from Q2 2023 |
| dimensionAtObservation | AllDimensions | Include all dimensions at observation level |

### Metadata Verification

Dimension order was verified using `DimensionList` and its `position` attributes. Filter codes were checked against the referenced codelists.

For example, `CL_STATE` confirms that `1` represents New South Wales. Restricting the query to NSW changes the key to `.1..TOT.9.TOT..Q`.

`TIME_PERIOD` is the ninth dimension in the metadata; time filtering is handled separately through query parameters.


## Dataset 2: 


## Building Approvals — API and Metadata

- **Agency:** ABS
- **Dataset ID:** `BA_SA2`
- **Version:** `2.0.0`
- **Description:** Building approvals by SA2 and higher geographic levels, from July 2021 onwards.
- **Measures:** Number of dwelling units; Value of building jobs; Number of building jobs valued $50,000 or more.
- **Units:** Dwelling counts, monetary values and building job counts. Monetary units and scaling factors require verification in the extracted data.
- **Geography:** SA2 and higher geographic levels, using ASGS 2021. The current query selects Australia and the eight states/territories only.
- **Frequency:** Monthly.
- **Selected start period:** July 2023. Actual coverage requires verification for each selected series.
- **Dimensions:** Measure; Sector of Ownership; Type of Work; Type of Building; Region Type; Region; Frequency; Time Period.
- **Interpretation:** Approvals represent permission to build, rather than actual commencements or completions.

### API URLs

**Data query:**
https://data.api.abs.gov.au/rest/data/ABS,BA_SA2,2.0.0/..TOT.TOT..1+2+3+4+5+6+7+8+AUS.M?startPeriod=2023-07&dimensionAtObservation=AllDimensions

**Structure query (metadata):**
https://data.api.abs.gov.au/rest/dataflow/ABS/BA_SA2/2.0.0?detail=referencepartial&references=all

### Dimension Filters

The key contains seven dimension positions separated by dots. Empty positions leave the corresponding dimension unrestricted; `+` selects multiple codes.

| Position | Dimension ID | Description | Selected value |
|----------|--------------|-------------|----------------|
| 1 | MEASURE | Measure | Unrestricted |
| 2 | SECTOR | Sector of ownership | Unrestricted |
| 3 | WORK_TYPE | Type of work | TOT — Total Work |
| 4 | BUILDING_TYPE | Type of building | TOT — Total |
| 5 | REGION_TYPE | Geographic level | Unrestricted |
| 6 | REGION | Geographic area | 1–8 and AUS — States/territories and Australia |
| 7 | FREQ | Frequency | M — Monthly |

The current query selects state/territory and national data rather than individual SA2 areas.

### Available Measures

| Code | Measure |
|------|---------|
| 1 | Number of dwelling units |
| 2 | Value of building jobs |
| 3 | Number of building jobs valued $50,000 or more |

### Query Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| startPeriod | 2023-07 | Request data from July 2023 |
| dimensionAtObservation | AllDimensions | Include all dimensions at observation level |

### Metadata Verification

Dimension order was verified using `DimensionList` and its `position` attributes. Filter codes were checked against the referenced codelists.

For example, `CL_ASGS_2021` confirms that `1` represents New South Wales. Selecting NSW only changes the key to `..TOT.TOT..1.M`.

`TIME_PERIOD` is the eighth dimension in the metadata; time filtering is handled separately through query parameters.