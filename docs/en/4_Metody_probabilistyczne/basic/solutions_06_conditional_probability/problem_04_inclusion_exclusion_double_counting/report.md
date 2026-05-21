# Problem 4 — Inclusion-Exclusion and Double Counting

## Generated files

- Regions: [`regions.csv`](regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of employees is 200.

Let:

$$
A=\text{the employee uses Tool A},
$$

$$
B=\text{the employee uses Tool B}.
$$

The survey gives:

$$
|A|=130,\quad |B|=90,\quad |A\cap B|=60.
$$

## Basic probabilities

$$
P(A)=\frac{130}{200}=0.65.
$$

$$
P(B)=\frac{90}{200}=0.45.
$$

$$
P(A\cap B)=\frac{60}{200}=0.30.
$$

## Inclusion-exclusion

Using inclusion-exclusion:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

Therefore:

$$
P(A\cup B)=0.65+0.45-0.30=0.80.
$$

So 80% of employees use at least one of the two tools.

## Remaining regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(A\cap B\) | uses both Tool A and Tool B | 60 | 0.30 |
| \(A\setminus B\) | uses Tool A but not Tool B | 70 | 0.35 |
| \(B\setminus A\) | uses Tool B but not Tool A | 30 | 0.15 |
| \(A^c\cap B^c\) | uses neither tool | 40 | 0.20 |

The three remaining regions requested in the task are:

$$
P(A\setminus B)=\frac{70}{200}=0.35,
$$

$$
P(B\setminus A)=\frac{30}{200}=0.15,
$$

$$
P(A^c\cap B^c)=\frac{40}{200}=0.20.
$$

## Conditional probabilities

The probability that an employee uses Tool A given that the employee uses Tool B is:

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
=\frac{60}{90}
\approx 0.6667.
$$

The probability that an employee uses Tool B given that the employee uses Tool A is:

$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)}
=\frac{60}{130}
\approx 0.4615.
$$

## Why \(P(A\cup B)\neq P(A)+P(B)\)

If we add \(P(A)+P(B)\), we get:

$$
P(A)+P(B)=0.65+0.45=1.10.
$$

This is not equal to \(P(A\cup B)=0.80\), because employees who use both tools are counted twice: once in \(A\) and once in \(B\).

The group counted twice is:

$$
A\cap B.
$$

This group has probability:

$$
P(A\cap B)=0.30.
$$

Subtracting this overlap gives the correct union probability:

$$
1.10-0.30=0.80.
$$
