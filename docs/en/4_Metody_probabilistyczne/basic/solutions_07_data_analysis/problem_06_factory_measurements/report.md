# Problem 6 — Factory Measurements and Specification Limits

## Generated files

- Dataset: [`problem_06_factory_measurements.csv`](problem_06_factory_measurements.csv)
- Overall summary: [`length_summary_overall.csv`](length_summary_overall.csv)
- Machine summary: [`length_summary_by_machine.csv`](length_summary_by_machine.csv)
- Within-spec counts: [`within_spec_counts_by_machine.csv`](within_spec_counts_by_machine.csv)
- Boxplot: [`length_boxplots_by_machine.png`](length_boxplots_by_machine.png)
- Within-spec plot: [`within_spec_proportion_by_machine.png`](within_spec_proportion_by_machine.png)
- Mean-deviation plot: [`mean_deviation_by_machine.png`](mean_deviation_by_machine.png)

## Description

One row represents one manufactured part, the machine that produced it, its measured length, and whether it is within specification.


## Machine summary

| machine | count | mean | median | std | mean_deviation | mean_abs_deviation | within_spec_proportion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M1 | 180 | 49.9813 | 49.9720 | 0.5343 | -0.0187 | 0.4399 | 1.0000 |
| M2 | 180 | 50.3074 | 50.2755 | 0.7910 | 0.3074 | 0.6513 | 0.9222 |
| M3 | 180 | 49.7106 | 49.7310 | 0.6135 | -0.2894 | 0.5426 | 0.9778 |


## Interpretation

M1 is closest to the target and least variable. M2 has the largest mean length and largest variability, which explains its lower within-spec proportion; this shows why mean and spread must be interpreted together.
