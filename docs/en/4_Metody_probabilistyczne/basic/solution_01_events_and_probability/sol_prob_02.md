## Task 2 — Rolling a Die

Experiment: rolling a fair six-sided die.

Important assumption: the order of outcomes matters, so sequences like (2,5) and (5,2) represent different results.


## 1. Sample space Ω₁ (one roll)

For a single roll of a die there are six possible outcomes.

| Outcome |
|-------|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |

$$
\Omega_1 = \{1,2,3,4,5,6\}
$$

Number of elementary outcomes:

$$
|\Omega_1| = 6
$$

Note: each outcome represents the number that appears on the die after one roll.


## 2. Sample space Ω₂ (two rolls)

For two consecutive rolls we consider ordered pairs of numbers.

Note: the order matters because the first roll and the second roll are different stages of the experiment.

Examples of possible outcomes:

| First roll | Second roll | Outcome |
|-----------|------------|--------|
| 1 | 1 | (1,1) |
| 1 | 2 | (1,2) |
| 3 | 5 | (3,5) |
| 6 | 4 | (6,4) |

In general the sample space contains all ordered pairs:

$$
\Omega_2 = \{(i,j) \mid i,j \in \{1,2,3,4,5,6\}\}
$$

Number of elementary outcomes:

$$
|\Omega_2| = 6 \times 6 = 36
$$

Note: (2,5) means the first roll gives 2 and the second roll gives 5.


## 3. Sample space Ω₃ (three rolls)

For three rolls we consider ordered triples of results.

Examples of outcomes:

| Roll 1 | Roll 2 | Roll 3 | Outcome |
|------|------|------|------|
| 1 | 1 | 1 | (1,1,1) |
| 2 | 4 | 6 | (2,4,6) |
| 5 | 3 | 2 | (5,3,2) |
| 6 | 6 | 6 | (6,6,6) |

The sample space contains all ordered triples:

$$
\Omega_3 = \{(i,j,k) \mid i,j,k \in \{1,2,3,4,5,6\}\}
$$

Number of elementary outcomes:

$$
|\Omega_3| = 6 \times 6 \times 6 = 216
$$

Note: each triple describes the full sequence of three rolls.

## 4. Number of elementary outcomes

| Number of rolls | Outcomes |
|---------------|-----------|
| 1 | 6 |
| 2 | 36 |
| 3 | 216 |

Observation:

Each roll of a die has six possible outcomes.

Therefore the number of outcomes grows multiplicatively.

General rule:

$$
|\Omega_n| = 6^n
$$

Note: this is similar to the coin experiment, but there we had two outcomes per step instead of six.


## 5. Meaning of an elementary outcome

An elementary outcome represents one complete possible result of the experiment.

Examples:

1 → the die shows 1 in a single roll.

(3,5) → the first roll gives 3 and the second roll gives 5.

(2,4,6) → the results of three rolls are 2, then 4, then 6.

Note: each elementary outcome describes exactly one possible sequence of results.