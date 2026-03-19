# Solution

## Task 10 — Urn Models

Urn: 5 red, 4 blue, 3 green. Total: 12 balls.

---

### 1. Three balls without replacement, order ignored

$$\binom{12}{3} = \frac{12!}{3! \cdot 9!} = 220$$

---

### 2. Samples (order ignored) with exactly two red balls

Choose 2 red from 5, 1 from 7 non-red.

$$\binom{5}{2} \times \binom{7}{1} = 10 \times 7 = 70$$

---

### 3. Three balls drawn, order of colors recorded

Ordered selection of 3 balls without replacement.

$$\frac{12!}{9!} = 12 \times 11 \times 10 = 1\,320$$

---

### 4. Ordered outcomes with exactly two red balls

Choose 2 red from 5, 1 non-red from 7. Arrange the 3 in order: $3!$ ways.

$$\binom{5}{2} \times \binom{7}{1} \times 3! = 10 \times 7 \times 6 = 420$$
