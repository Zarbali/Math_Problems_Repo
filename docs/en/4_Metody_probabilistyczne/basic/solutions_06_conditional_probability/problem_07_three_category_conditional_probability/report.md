# Problem 7 — Conditional Probability with Three Categories

## Generated files

- Activity-level summary: [`activity_level_summary.csv`](activity_level_summary.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of customers is 400.

Let:

$$
H=\text{the customer has high activity},
$$

$$
M=\text{the customer has medium activity},
$$

$$
L=\text{the customer has low activity},
$$

$$
R=\text{the customer renewed the subscription}.
$$

## Partition of the sample space

The events \(H\), \(M\), and \(L\) form a partition of the sample space because every customer belongs to exactly one activity level:

- high activity,
- medium activity,
- low activity.

The categories do not overlap, and together they cover all 400 customers.

## Activity-level summary

| Activity level | Total count | Renewed count | \(P(\text{category})\) | \(P(R\mid \text{category})\) | Contribution to \(P(R)\) | \(P(\text{category}\mid R)\) |
| :------------- | ----------: | ------------: | ---------------------: | ---------------------------: | -----------------------: | ---------------------------: |
| High | 100 | 80 | 0.250 | 0.800 | 0.200 | 0.400 |
| Medium | 150 | 90 | 0.375 | 0.600 | 0.225 | 0.450 |
| Low | 150 | 30 | 0.375 | 0.200 | 0.075 | 0.150 |

## Category probabilities

$$
P(H)=\frac{100}{400}=0.25.
$$

$$
P(M)=\frac{150}{400}=0.375.
$$

$$
P(L)=\frac{150}{400}=0.375.
$$

## Conditional renewal probabilities

$$
P(R\mid H)=\frac{80}{100}=0.80.
$$

$$
P(R\mid M)=\frac{90}{150}=0.60.
$$

$$
P(R\mid L)=\frac{30}{150}=0.20.
$$

## Law of total probability

Using the law of total probability:

$$
P(R)=P(R\mid H)P(H)+P(R\mid M)P(M)+P(R\mid L)P(L).
$$

Substituting the values:

$$
P(R)=0.80\cdot 0.25+0.60\cdot 0.375+0.20\cdot 0.375.
$$

Therefore:

$$
P(R)=0.200+0.225+0.075=0.500.
$$

This agrees with the table, because:

$$
P(R)=\frac{200}{400}=0.50.
$$

## Reverse conditional probabilities

Among customers who renewed, the probability of high activity is:

$$
P(H\mid R)=\frac{80}{200}=0.40.
$$

Among customers who renewed, the probability of medium activity is:

$$
P(M\mid R)=\frac{90}{200}=0.45.
$$

Among customers who renewed, the probability of low activity is:

$$
P(L\mid R)=\frac{30}{200}=0.15.
$$

## Interpretation

\(P(R\mid H)=0.80\) means that among high-activity customers, 80% renewed.

\(P(H\mid R)=0.40\) means that among customers who renewed, 40% were high-activity customers.

These are different questions. High-activity customers have the highest renewal rate, but medium-activity customers form the largest group among renewed customers because there are more medium-activity customers in the dataset.
