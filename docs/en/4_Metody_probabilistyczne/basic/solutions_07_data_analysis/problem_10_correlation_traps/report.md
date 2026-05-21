# Problem 10 — Correlation Traps

## Generated files

- Dataset: [`problem_10_correlation_traps.csv`](problem_10_correlation_traps.csv)
- Dataset without outliers: [`problem_10_without_outlier_group.csv`](problem_10_without_outlier_group.csv)
- Outlier observations: [`outlier_group_observations.csv`](outlier_group_observations.csv)
- Correlation summary: [`correlation_summary.csv`](correlation_summary.csv)
- Group summary: [`summary_by_group.csv`](summary_by_group.csv)
- Scatter with outliers: [`scatter_with_outliers.png`](scatter_with_outliers.png)
- Scatter without outliers: [`scatter_without_outliers.png`](scatter_without_outliers.png)
- Correlation plot: [`correlation_by_scope.png`](correlation_by_scope.png)

## Description

One row represents one observation with two numerical variables and a group label.


## Correlation summary

| data_scope | observation_count | correlation |
| --- | --- | --- |
| all observations | 264 | 0.0179 |
| without outlier_group | 260 | 0.0572 |
| left_branch only | 125 | -0.9428 |
| outlier_group only | 4 | 0.5292 |
| right_branch only | 135 | 0.9405 |


## Group summary

| group | observation_count | mean_x | mean_y | min_x | max_x | min_y | max_y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| left_branch | 125 | -2.1482 | 5.9510 | -3.9950 | -0.0630 | -2.1630 | 16.8040 |
| outlier_group | 4 | 8.2500 | 2.1250 | 7.5000 | 9.0000 | 1.0000 | 3.0000 |
| right_branch | 135 | 2.1446 | 6.0978 | 0.0690 | 3.9980 | -2.5950 | 17.5570 |


## Interpretation

The overall correlation is close to zero, but the scatter plot shows a strong U-shaped relationship. Within each branch the relationship is almost linear, so this problem demonstrates why correlation must be interpreted together with visualizations and subgroup structure.
