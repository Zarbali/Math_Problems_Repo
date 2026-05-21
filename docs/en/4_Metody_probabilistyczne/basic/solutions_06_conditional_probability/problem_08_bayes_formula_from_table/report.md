# Problem 8 — Bayes' Formula from a Table

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)
- Suspicious transactions breakdown: [`suspicious_transactions_breakdown.csv`](suspicious_transactions_breakdown.csv)

## Data

The total number of transactions is 10000.

Let:

$$
F=\text{the transaction is fraudulent},
$$

$$
S=\text{the transaction is marked suspicious}.
$$

## Basic probabilities

The base rate of fraud is:

$$
P(F)=\frac{100}{10000}=0.01.
$$

The probability that a fraudulent transaction is marked suspicious is:

$$
P(S\mid F)=\frac{98}{100}=0.98.
$$

The probability that a legitimate transaction is marked suspicious is:

$$
P(S\mid F^c)=\frac{297}{9900}=0.03.
$$

## Four regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(F\cap S\) | fraudulent and marked suspicious | 98 | 0.0098 |
| \(F\cap S^c\) | fraudulent and not marked suspicious | 2 | 0.0002 |
| \(F^c\cap S\) | legitimate and marked suspicious | 297 | 0.0297 |
| \(F^c\cap S^c\) | legitimate and not marked suspicious | 9603 | 0.9603 |

## Law of total probability

Using the law of total probability:

$$
P(S)=P(S\mid F)P(F)+P(S\mid F^c)P(F^c).
$$

Substituting the values:

$$
P(S)=0.98\cdot 0.01+0.03\cdot 0.99.
$$

Therefore:

$$
P(S)=0.0098+0.0297=0.0395.
$$

This agrees with the table:

$$
P(S)=\frac{395}{10000}=0.0395.
$$

## Bayes' formula

Bayes' formula gives:

$$
P(F\mid S)=\frac{P(S\mid F)P(F)}{P(S)}.
$$

So:

$$
P(F\mid S)=\frac{0.98\cdot 0.01}{0.0395}
=\frac{0.0098}{0.0395}
\approx 0.2481.
$$

Thus, among suspicious transactions, about 24.81% are fraudulent.

The complementary probability is:

$$
P(F^c\mid S)=1-P(F\mid S)\approx 0.7519.
$$

So about 75.19% of suspicious transactions are legitimate.

## Suspicious transactions breakdown

| Suspicious transaction type | Count | Conditional probability given suspicious |
| :-------------------------- | ----: | ---------------------------------------: |
| fraudulent | 98 | 0.2481 |
| legitimate | 297 | 0.7519 |

Among suspicious transactions, most transactions are legitimate, not fraudulent.

## Why this can happen

This can happen because fraudulent transactions are rare. The base rate is only:

$$
P(F)=0.01.
$$

Even though the system detects fraudulent transactions very well, there are many more legitimate transactions than fraudulent transactions. A small false positive rate applied to a very large legitimate group can produce many suspicious legitimate transactions.

Here, the system marks 98 fraudulent transactions as suspicious, but it also marks 297 legitimate transactions as suspicious. Therefore, most suspicious transactions are legitimate.

## Role of the base rate

The base rate \(P(F)\) tells us how common fraud is before using the detection system. It strongly affects \(P(F\mid S)\).

Ignoring the base rate can lead to the mistaken conclusion that a suspicious transaction is almost certainly fraudulent. In reality, because fraud is rare, a suspicious transaction has probability only about 0.2481 of being fraudulent in this dataset.
