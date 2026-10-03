# Dataset Overview

## Dataset 1:

| # | Metadata item | Findings |
|---|---|---|
| 1 | Dataset ID and version | BUILDING_ACTIVITY, version 1.0.0 |
| 2 | Description | Estimates the value of building work and the number of dwellings commenced, completed, under construction and in the pipeline. |
| 3 | Measures | **Building work value:** done during the quarter, yet to be done, commenced, completed and under construction.<br>**Dwelling counts:** commenced, completed and under construction. <br>**The complete measure list is still being verified.** |
| 4 | Units | Monetary values in Australian dollars (AUD) and counts of dwelling units.|
| 5 | Geography | Australia and states/territories.  |
| 6 | Time | Quarterly. The time selector displays 1955 Q1–2026 Q1.  |
| 7 | Other Dimensions | Price Adjustment; Type of Work; Sector of Ownership; Type of Building; Adjustment Type. Available categories within each dimension still need recording. |
| 8 | Codes and labels | Labels are visible in Data Explorer, but the corresponding codes have not yet been recorded. Verify code-to-label mappings using the API metadata or a download containing both codes and labels. |
| 9 | Notes | Data Explorer reports 670,203 unfiltered data points and a last update of 8 July 2026. The update date differs from the reference period. Review the ABS methodology for revisions and limitations; check missing observations after extraction. |


## Dataset 2: 

| # | Metadata item | Findings |
|---|---|---|
| 1 | Dataset ID and version | BA_SA2, version 2.0.0 |
| 2 | Description | Building approvals by SA2 and higher geographic levels, from July 2021 onwards. |
| 3 | Measures | Number of dwelling units; Value of building jobs. |
| 4 | Units | Dwelling counts and monetary values. The monetary unit and scaling factor still need verification. |
| 5 | Geography | SA2 and higher geographic levels. The current API query selects Australia and the eight states/territories only. The geographic classification edition still needs verification. |
| 6 | Time | Monthly. The time selector displays July 2021–July 2026. The current API query requests data from July 2023 onwards. Actual coverage needs verification for each selected series. |
| 7 | Other Dimensions | Sector of Ownership; Type of Work; Type of Building; Region; Frequency. |
| 8 | Codes and labels | Current selections include TOT for Total Work and Total Building; M for Monthly; AUS for Australia; and region codes 1–8 for the states/territories. Other mappings still need verification. |
| 9 | Notes | Approvals represent permission to build, rather than actual commencements or completions. The screenshot shows 1,998 selected data points, not the full dataset size. Do not assume continuous coverage across geographic classification editions. |