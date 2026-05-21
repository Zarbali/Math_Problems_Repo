# Problem 5 — Customer Survey and Conditional Frequencies

## Generated files

- Dataset: [`problem_05_customer_survey.csv`](problem_05_customer_survey.csv)
- Age frequencies: [`frequency_age_group.csv`](frequency_age_group.csv)
- Channel frequencies: [`frequency_channel.csv`](frequency_channel.csv)
- Satisfaction frequencies: [`frequency_satisfaction.csv`](frequency_satisfaction.csv)
- Renewed frequencies: [`frequency_renewed.csv`](frequency_renewed.csv)
- Conditional probabilities: [`conditional_probabilities.csv`](conditional_probabilities.csv)
- Renewal by channel: [`renewal_rate_by_channel.csv`](renewal_rate_by_channel.csv)
- Renewal by satisfaction: [`renewal_rate_by_satisfaction.csv`](renewal_rate_by_satisfaction.csv)
- Satisfaction plot: [`satisfaction_frequency_bar.png`](satisfaction_frequency_bar.png)
- Channel plot: [`channel_frequency_bar.png`](channel_frequency_bar.png)
- Age plot: [`age_group_frequency_bar.png`](age_group_frequency_bar.png)
- Renewal by channel plot: [`renewal_rate_by_channel.png`](renewal_rate_by_channel.png)
- Renewal by satisfaction plot: [`renewal_rate_by_satisfaction.png`](renewal_rate_by_satisfaction.png)

## Description

One row represents one surveyed customer, with categorical attributes, a satisfaction score, and a renewal indicator.


## Conditional probabilities

| quantity | value |
| --- | --- |
| probability of renewal among customers with satisfaction equal to 5 | 0.9545 |
| probability of satisfaction equal to 5 among customers who renewed | 0.2313 |
| overall renewal rate | 0.7567 |


## Renewal by satisfaction

| satisfaction | renewed_customers | total_customers | renewal_rate |
| --- | --- | --- | --- |
| 1.0000 | 3.0000 | 5.0000 | 0.6000 |
| 2.0000 | 27.0000 | 51.0000 | 0.5294 |
| 3.0000 | 140.0000 | 217.0000 | 0.6452 |
| 4.0000 | 179.0000 | 217.0000 | 0.8249 |
| 5.0000 | 105.0000 | 110.0000 | 0.9545 |


## Interpretation

The renewal rate increases with satisfaction, and mobile-app customers have the highest renewal rate. The two conditional probabilities answer different questions: renewal among very satisfied customers versus the proportion of very satisfied customers among those who renewed.
