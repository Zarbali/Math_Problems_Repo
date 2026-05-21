# Problem 3 — Exam Scores in Two Groups

## Generated files

- Dataset: [`problem_03_exam_scores.csv`](problem_03_exam_scores.csv)
- Overall summary: [`overall_score_summary.csv`](overall_score_summary.csv)
- Group summary: [`score_summary_by_group.csv`](score_summary_by_group.csv)
- Pass rates: [`pass_rate_by_group.csv`](pass_rate_by_group.csv)
- Histograms: [`score_histograms_by_group.png`](score_histograms_by_group.png)
- Boxplots: [`score_boxplots_by_group.png`](score_boxplots_by_group.png)
- Pass-rate plot: [`pass_rate_by_group.png`](pass_rate_by_group.png)

## Description

One row represents one student, with group membership, exam score, and pass/fail indicator.


## Overall summary

| count | mean | median | variance | std | min | q1 | q3 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 240.0000 | 71.1275 | 70.4000 | 230.7435 | 15.1902 | 27.6000 | 61.6500 | 82.3500 | 100.0000 |


## Group summary

| group | count | mean | median | variance | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 120 | 69.8492 | 68.9000 | 132.1936 | 11.4975 | 39.9000 | 94.2000 |
| B | 120 | 72.4058 | 72.4500 | 327.9367 | 18.1090 | 27.6000 | 100.0000 |


## Pass rates

| group | passed_students | total_students | pass_rate |
| --- | --- | --- | --- |
| A | 117 | 120 | 0.9750 |
| B | 105 | 120 | 0.8750 |


## Interpretation

Group B has the higher mean and median, but it also has much larger variability and a lower pass rate. This is a useful example of why comparing only means can hide important distributional differences.
