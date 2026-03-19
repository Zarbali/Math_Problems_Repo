# Task 6 — Combinations in Card Problems

---

## Problem Statement

A standard deck contains 52 cards.

1. In how many ways can 5 cards be drawn so that the hand contains **exactly 2 hearts**?  
2. In how many ways can a 5-card hand contain **at least one heart**?  
3. In how many ways can a 5-card hand contain **no face cards (J, Q, K)**?  

---

## Definitions / Theory

Standard 52-card deck:
- 4 suits → 13 cards each  
- Hearts: 13  
- Non-hearts: 39  
- Face cards (J, Q, K): 3 per suit → 12 total  
- Non-face cards: 52 − 12 = 40  

A 5-card hand is an **unordered selection**, so combinations are used:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Total number of 5-card hands:

$$
\binom{52}{5} = 2\,598\,960
$$

---

## Step-by-Step Solutions

---

### 🔹 Problem 1 — Exactly 2 hearts

The hand must contain:
- exactly 2 hearts  
- exactly 3 non-hearts  

This splits the selection into two independent parts.

---

**Step 1 — Choose 2 hearts from 13**

$$
\binom{13}{2} = \frac{13 \cdot 12}{2} = 78
$$

---

**Step 2 — Choose 3 non-hearts from 39**

$$
\binom{39}{3} = \frac{39 \cdot 38 \cdot 37}{3 \cdot 2 \cdot 1} = 9\,139
$$

---

**Step 3 — Multiply (independent choices)**

$$
\binom{13}{2} \cdot \binom{39}{3}
$$

$$
= 78 \cdot 9\,139 = 712\,842
$$

---

### 🔹 Problem 2 — At least one heart

“At least one” means:
- 1 heart  
- 2 hearts  
- 3 hearts  
- 4 hearts  
- 5 hearts  

Counting all cases directly is complicated, so the complement method is used.

---

**Step 1 — Total number of hands**

$$
\binom{52}{5} = 2\,598\,960
$$

---

**Step 2 — Hands with NO hearts**

All 5 cards are chosen from non-hearts (39 cards):

$$
\binom{39}{5} = 575\,757
$$

---

**Step 3 — Subtract**

$$
\binom{52}{5} - \binom{39}{5}
$$

$$
= 2\,598\,960 - 575\,757 = 2\,023\,203
$$

---

### 🔹 Problem 3 — No face cards

The hand must contain only non-face cards.

There are 40 such cards.

---

**Step 1 — Choose all 5 cards from 40**

$$
\binom{40}{5}
$$

---

**Step 2 — Compute**

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

This is reasonable because getting exactly 2 hearts is more restrictive than getting at least one.