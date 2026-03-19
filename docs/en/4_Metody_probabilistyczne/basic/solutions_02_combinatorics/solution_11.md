# Task 11 — Modeling Outcomes

---

## Problem Statement

In combinatorial and probabilistic problems, the number of possible outcomes depends on how the results of an experiment are recorded.

We analyze how counting changes depending on:

- distinguishable vs indistinguishable objects  
- whether order is recorded or ignored  
- whether positions are treated as distinct  

---

## Definitions / Theory

### Distinguishable vs indistinguishable objects

- **Distinguishable objects**: each object is unique (labeled)  
  → swapping two objects gives a new outcome  

- **Indistinguishable objects**: identical objects  
  → swapping does NOT create a new outcome  

Formula for repeated elements:

$$
\frac{n!}{n_1! \cdot n_2! \cdot \dots}
$$

This removes overcounting caused by identical objects.

---

### Order matters vs order ignored

- **Order ignored** → use combinations  
- **Order recorded** → use permutations  

Key idea:

Each unordered selection can correspond to multiple ordered sequences.

---

### Leading digit restriction

- In numbers → first digit cannot be zero  
- In PIN codes → zero is allowed everywhere  

---

## 1. Distinguishable vs Indistinguishable Objects

Box contains:

- 4 red  
- 4 blue  
- 3 green  

Total:

$$
4 + 4 + 3 = 11
$$

---

### 🔹 (a) Indistinguishable (same colors identical)

We use permutation with repetition:

$$
\frac{11!}{4! \cdot 4! \cdot 3!}
$$

---

### Step-by-step

$$
11! = 39\,916\,800
$$

$$
4! = 24,\quad 3! = 6
$$

$$
4! \cdot 4! \cdot 3! = 24 \cdot 24 \cdot 6 = 3456
$$

$$
\frac{39\,916\,800}{3456} = 115\,500
$$

---

### Final Answer

$$
115\,500
$$

---

### 🔹 (b) All balls distinguishable

Now every ball is unique.

We use simple permutation:

$$
11!
$$

---

### Result

$$
11! = 39\,916\,800
$$

---

### 🔹 (c) Why results differ

- In case (a), swapping two red balls gives the same arrangement  
- In case (b), swapping labeled balls gives a new arrangement  

So we divide by factorials to remove duplicate arrangements.

---

## 2. Recording Order vs Ignoring Order

We draw 3 balls without replacement.

---

### 🔹 (a) Order ignored

We only care which balls are selected.

---

### Formula

$$
\binom{11}{3}
$$

---

### Compute

$$
\frac{11 \cdot 10 \cdot 9}{6} = \frac{990}{6} = 165
$$

---

### Final Answer

$$
165
$$

---

### 🔹 (b) Order recorded

Now sequence matters.

---

### Step-by-step

First draw: 11 choices  
Second: 10 choices  
Third: 9 choices  

$$
11 \cdot 10 \cdot 9 = 990
$$

---

### Final Answer

$$
990
$$

---

### 🔹 (c) Why results differ

- When order is ignored → (R, B, G) = (B, R, G)  
- When order is recorded → they are different  

Each unordered outcome can correspond to multiple ordered ones.

---

## 3. PIN Code vs Number

---

### 🔹 (a) PIN code (repetition allowed)

Each digit has 10 choices:

$$
10^4 = 10\,000
$$

---

### 🔹 (b) 4-digit number

First digit cannot be zero.

---

### Step-by-step

First digit: 9 choices  
Other digits: 10 each  

$$
9 \cdot 10^3 = 9\,000
$$

---

### 🔹 (c) Why different

- PIN allows leading zero (example: 0123)  
- Number does not  

So total outcomes differ.

---

### 🔹 (d) Why 1234 and 4321 are different

Order matters.

Changing the order changes the outcome.

So these are two different results.

---

## Final Summary

| Situation | Model | Result |
|----------|------|--------|
| Indistinguishable | permutation with repetition | 115,500 |
| Distinguishable | permutation | 39,916,800 |
| Order ignored | combination | 165 |
| Order recorded | permutation | 990 |
| PIN code | sequences with repetition | 10,000 |
| Number | restricted sequence | 9,000 |

---

## Key Insight

The number of outcomes depends entirely on:

- whether objects are distinguishable  
- whether order matters  
- whether positions have restrictions  

Changing any of these changes the counting model.