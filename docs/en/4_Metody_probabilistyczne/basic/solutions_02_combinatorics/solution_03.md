# Solution

## Task 3 — Permutations with Repeated Elements

Formula: $\frac{n!}{n_1! \, n_2! \, \cdots \, n_r!}$ when there are $n_1$ identical of type 1, $n_2$ of type 2, etc.

---

### 1. Arrangements of MISSISSIPPI

Letter counts: M(1), I(4), S(4), P(2). Total: 11 letters.

$$\frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39\,916\,800}{24 \cdot 24 \cdot 2} = 34\,650$$

---

### 2. Arrangements of STATISTICS

Letter counts: S(3), T(3), A(1), I(2), C(1). Total: 10 letters.

$$\frac{10!}{3! \cdot 3! \cdot 1! \cdot 2! \cdot 1!} = \frac{3\,628\,800}{6 \cdot 6 \cdot 2} = 50\,400$$

---

### 3. Arrangements of STATISTICS that start with S

Fix S in the first position. Remaining 9 letters: S(2), T(3), A(1), I(2), C(1).

$$\frac{9!}{2! \cdot 3! \cdot 1! \cdot 2! \cdot 1!} = \frac{362\,880}{2 \cdot 6 \cdot 2} = 15\,120$$
