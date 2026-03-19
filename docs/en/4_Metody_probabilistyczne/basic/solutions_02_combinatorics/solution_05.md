# Task 5 — Combinations

---

## Definitions / Theory

### When to use combinations

Combination is used when:

| Condition | Meaning |
|----------|--------|
| Order does NOT matter | {A,B} = {B,A} |
| We choose a subset | Not arranging, only selecting |

---

### General Formula

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

---

### Meaning of the formula

| Part | Meaning |
|------|--------|
| $n!$ | all possible permutations |
| $k!$ | removes ordering of chosen elements |
| $(n-k)!$ | removes ordering of unchosen elements |

---

### Key Idea

We divide because:

- selecting 4 people does not depend on order  
- permutations would overcount  

---

## Problem Setup

We choose committees from 12 students.

---

## 🔹 Problem 1 — Committee of 4

---

### Step 1 — identify model

| Property | Value |
|----------|------|
| Order matters | No |
| Selection | Yes |

→ Combination

---

### Step 2 — formula

$$
\binom{12}{4}
$$

---

### Step 3 — compute

$$
\frac{12 \cdot 11 \cdot 10 \cdot 9}{4 \cdot 3 \cdot 2 \cdot 1}
$$

---

### Step 4 — simplify

$$
12 \cdot 11 \cdot 10 \cdot 9 = 11\,880
$$

$$
4! = 24
$$

$$
\frac{11\,880}{24} = 495
$$

---

### Final Answer

$$
495
$$

---

## 🔹 Problem 2 — Committee contains a specific student

---

### Idea

Fix one student first.

---

### Step 1 — remaining choices

| Total students | Already chosen | Remaining |
|---------------|---------------|----------|
| 12 | 1 | 11 |

We choose 3 more.

---

### Step 2 — formula

$$
\binom{11}{3}
$$

---

### Step 3 — compute

$$
\frac{11 \cdot 10 \cdot 9}{6}
$$

$$
= \frac{990}{6} = 165
$$

---

### Final Answer

$$
165
$$

---

## 🔹 Problem 3 — At least one of two students

---

### Idea

Use complement:

| Case | Meaning |
|------|--------|
| Total | all committees |
| None | exclude both students |

---

### Step 1 — total

$$
\binom{12}{4} = 495
$$

---

### Step 2 — exclude both

| Remaining students | Count |
|------------------|------|
| Total | 12 |
| Excluded | 2 |
| Available | 10 |

$$
\binom{10}{4}
$$

---

### Step 3 — compute

$$
\frac{10 \cdot 9 \cdot 8 \cdot 7}{24} = 210
$$

---

### Step 4 — subtract

$$
495 - 210 = 285
$$

---

### Final Answer

$$
285
$$

---

## 🔹 Problem 4 — Exactly two women

---

### Step 1 — split into groups

| Group | Total |
|------|------|
| Women | 5 |
| Men | 7 |

---

### Step 2 — choose from each group

| Group | Choose | Ways |
|------|--------|------|
| Women | 2 | $\binom{5}{2} = 10$ |
| Men | 2 | $\binom{7}{2} = 21$ |

---

### Step 3 — multiply

$$
10 \cdot 21 = 210
$$

---

### Final Answer

$$
210
$$

---

## Final Summary

| Problem | Model | Result |
|--------|------|--------|
| Committee of 4 | combination | 495 |
| Contains specific | combination | 165 |
| At least one of two | complement | 285 |
| Exactly 2 women | product of combinations | 210 |

---

## Key Insight

- Combination ignores order  
- Complement simplifies conditions  
- Splitting into groups helps structure the solution  