# Task 2 — Permutations

---

## Definitions / Theory

### What is a permutation?

A permutation is an arrangement of objects where:

- all objects are used  
- order matters  

---

### Basic Formula

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 1
$$

---

### Special techniques

| Method | When used | Idea |
|--------|----------|------|
| Block method | objects must stay together | treat as one unit |
| Complement | avoid complex counting | total − unwanted |
| Fixed position | restriction exists | reduce number of objects |

---

## Solutions

---

## 🔹 Problem 1 — 8 books

---

### Step 1 — identify model

| Property | Value |
|----------|------|
| All objects used | Yes |
| Order matters | Yes |

→ permutation

---

### Step 2 — formula

$$
8!
$$

---

### Step 3 — compute

$$
8! = 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1
$$

---

### Step 4 — simplify

$$
8 \cdot 7 = 56
$$

$$
56 \cdot 6 = 336
$$

$$
336 \cdot 5 = 1680
$$

$$
1680 \cdot 4 = 6720
$$

$$
6720 \cdot 3 = 20\,160
$$

$$
20\,160 \cdot 2 = 40\,320
$$

---

### Final Answer

$$
40\,320
$$

---

## 🔹 Problem 2 — Two people together

---

### Step 1 — idea

Treat the two people as one block.

---

### Step 2 — count objects

| Objects | Count |
|--------|------|
| Block | 1 |
| Other people | 6 |
| Total | 7 |

---

### Step 3 — arrange

$$
7!
$$

---

### Step 4 — internal order

Inside block:

$$
2 \text{ ways}
$$

---

### Step 5 — compute

$$
7! = 5040
$$

$$
5040 \cdot 2 = 10\,080
$$

---

### Final Answer

$$
10\,080
$$

---

## 🔹 Problem 3 — NOT together

---

### Step 1 — idea

Use complement:

| Case | Meaning |
|------|--------|
| Total | all arrangements |
| Together | unwanted |

---

### Step 2 — total

$$
8! = 40\,320
$$

---

### Step 3 — together

$$
7! \cdot 2 = 10\,080
$$

---

### Step 4 — subtract

$$
40\,320 - 10\,080 = 30\,240
$$

---

### Final Answer

$$
30\,240
$$

---

## 🔹 Problem 4 — First fixed

---

### Step 1 — idea

First position is fixed → not permuted.

---

### Step 2 — remaining objects

| Total | Fixed | Remaining |
|------|------|----------|
| 10 | 1 | 9 |

---

### Step 3 — arrange

$$
9!
$$

---

### Step 4 — compute

$$
9! = 362\,880
$$

---

### Final Answer

$$
362\,880
$$

---

## Key Insight

Permutation problems change depending on constraints:

- grouping → block  
- restriction → fewer objects  
- exclusion → complement