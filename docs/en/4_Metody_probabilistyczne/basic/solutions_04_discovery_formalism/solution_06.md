# Problem 6 — Final discussion: the axiomatic point of view

The following discussion ties together **events**, **frequencies**, and **Kolmogorov’s axioms**, and explains why **countable additivity** is a further step beyond finite experiments.

---

## 1. What an axiomatic probability space is

| Object | Role |
|--------|------|
| **Sample space** $\Omega$ | Set of all possible “elementary outcomes” of a model (abstract or concrete). |
| **Events** $\mathcal{F}$ | A collection of subsets of $\Omega$ designated as measurable (a **$\sigma$-algebra** in full theory). |
| **Probability** $P$ | A function $P: \mathcal{F} \to [0,1]$ satisfying the **Kolmogorov axioms** below. |

The axioms do **not** say how to *compute* $P$ for a real die or coin — they say which **algebraic rules** any acceptable assignment must obey.

---

## 2. The Kolmogorov axioms (stated)

Let $(\Omega, \mathcal{F}, P)$ be a probability space.

| Axiom | Statement | Common name |
|-------|-----------|----------------|
| **K1** | For every $A \in \mathcal{F}$, $P(A) \ge 0$. | **Non-negativity** |
| **K2** | $P(\Omega) = 1$. | **Normalization** |
| **K3** | If $A_1, A_2, \ldots \in \mathcal{F}$ are **pairwise disjoint**, then $P\big(\bigcup_{i=1}^{\infty} A_i\big) = \sum_{i=1}^{\infty} P(A_i)$. | **Countable additivity** |

**Finite additivity** is the special case of K3 when only finitely many $A_i$ are non-empty (the rest are $\emptyset$, with $P(\emptyset)=0$, which follows from K1–K3).

---

## 3. What already appeared in the finite problems (1–5)

| Axiom / consequence | Where it came from (intuition) |
|---------------------|--------------------------------|
| **K1** | Frequencies $f(A)=n(A)/N$ are never negative; $P(A)$ is required to behave like a **proportion**. |
| **K2** | Every trial lands **somewhere** in $\Omega$; $f(\Omega)=1$. |
| **Finite additivity for disjoint events** | If $A\cap B=\emptyset$, then $n(A\cup B)=n(A)+n(B)$ — the heart of Problem 5, Parts B–D. |
| **$P(A^c)=1-P(A)$** | From normalization + disjointness of $A$ and $A^c$ (when the model assigns probability only to measurable pieces that partition $\Omega$). |

So: **non-negativity**, **normalization**, and **adding probabilities of disjoint pieces** are exactly what **finite counting** of outcomes suggests.

---

## 4. Why countable additivity is more subtle

| Finite experiments | Countable additivity |
|--------------------|----------------------|
| A finite experiment has **finitely many** trials $N$; Problems 1–5 partition $\Omega$ into **finitely many** cells. | K3 allows **infinitely many** disjoint pieces $A_1,A_2,\ldots$ in one formula. |
| Adding $n(A)+n(B)$ is **finite arithmetic**. | $\sum_{i=1}^{\infty} P(A_i)$ is an **infinite series** — convergence and order of terms matter for general series (here all terms are $\ge 0$, so life is easier). |
| No experiment lists “infinitely many disjoint rare events” in one table. | Needed for **rigorous limit theorems**, continuous models (e.g. $[0,1]$), and avoiding pathological set-theoretic issues when $\mathcal{F}$ is rich. |

**In plain words:** finite data justify **“if two events don’t overlap, add their proportions.”** Passing to **countably many** disjoint events is a **deliberate modeling choice**: it locks in continuity properties of $P$ that finite frequency tables **never directly display**, but that are needed when $\Omega$ is infinite or when limits are taken.

---

## 5. What goes beyond “count throws and divide”

| Theme | Comment |
|-------|---------|
| **$\sigma$-algebra** | Not every subset of a continuous $\Omega$ can be assigned a length-like probability without contradiction (Banach–Tarski-type issues); $\mathcal{F}$ specifies **measurable** events. |
| **Geometric / continuous probability** | On $[0,1]$, “probability = length” for intervals extends to a unique $P$ on a standard $\mathcal{F}$ — **not** visible from a single finite histogram alone. |
| **Long-run frequency interpretation** | Suggests **finite** additivity strongly; **countable** additivity is the axiom that makes the **mathematical** theory of limits (LLN, CLT) work cleanly. |

---

## 6. Closing picture

**Problems 1–5** trained: outcomes as points, events as sets, **AND/OR/NOT** as $\cap,\cup,{}^c$, and frequencies obeying **disjoint additivity** and **complements** on finite $\Omega$.

**Kolmogorov’s program** keeps that structure and adds: work on a precise class of events $\mathcal{F}$, and require **countable** disjoint additivity so that **infinite** decompositions and **limit** arguments are well-defined.

**Countable additivity** is therefore **not** something that appears directly in 1000 die rolls — it is the **axiom** that aligns finite intuition with a **complete** measure-theoretic framework for probability.
