# Task 9 — Digit Restrictions

---

## Problem Statement

1. How many 5-digit numbers exist?  
2. How many of them are even?  
3. How many contain no repeated digits?  
4. How many contain at least one repeated digit?  

---

## Definitions / Theory

### Structure of 5-digit numbers

A 5-digit number:

- cannot start with 0  
- first digit is from 1 to 9 → 9 choices  
- remaining digits are from 0 to 9 → 10 choices each  

---

### Order and repetition

- Order matters → digits form a number  
- Repetition may or may not be allowed depending on the problem  

---

### Multiplication principle

If a number is constructed step-by-step:

- total number of outcomes is the product of choices at each position  

---

### Even numbers

A number is even if its last digit is:

0, 2, 4, 6, or 8 → 5 choices  

---

### No repetition

If digits cannot repeat:

- each next position has fewer available digits  

---

### Complement method

Instead of counting:

“at least one repeated digit”

we compute:

$$
\text{total} - \text{no repetition}
$$

---

## Step-by-Step Solutions

---

## 🔹 Problem 1 — Total 5-digit numbers

---

### Step 1 — First digit

Digits 1–9 → 9 choices.

---

### Step 2 — Remaining digits

Each of the next 4 digits has 10 choices.

---

### Step 3 — Multiply

$$
9 \cdot 10 \cdot 10 \cdot 10 \cdot 10
$$

---

### Step 4 — Compute

$$
10^4 = 10,000
$$

$$
9 \cdot 10,000 = 90,000
$$

---

### Final Answer

$$
90,000
$$

---

## 🔹 Problem 2 — Even numbers

Last digit must be even.

---

### Step 1 — First digit

9 choices.

---

### Step 2 — Middle digits

3 digits → each has 10 choices.

---

### Step 3 — Last digit

Even digits: 0, 2, 4, 6, 8 → 5 choices.

---

### Step 4 — Multiply

$$
9 \cdot 10 \cdot 10 \cdot 10 \cdot 5
$$

---

### Step 5 — Compute

$$
10 \cdot 10 \cdot 10 = 1,000
$$

$$
9 \cdot 1,000 = 9,000
$$

$$
9,000 \cdot 5 = 45,000
$$

---

### Final Answer

$$
45,000
$$

---

## 🔹 Problem 3 — No repeated digits

Now repetition is not allowed.

---

### Step 1 — First digit

Digits 1–9 → 9 choices.

---

### Step 2 — Second digit

From 0–9, excluding first digit → 9 choices.

---

### Step 3 — Third digit

8 choices.

---

### Step 4 — Fourth digit

7 choices.

---

### Step 5 — Fifth digit

6 choices.

---

### Step 6 — Multiply

$$
9 \cdot 9 \cdot 8 \cdot 7 \cdot 6
$$

---

### Step 7 — Compute

$$
9 \cdot 9 = 81
$$

$$
81 \cdot 8 = 648
$$

$$
648 \cdot 7 = 4,536
$$

$$
4,536 \cdot 6 = 27,216
$$

---

### Final Answer

$$
27,216
$$

---

## 🔹 Problem 4 — At least one repeated digit

Use complement:

$$
\text{at least one repeat} = \text{total} - \text{no repetition}
$$

---

### Step 1 — Total

$$
90,000
$$

---

### Step 2 — No repetition

$$
27,216
$$

---

### Step 3 — Subtract

$$
90,000 - 27,216 = 62,784
$$

---

### Final Answer

$$
62,784
$$

---

## Final Results

| Problem | Answer |
|--------|--------|
| Total numbers | 90,000 |
| Even numbers | 45,000 |
| No repetition | 27,216 |
| At least one repeat | 62,784 |

---

## Interpretation / Sanity Check

- About half of the numbers are even → 45,000 out of 90,000  
- Numbers without repetition are fewer → 27,216  
- Most numbers contain repetition → 62,784  

This confirms that allowing repetition increases the number of possibilities.