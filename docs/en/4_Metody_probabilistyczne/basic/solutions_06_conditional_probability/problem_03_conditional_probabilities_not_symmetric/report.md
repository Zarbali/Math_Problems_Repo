# Problem 3 — Conditional Probabilities Are Not Symmetric

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of users is 150.

Let:

$$
W=\text{the user watched the lecture},
$$

$$
Q=\text{the user passed the quiz}.
$$

## Four regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(W\cap Q\) | watched lecture and passed quiz | 72 | 0.4800 |
| \(W\cap Q^c\) | watched lecture and did not pass quiz | 18 | 0.1200 |
| \(W^c\cap Q\) | did not watch lecture and passed quiz | 28 | 0.1867 |
| \(W^c\cap Q^c\) | did not watch lecture and did not pass quiz | 32 | 0.2133 |

## Conditional probabilities

The probability that a user passed the quiz given that the user watched the lecture is:

$$
P(Q\mid W)=\frac{72}{90}=0.80.
$$

The probability that a user watched the lecture given that the user passed the quiz is:

$$
P(W\mid Q)=\frac{72}{100}=0.72.
$$

The probability that a user passed the quiz given that the user did not watch the lecture is:

$$
P(Q\mid W^c)=\frac{28}{60}\approx 0.4667.
$$

The probability that a user watched the lecture given that the user did not pass the quiz is:

$$
P(W\mid Q^c)=\frac{18}{50}=0.36.
$$

## Why \(P(Q\mid W)\) and \(P(W\mid Q)\) are different

\(P(Q\mid W)\) looks only at users who watched the lecture. It asks:

> Among lecture watchers, what proportion passed the quiz?

\(P(W\mid Q)\) looks only at users who passed the quiz. It asks:

> Among users who passed the quiz, what proportion watched the lecture?

These are different reference groups, so the probabilities do not have to be equal.

## Which probability helps answer which question?

If we want to know whether watching the lecture helps, the more useful comparison is:

$$
P(Q\mid W) \quad \text{and} \quad P(Q\mid W^c).
$$

Here:

$$
P(Q\mid W)=0.80,
$$

while:

$$
P(Q\mid W^c)\approx 0.4667.
$$

The pass rate is much higher among users who watched the lecture.

If we want to describe users who passed the quiz, then \(P(W\mid Q)\) is more useful. It tells us that among users who passed, 72% watched the lecture.

## Conclusion

The data suggest that watching the lecture is associated with a higher quiz pass rate. However, the two conditional probabilities \(P(Q\mid W)\) and \(P(W\mid Q)\) answer different questions and should not be confused.
