# Solution

## Task 4 — Circular Permutations

Key idea: in circular arrangements, rotations are identical, so one position is fixed.

Formula:
$$(n - 1)!$$

---

### 1. 7 people around a round table

All 7 people are arranged in a circle.

Rotations are equivalent, so one position is fixed.

→ Model: circular permutation

$$
(7 - 1)! = 6! = 720
$$

Note: fixing one person removes duplicate rotations.

---

### 2. 7 people — two particular people must sit next to each other

The two people are treated as one block.

Now there are:
- 1 block
- 5 remaining people  
→ total: 6 units

Arrange these in a circle:

$$
(6 - 1)! = 5!
$$

Inside the block, the two people can switch positions:

$$
2 \text{ ways}
$$

Total:

$$
5! \cdot 2 = 120 \cdot 2 = 240
$$

Note: the block guarantees adjacency, and internal order adds a factor of 2.

---

### 3. 7 people — two particular people must sit opposite each other

Fix one person to remove rotational symmetry.

Now consider the position of the second person.

In a circle of 7 seats, there are exactly 2 positions opposite (maximally distant).

So:

- choose position for second person: $2$ ways  
- arrange remaining 5 people freely: $5!$

Total:

$$
2 \cdot 5! = 2 \cdot 120 = 240
$$

Note: fixing one person avoids overcounting rotations.