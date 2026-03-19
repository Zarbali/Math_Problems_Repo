# Task 7 — k-Permutations (Ordered Selections Without Repetition)

---

## Problem Statement

1. In how many ways can the first three places be assigned among 12 runners?  
2. How many 4-digit numbers with distinct digits can be formed from the digits 1–9?  
3. How many of these numbers are divisible by 5?  

---

## Definitions / Theory

### Ordered selections

In this task, the order **matters**.

Examples:
- first, second, third place → different order = different outcome  
- digits in a number → position matters  

So we use **k-permutations**.

---

### k-permutation formula

The number of ways to choose and arrange $k$ objects from $n$ distinct objects:

$$
P(n,k) = \frac{n!}{(n-k)!}
$$

---

### Equivalent multiplicative form

Instead of factorials, we can write:

$$
P(n,k) = n \cdot (n-1) \cdot (n-2) \cdots (n-k+1)
$$

This is often easier to compute step-by-step.

---

### Key idea

- No repetition → each next choice has fewer options  
- Order matters → we multiply choices step-by-step  

---

## Step-by-Step Solutions

---

## 🔹 Problem 1 — First three places among 12 runners

We assign:
- first place  
- second place  
- third place  

---

### Step 1 — First place

12 choices.

---

### Step 2 — Second place

11 choices (one already used).

---

### Step 3 — Third place

10 choices.

---

### Step 4 — Multiply

$$
12 \cdot 11 \cdot 10
$$

$$
= 1320
$$

---

### Using formula

$$
P(12,3) = \frac{12!}{9!} = 12 \cdot 11 \cdot 10 = 1320
$$

---

### Final Answer

$$
1320
$$

---

## 🔹 Problem 2 — 4-digit numbers with distinct digits (1–9)

We form a number digit by digit.

Digits available: 1 to 9 (no zero).

---

### Step 1 — First digit

9 choices.

---

### Step 2 — Second digit

8 choices (no repetition).

---

### Step 3 — Third digit

7 choices.

---

### Step 4 — Fourth digit

6 choices.

---

### Step 5 — Multiply

$$
9 \cdot 8 \cdot 7 \cdot 6
$$

$$
= 3024
$$

---

### Using formula

$$
P(9,4) = \frac{9!}{5!} = 9 \cdot 8 \cdot 7 \cdot 6 = 3024
$$

---

### Final Answer

$$
3024
$$

---

## 🔹 Problem 3 — Numbers divisible by 5

A number is divisible by 5 if its last digit is 5.

So we fix the last digit.

---

### Step 1 — Fix last digit

Last digit = 5 (1 choice).

---

### Step 2 — Remaining digits

We choose the first 3 digits from:

{1,2,3,4,6,7,8,9}

→ 8 digits (we remove 5).

---

### Step 3 — First digit

8 choices.

---

### Step 4 — Second digit

7 choices.

---

### Step 5 — Third digit

6 choices.

---

### Step 6 — Multiply

$$
8 \cdot 7 \cdot 6
$$

$$
= 336
$$

---

### Using formula

$$
P(8,3) = \frac{8!}{5!} = 8 \cdot 7 \cdot 6 = 336
$$

---

### Final Answer

$$
336
$$

---

## Final Results

| Problem | Formula | Answer |
|--------|--------|--------|
| First 3 places | $P(12,3)$ | 1320 |
| 4-digit numbers | $P(9,4)$ | 3024 |
| Divisible by 5 | $P(8,3)$ | 336 |

---

## Interpretation / Sanity Check

- In Problem 1, the number is large because order of winners matters  
- In Problem 2, the number decreases with each digit because repetition is not allowed  
- In Problem 3, fixing the last digit reduces the number of possibilities  

This confirms that constraints reduce the number of valid outcomes.