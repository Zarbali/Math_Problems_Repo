# Task 1 — Recognizing Counting Models

---

## Definitions / Theory

| Question | Meaning |
|----------|--------|
| All or some objects? | Determines permutation vs selection |
| Order matters? | If yes → permutation |
| Repetition allowed? | Changes formula |
| Identical objects? | Use division |

---

## Models Overview

| Model | When used | Formula |
|------|----------|--------|
| Permutation | all objects, order matters | $n!$ |
| Combination | order does not matter | $\binom{n}{k}$ |
| k-permutation | choose k, order matters | $P(n,k)$ |
| Sequence | repetition allowed | $n^k$ |
| Circular | rotation ignored | $(n-1)!$ |

---

## Solutions

---

### 1. 7 students in a line

| Property | Value |
|--------|------|
| All used | Yes |
| Order matters | Yes |

$$
7! = 5040
$$

---

### 2. Committee of 4 from 12

| Property | Value |
|--------|------|
| Order matters | No |

$$
\binom{12}{4} = 495
$$

---

### 3. Medals

| Property | Value |
|--------|------|
| Order matters | Yes |

$$
12 \cdot 11 \cdot 10 = 1320
$$

---

### 4. PIN code

| Property | Value |
|--------|------|
| Repetition | Allowed |

$$
10^6 = 1\,000\,000
$$

---

### 5. BANANA

| Letter | Count |
|--------|------|
| A | 3 |
| N | 2 |

$$
\frac{6!}{3! \cdot 2!} = 60
$$

---

### 6. Circular seating

$$
(6-1)! = 120
$$

---

## Key Insight

Correct model selection determines the entire solution.