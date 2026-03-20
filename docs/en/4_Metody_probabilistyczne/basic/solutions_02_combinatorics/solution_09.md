# Task 9 — Digit Restrictions

---

## Problem Statement

1. How many 5-digit numbers exist?  
2. How many of them are even?  
3. How many contain no repeated digits?  
4. How many contain at least one repeated digit?  

---

## Definitions / Theory

### Structure of a 5-digit number

A 5-digit number has 5 positions:

| Position | Description |
|---------|------------|
| Ten-thousands | cannot be 0 |
| Others | can be 0–9 |

So:

- First digit → {1,...,9} → 9 choices  
- Other digits → {0,...,9} → 10 choices each  

---

### Order and sequences

Digits form a number, so:

- order matters  
- we are working with sequences  

---

### Multiplication principle

If a number is built step-by-step:

$$
\text{Total} = n_1 \cdot n_2 \cdot \dots \cdot n_k
$$

Each step corresponds to one position in the number.

---

### Even numbers

A number is even if its last digit is:

$$
\{0,2,4,6,8\}
$$

→ 5 possible choices  

---

### No repetition

If repetition is not allowed:

- each chosen digit is removed from future choices  
- the number of options decreases step by step  

---

### Complement method

Instead of counting complex cases:

$$
\text{at least one repeat} = \text{total} - \text{no repetition}
$$

---

## Step-by-Step Solution

---

## 🔹 Problem 1 — Total 5-digit numbers

---

### Step 1 — Positions and choices

| Position | Available digits | Choices |
|----------|----------------|--------|
| Ten-thousands | {1,...,9} | 9 |
| Thousands | {0,...,9} | 10 |
| Hundreds | {0,...,9} | 10 |
| Tens | {0,...,9} | 10 |
| Units | {0,...,9} | 10 |

---

### Step 2 — Apply product rule

$$
9 \cdot 10 \cdot 10 \cdot 10 \cdot 10
$$

---

### Step 3 — Compute

$$
9 \cdot 10^4 = 9 \cdot 10,000 = 90,000
$$

---

### Final Answer

$$
90,000
$$

---

## 🔹 Problem 2 — Even numbers

---

### Step 1 — Key observation

Only the last digit determines whether the number is even.

---

### Step 2 — Positions and choices

| Position | Choices |
|----------|--------|
| First digit | 9 |
| Middle 3 digits | 10 each |
| Last digit (even) | 5 |

---

### Step 3 — Apply product rule

$$
9 \cdot 10 \cdot 10 \cdot 10 \cdot 5
$$

---

### Step 4 — Compute

$$
10^3 = 1,000
$$

$$
9 \cdot 1,000 \cdot 5 = 45,000
$$

---

### Final Answer

$$
45,000
$$

---

### Sanity check

Exactly half of all numbers should be even:

$$
\frac{90,000}{2} = 45,000
$$

✔ consistent result

---

## 🔹 Problem 3 — No repeated digits

---

### Step 1 — Key idea

Digits cannot repeat → choices decrease after each step.

---

### Step 2 — Positions and choices

| Position | Choices | Explanation |
|----------|--------|------------|
| First digit | 9 | cannot be 0 |
| Second digit | 9 | any except first |
| Third digit | 8 | exclude first two |
| Fourth digit | 7 | exclude used |
| Fifth digit | 6 | exclude used |

---

### Step 3 — Apply product rule

$$
9 \cdot 9 \cdot 8 \cdot 7 \cdot 6
$$

---

### Step 4 — Compute

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

---

### Step 1 — Strategy

Use complement instead of direct counting.

---

### Step 2 — Known values

| Quantity | Value |
|---------|------|
| Total numbers | 90,000 |
| No repetition | 27,216 |

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

| Problem | Result |
|--------|--------|
| Total numbers | 90,000 |
| Even numbers | 45,000 |
| No repetition | 27,216 |
| At least one repetition | 62,784 |

---

## Interpretation

- About half of all numbers are even  
- Numbers with repetition are more common  
- Restrictions reduce the number of outcomes  

This confirms that allowing repetition increases the total number of possibilities.