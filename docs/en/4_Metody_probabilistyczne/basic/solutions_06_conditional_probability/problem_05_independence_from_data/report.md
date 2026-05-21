# Problem 5 — Independence from Data

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of users is 200.

Let:

$$
A=\text{the user has a premium account},
$$

$$
M=\text{the user watched a movie during the weekend}.
$$

## Basic probabilities

The probability that a user has a premium account is:

$$
P(A)=\frac{120}{200}=0.60.
$$

The probability that a user watched a movie during the weekend is:

$$
P(M)=\frac{140}{200}=0.70.
$$

The probability that a user has a premium account and watched a movie is:

$$
P(A\cap M)=\frac{84}{200}=0.42.
$$

## Four regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(A\cap M\) | premium and watched a movie | 84 | 0.42 |
| \(A\cap M^c\) | premium and did not watch a movie | 36 | 0.18 |
| \(A^c\cap M\) | free and watched a movie | 56 | 0.28 |
| \(A^c\cap M^c\) | free and did not watch a movie | 24 | 0.12 |

## Conditional probabilities

The probability that a premium user watched a movie is:

$$
P(M\mid A)=\frac{84}{120}=0.70.
$$

The probability that a free user watched a movie is:

$$
P(M\mid A^c)=\frac{56}{80}=0.70.
$$

The two conditional probabilities are equal.

## Independence

To check independence, compare \(P(A\cap M)\) with \(P(A)P(M)\):

$$
P(A)P(M)=0.60\cdot 0.70=0.42.
$$

Also:

$$
P(A\cap M)=0.42.
$$

Since:

$$
P(A\cap M)=P(A)P(M),
$$

the events \(A\) and \(M\) are independent in this dataset.

Equivalently:

$$
P(M\mid A)=P(M\mid A^c)=P(M)=0.70.
$$

## Interpretation

Independence means that knowing whether a user has a premium account does not change the probability that the user watched a movie during the weekend.

In this dataset, 70% of premium users watched a movie and 70% of free users watched a movie. Therefore, account type does not appear to be related to watching a movie during the weekend.
