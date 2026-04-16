# Problem 4 — Building complex statements from simple ones

**Convention.** Row $i$ = first die, column $j$ = second die. Cell $(i,j)$ is marked **X** if the outcome belongs to the event. Sample space: all $36$ ordered pairs $(i,j)$.

---

## Theory — events, logic, and pictures

| Logical phrase | Set operation | On the grid |
|----------------|---------------|-------------|
| “$P$ **or** $Q$” | $P \cup Q$ | Mark cells in $P$, in $Q$, or in both. |
| “$P$ **and** $Q$” | $P \cap Q$ | Mark overlap only. |
| “**not** $P$” (within $\Omega$) | $P^c$ or $\Omega \setminus P$ | Unmark $P$; complement relative to full $6\times6$. |
| De Morgan | $(P \cup Q)^c = P^c \cap Q^c$ | “Neither $P$ nor $Q$.” |
| | $(P \cap Q)^c = P^c \cup Q^c$ | “Not both” — **all but** the intersection strip (here: all but two cells). |

**Role of the diagram.** Unions and complements are easy to **mis-count** from words alone; the grid shows **structure** (diagonals, strips, rectangles).

---

## Part A — basic statements

### $A$: the sum of the two results is equal to 7

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Condition $i+j=7$, $i,j \in \{1,\ldots,6\}$. | “Sum 7” is standard antidiagonal in the die grid. |
| 2 | Pairs: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ — **6** cells. | One pair per $i$; symmetric roles. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . X .
3     . . . X . .
4     . . X . . .
5     . X . . . .
6     X . . . . .
```

---

### $B$: the first die shows a greater number than the second

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $i > j$. | Strict inequality ⇒ **below** main diagonal (excluding $i=j$). |
| 2 | Row $i$: columns $1,\ldots,i-1$. | Total $15$ cells. |

```
      1 2 3 4 5 6
1     . . . . . .
2     X . . . . .
3     X X . . . .
4     X X X . . .
5     X X X X . .
6     X X X X X .
```

---

### $C$: at least one die shows 6

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $i=6$ **or** $j=6$. | Union of **row 6** and **column 6**. |
| 2 | $\lvert C\rvert = 6+6-1 = 11$. | Inclusion–exclusion for corner $(6,6)$. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . . X
3     . . . . . X
4     . . . . . X
5     . . . . . X
6     X X X X X X
```

---

## Part B — compound statements

Set-theoretic forms use $A,B,C$ above; complements are relative to the full $6\times 6$ sample space.

### 1. Sum 7 **or** at least one 6 — $A \cup C$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Start from $C$ (full cross). | $C$ already contains $(1,6)$ and $(6,1)$ on the sum-7 line. |
| 2 | Add remaining points of $A$ not in $C$. | Interior sum-7 pairs without a 6: $(2,5),(3,4),(4,3),(5,2)$. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . X X
3     . . . X . X
4     . . X . . X
5     . X . . . X
6     X X X X X X
```

---

### 2. Sum 7 **and** at least one 6 — $A \cap C$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Need $i+j=7$ and ($i=6$ or $j=6$). | Intersection: both conditions. |
| 2 | Only $(1,6)$ and $(6,1)$. | Other sum-7 pairs use only faces $1$–$5$. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . . .
3     . . . . . .
4     . . . . . .
5     . . . . . .
6     X . . . . .
```

---

### 3. First > second **and** at least one 6 — $B \cap C$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $i>j$ and ($i=6$ or $j=6$). | If $j=6$, need $i>6$ — impossible. So **must** have $i=6$, $j<6$. |
| 2 | Cells $(6,1),\ldots,(6,5)$ — **5** cells. | Bottom row except $(6,6)$ (there $i=j$, not $i>j$). |

```
      1 2 3 4 5 6
1     . . . . . .
2     . . . . . .
3     . . . . . .
4     . . . . . .
5     . . . . . .
6     X X X X X .
```

---

### 4. Sum 7, **but** first not greater than second — $A \cap B^{c}$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $B^c$: “not ($i>j$)” ⇒ $i \le j$. | Weak inequality includes diagonal. |
| 2 | On sum-7 line, keep $i \le j$: $(1,6),(2,5),(3,4)$. | Drop $(4,3),(5,2),(6,1)$ where $i>j$. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . X .
3     . . . X . .
4     . . . . . .
5     . . . . . .
6     . . . . . .
```

---

### 5. Sum 7, **and** no die shows 6 — $A \cap C^{c}$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $C^c$: both faces in $\{1,\ldots,5\}$. | Complement of “row 6 or column 6.” |
| 2 | On sum-7 line, exclude $(1,6),(6,1)$. | Leaves $(2,5),(3,4),(4,3),(5,2)$ — **4** cells. |

```
      1 2 3 4 5 6
1     . . . . . .
2     . . . . X .
3     . . . X . .
4     . . X . . .
5     . X . . . .
6     . . . . . .
```

---

### 6. At least one 6, **but** sum not 7 — $C \cap A^{c}$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | All of $C$ except the two cells in $A \cap C$. | Remove $(1,6),(6,1)$ from the cross. |
| 2 | $11 - 2 = 9$ cells. | Check: column 6 loses $(1,6)$; row 6 loses $(6,1)$. |

```
      1 2 3 4 5 6
1     . . . . . .
2     . . . . . X
3     . . . . . X
4     . . . . . X
5     . . . . . X
6     . X X X X X
```

---

### 7. Sum not 7 **and** first > second — $A^{c} \cap B$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Start from $B$ (below diagonal). | Then remove cells with $i+j=7$. |
| 2 | Remove $(4,3),(5,2),(6,1)$ from $B$. | These are the only sum-$7$ pairs with $i>j$; each must be excluded from $A^c\cap B$. |

```
      1 2 3 4 5 6
1     . . . . . .
2     X . . . . .
3     X X . . . .
4     X X . . . .
5     X . X X . .
6     . X X X X .
```

*(Row 5: $(5,2)$ lies on sum $7$, so it is excluded.)*

---

### 8. First not greater than second **and** at least one 6 — $B^{c} \cap C$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $i \le j$ and ($i=6$ or $j=6$). | Case $i=6$, $j<6$: then $i \le j$ fails. Case $j=6$: need $i \le 6$ — always true. |
| 2 | Event = **entire column 6**. | Six cells $(1,6),\ldots,(6,6)$. |

```
      1 2 3 4 5 6
1     . . . . . X
2     . . . . . X
3     . . . . . X
4     . . . . . X
5     . . . . . X
6     . . . . . X
```

---

### 9. Not (sum 7 **or** at least one 6) — $(A \cup C)^{c} = A^{c} \cap C^{c}$ (De Morgan)

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | $A^c \cap C^c$: neither sum 7 nor a 6. | Both dice in $\{1,\ldots,5\}$, and **not** the interior sum-7 pairs. |
| 2 | In the $5\times5$ block, **unmark** $(2,5),(3,4),(4,3),(5,2)$. | Those four are exactly sum 7 with no 6. |

```
      1 2 3 4 5 6
1     X X X X X .
2     X X X X . .
3     X X X . X .
4     X X . X X .
5     X . X X X .
6     . . . . . .
```

*(Inside the $5\times5$ block, the four antidiagonal sum-$7$ cells $(2,5),(3,4),(4,3),(5,2)$ stay unmarked.)*

---

### 10. Not (sum 7 **and** at least one 6) — $(A \cap C)^{c}$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Remove **only** $A \cap C = \{(1,6),(6,1)\}$ from $\Omega$. | De Morgan for intersection gives union of complements — “all outcomes except those two.” |
| 2 | $36 - 2 = 34$ marked cells. | Very different from item 9 (only **two** holes). |

```
      1 2 3 4 5 6
1     X X X X X .
2     X X X X X X
3     X X X X X X
4     X X X X X X
5     X X X X X X
6     . X X X X X
```

---

## Logic reference (for checking)

| Item | Event |
|:----:|--------|
| 1 | $A \cup C$ |
| 2 | $A \cap C$ |
| 3 | $B \cap C$ |
| 4 | $A \cap B^{c}$ |
| 5 | $A \cap C^{c}$ |
| 6 | $C \cap A^{c}$ |
| 7 | $A^{c} \cap B$ |
| 8 | $B^{c} \cap C$ |
| 9 | $(A \cup C)^{c}$ (De Morgan: $A^{c}\cap C^{c}$) |
| 10 | $(A \cap C)^{c}$ (De Morgan: $A^{c}\cup C^{c}$) |

**Items 9 vs 10:** Item 9 removes the **union** $A\cup C$ (large “forbidden” region). Item 10 removes only the **intersection** $A\cap C$ — **two** cells — so almost the whole grid stays in the event.

---

## Event sizes and probabilities (optional)

The sample space has $\lvert\Omega\rvert = 36$ equally likely outcomes (two independent fair dice). For any event $E$,

$$
P(E)=\frac{\lvert E\rvert}{\lvert\Omega\rvert}=\frac{\lvert E\rvert}{36}.
$$

| Item | $\lvert E\rvert$ | $P(E)$ | Reduced form |
|:----:|:----------------:|:------:|:-------------|
| 1 | 15 | $15/36$ | $5/12$ |
| 2 | 2 | $2/36$ | $1/18$ |
| 3 | 5 | $5/36$ | — |
| 4 | 3 | $3/36$ | $1/12$ |
| 5 | 4 | $4/36$ | $1/9$ |
| 6 | 9 | $9/36$ | $1/4$ |
| 7 | 12 | $12/36$ | $1/3$ |
| 8 | 6 | $6/36$ | $1/6$ |
| 9 | 21 | $21/36$ | $7/12$ |
| 10 | 34 | $34/36$ | $17/18$ |
