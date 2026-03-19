# Task 12 — Mixed Counting Problem

---

## Problem Statement

This task combines multiple counting models.

For each part, we must:

- identify the correct counting model  
- compute the number of possible outcomes  

---

## Definitions / Theory

### Choosing the correct model

To solve each part, we analyze:

- Does **order matter**?  
- Is **repetition allowed**?  
- Are objects **distinct or identical**?  

---

### Main counting models used

1. **Sequence with repetition**

Used when:
- order matters  
- repetition allowed  

$$
n^k
$$

---

2. **k-permutation (no repetition)**

Used when:
- order matters  
- no repetition  

$$
P(n,k) = \frac{n!}{(n-k)!}
$$

---

3. **Combination**

Used when:
- order does NOT matter  

$$
\binom{n}{k}
$$

---

4. **Circular permutation**

$$
(n-1)!
$$

---

5. **Product rule**

If a process has multiple independent steps:

$$
\text{Total} = (\text{step 1}) \times (\text{step 2}) \times \dots
$$

---

## 1. Student ID Codes

Format:

- 2 letters from 5 options  
- 3 digits from 10 options  

---

### 🔹 (a) Repetition allowed

Each position is independent.

---

Letters:

$$
5 \cdot 5 = 5^2 = 25
$$

Digits:

$$
10^3 = 1000
$$

---

### Multiply

$$
25 \cdot 1000 = 25\,000
$$

---

### Model

Sequence with repetition

---

### 🔹 (b) Letters no repeat, digits repeat

---

Letters:

$$
5 \cdot 4 = 20
$$

Digits:

$$
10^3 = 1000
$$

---

### Multiply

$$
20 \cdot 1000 = 20\,000
$$

---

### Model

k-permutation (letters) + sequence (digits)

---

### 🔹 (c) No repetition at all

---

Letters:

$$
5 \cdot 4 = 20
$$

Digits:

$$
10 \cdot 9 \cdot 8 = 720
$$

---

### Multiply

$$
20 \cdot 720 = 14\,400
$$

---

### Model

k-permutation

---

## 2. Medal Assignment

12 runners, 3 medals.

---

### 🔹 (a) Assign medals

Order matters (gold ≠ silver ≠ bronze)

---

$$
12 \cdot 11 \cdot 10 = 1320
$$

---

### Model

k-permutation

---

### 🔹 (b) Two specific runners must win medals

---

Step 1 — choose medals for them:

$$
\binom{3}{2} = 3
$$

---

Step 2 — assign medals:

$$
2! = 2
$$

---

Step 3 — remaining medal:

$$
10 \text{ choices}
$$

---

### Multiply

$$
3 \cdot 2 \cdot 10 = 60
$$

---

## 3. Committee Selection

10 students: 6 men, 4 women.

---

### 🔹 (a) Total committees

$$
\binom{10}{4} = 210
$$

---

### 🔹 (b) Exactly 2 women

---

Women:

$$
\binom{4}{2} = 6
$$

Men:

$$
\binom{6}{2} = 15
$$

---

### Multiply

$$
6 \cdot 15 = 90
$$

---

### 🔹 (c) At least one woman

---

Complement method:

$$
\binom{10}{4} - \binom{6}{4}
$$

---

$$
210 - 15 = 195
$$

---

## 4. Circular Seating

7 people around a table.

---

### 🔹 (a) Total arrangements

$$
(7-1)! = 6! = 720
$$

---

### 🔹 (b) Two people together

---

Treat as block → 6 objects:

$$
(6-1)! = 5! = 120
$$

Internal order:

$$
2
$$

---

### Multiply

$$
120 \cdot 2 = 240
$$

---

## 5. Passwords

Symbols:

$$
10 + 26 = 36
$$

---

### 🔹 (a) Repetition allowed

$$
36^5
$$

---

### Compute

$$
36^5 = 60\,466\,176
$$

---

### Model

Sequence with repetition

---

### 🔹 (b) No repetition

---

$$
36 \cdot 35 \cdot 34 \cdot 33 \cdot 32
$$

---

$$
= 45\,239\,040
$$

---

### Model

k-permutation

---

### 🔹 (c) Models used

- Repetition allowed → sequence  
- No repetition → k-permutation  

---

## Final Summary

| Section | Model | Answer |
|--------|------|--------|
| IDs (a) | sequence | 25,000 |
| IDs (b) | mixed | 20,000 |
| IDs (c) | k-permutation | 14,400 |
| Medals (a) | k-permutation | 1,320 |
| Medals (b) | mixed | 60 |
| Committee (a) | combination | 210 |
| Committee (b) | combination | 90 |
| Committee (c) | complement | 195 |
| Circular | circular permutation | 720 |
| Circular + block | block method | 240 |
| Passwords (a) | sequence | 60,466,176 |
| Passwords (b) | k-permutation | 45,239,040 |

---

## Key Insight

This task shows that the **correct model selection is the most important step**.

The same situation can give completely different results depending on:

- order  
- repetition  
- structure of the problem