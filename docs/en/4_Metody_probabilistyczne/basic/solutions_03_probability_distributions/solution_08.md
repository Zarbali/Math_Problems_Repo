# Task 8 — Geometric Model (Compilation Errors)

Each compilation fails with an error with probability **$p = 0.1$** and succeeds (no error) with probability **$1-p = 0.9$**. Compilations are **independent**. The programmer stops the mental experiment at the **first** error; let **$T$** be the index of the compilation on which that **first** error appears. Then $T$ has a **geometric** distribution on $\{1,2,3,\ldots\}$ with “success” = error on a trial:

$$
P(T = k) = (1-p)^{k-1} p, \qquad k = 1,2,\ldots
$$

---

## 1. First error on the 4th compilation

The first error occurs on compilation $4$ if and only if the first **three** compilations have **no** error and the **fourth** has an error:

$$
P(T = 4) = (1-p)^{3} p = (0.9)^{3} \cdot 0.1.
$$

Compute:

$$
(0.9)^{3} = 0.729, \qquad P(T = 4) = 0.729 \cdot 0.1 = \mathbf{0.0729}.
$$

So **$7.29\%$**.

---

## 2. First error no later than the 3rd compilation

The event $\{T \le 3\}$ means the first error is on compilation $1$, $2$, or $3$.

**Direct sum:**

$$
P(T \le 3) = P(T=1) + P(T=2) + P(T=3) = p + (1-p)p + (1-p)^{2}p.
$$

With $p = 0.1$:

$$
P(T=1) = 0.1, \quad P(T=2) = 0.9 \cdot 0.1 = 0.09, \quad P(T=3) = 0.9^{2} \cdot 0.1 = 0.081,
$$

$$
P(T \le 3) = 0.1 + 0.09 + 0.081 = \mathbf{0.271}.
$$

**Complement (often faster):** $\{T \le 3\}$ is the complement of $\{T > 3\}$. The event $\{T > 3\}$ means **no** error in the first three compilations:

$$
P(T > 3) = (1-p)^{3} = (0.9)^{3} = 0.729,
$$

$$
P(T \le 3) = 1 - 0.729 = \mathbf{0.271}.
$$

So **$27.1\%$**.

---

## Final result

| Quantity | Expression | Value |
|----------|------------|--------|
| $P(T = 4)$ | $(0.9)^{3} \cdot 0.1$ | $0.0729$ |
| $P(T \le 3)$ | $1 - (0.9)^{3}$ | $0.271$ |

---

## Quick sanity checks

1. **$P(T=4) < P(T=1)$** because waiting until the 4th trial requires three “failures” (no error) in a row: $(0.9)^3 p < p$.  
2. **$P(T \le 3)$** is the cdf of the geometric at $3$: $1 - (1-p)^{3}$.  
3. **$\mathbb{E}[T] = 1/p = 10$** on average — many compilations before the first error if $p$ is small.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $P(T=4) = (0.1)^{4}$ or $\binom{4}{1}(0.1)(\cdots)$ | The geometric law is **not** “four independent errors”; it is **one** first error at position $4$. |
| Computing $P(T \le 3)$ as $3 \cdot 0.1$ | Events $\{T=1\},\{T=2\},\{T=3\}$ are **disjoint**, but probabilities are not equal — use sum or $1-(0.9)^3$. |
| Confusing “success” with “no error” | Here **success** in the geometric sense is **error** (probability $p$ per trial), matching the problem. |
