# Task 7 — k-Permutations (Ordered Selections Without Repetition)

---

## Problem Statement

1. In how many ways can the first three places be assigned among 12 runners?  
2. How many 4-digit numbers with distinct digits can be formed from the digits 1–9?  
3. How many of these numbers are divisible by 5?  

---

## Definitions / Theory

### Counting model selection

The key question in counting problems is:

- Does **order matter**?
- Is **repetition allowed**?

The answers determine which model to use.

---

### Ordered selection without repetition

In this task:

- Order **matters** (positions or digit order change the result)
- Repetition is **not allowed**

Therefore, we use **k-permutations**.

---

### k-permutation formula

The number of ways to choose and arrange $k$ objects from $n$ distinct objects is:

$$
P(n,k) = \frac{n!}{(n-k)!}
$$

---

### Meaning of the formula

- $n!$ counts all arrangements of all objects  
- $(n-k)!$ removes the unused part  
- The result gives arrangements of only $k$ elements  

---

### Multiplicative interpretation

Instead of factorials, we can think step-by-step:

$$
P(n,k) = n \cdot (n-1) \cdot (n-2) \cdots (n-k+1)
$$

This reflects the process:

- first choice → $n$ options  
- second → $n-1$  
- third → $n-2$  

Each step has fewer options because repetition is not allowed.

---

### Why multiplication is used

Each step is independent:

- choosing the first element does not depend on future choices  
- total number of outcomes is the product of choices  

This follows the **multiplication principle**.

---

### Special constraints

Sometimes we impose conditions:

- fixing a position (e.g., last digit must be 5)  
- removing elements from the pool  

These constraints reduce the number of available choices at each step.

---

## Step-by-Step Solutions

---

## 🔹 Problem 1 — First three places among 12 runners

We assign ordered positions:
- first place  
- second place  
- third place  

Order matters because changing positions gives a different result.

---

### Step 1 — First place

There are 12 runners → 12 choices.

---

### Step 2 — Second place

One runner already used → 11 choices.

---

### Step 3 — Third place

Two runners already used → 10 choices.

---

### Step 4 — Multiply

$$
12 \cdot 11 \cdot 10
$$

$$
= 1320
$$

---

### Formula form

$$
P(12,3) = \frac{12!}{9!} = 12 \cdot 11 \cdot 10
$$

---

### Final Answer

$$
1320
$$

---

## 🔹 Problem 2 — 4-digit numbers with distinct digits

We form numbers digit by digit.

Digits available: 1–9 (no zero).

---

### Step 1 — First digit

Any of 9 digits → 9 choices.

---

### Step 2 — Second digit

One used → 8 choices.

---

### Step 3 — Third digit

Two used → 7 choices.

---

### Step 4 — Fourth digit

Three used → 6 choices.

---

### Step 5 — Multiply

$$
9 \cdot 8 \cdot 7 \cdot 6
$$

$$
= 3024
$$

---

### Formula form

$$
P(9,4) = \frac{9!}{5!} = 3024
$$

---

### Final Answer

$$
3024
$$

---

## 🔹 Problem 3 — Numbers divisible by 5

A number is divisible by 5 if the last digit is 5.

So we fix the last position.

---

### Step 1 — Fix last digit

Last digit = 5 → 1 choice.

---

### Step 2 — Available digits

Remaining digits:

{1,2,3,4,6,7,8,9}

Total: 8 digits.

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

### Formula form

$$
P(8,3) = \frac{8!}{5!} = 336
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

- Problem 1: large number because all orders are different  
- Problem 2: decreases each step due to no repetition  
- Problem 3: fixing a digit reduces possibilities  

This confirms that constraints directly reduce the number of valid outcomes.