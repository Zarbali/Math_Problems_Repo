# Problem 2 — Four Regions of a Sample Space

## Generated files

- Four regions: [`four_regions.csv`](four_regions.csv)
- Probability summary: [`probability_summary.csv`](probability_summary.csv)

## Data

The total number of support tickets is 350.

Let:

$$
T=\text{the ticket is technical},
$$

$$
S=\text{the ticket was solved during the first contact}.
$$

## Four disjoint regions

| Region | Description | Count | Probability |
| :----- | :---------- | ----: | ----------: |
| \(T\cap S\) | technical and solved during first contact | 90 | 0.2571 |
| \(T\cap S^c\) | technical and not solved during first contact | 60 | 0.1714 |
| \(T^c\cap S\) | non-technical and solved during first contact | 160 | 0.4571 |
| \(T^c\cap S^c\) | non-technical and not solved during first contact | 40 | 0.1143 |

These probabilities add up to:

$$
0.2571+0.1714+0.4571+0.1143=1.
$$

Using exact fractions:

$$
\frac{90+60+160+40}{350}=\frac{350}{350}=1.
$$

## Union probabilities

First:

$$
P(T)=\frac{150}{350}\approx 0.4286,
$$

and:

$$
P(S)=\frac{250}{350}\approx 0.7143.
$$

Also:

$$
P(T\cap S)=\frac{90}{350}\approx 0.2571.
$$

Therefore:

$$
P(T\cup S)=P(T)+P(S)-P(T\cap S).
$$

So:

$$
P(T\cup S)=0.4286+0.7143-0.2571=0.8857.
$$

Now:

$$
P(T^c)=\frac{200}{350}\approx 0.5714,
$$

and:

$$
P(T^c\cap S)=\frac{160}{350}\approx 0.4571.
$$

Thus:

$$
P(T^c\cup S)=P(T^c)+P(S)-P(T^c\cap S).
$$

So:

$$
P(T^c\cup S)=0.5714+0.7143-0.4571=0.8286.
$$

## Conditional probabilities

The probability that a technical ticket was solved during the first contact is:

$$
P(S\mid T)=\frac{P(T\cap S)}{P(T)}
=\frac{90/350}{150/350}
=\frac{90}{150}
=0.60.
$$

The probability that a non-technical ticket was solved during the first contact is:

$$
P(S\mid T^c)=\frac{P(T^c\cap S)}{P(T^c)}
=\frac{160/350}{200/350}
=\frac{160}{200}
=0.80.
$$

## Interpretation

Being a technical ticket changes the probability of being solved during the first contact.

For technical tickets, the first-contact resolution probability is 0.60. For non-technical tickets, it is 0.80. In this dataset, technical tickets are less likely to be solved during the first contact.
