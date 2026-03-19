# Solution

## Task 5 — Combinations

Formula:
$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Key idea: order does not matter, only selection.

---

### 1. Committee of 4 from 12 students

Choose 4 students out of 12.

$$
\binom{12}{4} = \frac{12!}{4! \cdot 8!} = 495
$$

Note: different orders of the same people represent the same committee.

---

### 2. Committees containing a particular student

Fix the chosen student.

Now choose the remaining 3 from the other 11 students.

$$
\binom{11}{3} = \frac{11!}{3! \cdot 8!} = 165
$$

Note: fixing one element reduces the selection size.

---

### 3. Committees containing at least one of two particular students

Use complement:

Total committees minus committees with none of the two students.

$$
\binom{12}{4} - \binom{10}{4}
$$

$$
= 495 - 210 = 285
$$

Note: easier to count the opposite case and subtract.

---

### 4. Committees with exactly two women (7 men, 5 women)

Select:
- 2 women from 5  
- 2 men from 7  

$$
\binom{5}{2} \cdot \binom{7}{2} = 10 \cdot 21 = 210
$$

Note: independent selections are multiplied.