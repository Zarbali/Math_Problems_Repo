# Task 4 — Circular Permutations

---

## Definitions / Theory

In circular arrangements:

- rotating the arrangement does NOT create a new outcome  
- only relative positions matter  

---

### Key Formula

$$
(n-1)!
$$

---

### Why (n-1)!

We fix one object to eliminate rotation symmetry, then arrange the rest.

---

## Solutions

---

## 🔹 1. 7 people

---

### Step 1 — fix one person

Fix 1 person → remove rotation.

Remaining:

$$
6 \text{ people}
$$

---

### Step 2 — arrange

$$
6! = 720
$$

---

### Final Answer

$$
720
$$

---

## 🔹 2. Two people together

---

### Step 1 — create block

Treat the two people as one unit.

Total units:

$$
6
$$

---

### Step 2 — circular arrangement

$$
(6-1)! = 5! = 120
$$

---

### Step 3 — internal order

Inside the block:

$$
2 \text{ ways}
$$

---

### Step 4 — multiply

$$
120 \cdot 2 = 240
$$

---

### Final Answer

$$
240
$$

---

## 🔹 3. Opposite seats

---

### Step 1 — fix one person

Fix person A.

---

### Step 2 — choose position for B

Opposite positions:

$$
2 \text{ choices}
$$

---

### Step 3 — arrange remaining

$$
5! = 120
$$

---

### Step 4 — multiply

$$
2 \cdot 120 = 240
$$

---

### Final Answer

$$
240
$$

---

## Key Insight

Fixing one element removes rotational duplicates.