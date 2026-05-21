# Problem 1 — Event Algebra from a Two-Way Table

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of students is 100.

Let:

$$
A=\text{the student attends lectures regularly},
$$

$$
B=\text{the student submits homework on time}.
$$

## Four disjoint regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(A\cap B\) | attends regularly and submits on time | 48 | 0.48 |
| \(A\cap B^c\) | attends regularly and does not submit on time | 12 | 0.12 |
| \(A^c\cap B\) | does not attend regularly and submits on time | 22 | 0.22 |
| \(A^c\cap B^c\) | does not attend regularly and does not submit on time | 18 | 0.18 |

These four regions add up to:

$$
0.48+0.12+0.22+0.18=1.
$$

## Probabilities of \(A\), \(B\), and \(A\cup B\)

We have:

$$
P(A)=P(A\cap B)+P(A\cap B^c)=0.48+0.12=0.60.
$$

Also:

$$
P(B)=P(A\cap B)+P(A^c\cap B)=0.48+0.22=0.70.
$$

Using inclusion-exclusion:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

Therefore:

$$
P(A\cup B)=0.60+0.70-0.48=0.82.
$$

## Conditional probabilities

The probability that a student attends lectures regularly given that the student submits homework on time is:

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
=\frac{0.48}{0.70}
\approx 0.6857.
$$

The probability that a student submits homework on time given that the student attends lectures regularly is:

$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)}
=\frac{0.48}{0.60}
=0.80.
$$

## Mutual exclusiveness

The events \(A\) and \(B\) are not mutually exclusive, because:

$$
P(A\cap B)=0.48\neq 0.
$$

There are 48 students who both attend lectures regularly and submit homework on time.

## Independence

To check independence, compare \(P(A\cap B)\) with \(P(A)P(B)\):

$$
P(A)P(B)=0.60\cdot 0.70=0.42.
$$

But:

$$
P(A\cap B)=0.48.
$$

Since:

$$
0.48\neq 0.42,
$$

the events \(A\) and \(B\) are not independent.

Equivalently, \(P(B\mid A)=0.80\) is different from \(P(B)=0.70\), so knowing that a student attends lectures regularly changes the probability that the student submits homework on time.

## Interpretation

\(P(A\mid B)\approx 0.6857\) means that among students who submit homework on time, about 68.57% attend lectures regularly.

\(P(B\mid A)=0.80\) means that among students who attend lectures regularly, 80% submit homework on time.
