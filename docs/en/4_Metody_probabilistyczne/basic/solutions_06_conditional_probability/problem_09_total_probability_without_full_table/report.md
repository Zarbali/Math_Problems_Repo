# Problem 9 — Law of Total Probability Without a Full Table

## Generated files

- Channel cancellation summary: [`channel_cancellation_summary.csv`](channel_cancellation_summary.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

Let:

$$
W=\text{the order came through the website},
$$

$$
A=\text{the order came through the mobile app},
$$

$$
H=\text{the order came by phone},
$$

$$
C=\text{the order is cancelled}.
$$

The given probabilities are:

$$
P(W)=0.50,\quad P(A)=0.35,\quad P(H)=0.15.
$$

The cancellation probabilities are:

$$
P(C\mid W)=0.04,\quad P(C\mid A)=0.06,\quad P(C\mid H)=0.10.
$$

## Partition

The events \(W\), \(A\), and \(H\) form a partition of the sample space because every order comes through exactly one of the three channels:

- website,
- mobile app,
- phone.

The events are mutually exclusive and their probabilities add up to:

$$
0.50+0.35+0.15=1.
$$

## Law of total probability

Using the law of total probability:

$$
P(C)=P(C\mid W)P(W)+P(C\mid A)P(A)+P(C\mid H)P(H).
$$

Substituting the values:

$$
P(C)=0.04\cdot 0.50+0.06\cdot 0.35+0.10\cdot 0.15.
$$

Therefore:

$$
P(C)=0.020+0.021+0.015=0.056.
$$

## Channel contributions

| Channel | \(P(\text{channel})\) | \(P(C\mid \text{channel})\) | Contribution to \(P(C)\) | \(P(\text{channel}\mid C)\) |
| :------ | --------------------: | --------------------------: | -----------------------: | --------------------------: |
| website | 0.50 | 0.04 | 0.020 | 0.3571 |
| mobile app | 0.35 | 0.06 | 0.021 | 0.3750 |
| phone | 0.15 | 0.10 | 0.015 | 0.2679 |

## Reverse conditional probabilities

Using Bayes' formula:

$$
P(W\mid C)=\frac{P(C\mid W)P(W)}{P(C)}
=\frac{0.020}{0.056}
\approx 0.3571.
$$

Similarly:

$$
P(A\mid C)=\frac{0.021}{0.056}=0.3750.
$$

And:

$$
P(H\mid C)=\frac{0.015}{0.056}\approx 0.2679.
$$

## Most likely channel among cancelled orders

Among cancelled orders, the most likely channel is the mobile app:

$$
P(A\mid C)=0.3750.
$$

This is slightly larger than:

$$
P(W\mid C)\approx 0.3571
$$

and:

$$
P(H\mid C)\approx 0.2679.
$$

## Is this necessarily the channel with the highest cancellation rate?

No. The phone channel has the highest cancellation rate:

$$
P(C\mid H)=0.10.
$$

However, phone orders are only 15% of all orders. The mobile app has a lower cancellation rate than phone, but it represents a larger share of all orders. Therefore, cancelled orders are most likely to come from the mobile app, not from phone.

This shows why both the conditional cancellation rate and the base proportion of each channel matter.
