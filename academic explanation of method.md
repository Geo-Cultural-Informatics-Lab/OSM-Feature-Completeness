Feature Completeness Assessment Method

This study proposes a method for assessing the completeness of geospatial feature datasets, such as OpenStreetMap (OSM) roads or buildings, based on their temporal evolution.

The method relies on the assumption that mapping processes typically follow a coarse-to-fine pattern, where large and prominent features are digitized earlier, followed by smaller and more detailed elements. Consequently, the average feature size is expected to decrease over time and converge toward a stable value as the dataset approaches completeness.

To capture this behavior, we define a cumulative measure of average feature size:

cc_t = size_t / count_t

where size_t denotes the cumulative size (e.g., total length or area) and count_t denotes the cumulative number of features at time t.

To enable comparison across time, the measure is normalized:

ccp_t = cc_t / max(cc_t)

where ccp_t represents the relative cumulative change, scaled to the range [0,1].

A dataset is considered complete if a saturation period can be identified in which the relative cumulative change remains consistently low and stable. The detection of this period is subject to the following conditions:

(1) Low Relative Change:  
The normalized measure must remain below a predefined threshold (alpha), indicating minimal structural change in the dataset.

(2) Temporal Stability:  
This condition must persist for a minimum duration (e.g., two years), ensuring that the observed stability is not a short-term fluctuation.

(3) Robustness to External Events:  
The method accounts for potential disruptions such as large data imports or coordinated mapping campaigns, which may artificially alter the temporal signal.

(4) Bounded Growth After Saturation:  
To prevent false identification of completeness, the total growth after the detected saturation point must remain bounded. Specifically, the ratio between the final feature count and the count at the saturation point must not exceed a predefined threshold.

If all conditions are satisfied, the method identifies a saturation point and estimates the time at which the dataset reaches a predefined completeness level (e.g., 80%). Otherwise, the dataset is classified as incomplete.

Overall, the proposed approach provides a robust, data-driven framework for detecting completeness by identifying stabilization in the structural properties of mapped features over time.
