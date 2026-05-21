# Problem 4 — Delivery Times, Skewness, and Outliers

## Generated files

- Dataset: [`problem_04_delivery_times.csv`](problem_04_delivery_times.csv)
- Overall summary: [`delivery_time_summary.csv`](delivery_time_summary.csv)
- Zone summary: [`delivery_time_summary_by_zone.csv`](delivery_time_summary_by_zone.csv)
- Outliers: [`outliers_1_5_iqr.csv`](outliers_1_5_iqr.csv)
- Histogram: [`delivery_time_histogram.png`](delivery_time_histogram.png)
- Boxplot: [`delivery_time_boxplot_by_zone.png`](delivery_time_boxplot_by_zone.png)

## Description

One row represents one delivery with a zone, delivery time, and delayed/not delayed indicator.


## Overall summary

| deliveries | mean | median | q1 | q2 | q3 | iqr | lower_fence | upper_fence | possible_outliers | delayed_proportion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 350.0000 | 37.7300 | 33.3000 | 24.6250 | 33.3000 | 43.7750 | 19.1500 | -4.1000 | 72.5000 | 20.0000 | 0.1000 |


## Zone summary

| zone | count | mean | median | std | min | max | delayed_proportion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| central | 154 | 38.6864 | 33.0000 | 25.3375 | 10.0000 | 232.5000 | 0.1169 |
| remote | 56 | 39.1679 | 36.4500 | 18.5686 | 16.0000 | 128.1000 | 0.0893 |
| suburban | 140 | 36.1029 | 33.0500 | 19.8546 | 11.3000 | 151.0000 | 0.0857 |


## Interpretation

The mean is larger than the median because the distribution is right-skewed and contains unusually long delivery times. The boxplot and outlier file make this visible; the median is therefore a better description of a typical delivery than the mean alone.
