# Solution

## Task 5 — Combinations

Formula: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

---

### 1. Committee of 4 from 12 students

$$\binom{12}{4} = \frac{12!}{4! \cdot 8!} = 495$$

---

### 2. Committees containing a particular student

Include that student. Choose the remaining 3 from the other 11.

$$\binom{11}{3} = \frac{11!}{3! \cdot 8!} = 165$$

---

### 3. Committees containing at least one of two particular students

Use complement: total minus committees that contain neither.

- Total: $\binom{12}{4} = 495$
- Neither of the two: choose all 4 from the other 10: $\binom{10}{4} = 210$

$$\binom{12}{4} - \binom{10}{4} = 495 - 210 = 285$$

---

### 4. Committees with exactly two women (7 men, 5 women)

Choose 2 women from 5 and 2 men from 7.

$$\binom{5}{2} \times \binom{7}{2} = 10 \times 21 = 210$$
