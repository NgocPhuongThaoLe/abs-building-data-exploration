# PLANNING 
## Phase 1: Data Exploration
  Objective: 
  Explore the data set to identify project direction. 
  
  Dataset used: This project plans to explore Australian Bureau of Statistics (ABS) datasets:
+ BA_SA2 — Building approvals at the Statistical Area Level 2 (SA2) level.
+ BUILDING_ACTIVITY — Building activity, including dwelling commencements, completions and buildings under construction.
  
### Step 1: Explore Metadata
Objective: Explore the metadata of both datasets to understand their structure, dimensions, measures, geographic coverage and time periods, and identify limitations and potential ways to combine them for analysis.

Metadata findings are documented in [docs/01_dataset_overview.md](docs/01_dataset_overview.md)

### Step 2: Extract Data
- Identify API endpoints and parameters. 
- Write `src/extract.py` with request timeouts and HTTP status checks.
- Save raw responses to `data/raw/`.
- Record dataset versions, URLs, parameters and extraction timestamps.
- Rerun the script and load both samples with pandas.


### Step 3: Explore Structure and Data Quality
- Use `01_EDA_Building_activity` `02_EDA_BA_SA2` to inspect columns, data types, grain and unique keys.
- Check coverage, missing values, duplicates, geographic levels, units and adjustments.
- Document in `02_data_building_activity_exploration` and  `03_BA_SA2_exploration`


### Step 4: Explore Patterns and Dataset Compatibility
- Expand extraction to a suitable exploration scope.
- Create 4–6 charts in `02_patterns_and_questions.ipynb`.
- Record observations, follow-up questions and limitations.
- Check whether both datasets align by geography, time, measures and units.

### Step 5: Evaluate and Select a Project Idea
- Document 2–3 ideas in `docs/idea_candidates.md`.
- Define users, problems, questions, supporting evidence, data needs, scope, outputs and limitations.
- Score ideas by user value, data support, interest, feasibility and Data Engineering potential.
- Select an idea and write a short project brief with metrics, exclusions and completion criteria.

