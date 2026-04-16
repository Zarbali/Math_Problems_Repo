# Problem 5 — From recorded frequencies to probability

**Experiment (wording of the task).** A six-sided die is rolled **1000** times. The numbers of occurrences of the elementary outcomes are

$$
n(\{1\})=168,\qquad n(\{2\})=154,\qquad n(\{3\})=181,
$$

$$
n(\{4\})=167,\qquad n(\{5\})=160,\qquad n(\{6\})=170.
$$

Hence

$$
\Omega=\{1,2,3,4,5,6\},
$$

and every event is a subset of $\Omega$. For any $A\subseteq\Omega$, the **observed frequency** is defined exactly as in the problem:

$$
f(A)=\frac{n(A)}{1000},
$$

where $n(A)$ is the number of throws in which the event $A$ occurred.

**Consistency of the data.**

$$
168+154+181+167+160+170=1000.
$$

So $N=1000$ throws are accounted for, and all frequencies below are **rational numbers with denominator $1000$**.

---

## Reference table — elementary outcomes

For each face $k$, write $f(\{k\})=\dfrac{n(\{k\})}{1000}$. A decimal approximation is added only for quick reading.

| $k$ | $n(\{k\})$ | $f(\{k\})$ | $\approx$ |
|:---:|:----------:|:----------:|----------:|
| 1 | 168 | $\dfrac{168}{1000}$ | 0.168 |
| 2 | 154 | $\dfrac{154}{1000}$ | 0.154 |
| 3 | 181 | $\dfrac{181}{1000}$ | 0.181 |
| 4 | 167 | $\dfrac{167}{1000}$ | 0.167 |
| 5 | 160 | $\dfrac{160}{1000}$ | 0.160 |
| 6 | 170 | $\dfrac{170}{1000}$ | 0.170 |
| **Σ** | **1000** | $\dfrac{1000}{1000}=1$ | 1 |

---

## Theory used in the solution

| Name | Formal rule |
|------|-------------|
| Disjoint union | If $A\cap B=\emptyset$, then $n(A\cup B)=n(A)+n(B)$ and $f(A\cup B)=f(A)+f(B)$. |
| Partition | Pairwise disjoint $E_i$ with $\bigcup_i E_i=\Omega$ imply $\sum_i n(E_i)=N$ and $\sum_i f(E_i)=1$. |
| Complement | $n(A^c)=N-n(A)$, hence $f(A^c)=1-f(A)$. |
| Inclusion–exclusion | $n(M\cup N)=n(M)+n(N)-n(M\cap N)$. |

---

## Part A — From elementary outcomes to events

**Method (as required).** First compute $n(\cdot)$ by summing the relevant $n(\{k\})$; then

$$
f(\cdot)=\frac{n(\cdot)}{1000}.
$$

The events are labeled $A,\ldots,E$ as in the problem statement.

| # | Event | How $n(\cdot)$ is obtained | $n(\cdot)$ | $f(\cdot)=\dfrac{n(\cdot)}{1000}$ |
|---|------|---------------------------|------------|-----------------------------------|
| 1 | $A=\{2,4,6\}$ | $154+167+170$ | $491$ | $\dfrac{491}{1000}$ |
| 2 | $B=\{1,2,3\}$ | $168+154+181$ | $503$ | $\dfrac{503}{1000}$ |
| 3 | $C=\{5,6\}$ | $160+170$ | $330$ | $\dfrac{330}{1000}=\dfrac{33}{100}$ |
| 4 | $D=\{1,3,5\}$ | $168+181+160$ | $509$ | $\dfrac{509}{1000}$ |
| 5 | $E=\{1,2,3,4\}$ | $168+154+181+167$ | $670$ | $\dfrac{670}{1000}=\dfrac{67}{100}$ |

*(For $C$ and $E$, a cancelled form is shown; the definition $f=n/1000$ always uses denominator $1000$.)*

---

## Part B — How frequencies combine

For each item: **why** the identity is true for counts, then **verification** with explicit fractions.

### B.1 — $f(\{2,4,6\}) = f(\{2\})+f(\{4\})+f(\{6\})$

The sets $\{2\}$, $\{4\}$, $\{6\}$ are pairwise disjoint, so

$$
n(\{2,4,6\})=n(\{2\})+n(\{4\})+n(\{6\}).
$$

Dividing by $1000$ gives the identity for $f$.

**Verification.**

$$
f(\{2,4,6\})=\frac{491}{1000}
=\frac{154}{1000}+\frac{167}{1000}+\frac{170}{1000}
=f(\{2\})+f(\{4\})+f(\{6\}).
$$

---

### B.2 — $f(\{1,2,3,4\}) = f(\{1,2\})+f(\{3,4\})$

The sets $\{1,2\}$ and $\{3,4\}$ are disjoint and their union is $\{1,2,3,4\}$. Hence

$$
n(\{1,2,3,4\})=n(\{1,2\})+n(\{3,4\}),\qquad
n(\{1,2\})=322,\quad n(\{3,4\})=348.
$$

**Verification.**

$$
f(\{1,2,3,4\})=\frac{670}{1000}
=\frac{322}{1000}+\frac{348}{1000}
=f(\{1,2\})+f(\{3,4\}).
$$

---

### B.3 — $f(\{1,3,5\})+f(\{2,4,6\})=1$

Odd and even faces form a **partition** of $\Omega$, so

$$
n(\{1,3,5\})+n(\{2,4,6\})=1000.
$$

**Verification.**

$$
f(\{1,3,5\})+f(\{2,4,6\})
=\frac{509}{1000}+\frac{491}{1000}
=\frac{1000}{1000}=1.
$$

---

### B.4 — $f(\{5,6\})=1-f(\{1,2,3,4\})$

Here $\{5,6\}=\{1,2,3,4\}^c$ in $\Omega$, so $n(\{5,6\})=1000-n(\{1,2,3,4\})$.

**Verification.**

$$
f(\{5,6\})=\frac{330}{1000},
\qquad
1-f(\{1,2,3,4\})=1-\frac{670}{1000}
=\frac{1000-670}{1000}
=\frac{330}{1000}.
$$

---

## Part C — When simple addition works and when it fails

### C.1 — $f(\{1,2\}\cup\{5,6\}) = f(\{1,2\})+f(\{5,6\})$

The sets $\{1,2\}$ and $\{5,6\}$ are disjoint. Therefore

$$
n(\{1,2\}\cup\{5,6\})=n(\{1,2\})+n(\{5,6\})=322+330=652.
$$

**Verification.**

$$
f(\{1,2\}\cup\{5,6\})=\frac{652}{1000}
=\frac{322}{1000}+\frac{330}{1000}
=f(\{1,2\})+f(\{5,6\}).
$$

---

### C.2–C.4 — $M=\{1,2,3\}$, $N=\{3,4,5\}$

**Computed quantities (exact fractions).**

$$
f(M)=\frac{503}{1000},\qquad
f(N)=\frac{508}{1000},\qquad
M\cup N=\{1,2,3,4,5\},\qquad
f(M\cup N)=\frac{830}{1000}=\frac{83}{100}.
$$

Also

$$
f(M)+f(N)=\frac{503}{1000}+\frac{508}{1000}=\frac{1011}{1000}.
$$

Note $\dfrac{1011}{1000}>1$: a frequency cannot exceed $1$, so this sum **cannot** equal $f(M\cup N)$. Indeed

$$
\frac{1011}{1000}\neq\frac{830}{1000}.
$$

**Why $f(M\cup N)\neq f(M)+f(N)$.**  
Here $M\cap N=\{3\}$. The raw sum $n(M)+n(N)$ counts the outcome $3$ **twice**, whereas $n(M\cup N)$ counts each throw once. Inclusion–exclusion gives

$$
n(M\cup N)=n(M)+n(N)-n(M\cap N)=503+508-181=830.
$$

In fractions,

$$
f(M\cup N)=\frac{830}{1000}
=\frac{503}{1000}+\frac{508}{1000}-\frac{181}{1000}
=f(M)+f(N)-f(\{3\}).
$$

**C.4 — Double counting in $f(M)+f(N)$.**  
The only elementary outcome whose contribution is duplicated in the **sum of frequencies** $f(M)+f(N)$ is **$3$** (equivalently, the mass $\dfrac{181}{1000}$ is counted twice in $\dfrac{1011}{1000}$).

---

## Part D — Covering the whole sample space

**D.1 — Sum of singleton frequencies.**

$$
\sum_{k=1}^{6} f(\{k\})
=\frac{168+154+181+167+160+170}{1000}
=\frac{1000}{1000}=1.
$$

**D.2 — Why the result is $1$.**  
The events $\{1\},\ldots,\{6\}$ partition $\Omega$: each throw yields exactly one face, so $\sum_k n(\{k\})=N$ and $\sum_k f(\{k\})=N/N=1$.

**D.3 — Disjoint blocks $\{1,2\}$, $\{3,4\}$, $\{5,6\}$.**

$$
f(\{1,2\})+f(\{3,4\})+f(\{5,6\})
=\frac{322}{1000}+\frac{348}{1000}+\frac{330}{1000}
=\frac{1000}{1000}=1.
$$

**D.4 — Why this sum is $1$.**  
The three blocks are pairwise disjoint and their union is $\Omega$, so the same partition argument as in D.2 applies.

**D.5 — General statement.**  
If $E_1,\ldots,E_m$ are pairwise disjoint and $\bigcup_{i=1}^{m} E_i=\Omega$, then

$$
\sum_{i=1}^{m} f(E_i)=\frac{1}{N}\sum_{i=1}^{m} n(E_i)=\frac{N}{N}=1.
$$

---

## Part E — From observed frequency to probability

Observed frequencies come from **1000 real throws**. A probability assignment $P(A)$ is a mathematical idealization (expected long-run proportion, or another agreed meaning) that should respect the same **algebraic patterns** as $f$.

| # | Desired property of $P$ | Reason suggested by frequencies |
|:---:|:---------------------------|----------------------------------|
| E.1 | Values in $[0,1]$ | $f(A)=n(A)/N$ always satisfies $0\le n(A)\le N$. |
| E.2 | $P(\emptyset)=0$ | $n(\emptyset)=0$, so $f(\emptyset)=0$. |
| E.3 | $P(\Omega)=1$ | $n(\Omega)=N$, so $f(\Omega)=1$. |
| E.4 | Finite additivity on disjoint events | If $A\cap B=\emptyset$, then $n(A\cup B)=n(A)+n(B)$, hence $f(A\cup B)=f(A)+f(B)$. |
| E.5 | $P(A^c)=1-P(A)$ | $n(A^c)=N-n(A)$ implies $f(A^c)=1-f(A)$. |

On finite data, equalities hold only up to rounding or sampling fluctuation; in the axiomatic model, the corresponding properties are required **exactly**.

---

## Part F — Conclusion (three levels)

| # | Level | Connection |
|:---:|:------|:-----------|
| 1 | **Elementary outcomes and events** | $\Omega$ describes one throw; events $A\subseteq\Omega$ encode yes/no questions about the outcome. |
| 2 | **Observed frequencies** | $f(A)=n(A)/1000$ summarizes a **real** experiment; obeys additivity on disjoint pieces, sums to $1$ on partitions, and complementarity. |
| 3 | **Probability as abstraction** | A map $P$ packages the same rules without fixing a single sample; it supports limits, models, and theory beyond one run of 1000 throws. |

**Summary chain:** outcomes $\to$ counts $n(A)$ $\to$ frequencies $f(A)=n(A)/1000$ $\to$ axiomatic probability $P(A)$ with parallel properties.
