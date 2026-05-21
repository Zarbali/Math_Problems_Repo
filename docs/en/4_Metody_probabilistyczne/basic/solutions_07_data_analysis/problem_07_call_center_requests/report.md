# Problem 7 — Call Center Requests Over Time

## Generated files

- Dataset: [`problem_07_call_center_requests.csv`](problem_07_call_center_requests.csv)
- Hourly summary: [`hourly_requests_summary.csv`](hourly_requests_summary.csv)
- Day-type summary: [`requests_summary_by_day_type.csv`](requests_summary_by_day_type.csv)
- Average by hour: [`average_requests_by_hour.csv`](average_requests_by_hour.csv)
- Average by hour/day type: [`average_requests_by_hour_and_day_type.csv`](average_requests_by_hour_and_day_type.csv)
- Daily totals: [`daily_total_requests.csv`](daily_total_requests.csv)
- Daily summary: [`daily_total_summary_by_day_type.csv`](daily_total_summary_by_day_type.csv)
- Average-hour plot: [`average_requests_by_hour.png`](average_requests_by_hour.png)
- Average-hour/day-type plot: [`average_requests_by_hour_and_day_type.png`](average_requests_by_hour_and_day_type.png)
- Histogram: [`hourly_requests_histogram.png`](hourly_requests_histogram.png)
- Day-type bar plot: [`mean_hourly_requests_by_day_type.png`](mean_hourly_requests_by_day_type.png)

## Description

One row represents one hour in the call center, including date, day type, hour, and request count.


## Hourly summary

| count | mean | median | variance | std | min | q1 | q3 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 720.0000 | 3.8542 | 3.0000 | 11.1484 | 3.3389 | 0.0000 | 1.0000 | 6.0000 | 19.0000 |


## Day-type summary

| day_type | hours | mean | variance | std | min | max |
| --- | --- | --- | --- | --- | --- | --- |
| weekday | 504 | 4.3452 | 12.9700 | 3.6014 | 0 | 19 |
| weekend | 216 | 2.7083 | 5.0541 | 2.2481 | 0 | 9 |


## Interpretation

The dataset is related to Poisson count models, but the whole table should not be treated as one fixed-rate Poisson sample. Hour and day type change the request rate, so the overall variance is inflated by mixing different conditions.
