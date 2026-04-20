# **Feature Completeness Assessment**

The `assess_feature_completeness` method is designed to evaluate whether a given region’s dataset (e.g., roads or buildings in OSM) can be considered complete.

## Core Idea

The method analyzes the time series of the average feature size, defined as the ratio between cumulative size (e.g., length or area) and cumulative feature count.

We assume that, in most OpenStreetMap mapping processes, features are added from large to small:
- Large, prominent features (e.g., major roads, large buildings) are mapped first
- Smaller, finer details are added later

As a result, the average size per feature is expected to decrease over time and eventually stabilize as mapping becomes more complete.

To capture this behavior, the method relies on cumulative values, which smooth short-term fluctuations and emphasize long-term trends.

## Mathematical Definition

For each timestamp t in [1, T] (monthly intervals):

cc_t = size_t / count_t

ccp_t = cc_t / max(cc_t)

Where:
- size_t is the cumulative size (length or area) at time t
- count_t is the cumulative number of features at time t
- cc_t represents the average size per feature
- ccp_t is the normalized average size (scaled to [0,1])

## Detecting Completeness

A dataset is considered complete if a stable saturation period can be identified. This period represents a stage where additional mapping does not significantly change the structure of the data.

The following conditions are applied:

1) Low Relative Change  
The normalized average size must remain below a threshold:
ccp_t < alpha  
(Default: alpha = 0.1)

2) Temporal Stability  
The low-change condition must persist for a minimum duration:
(Default: 2 years)

3) No Disruptive Events  
The stable period must not include significant anomalies such as:
- Large imports
- Humanitarian mapping events (e.g., HOT)
- Bulk edits

4) Bounded Post-Saturation Growth  
After the detected saturation point, total growth must remain limited:
count_T / count_sat < saturation_threshold  
(Default: 1.5)

This prevents cases where the data appears locally stable but continues to grow significantly afterward.

## Output

If all conditions are satisfied, the method:
- Identifies a saturation point
- Estimates when the dataset reached 80% completeness
- Returns either:
  - The full annotated time series, or
  - A truncated version up to the saturation point

If the conditions are not met, the dataset is classified as incomplete, and the full time series is returned for inspection.

## Summary

The method detects completeness by identifying when the average feature size stabilizes over time, with no significant structural or volumetric changes afterward.
