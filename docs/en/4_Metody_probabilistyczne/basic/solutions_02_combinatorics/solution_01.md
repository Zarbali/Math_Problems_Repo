# Solution

## Task 1 — Recognizing Counting Models

---

### 1. Arranging 7 students in a line

All 7 students are used.  
Order matters because positions in the line are different.  
No repetition. All students are distinguishable.

→ Model: permutation

$$7! = 5040$$

Note: changing the order produces a different arrangement.

---

### 2. Choosing 4 members of a committee from 12 people

4 people are selected from 12.  
Order does not matter because a committee is a set.  
No repetition. All people are distinguishable.

→ Model: combination

$$\binom{12}{4} = \frac{12!}{4! \cdot 8!}$$

Note: different orderings of the same people represent the same committee.

---

### 3. Assigning gold, silver, and bronze medals among 15 athletes

3 athletes are selected and assigned different roles (gold, silver, bronze).  
Order matters because medals are different.  
No repetition. Athletes are distinguishable.

→ Model: k-permutation

$$P(15,3) = 15 \cdot 14 \cdot 13 = 2730$$

Note: (A, B, C) is different from (B, A, C).

---

### 4. Forming a 6-digit PIN code

A sequence of 6 digits is formed.  
Each position has 10 possible digits (0–9).  
Repetition is allowed. Order matters.

→ Model: sequence with repetition

$$10^6 = 1\,000\,000$$

Note: each position is chosen independently.

---

### 5. Arranging the letters of the word BANANA

All 6 letters are used.  
Order matters.  
Letters repeat: A appears 3 times, N appears 2 times.

→ Model: permutation with repeated elements

$$\frac{6!}{3! \cdot 2!} = 60$$

Note: division removes overcounting due to identical letters.

---

### 6. Seating 6 people around a round table

All 6 people are arranged in a circle.  
Order matters only relative to others.  
Rotations represent the same arrangement.

→ Model: circular permutation

$$(6-1)! = 5! = 120$$

Note: one position is fixed to eliminate equivalent rotations.