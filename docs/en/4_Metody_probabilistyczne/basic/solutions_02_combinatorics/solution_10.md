# Task 10 — Urn Models

---

## Problem Statement

An urn contains:

- 5 red balls  
- 4 blue balls  
- 3 green balls  

Total: 12 balls.

---

### Problems

1. Three balls are drawn without replacement. How many samples are possible if order is ignored?  
2. How many samples contain exactly two red balls?  
3. Three balls are drawn and the order of colors is recorded. How many outcomes are possible?  
4. How many ordered outcomes contain exactly two red balls?  

---

## Definitions / Theory

### Total number of objects

Total balls:

$$
5 + 4 + 3 = 12
$$

---

### Two different models

This task involves **two types of counting models**:

---

### 1. Order ignored → combinations

Used when:

- we only care which balls are selected  
- order does not matter  

Formula:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

---

### 2. Order recorded → permutations

Used when:

- the sequence of draws matters  
- different orders count as different outcomes  

Formula:

$$
P(n,k) = \frac{n!}{(n-k)!}
$$

---

### Without replacement

Once a ball is drawn, it cannot be selected again.

So the number of available choices decreases at each step.

---

### Product rule

When selecting from different groups:

- choose from one group  
- choose from another group  

Total ways are multiplied.

---

### Arrangements of selected objects

If we select objects and then arrange them:

- we multiply by the number of permutations  

For 3 objects:

$$
3! = 6
$$

---

## Step-by-Step Solutions

---

## 🔹 Problem 1 — Order ignored

We choose 3 balls from 12.

---

### Step 1 — formula

$$
\binom{12}{3}
$$

---

### Step 2 — expand

$$
\frac{12 \cdot 11 \cdot 10}{3 \cdot 2 \cdot 1}
$$

---

### Step 3 — compute

$$
12 \cdot 11 \cdot 10 = 1320
$$

$$
3! = 6
$$

$$
\frac{1320}{6} = 220
$$

---

### Final Answer

$$
220
$$

---

## 🔹 Problem 2 — Exactly two red (order ignored)

We select:

- 2 red balls from 5  
- 1 non-red ball from remaining 7  

---

### Step 1 — choose red

$$
\binom{5}{2} = \frac{5 \cdot 4}{2} = 10
$$

---

### Step 2 — choose non-red

$$
\binom{7}{1} = 7
$$

---

### Step 3 — multiply

$$
10 \cdot 7 = 70
$$

---

### Final Answer

$$
70
$$

---

## 🔹 Problem 3 — Order recorded

Now order matters.

We draw 3 balls in sequence.

---

### Step 1 — choices

First draw: 12 choices  
Second draw: 11 choices  
Third draw: 10 choices  

---

### Step 2 — multiply

$$
12 \cdot 11 \cdot 10
$$

$$
= 1320
$$

---

### Formula form

$$
P(12,3) = 1320
$$

---

### Final Answer

$$
1320
$$

---

## 🔹 Problem 4 — Exactly two red (order recorded)

We first select:

- 2 red balls  
- 1 non-red ball  

Then we arrange them.

---

### Step 1 — choose red

$$
\binom{5}{2} = 10
$$

---

### Step 2 — choose non-red

$$
\binom{7}{1} = 7
$$

---

### Step 3 — arrange

We arrange 3 balls:

$$
3! = 6
$$

---

### Step 4 — multiply

$$
10 \cdot 7 \cdot 6
$$

$$
= 420
$$

---

### Final Answer

$$
420
$$

---

## Final Results

| Problem | Answer |
|--------|--------|
| Order ignored | 220 |
| Exactly 2 red (unordered) | 70 |
| Order recorded | 1320 |
| Exactly 2 red (ordered) | 420 |

---

## Interpretation / Sanity Check

- Ordered outcomes (1320) are much larger than unordered (220)  
- Adding order multiplies possibilities  
- Constraints (exactly 2 red) reduce outcomes  

This confirms the correctness of the model selection.