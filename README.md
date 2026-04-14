# OSM-Feature-Completeness
Repository includes development and testing of the feature completness metric

**Last updated:** 26 August 2025  

---

## Overview

This project focuses on the development and evaluation of a **Spatial Data Feature Completeness Index**, designed to quantify the level of completeness of geographic features (roads and buildings) over time.

The index is based on the concept of **increment per normalized feature unit**, where:
- Roads: cumulative length divided by number of features  
- Buildings: cumulative area divided by number of features  

The goal of the index is to capture the maturity and completeness level of mapped data within a given region.

---

## Methodology

The workflow was conducted in several sequential stages:

### 1. Exploratory Phase
A review of existing completeness metrics was performed, along with initial experiments on time-series data from various geographic regions, in order to understand potential behavioral patterns.

### 2. Metric Definition
A candidate metric was selected based on the concept of increment per normalized unit:

- Roads:  
  cumulative length / number of road features  

- Buildings:  
  cumulative area / number of building features  

This metric is intended to approximate the average contribution of newly added features over time.

---

## Validation Framework

A series of validation tests was conducted to evaluate the quality and robustness of the metric:

### Validation Test 1 – Controlled Regions
The metric was evaluated on regions where:
- Buildings are considered complete  
- Roads are considered incomplete  

A statistical threshold of α = 0.1 was used.

---

### Validation Test 2 – Density and Distribution Analysis
Histogram-based analysis of feature density was performed at the final extraction date (01/01/2025), in order to assess whether the metric aligns with expected distributional behavior.

---

### Validation Test 3 – Global Random Regions
The metric was applied to randomly selected regions worldwide to assess its generalization ability.

---

### Validation Test 4 – Maximum Increment Constraint
A constraint on maximum allowed increment was introduced for regions considered complete, in order to stabilize the metric under saturation conditions.

---

## Data and Implementation

### Code
All analyses were implemented using Jupyter notebooks organized according to the workflow stages described above.  
A dedicated reusable functions module was also developed to ensure reproducibility and facilitate further experimentation.

### Data
The dataset consists of time-series extractions of spatial polygons, where each polygon was sampled at monthly intervals.

To reduce computational overhead and repeated API calls, all extracted data were stored locally as CSV files.

---

## Repository Structure

### Code/Quality measures/Feature completeness

This directory contains notebooks organized according to the research workflow:

- **Functions**  
  A notebook containing all functions used throughout the analysis.  
  Also available as a `.py` module for reuse.

- **measure_test**  
  Initial evaluation of candidate metrics, used to determine the final chosen formulation.

- **measure_test_2**  
  Evaluation of the selected metric on a sample of large-scale change events.

- **validity_events_building_1_ways_0**  
  Validation in regions where buildings are complete and roads are incomplete (α = 0.1).

- **validity_density**  
  Density-based analysis of buildings and roads at the final data extraction date.

- **validity_new_areas**  
  Evaluation on randomly selected global regions.

- **Updated validity_density**  
  Revised version incorporating metric adjustments and absolute increment thresholds.

---

### Data/Feature completeness on large scale sample

This directory includes:

#### Main Data Files
CSV files containing sampled extraction results.  
These were pre-saved to avoid repeated API queries.

#### Subdirectories

- **tests**  
  Results of metric evaluation experiments (including corrected versions, α = 0.1).

- **validity**  
  Density extraction outputs used in validation tests (stages D–F).

- **plots**  
  Visualizations generated throughout the analysis, organized by workflow stage.

---

## Notes and Limitations

- In Validation Test 3, some plots exhibited nearly linear behavior.  
  This is likely due to the structure of the time-series data after API extraction.

- These results raise concerns regarding the robustness and generalizability of the metric across heterogeneous regions.

- In contrast, results from Validation Test 2 suggest that imposing strict density constraints may reduce the ability of the metric to represent completeness accurately.

- An additional analysis was performed to examine saturation behavior, where regions exceeding 150% cumulative growth were classified as non-saturated.

---

## Future Work

- Improve preprocessing and structuring of API-derived time-series data  
- Enhance robustness of the metric across diverse geographic contexts  
- Re-evaluate the role of density constraints in completeness estimation  
- Investigate anomalies observed in global validation experiments  

---

## Conclusion

This study proposes a methodology for measuring spatial data completeness using a normalized increment-based metric.  
While initial results are promising, further refinement and validation are required to ensure robustness and applicability at scale.