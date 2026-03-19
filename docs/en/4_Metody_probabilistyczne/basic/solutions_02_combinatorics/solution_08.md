# Task 8 — Sequences with Repetition

---

## Problem Statement

1. How many 5-digit PIN codes are possible if digits may repeat?  
2. How many such codes contain at least one repeated digit?  
3. How many such codes have all digits different?  

---

## Definitions / Theory

### Nature of the model

We construct a 5-digit PIN code.

Key properties:

- Order matters → different sequences represent different codes  
- Digits may repeat → the same digit can appear multiple times  
- Each position is chosen independently  

---

### Sequence with repetition

If we form a sequence of length $k$ from $n$ symbols, and repetition is allowed:

$$
\text{Total number of sequences} = n^k
$$

---

### Why this formula works

Each position is filled independently:

- first position → $n$ choices  
- second position → $n$ choices  
- third position → $n$ choices  

So we multiply:

$$
n \cdot n \cdot n \cdots = n^k
$$

---

### Complement method

Sometimes it is easier to count the opposite case.

Instead of counting:
“at least one repeated digit”

we count:
“all digits are different”

and subtract from total.

---

### k-permutation for distinct digits

If all digits must be different, we use:

$$
P(n,k) = n \cdot (n-1) \cdot (n-2) \cdots
$$

because each next position has fewer choices.

---

## Step-by-Step Solutions

---

## 🔹 Problem 1 — Total PIN codes

Digits available: 0–9 → 10 digits.

Each of the 5 positions has 10 choices.

---

### Step 1 — Multiply choices

$$
10 \cdot 10 \cdot 10 \cdot 10 \cdot 10
$$

---

### Step 2 — Write as power

$$
10^5
$$

---

### Step 3 — Compute

$$
10^5 = 100,000
$$

---

### Final Answer

$$
100,000
$$

---

## 🔹 Problem 2 — At least one repeated digit

Use complement:

$$
\text{at least one repeat} = \text{total} - \text{all different}
$$

---

### Step 1 — Total

$$
10^5 = 100,000
$$

---

### Step 2 — All digits different

Now repetition is NOT allowed.

---

#### First digit

10 choices.

#### Second digit

9 choices.

#### Third digit

8 choices.

#### Fourth digit

7 choices.

#### Fifth digit

6 choices.

---

### Step 3 — Multiply

$$
10 \cdot 9 \cdot 8 \cdot 7 \cdot 6
$$

Step-by-step:

$$
10 \cdot 9 = 90
$$

$$
90 \cdot 8 = 720
$$

$$
720 \cdot 7 = 5040
$$

$$
5040 \cdot 6 = 30,240
$$

---

### Step 4 — Subtract

$$
100,000 - 30,240 = 69,760
$$

---

### Final Answer

$$
69,760
$$

---

## 🔹 Problem 3 — All digits different

We already computed this.

---

### Step 1 — Multiply

$$
10 \cdot 9 \cdot 8 \cdot 7 \cdot 6
$$

---

### Step 2 — Result

$$
= 30,240
$$

---

### Using formula

$$
P(10,5) = 30,240
$$

---

### Final Answer

$$
30,240
$$

---

## Final Results

| Problem | Formula | Answer |
|--------|--------|--------|
| Total codes | $10^5$ | 100,000 |
| At least one repeat | $10^5 - P(10,5)$ | 69,760 |
| All digits different | $P(10,5)$ | 30,240 |

---

## Interpretation / Sanity Check

- Most codes contain repeated digits → 69,760 is large  
- Only 30,240 codes have all digits different → much smaller  
- This confirms that allowing repetition increases the number of outcomes  

The results are consistent with intuition.