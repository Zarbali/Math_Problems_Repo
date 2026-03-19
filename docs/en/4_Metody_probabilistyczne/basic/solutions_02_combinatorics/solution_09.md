# Solution

## Task 9 — Digit Restrictions

5-digit numbers: first digit 1–9 (no leading zero), remaining digits 0–9.

---

### 1. Total 5-digit numbers

First digit: 9 choices. Remaining 4: 10 each.

$$9 \times 10^4 = 90\,000$$

---

### 2. Even 5-digit numbers

Last digit: 0, 2, 4, 6, 8 (5 choices). First digit: 9. Middle 3: 10 each.

$$9 \times 10 \times 10 \times 10 \times 5 = 45\,000$$

---

### 3. No repeated digits

First: 9 (1–9). Second: 9 (0–9 excluding first). Third: 8. Fourth: 7. Fifth: 6.

$$9 \times 9 \times 8 \times 7 \times 6 = 27\,216$$

---

### 4. At least one repeated digit

Complement: total minus no repeated.

$$90\,000 - 27\,216 = 62\,784$$
