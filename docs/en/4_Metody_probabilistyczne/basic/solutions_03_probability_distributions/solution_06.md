# Task 6 — Binomial Model (Defective Parts)

Each part is either **defective** (probability $p$) or **good** (probability $1-p$). Inspections are **independent**, and $p = 0.04$ is the same for each of the **$n = 10$** parts checked. The number of defectives among the 10 follows a **binomial** distribution $\mathrm{Binomial}(10,\,0.04)$.

---

## Model

Let $X$ be the number of defective parts among the $10$ inspected. Then

$$
X \sim \mathrm{Binomial}(n,p) \quad \text{with } n = 10,\quad p = 0.04,
$$

$$
P(X = k) = \binom{10}{k} p^{k} (1-p)^{10-k}, \qquad k = 0,1,\ldots,10.
$$

Here $1-p = 0.96$.

---

## Probability of exactly 2 defective parts

$$
P(X = 2) = \binom{10}{2} (0.04)^{2} (0.96)^{8}.
$$

Now $\displaystyle \binom{10}{2} = \frac{10\cdot 9}{2} = 45$, so

$$
P(X = 2) = 45 \cdot (0.04)^{2} \cdot (0.96)^{8}.
$$

Numerically (calculator):

- $(0.04)^{2} = 0.0016$,
- $(0.96)^{8} \approx 0.72139$,
- $P(X = 2) \approx 45 \cdot 0.0016 \cdot 0.72139 \approx \mathbf{0.0519}$.

So about **$5.2\%$** (more precisely $\approx 0.05194$).

---

## Probability of at least one defective part

“At least one defective” is the event $\{X \ge 1\}$. The complement is “no defectives,” $\{X = 0\}$:

$$
P(X \ge 1) = 1 - P(X = 0) = 1 - (1-p)^{n} = 1 - (0.96)^{10}.
$$

Now $(0.96)^{10} \approx 0.66483$, hence

$$
P(X \ge 1) \approx 1 - 0.66483 = \mathbf{0.33517}.
$$

So about **$33.5\%$**.

*(Equivalently: $P(X \ge 1) = 1 - \binom{10}{0} p^{0}(1-p)^{10} = 1 - 0.96^{10}$.)*

---

## Final result

| Quantity | Expression | Approximate value |
|----------|------------|-------------------|
| $P(X = 2)$ | $\binom{10}{2}(0.04)^{2}(0.96)^{8}$ | $\approx 0.0519$ |
| $P(X \ge 1)$ | $1 - (0.96)^{10}$ | $\approx 0.335$ |

---

## Quick sanity checks

1. **$P(X \ge 1)$** is between $P(X=1)$ and $1$; it must exceed $P(X=2)$ alone — here $0.335 \gg 0.052$, consistent.  
2. **Mean** $\mathbb{E}[X] = np = 10 \cdot 0.04 = 0.4$; expecting exactly $2$ defectives is possible but not the most likely single value (the mode is near $0$ for small $p$).  
3. **$P(X=0)$** dominates when $p$ is small: $(0.96)^{10} \approx 0.665$, so “no defectives” is still the most probable **single** count among $k=0,1,\ldots$.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $10 \cdot 0.04 = 0.4$ as $P(X=2)$ | That is the **expected** count, not a probability. |
| Confusing $P(X \ge 1)$ with $10 \cdot 0.04$ | Overlap of events is not additive; use **complement** $1 - P(X=0)$. |
| Forgetting independence | The binomial formula assumes **independent** Bernoulli trials. |
