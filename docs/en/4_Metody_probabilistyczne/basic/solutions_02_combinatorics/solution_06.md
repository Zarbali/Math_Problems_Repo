# Task 6 — Combinations in Card Problems

---

## Problem Statement

A standard deck contains 52 cards.

1. In how many ways can 5 cards be drawn so that the hand contains exactly 2 hearts?  
2. In how many ways can a 5-card hand contain at least one heart?  
3. In how many ways can a 5-card hand contain no face cards (J, Q, K)?  

---

## Definitions / Theory

### Structure of a standard deck

A standard deck contains:

- 4 suits: Hearts, Diamonds, Clubs, Spades  
- 13 ranks in each suit: A, 2–10, J, Q, K  

From this:

- Hearts: 13 cards  
- Non-hearts: $52 - 13 = 39$ cards  

---

### Face cards

Face cards are:

- Jack (J), Queen (Q), King (K)  
- 3 per suit → $3 \times 4 = 12$ cards  

So:

- Face cards: 12  
- Non-face cards: $52 - 12 = 40$  

---

### Nature of a 5-card hand

A 5-card hand is an **unordered selection**:
- The order of cards does not matter  
- Only the combination of cards matters  

Therefore, we use **combinations**, not permutations.

---

### Combination formula

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

---

### Total number of possible hands

$$
\binom{52}{5} = \frac{52!}{5! \cdot 47!} = 2,598,960
$$

This represents the **entire sample space**.

---

### Product rule

If a selection is split into independent parts:

$$
\text{Total ways} = (\text{ways for part 1}) \times (\text{ways for part 2})
$$

Used when selecting from different groups (hearts and non-hearts).

---

### Complement method

Instead of counting a complex event directly, we count its opposite:

$$
|\text{at least one}| = |\text{total}| - |\text{none}|
$$

This simplifies calculations significantly.

---

## Step-by-Step Solutions

---

## 🔹 Problem 1 — Exactly 2 hearts

We must choose:
- 2 hearts from 13  
- 3 non-hearts from 39  

---

### Step 1 — Choose hearts

$$
\binom{13}{2} = \frac{13 \cdot 12}{2} = 78
$$

---

### Step 2 — Choose non-hearts

$$
\binom{39}{3} = \frac{39 \cdot 38 \cdot 37}{6}
$$

$$
39 \cdot 38 = 1,482
$$

$$
1,482 \cdot 37 = 54,834
$$

$$
\frac{54,834}{6} = 9,139
$$

---

### Step 3 — Multiply

$$
78 \cdot 9,139 = 712,842
$$

---

### Final Answer

$$
712,842
$$

---

## 🔹 Problem 2 — At least one heart

Use complement method.

---

### Step 1 — Total hands

$$
\binom{52}{5} = 2,598,960
$$

---

### Step 2 — No hearts

$$
\binom{39}{5} = \frac{39 \cdot 38 \cdot 37 \cdot 36 \cdot 35}{120}
$$

$$
39 \cdot 38 = 1,482
$$

$$
1,482 \cdot 37 = 54,834
$$

$$
54,834 \cdot 36 = 1,974,024
$$

$$
1,974,024 \cdot 35 = 69,090,840
$$

$$
\frac{69,090,840}{120} = 575,757
$$

---

### Step 3 — Subtract

$$
2,598,960 - 575,757 = 2,023,203
$$

---

### Final Answer

$$
2,023,203
$$

---

## 🔹 Problem 3 — No face cards

We choose all cards from 40 non-face cards.

---

### Step 1 — Formula

$$
\binom{40}{5} = \frac{40 \cdot 39 \cdot 38 \cdot 37 \cdot 36}{120}
$$

---

### Step 2 — Compute

$$
40 \cdot 39 = 1,560
$$

$$
1,560 \cdot 38 = 59,280
$$

$$
59,280 \cdot 37 = 2,193,360
$$

$$
2,193,360 \cdot 36 = 78,960,960
$$

---

### Step 3 — Divide

$$
\frac{78,960,960}{120} = 658,008
$$

---

### Final Answer

$$
658,008
$$

---

## Final Results

| Problem | Answer |
|--------|--------|
| Exactly 2 hearts | 712,842 |
| At least one heart | 2,023,203 |
| No face cards | 658,008 |

---

## Interpretation / Sanity Check

### At least one heart

$$
\frac{2,023,203}{2,598,960} \approx 0.778
$$

Since about one quarter of the deck are hearts, most hands are expected to contain at least one.

---

### Exactly 2 hearts

$$
\frac{712,842}{2,598,960} \approx 0.274
$$

This is reasonable since this event is more restrictive.