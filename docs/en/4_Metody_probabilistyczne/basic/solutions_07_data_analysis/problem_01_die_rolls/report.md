# Problem 1 — Die Rolls and Empirical Distribution

## Generated files

- Dataset: [`problem_01_die_rolls.csv`](problem_01_die_rolls.csv)
- Frequency table: [`frequency_table.csv`](frequency_table.csv)
- Event probabilities: [`event_probabilities.csv`](event_probabilities.csv)
- Distribution plot: [`empirical_distribution.png`](empirical_distribution.png)
- Seed/sample-size comparison: [`seed_sample_size_comparison.csv`](seed_sample_size_comparison.csv)
- Seed/sample-size plot: [`seed_sample_size_comparison.png`](seed_sample_size_comparison.png)

## Description

One row represents one die roll. The columns record the trial number, the observed face, and indicators for two events: even result and result at least 5.


## Frequency table

| roll | frequency | relative_frequency | fair_die_probability | generating_probability |
| --- | --- | --- | --- | --- |
| 1.0000 | 157.0000 | 0.1570 | 0.1667 | 0.1400 |
| 2.0000 | 174.0000 | 0.1740 | 0.1667 | 0.1600 |
| 3.0000 | 151.0000 | 0.1510 | 0.1667 | 0.1700 |
| 4.0000 | 184.0000 | 0.1840 | 0.1667 | 0.1800 |
| 5.0000 | 158.0000 | 0.1580 | 0.1667 | 0.1600 |
| 6.0000 | 176.0000 | 0.1760 | 0.1667 | 0.1900 |


## Empirical probabilities

| event | empirical_probability | fair_die_probability |
| --- | --- | --- |
| result is even | 0.5340 | 0.5000 |
| result is at least 5 | 0.3340 | 0.3333 |
| result is equal to 6 | 0.1760 | 0.1667 |


## Interpretation

The empirical distribution is close to, but not identical with, either the fair-die reference or the generating probabilities. The seed/sample-size plot shows the central lesson: changing the seed changes the empirical sample, while larger samples usually fluctuate less around the generating distribution.
