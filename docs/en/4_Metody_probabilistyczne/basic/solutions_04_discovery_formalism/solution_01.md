# Problem 1 — Coin × Coin

---

## Theory — concepts used

| Idea | Meaning |
|------|--------|
| **Sample space** $\Omega$ | All **elementary outcomes** of the experiment — here, both tosses together. |
| **Elementary outcome** | One full result that cannot be split further; here each cell of the $2\times 2$ table is one outcome. |
| **Event** | Any **subset** of $\Omega$; in the grid, marking cells with `X` shows exactly which outcomes belong to the event. |
| **Product structure** | First toss $\times$ second toss: each row is a value of the first toss, each column a value of the second — so the table is a **Cartesian product** $\{\mathrm{H},\mathrm{T}\}\times\{\mathrm{H},\mathrm{T}\}$. |

**Why the grid helps.** Listing “HH, HT, TH, TT” is correct but hides **structure** (which coordinate is which). The table keeps “first toss” and “second toss” visible, so phrases like “first is tails” become **one row**, and “second is heads” becomes **one column**.

---

## Convention (fixed for this experiment)

| Cell position | First toss | Second toss | Outcome as a pair |
|---------------|------------|-------------|-------------------|
| top-left | H | H | HH |
| top-right | H | T | HT |
| bottom-left | T | H | TH |
| bottom-right | T | T | TT |

**Why this matters:** “Exactly one head” is not “pick one H from the alphabet” — it is **exactly two** cells: HT and TH. The grid prevents mixing up order.

Notation: **X** = outcome in the event; **.** = not in the event.

---

## Part A — marking events (step by step)

### 1. Exactly one head

| Step | Procedure | Justification |
|:----:|-------------|---------------|
| 1 | Translate words into counts of H | “Exactly one head” means one H and one T in the pair. |
| 2 | List pairs | HT (first H, second T) and TH (first T, second H). |
| 3 | Mark those cells | Only those two cells get X. |

```
      H   T
H     .   X
T     X   .
```

### 2. Both tosses are the same

| Step | Procedure | Justification |
|:----:|-------------|---------------|
| 1 | “Same” means both H or both T | No mixing. |
| 2 | Pairs | HH and TT only. |

```
      H   T
H     X   .
T     .   X
```

### 3. At least one head

| Step | Procedure | Justification |
|:----:|-------------|---------------|
| 1 | Negate: fail only when **no** head | No head ⇔ both T ⇔ TT. |
| 2 | Mark all cells except TT | Union of “first H” and “second H” is easier to see as “not only bottom-right.” |

```
      H   T
H     X   X
T     X   .
```

**Link to set language:** this event is $\Omega\setminus\{\mathrm{TT}\}$, i.e. the **complement** of {TT}.

### 4. The first toss is tails

| Step | Procedure | Justification |
|:----:|-------------|---------------|
| 1 | First toss = row label | T is the **bottom** row. |
| 2 | Mark the whole row | TH and TT. |

```
      H   T
H     .   .
T     X   X
```

### 5. The second toss is heads

| Step | Procedure | Justification |
|:----:|-------------|---------------|
| 1 | Second toss = column label | H is the **left** column. |
| 2 | Mark the whole column | HH and TH. |

```
      H   T
H     X   .
T     X   .
```

---

## Part B — interpreting a marked grid

### Case 1

```
      H   T
H     X   X
T     .   .
```

| Step | Observation | Conclusion |
|:----:|-------------|------------|
| 1 | Both X lie in the **top** row | First toss is fixed to H. |
| 2 | No mark in bottom row | First toss is never T. |

**Event:** **the first toss is heads** (outcomes HH and HT).

### Case 2

```
      H   T
H     .   X
T     X   .
```

| Step | Observation | Conclusion |
|:----:|-------------|------------|
| 1 | Cells are HT and TH | One H and one T, order different. |
| 2 | Same as Part A.1 | **Exactly one head** ⇔ **the two tosses differ**. |

---

## Summary table (Part A)

| # | Verbal statement | Cells (outcomes) | Size |
|---|------------------|------------------|:----:|
| 1 | Exactly one head | HT, TH | 2 |
| 2 | Both same | HH, TT | 2 |
| 3 | At least one head | HH, HT, TH | 3 |
| 4 | First tails | TH, TT | 2 |
| 5 | Second heads | HH, TH | 2 |

---

## Consistency check

- $\lvert\Omega\rvert=4$; each event is a subset.  
- Part A.3 is the complement of {TT}.  
- Case 1 = row H; Case 2 = symmetric outcomes HT ∪ TH.
