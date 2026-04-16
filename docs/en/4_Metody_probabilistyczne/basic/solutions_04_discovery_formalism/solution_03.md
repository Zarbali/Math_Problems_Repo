# Problem 3 — Weather (7 days × 3 states)

**Convention.** Columns are **days**; rows are **states** S, C, R. An **X** in cell (state, day) means that on that day the weather **may** be that state, and the **only** states allowed that day are those rows in that column which carry an **X**. If **no** cell in a column is marked, that day is **unrestricted** (any of S, C, R is allowed).

*(Example: only Sat and Sun marked in row S means both weekend days must be sunny; unmarked columns mean no restriction that day. If S and C are marked in every column and R never, each day is sunny or cloudy only.)*

A full week is one choice of state per day — a vector in $\{S,C,R\}^7$. When **each column** is filled independently with a subset of allowed states, the grid describes a **cylinder set** (a **product** of one-day restrictions).

---

## Theory — grids, products, and unions

| Concept | Meaning |
|--------|---------|
| **Outcome** | A 7-tuple $(\omega_{\mathrm{Mon}},\ldots,\omega_{\mathrm{Sun}})$ with each $\omega_d \in \{S,C,R\}$. |
| **Product event** | $\{\omega : \omega_d \in A_d \text{ for all } d\}$ where each $A_d \subseteq \{S,C,R\}$ — “column $d$ may only use states in $A_d$.” |
| **Why products are easy on the grid** | The grid is read **per column**: allowed rows for that day only. |
| **Union of two product events** | “Rain Wed **or** rain Fri” links **two** days; it is **not** always one product of seven column restrictions (see Part A.3). |

**Why “empty column = free”?** If no X appears in a column, the problem’s convention does **not** forbid any state that day — all three are possible. That matches “no information” about that day.

---

## Part A — marking events

### 1. Monday is sunny

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Require $\omega_{\mathrm{Mon}} = S$. | “Monday is sunny” fixes **one** coordinate. |
| 2 | Mark only (S, Mon). Leave other columns blank. | Blank columns ⇒ **no restriction** Tue–Sun. |

```
      Mon Tue Wed Thu Fri Sat Sun
S     X   .   .   .   .   .   .
C     .   .   .   .   .   .   .
R     .   .   .   .   .   .   .
```

**Outcome set:** $\{S\} \times \{S,C,R\}^6$ — a **cylinder** over Monday.

---

### 2. The weekend (Saturday and Sunday) is rainy

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Require $\omega_{\mathrm{Sat}} = R$ and $\omega_{\mathrm{Sun}} = R$. | “Weekend is rainy” = **two** fixed coordinates. |
| 2 | Mark (R, Sat) and (R, Sun). Mon–Fri blank. | Independent “free” days stay unrestricted. |

```
      Mon Tue Wed Thu Fri Sat Sun
S     .   .   .   .   .   .   .
C     .   .   .   .   .   .   .
R     .   .   .   .   .   X   X
```

**Outcome set:** $\{S,C,R\}^5 \times \{R\} \times \{R\}$.

---

### 3. It rains on Wednesday or Friday

**Set-theoretic form.** Let $\omega_{\mathrm{Wed}}$ and $\omega_{\mathrm{Fri}}$ be the states on those days. The event is

$$
\{\omega_{\mathrm{Wed}} = R\} \;\cup\; \{\omega_{\mathrm{Fri}} = R\}.
$$

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | Translate “or” → **set union** of two events. | Logical OR corresponds to $\cup$ on sets of outcomes. |
| 2 | Recognize: this is **not** “Wed rainy **and** Fri rainy.” | AND would be **intersection** — smaller event. |
| 3 | **No single** family $A_{\mathrm{Mon}},\ldots,A_{\mathrm{Sun}}$ with $A_d \subseteq \{S,C,R\}$ yields exactly this event as $\{\omega : \forall d,\ \omega_d \in A_d\}$. | A **pure product** fixes each day’s allowed set **independently**. Here Wed and Fri are linked by **OR**: there is no assignment of per-column allowed subsets whose product equals “rain on Wed or rain on Fri” exactly — any such product either omits some intended outcomes or admits some unintended ones. *(Sketch: an OR ties two coordinates; a product cannot express “at least one of these two coordinates is R” as independent column restrictions.)* |

**Diagrammatic representation**

| Grid | Event described |
|------|-----------------|
| **Cylinder A** — only Wed fixed to R | $\{\omega_{\mathrm{Wed}}=R\}$ (Fri free among S,C,R). |
| **Cylinder B** — only Fri fixed to R | $\{\omega_{\mathrm{Fri}}=R\}$ (Wed free). |

**Cylinder A — “Wednesday is rainy”** (Friday unrestricted):

```
      Mon Tue Wed Thu Fri Sat Sun
S     .   .   .   .   .   .   .
C     .   .   .   .   .   .   .
R     .   .   X   .   .   .   .
```

**Cylinder B — “Friday is rainy”** (Wednesday unrestricted):

```
      Mon Tue Wed Thu Fri Sat Sun
S     .   .   .   .   .   .   .
C     .   .   .   .   .   .   .
R     .   .   .   .   X   .   .
```

The problem’s event is **outcomes in A or in B** — equivalently: **not** (Wednesday non-rainy **and** Friday non-rainy).

| For a single summary grid | Verdict |
|---------------------------|---------|
| One product picture for “Wed OR Fri rainy” | **In general impossible** without losing precision; state the **union** and use two cylinders (or equivalent set description). |

---

### 4. There is no rainy day during the week

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | For **every** day, forbid R: only S and C allowed. | “No rainy day” = each coordinate $\in \{S,C\}$. |
| 2 | Mark S and C in **all seven** columns; leave R row empty. | Each column’s allowed set is $\{S,C\}$. |

```
      Mon Tue Wed Thu Fri Sat Sun
S     X   X   X   X   X   X   X
C     X   X   X   X   X   X   X
R     .   .   .   .   .   .   .
```

**Outcome set:** $\{S,C\}^7$ — a **product** (same pattern as Part B Case 2).

---

### 5. Thursday is not sunny

| Step | Procedure | Justification |
|------|-------------|---------------|
| 1 | “Not sunny” on Thu ⇒ $\omega_{\mathrm{Thu}} \in \{C,R\}$. | Complement of {S} for that day. |
| 2 | Mark C and Thu, R and Thu; other columns blank. | One column restricted; rest free. |

```
      Mon Tue Wed Thu Fri Sat Sun
S     .   .   .   .   .   .   .
C     .   .   .   X   .   .   .
R     .   .   .   X   .   .   .
```

---

## Part B — interpretation

### Case 1

```
      Mon Tue Wed Thu Fri Sat Sun
S     .   .   .   .   .   X   X
C     .   .   .   .   .   .   .
R     .   .   .   .   .   .   .
```

| Step | Observation | Conclusion |
|------|-------------|------------|
| 1 | Only Sat and Sun have marks; both in row S. | $\omega_{\mathrm{Sat}}=\omega_{\mathrm{Sun}}=S$. |
| 2 | Mon–Fri columns empty. | Mon–Fri **unrestricted** (any of S,C,R). |

**Event:** **Saturday and Sunday are both sunny.** Same logical shape as Part A.1–2: fix some days, leave others free.

---

### Case 2

```
      Mon Tue Wed Thu Fri Sat Sun
S     X   X   X   X   X   X   X
C     X   X   X   X   X   X   X
R     .   .   .   .   .   .   .
```

| Step | Observation | Conclusion |
|------|-------------|------------|
| 1 | Every day: S and C allowed, R forbidden. | Each day $\in \{S,C\}$. |
| 2 | Full week pattern. | **Never rains** during the week — same as Part A.4. |

**Event:** every day is sunny or cloudy; **no rainy day**.

---

## Summary

| Part | Event type | Product grid? |
|------|------------|----------------|
| A.1, A.2, A.4, A.5 | Cylinder / product | Yes |
| A.3 | Union of two “one-day rain” cylinders | **No** single product; use $\cup$ or two grids |
| B.1 | Fix weekend sunny | Yes |
| B.2 | No rain all week | Yes |

---

## Short checks

- Part A.1 and A.5 fix **one** column; others free — matches the “dots = unrestricted” reading of Case 1 style.  
- Part A.4 matches Case 2.  
- Part A.3: OR of two day-specific events is the first case where a **pure** product grid is insufficient — an important structural point.
