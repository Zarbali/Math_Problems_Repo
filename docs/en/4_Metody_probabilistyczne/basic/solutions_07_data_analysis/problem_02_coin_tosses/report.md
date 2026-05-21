# Problem 2 — Coin Tosses and Relative Frequencies

## Generated files

- Dataset: [`problem_02_coin_tosses.csv`](problem_02_coin_tosses.csv)
- Frequency table: [`frequency_table.csv`](frequency_table.csv)
- Checkpoints: [`relative_frequency_checkpoints.csv`](relative_frequency_checkpoints.csv)
- Line plot: [`relative_frequency_heads.png`](relative_frequency_heads.png)
- Seed comparison: [`seed_sample_size_comparison.csv`](seed_sample_size_comparison.csv)
- Seed comparison plot: [`seed_sample_size_comparison.png`](seed_sample_size_comparison.png)

## Description

One row represents one coin toss. The cumulative columns show how the empirical proportion of heads changes as more observations are collected.


## Frequency table

| result | frequency | relative_frequency |
| --- | --- | --- |
| H | 1038 | 0.5190 |
| T | 962 | 0.4810 |


## Checkpoints

| trial | cumulative_heads | relative_frequency_heads |
| --- | --- | --- |
| 10.0000 | 6.0000 | 0.6000 |
| 20.0000 | 13.0000 | 0.6500 |
| 50.0000 | 27.0000 | 0.5400 |
| 100.0000 | 55.0000 | 0.5500 |
| 200.0000 | 105.0000 | 0.5250 |
| 500.0000 | 262.0000 | 0.5240 |
| 1000.0000 | 521.0000 | 0.5210 |
| 2000.0000 | 1038.0000 | 0.5190 |


## Interpretation

Early relative frequencies move strongly because each new toss has high influence. Later the curve becomes more stable and stays near the generating value 0.52; different seeds still create different samples, especially for small sample sizes.
