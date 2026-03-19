# Task 6 — Combinations in Card Problems

---

## Problem Statement

1. In how many ways can 5 cards be drawn so that the hand contains **exactly 2 hearts**?  
2. In how many ways can a 5-card hand contain **at least one heart**?  
3. In how many ways can a 5-card hand contain **no face cards (J, Q, K)**?  

---

## Definitions / Theory

A standard deck contains:

- 52 total cards  
- 13 hearts  
- 39 non-hearts  
- 12 face cards (J, Q, K)  
- 40 non-face cards  

In card problems, **order does not matter**, so combinations are used:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

---

## Step-by-Step Solutions

---

### Problem 1 — Exactly 2 hearts

We split the selection:

- choose 2 hearts from 13  
- choose 3 non-hearts from 39  

$$
\binom{13}{2} \cdot \binom{39}{3}
$$

$$
= 78 \cdot 9\,139 = 712\,842
$$

---

### Problem 2 — At least one heart

Use complement:

- total hands:  
$$\binom{52}{5} = 2\,598\,960$$  

- hands with no hearts:  
$$\binom{39}{5} = 575\,757$$  

$$
\binom{52}{5} - \binom{39}{5}
$$

$$
= 2\,598\,960 - 575\,757 = 2\,023\,203
$$

---

### Problem 3 — No face cards

All cards must come from non-face cards (40 cards):

$$
\binom{40}{5} = 658\,008
$$

---

## Final Results

| Problem | Formula | Answer |
|--------|--------|--------|
| Exactly 2 hearts | $\binom{13}{2} \cdot \binom{39}{3}$ | 712,842 |
| At least one heart | $\binom{52}{5} - \binom{39}{5}$ | 2,023,203 |
| No face cards | $\binom{40}{5}$ | 658,008 |

---

## Interpretation / Sanity Check

### Probability of at least one heart

$$
\frac{2\,023\,203}{2\,598\,960} \approx 0.778
$$

Since about one quarter of the deck are hearts, it is expected that most hands contain at least one heart.

---

### Probability of exactly 2 hearts

$$
\frac{712\,842}{2\,598\,960} \approx 0.274
$$

This is a reasonable value since getting exactly 2 hearts is more specific than getting at least one.