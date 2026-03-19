# Solution

## Task 2 — Permutations

---

### 1. Arranging 8 different books on a shelf

All 8 books are used.  
Order matters (different positions on the shelf).  
No repetition. All books are distinguishable.

→ Model: permutation

$$8! = 40\,320$$

Note: each arrangement is a different ordering of the same books.

---

### 2. 8 people in a row — two particular people must sit next to each other

The two fixed people are treated as one block.

Instead of 8 individuals, we arrange:
- 1 block (the pair)
- 6 remaining people

Total: 7 objects.

- Arrange 7 objects: $7!$
- Inside the block, the two people can switch places: $2$ ways

→ Total number of arrangements:

$$7! \cdot 2 = 5\,040 \cdot 2 = 10\,080$$

Note: the block ensures the two people are always adjacent.

---

### 3. 8 people in a row — those two must NOT sit next to each other

Use complement:

Total arrangements minus arrangements where they sit together.

- Total arrangements: $8!$
- Arrangements where they sit together: $7! \cdot 2$

→ Result:

$$8! - 7! \cdot 2 = 40\,320 - 10\,080 = 30\,240$$

or factored form:

$$7!(8 - 2) = 7! \cdot 6$$

Note: easier to count the opposite case and subtract.

---

### 4. Ordering 10 questions — first question fixed

The first position is fixed and cannot change.  
Only the remaining 9 questions can be rearranged.

→ Model: permutation of 9 elements

$$9! = 362\,880$$

Note: fixing one position reduces the number of permutations.