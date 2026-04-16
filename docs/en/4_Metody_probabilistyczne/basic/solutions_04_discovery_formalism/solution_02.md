# Problem 2 — Die × Die

**Source:** `04_discovery_formalism.md` — Problem 2.

**Convention.** Row index = **first** die, column index = **second** die. Cell $(i,j)$ means first die shows $i$, second shows $j$. There are $6 \times 6 = 36$ elementary outcomes.

---

## Part A — marking events

### 1. The sum is equal to 8

Pairs with $i+j=8$: $(2,6)$, $(3,5)$, $(4,4)$, $(5,3)$, $(6,2)$.

```
      1 2 3 4 5 6
1     . . . . . .
2     . . . . . X
3     . . . . X .
4     . . . X . .
5     . . X . . .
6     . X . . . .
```

### 2. The first die is greater than the second

Need $i > j$. For each row $i$, mark columns $j = 1,\ldots,i-1$.

```
      1 2 3 4 5 6
1     . . . . . .
2     X . . . . .
3     X X . . . .
4     X X X . . .
5     X X X X . .
6     X X X X X .
```

### 3. Both dice show even numbers

Even faces: $\{2,4,6\}$. Both even means row and column in $\{2,4,6\}$ — a $3 \times 3$ block at those indices.

```
      1 2 3 4 5 6
1     . . . . . .
2     . X . X . X
3     . . . . . .
4     . X . X . X
5     . . . . . .
6     . X . X . X
```

### 4. At least one die shows 6

All cells in **row 6** or **column 6** (union of the two strips).

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . . X
3     . . . . . X
4     . . . . . X
5     . . . . . X
6     X X X X X X
```

### 5. Exactly one die shows 1

Either (first is 1 and second is not 1) or (second is 1 and first is not 1). Exclude $(1,1)$ where **both** show 1.

- Row 1, columns $2$–$6$: HT style “only first is 1” — actually first=1, second≠1.
- Column 1, rows $2$–$6$: second=1, first≠1.

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

Marked cells are those with **first die $\in \{3,4,5,6\}$** and **second die $\in \{3,4,5,6\}$**.

**Event:** both dice show a number **at least 3** (neither die shows 1 or 2). Equivalently: $\min(i,j) \ge 3$ in the sense that both $i \ge 3$ and $j \ge 3$.

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

The marked cells are exactly $(1,1),(2,2),\ldots,(6,6)$ — the **main diagonal**.

**Event:** **both dice show the same number** (doubles: $1$–$1$, $2$–$2$, …, $6$–$6$).

---

## Short checks

- Part A.1: five cells — standard antidiagonal band for sum $8$.  
- Part A.4: $11$ cells ($6+6-1$) for “row 6 or column 6.”  
- Part A.5: $5+5=10$ cells; $(1,1)$ is correctly left unmarked.  
- Case 2 is the equality event $\{(i,j): i=j\}$.
