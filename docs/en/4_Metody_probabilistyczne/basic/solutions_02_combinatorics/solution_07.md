# Solution

## Task 7 — k-Permutations (Ordered Selections Without Repetition)

Formula: $P(n,k) = \frac{n!}{(n-k)!}$

---

### 1. First three places among 12 runners

$$\frac{12!}{9!} = 12 \times 11 \times 10 = 1\,320$$

---

### 2. 4-digit numbers with distinct digits from 1–9

Digits 1–9, no repetition. First digit: 9 choices; second: 8; third: 7; fourth: 6.

$$9 \times 8 \times 7 \times 6 = P(9,4) = 3\,024$$

---

### 3. 4-digit numbers (distinct digits from 1–9) divisible by 5

Last digit must be 5. Choose first 3 digits from $\{1,2,3,4,6,7,8,9\}$ (8 digits, no 5).

$$8 \times 7 \times 6 = P(8,3) = 336$$
