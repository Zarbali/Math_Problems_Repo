# Problem 8 — Waiting Times and Empirical CDF

## Generated files

- Dataset: [`problem_08_waiting_times.csv`](problem_08_waiting_times.csv)
- Overall summary: [`waiting_time_summary_overall.csv`](waiting_time_summary_overall.csv)
- Service summary: [`waiting_time_summary_by_service_type.csv`](waiting_time_summary_by_service_type.csv)
- ECDF estimates: [`ecdf_probability_estimates.csv`](ecdf_probability_estimates.csv)
- Quantiles: [`waiting_time_quantiles_by_service_type.csv`](waiting_time_quantiles_by_service_type.csv)
- Histograms: [`waiting_time_histograms_by_service_type.png`](waiting_time_histograms_by_service_type.png)
- ECDF plot: [`waiting_time_ecdf_by_service_type.png`](waiting_time_ecdf_by_service_type.png)
- Boxplot: [`waiting_time_boxplot_by_service_type.png`](waiting_time_boxplot_by_service_type.png)

## Description

One row represents one service ticket, its service type, waiting time, and whether it was resolved within 10 minutes.


## Service summary

| service_type | tickets | mean | median | q1 | q3 | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| priority | 160 | 5.8512 | 5.1250 | 2.6475 | 7.9425 | 3.9044 | 0.4600 | 26.4900 |
| standard | 340 | 14.2555 | 12.2400 | 7.1850 | 19.9025 | 9.0519 | 0.6500 | 55.3400 |


## ECDF estimates

| event | empirical_probability |
| --- | --- |
| waiting time <= 5 | 0.2440 |
| waiting time <= 10 | 0.5380 |
| waiting time > 20 | 0.1700 |


## Interpretation

Priority tickets have shorter waiting times across the distribution, not only on average. The ECDF makes probability statements such as probability of waiting at most 10 minutes visible directly from the data.
