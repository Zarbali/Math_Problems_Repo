# Task 3 — Permutations with Repeated Elements

---

## Definitions / Theory

When arranging objects where some are identical, using $n!$ overcounts the number of arrangements.

Reason:
Swapping identical elements does NOT create a new outcome.

---

### General Formula

If:

- total elements = $n$
- $n_1, n_2, \dots$ identical elements

Then:

$$
\frac{n!}{n_1! \cdot n_2! \cdot \dots}
$$

---

### Why we divide

Each group of identical elements can be rearranged internally without changing the arrangement.

So we divide by:

$$
n_1!,\; n_2!,\; \dots
$$

to remove duplicate counts.

---

## Solutions

---

## 🔹 1. MISSISSIPPI

---

### Step 1 — count letters

| Letter | Count |
|--------|------|
| M | 1 |
| I | 4 |
| S | 4 |
| P | 2 |

Total:

$$
1 + 4 + 4 + 2 = 11
$$

---

### Step 2 — apply formula

$$
\frac{11!}{4! \cdot 4! \cdot 2!}
$$

---

### Step 3 — compute factorials

$$
11! = 39\,916\,800
$$

$$
4! = 24,\quad 2! = 2
$$

---

### Step 4 — denominator

$$
4! \cdot 4! \cdot 2! = 24 \cdot 24 \cdot 2 = 1152
$$

---

### Step 5 — divide

$$
\frac{39\,916\,800}{1152} = 34\,650
$$

---

### Final Answer

$$
34\,650
$$

---

## 🔹 2. STATISTICS

---

### Step 1 — count letters

| Letter | Count |
|--------|------|
| S | 3 |
| T | 3 |
| I | 2 |
| A | 1 |
| C | 1 |

Total:

$$
10
$$

---

### Step 2 — formula

$$
\frac{10!}{3! \cdot 3! \cdot 2!}
$$

---

### Step 3 — compute

$$
10! = 3\,628\,800
$$

$$
3! = 6,\quad 2! = 2
$$

---

### Step 4 — denominator

$$
6 \cdot 6 \cdot 2 = 72
$$

---

### Step 5 — divide

$$
\frac{3\,628\,800}{72} = 50\,400
$$

---

### Final Answer

$$
50\,400
$$

---

## 🔹 3. Starting with S

---

### Step 1 — fix first position

We place S in the first position.

Remaining letters:

| Letter | Count |
|--------|------|
| S | 2 |
| T | 3 |
| I | 2 |
| A | 1 |
| C | 1 |

Total:

$$
9
$$

---

### Step 2 — formula

$$
\frac{9!}{2! \cdot 3! \cdot 2!}
$$

---

### Step 3 — compute

$$
9! = 362\,880
$$

$$
2! = 2,\quad 3! = 6
$$

---

### Step 4 — denominator

$$
2 \cdot 6 \cdot 2 = 24
$$

---

### Step 5 — divide

$$
\frac{362\,880}{24} = 15\,120
$$

---

### Final Answer

$$
15\,120
$$

---

## Key Insight

Permutation with repetition corrects overcounting caused by identical elements.