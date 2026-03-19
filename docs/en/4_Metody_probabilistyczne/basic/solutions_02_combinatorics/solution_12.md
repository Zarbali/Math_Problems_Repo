# Solution

## Task 12 — Mixed Counting Problem

---

### 1. Student ID Codes

Format: 2 letters from $\{A,B,C,D,E\}$, then 3 digits (0–9).

#### (a) Letters and digits may repeat

Sequence with repetition: $5^2 \times 10^3 = 25\,000$

#### (b) Letters may not repeat, digits may repeat

Letters: $P(5,2) = 5 \times 4 = 20$. Digits: $10^3 = 1\,000$.

$$20 \times 1\,000 = 20\,000$$

#### (c) Neither letters nor digits repeat

$$P(5,2) \times P(10,3) = 20 \times 720 = 14\,400$$

---

### 2. Medal Assignment (12 runners)

#### (a) Assign gold, silver, bronze

k-permutation: $\frac{12!}{9!} = 12 \times 11 \times 10 = 1\,320$

#### (b) Two particular runners must both receive medals

They get 2 of the 3 medals. Choose which 2 medals: $\binom{3}{2} = 3$. Assign those 2 medals to the 2 runners: $2! = 2$. Assign the remaining medal to one of 10 others: $10$.

$$3 \times 2 \times 10 = 60$$

---

### 3. Committee Selection (10 students: 6 men, 4 women)

#### (a) Committee of 4

$$\binom{10}{4} = 210$$

#### (b) Exactly two women

$$\binom{4}{2} \times \binom{6}{2} = 6 \times 15 = 90$$

#### (c) At least one woman

Complement: $\binom{10}{4} - \binom{6}{4} = 210 - 15 = 195$

---

### 4. Circular Seating (7 people)

#### (a) Seating arrangements

$$(7-1)! = 6! = 720$$

#### (b) Two particular people next to each other

Treat as block: $(6-1)! \times 2 = 5! \times 2 = 240$

---

### 5. Passwords (5 characters from 0–9 and A–Z)

Total symbols: $10 + 26 = 36$.

#### (a) Repetition allowed

Sequence with repetition: $36^5 = 60\,466\,176$

#### (b) No character may repeat

k-permutation: $P(36,5) = 36 \times 35 \times 34 \times 33 \times 32 = 45\,239\,040$

#### (c) Counting models

- (a): **sequence with repetition** ($n^k$)
- (b): **k-permutation** ($P(n,k)$)
