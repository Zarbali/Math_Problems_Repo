# Problem 2 — Die × Die

**Convention.** Row index = **first** die, column index = **second** die. Cell $(i,j)$ means first die shows $i$, second shows $j$. There are $6 \times 6 = 36$ elementary outcomes.

---

## Theory — why a grid?

| Idea | Meaning |
|------|---------|
| **Sample space** | $\Omega = \{(i,j): i,j \in \{1,\ldots,6\}\}$ — all ordered pairs of faces. |
| **Event** | Any subset $E \subseteq \Omega$. Marking cells is drawing that subset on the grid. |
| **Counting** | $\lvert E\rvert$ = number of marked cells; if the dice are fair and independent, $P(E)=\lvert E\rvert/36$. |
| **Why ordered pairs?** | Die 1 and die 2 are **distinguishable** (e.g. red vs blue); $(3,5) \neq (5,3)$. |

**Why row = first, column = second?** A fixed convention ensures a single unambiguous reading of each cell. Any consistent rule suffices; here row = first die, column = second die.

---

## Part A — marking events

For each subproblem: **(1)** describe the condition in symbols, **(2)** list or characterize pairs, **(3)** mark the grid, **(4)** count cells (optional check).

### 1. The sum is equal to 8

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Require $i + j = 8$ with $i,j \in \{1,\ldots,6\}$. | “Sum 8” is a property of the **pair** $(i,j)$, not of one die alone. |
| 2 | Solve: $j = 8-i$. Need $1 \le j \le 6$ ⇒ $i \in \{2,3,4,5,6\}$. | Each valid $i$ gives **exactly one** $j$. |
| 3 | Pairs: $(2,6),(3,5),(4,4),(5,3),(6,2)$ — **5** cells. | These are all solutions in the grid; $(1,7)$ is impossible on a die. |

```
      1 2 3 4 5 6
1     . . . . . .
2     . . . . . X
3     . . . . X .
4     . . . X . .
5     . . X . . .
6     . X . . . .
```

**Shape:** cells lie on an “anti-diagonal” line (constant $i+j$).

---

### 2. The first die is greater than the second

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Condition: $i > j$. | “First greater than second” compares **coordinates**, not sums. |
| 2 | For row $i$, mark columns $j = 1,\ldots,i-1$. | Those are exactly the $j$ with $j < i$. |
| 3 | Row 1: no marks. Row 6: five marks ($j=1..5$). | Matches $i-1$ cells per row; total $0+1+2+3+4+5 = 15$. |

```
      1 2 3 4 5 6
1     . . . . . .
2     X . . . . .
3     X X . . . .
4     X X X . . .
5     X X X X . .
6     X X X X X .
```

**Shape:** strictly below the main diagonal (no diagonal — $i=j$ is excluded).

---

### 3. Both dice show even numbers

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Even faces: $\{2,4,6\}$. | Standard labeling on a d6. |
| 2 | Need $i \in \{2,4,6\}$ **and** $j \in \{2,4,6\}$. | “Both even” = **two** independent conditions on $i$ and $j$. |
| 3 | Mark a $3 \times 3$ block at those rows and columns. | Cartesian product: $3$ choices × $3$ choices = **9** cells. |

```
      1 2 3 4 5 6
1     . . . . . .
2     . X . X . X
3     . . . . . .
4     . X . X . X
5     . . . . . .
6     . X . X . X
```

**Contrast with sum problems:** here the event is a **rectangle** (product set), not a diagonal band.

---

### 4. At least one die shows 6

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Event = $\{i=6\} \cup \{j=6\}$ (“row 6 **or** column 6”). | “At least one 6” is a **union** of two strips. |
| 2 | Row 6 has 6 cells; column 6 has 6 cells; overlap is $(6,6)$ once. | Inclusion–exclusion: $6+6-1 = 11$ cells. |
| 3 | Mark full row 6 and full column 6. | Visual union: cross/plus shape. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . . X
3     . . . . . X
4     . . . . . X
5     . . . . . X
6     X X X X X X
```

**Common mistake:** counting $6+6=12$ and forgetting the double-counted corner $(6,6)$.

---

### 5. Exactly one die shows 1

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Split: $(i=1, j\neq 1)$ **or** $(j=1, i\neq 1)$. | “Exactly one” = first-only **or** second-only; **mutually exclusive** because $(1,1)$ would be both. |
| 2 | First part: row 1, columns $2$–$6$ → **5** cells. | $j \neq 1$ removes column 1 from row 1. |
| 3 | Second part: column 1, rows $2$–$6$ → **5** cells. | $i \neq 1$ removes row 1 from column 1. |
| 4 | Total $5+5=10$; $(1,1)$ unmarked. | Marking $(1,1)$ would classify the outcome as “two 1s,” not “exactly one.” |

```
      1 2 3 4 5 6
1     . X X X X X
2     X . . . . .
3     X . . . . .
4     X . . . . .
5     X . . . . .
6     X . . . . .
```

---

## Part B — interpretation

### Case 1

```
      1 2 3 4 5 6
1     . . . . . .
2     . . . . . .
3     . . X X X X
4     . . X X X X
5     . . X X X X
6     . . X X X X
```

| Step | Observation | Conclusion |
|------|-------------|------------|
| 1 | Marked rows: $3,4,5,6$ only. | First die $i \ge 3$. |
| 2 | Marked columns: $3,4,5,6$ only. | Second die $j \ge 3$. |
| 3 | Full rectangle on those indices. | Event = **both** dice $\ge 3$ (neither shows 1 or 2). |

**Formal:** $\{(i,j): i \ge 3,\ j \ge 3\} = \{3,4,5,6\} \times \{3,4,5,6\}$ — a **product** event (rectangle).

---

### Case 2

```
      1 2 3 4 5 6
1     X . . . . .
2     . X . . . .
3     . . X . . .
4     . . . X . .
5     . . . . X .
6     . . . . . X
```

| Step | Observation | Conclusion |
|------|-------------|------------|
| 1 | Marks at $(1,1),(2,2),\ldots,(6,6)$. | These satisfy $i = j$. |
| 2 | No other cells marked. | Off-diagonal pairs have $i \neq j$. |

**Event:** **doubles** — both dice show the same number. **Formal:** $\{(i,j): i=j\}$.

---

## Summary table (Part A)

| # | Event (words) | Condition | $\lvert E\rvert$ |
|---|----------------|-----------|:----------------:|
| 1 | Sum 8 | $i+j=8$ | 5 |
| 2 | First > second | $i>j$ | 15 |
| 3 | Both even | $i,j \in \{2,4,6\}$ | 9 |
| 4 | At least one 6 | $i=6$ or $j=6$ | 11 |
| 5 | Exactly one 1 | $(i=1,j\neq1)$ or $(j=1,i\neq1)$ | 10 |

---

## Short checks

- Part A.1: five cells — anti-diagonal band for constant sum.  
- Part A.4: $11$ cells ($6+6-1$) for row 6 ∪ column 6.  
- Part A.5: $5+5=10$; $(1,1)$ correctly excluded.  
- Part B Case 2: equality event $\{(i,j): i=j\}$.
