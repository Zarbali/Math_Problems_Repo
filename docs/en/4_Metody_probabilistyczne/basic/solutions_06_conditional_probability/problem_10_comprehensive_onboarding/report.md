# Problem 10 — Comprehensive Problem: Event Algebra, Conditioning, Independence, and Bayes

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of users is 500.

Let:

$$
T=\text{the user received the tutorial},
$$

$$
C=\text{the user completed onboarding}.
$$

## Four disjoint regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(T\cap C\) | received tutorial and completed onboarding | 180 | 0.36 |
| \(T\cap C^c\) | received tutorial and did not complete onboarding | 70 | 0.14 |
| \(T^c\cap C\) | did not receive tutorial and completed onboarding | 120 | 0.24 |
| \(T^c\cap C^c\) | did not receive tutorial and did not complete onboarding | 130 | 0.26 |

The four probabilities add up to:

$$
0.36+0.14+0.24+0.26=1.
$$

## Probabilities of \(T\), \(C\), and \(T\cup C\)

The probability that a user received the tutorial is:

$$
P(T)=\frac{250}{500}=0.50.
$$

The probability that a user completed onboarding is:

$$
P(C)=\frac{300}{500}=0.60.
$$

The probability that a user both received the tutorial and completed onboarding is:

$$
P(T\cap C)=\frac{180}{500}=0.36.
$$

Using inclusion-exclusion:

$$
P(T\cup C)=P(T)+P(C)-P(T\cap C).
$$

Therefore:

$$
P(T\cup C)=0.50+0.60-0.36=0.74.
$$

## Completion probabilities by tutorial status

The probability that a user completed onboarding given that the user received the tutorial is:

$$
P(C\mid T)=\frac{180}{250}=0.72.
$$

The probability that a user completed onboarding given that the user did not receive the tutorial is:

$$
P(C\mid T^c)=\frac{120}{250}=0.48.
$$

The difference is:

$$
0.72-0.48=0.24.
$$

The ratio is:

$$
\frac{0.72}{0.48}=1.5.
$$

So the completion rate is 1.5 times as large among users who received the tutorial.

## Tutorial probabilities by completion status

The probability that a user received the tutorial given that the user completed onboarding is:

$$
P(T\mid C)=\frac{180}{300}=0.60.
$$

The probability that a user received the tutorial given that the user did not complete onboarding is:

$$
P(T\mid C^c)=\frac{70}{200}=0.35.
$$

## Independence

To check independence, compare \(P(T\cap C)\) with \(P(T)P(C)\):

$$
P(T)P(C)=0.50\cdot 0.60=0.30.
$$

But:

$$
P(T\cap C)=0.36.
$$

Since:

$$
0.36\neq 0.30,
$$

the events \(T\) and \(C\) are not independent.

Equivalently:

$$
P(C\mid T)=0.72
$$

is different from:

$$
P(C)=0.60.
$$

## Does receiving the tutorial change completion probability?

Yes. The completion probability is higher for users who received the tutorial:

$$
P(C\mid T)=0.72
$$

compared with:

$$
P(C\mid T^c)=0.48.
$$

In this dataset, receiving the tutorial is associated with a higher probability of completing onboarding.

## Difference between \(P(C\mid T)\) and \(P(T\mid C)\)

\(P(C\mid T)=0.72\) asks:

> Among users who received the tutorial, what proportion completed onboarding?

\(P(T\mid C)=0.60\) asks:

> Among users who completed onboarding, what proportion received the tutorial?

These are different questions because they use different reference groups.

## Short interpretation

The data suggest that the tutorial is associated with better onboarding completion. Users who received the tutorial completed onboarding at a rate of 72%, while users who did not receive the tutorial completed onboarding at a rate of 48%. The events of receiving the tutorial and completing onboarding are not independent.
