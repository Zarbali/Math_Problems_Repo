# Problem 1 — Coin × Coin

**Source:** `04_discovery_formalism.md` — Problem 1.

**Convention (from the problem).** Rows label the **first** toss, columns label the **second** toss. So:

| Cell | First toss | Second toss | As a pair |
|------|------------|-------------|-----------|
| top-left | H | H | HH |
| top-right | H | T | HT |
| bottom-left | T | H | TH |
| bottom-right | T | T | TT |

Each cell is one **elementary outcome** of the compound experiment “two tosses.”

---

## Part A — marking events

`X` = outcome belongs to the event; `.` = does not.

### 1. Exactly one head

Exactly one head means one H and one T: either HT or TH.

```
      H   T
H     .   X
T     X   .
```

### 2. Both tosses are the same

Both H (HH) or both T (TT).

```
      H   T
H     X   .
T     .   X
```

### 3. At least one head

Every outcome except TT (no heads).

```
      H   T
H     X   X
T     X   .
```

### 4. The first toss is tails

The first toss is tails on the **bottom row** only: TH and TT.

```
      H   T
H     .   .
T     X   X
```

### 5. The second toss is heads

The second toss is heads in the **left column** only: HH and TH.

```
      H   T
H     X   .
T     X   .
```

---

## Part B — interpretation

### Case 1

```
      H   T
H     X   X
T     .   .
```

Both marked cells lie in the **top row** (first toss H). So the event is: **the first toss is heads** (equivalently: “not tails on the first toss”).

### Case 2

```
      H   T
H     .   X
T     X   .
```

The marked cells are HT and TH: one head and one tail, in either order. So the event is: **exactly one head** (same as Part A.1). Equivalently: **the two tosses are different** (first ≠ second).

---

## Short consistency check

- There are $2 \times 2 = 4$ elementary outcomes; each Part A diagram marks a subset of those four.  
- “At least one head” is the complement of “both tails” (only TT unmarked in A.3).  
- Case 1 is the union of HH and HT; Case 2 is the symmetric difference of the two rows or the union of “H then T” and “T then H.”
