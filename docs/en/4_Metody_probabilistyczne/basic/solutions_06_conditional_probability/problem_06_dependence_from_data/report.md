# Problem 6 — Dependence from Data

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of parcels is 600.

Let:

$$
I=\text{the parcel is international},
$$

$$
D=\text{the parcel is delayed}.
$$

## Basic probabilities

The probability that a parcel is international is:

$$
P(I)=\frac{200}{600}=\frac{1}{3}\approx 0.3333.
$$

The probability that a parcel is delayed is:

$$
P(D)=\frac{60}{600}=0.10.
$$

The probability that a parcel is both international and delayed is:

$$
P(I\cap D)=\frac{36}{600}=0.06.
$$

## Four regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(I\cap D\) | international and delayed | 36 | 0.0600 |
| \(I\cap D^c\) | international and not delayed | 164 | 0.2733 |
| \(I^c\cap D\) | domestic and delayed | 24 | 0.0400 |
| \(I^c\cap D^c\) | domestic and not delayed | 376 | 0.6267 |

## Conditional probabilities

The probability that an international parcel is delayed is:

$$
P(D\mid I)=\frac{36}{200}=0.18.
$$

The probability that a domestic parcel is delayed is:

$$
P(D\mid I^c)=\frac{24}{400}=0.06.
$$

The probability that a delayed parcel is international is:

$$
P(I\mid D)=\frac{36}{60}=0.60.
$$

## Independence

To check independence, compare \(P(I\cap D)\) with \(P(I)P(D)\):

$$
P(I)P(D)=\frac{1}{3}\cdot 0.10\approx 0.0333.
$$

But:

$$
P(I\cap D)=0.06.
$$

Since:

$$
0.06\neq 0.0333,
$$

the events \(I\) and \(D\) are not independent.

Equivalently:

$$
P(D\mid I)=0.18
$$

is different from:

$$
P(D)=0.10.
$$

## Does international shipping increase the probability of delay?

Yes. The delay probability for international parcels is:

$$
P(D\mid I)=0.18,
$$

while the delay probability for domestic parcels is:

$$
P(D\mid I^c)=0.06.
$$

The difference is:

$$
0.18-0.06=0.12.
$$

The risk ratio is:

$$
\frac{0.18}{0.06}=3.
$$

So international parcels are three times as likely to be delayed as domestic parcels in this dataset.

## Difference between \(P(D\mid I)\) and \(P(I\mid D)\)

\(P(D\mid I)=0.18\) asks:

> Among international parcels, what proportion are delayed?

\(P(I\mid D)=0.60\) asks:

> Among delayed parcels, what proportion are international?

These are different conditional probabilities because they use different reference groups.
