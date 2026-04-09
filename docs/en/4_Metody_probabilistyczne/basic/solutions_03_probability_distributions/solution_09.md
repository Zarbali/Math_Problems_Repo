# Task 9 — Poisson Model (Customer Requests)

The center receives on average **$5$ requests per hour**. For a **one-hour** window, model the number of requests $X$ by a **Poisson** distribution with parameter

$$
\lambda = 5,
$$

the expected number of requests in that hour (rate $\times$ duration: $5/\text{hour} \times 1\,\text{hour}$).

---

## Probability mass function

For $X \sim \mathrm{Poisson}(\lambda)$,

$$
P(X = k) = \frac{e^{-\lambda}\, \lambda^{k}}{k!}, \qquad k = 0,1,2,\ldots
$$

---

## 1. Exactly 3 requests in one hour

Set $k = 3$ and $\lambda = 5$:

$$
P(X = 3) = \frac{e^{-5}\, 5^{3}}{3!} = \frac{e^{-5} \cdot 125}{6}.
$$

Numerically: $e^{-5} \approx 0.0067379$, so

$$
P(X = 3) \approx \frac{0.0067379 \cdot 125}{6} \approx \mathbf{0.1404}.
$$

So about **$14.0\%$** (more precisely $\approx 0.14037$).

---

## 2. At least one request in one hour

$$
P(X \ge 1) = 1 - P(X = 0) = 1 - e^{-\lambda} = 1 - e^{-5}.
$$

Since $e^{-5} \approx 0.0067379$,

$$
P(X \ge 1) \approx 1 - 0.0067379 = \mathbf{0.99326}.
$$

So about **$99.3\%$**.

---

## Final result

| Quantity | Formula | Approximate value |
|----------|---------|-------------------|
| $P(X = 3)$ | $e^{-5} \cdot 5^{3} / 3!$ | $\approx 0.140$ |
| $P(X \ge 1)$ | $1 - e^{-5}$ | $\approx 0.993$ |

---

## Quick sanity checks

1. **$\mathbb{E}[X] = \lambda = 5$** — observing exactly $3$ is below the mean, so probability is moderate, not maximal at $k=5$ (mode near $\lfloor\lambda\rfloor$).  
2. **$P(X \ge 1)$** is very close to $1$ because $P(X=0)=e^{-5}$ is tiny.  
3. **$\sum_{k=0}^{\infty} P(X=k) = 1$** — Poisson is a proper distribution on $\mathbb{N}_0$.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $\lambda = 5$ for a **half-hour** without scaling | If the interval length changes, $\lambda$ scales (e.g. $2.5$ for half an hour at $5/\text{hour}$). |
| Writing $P(X=3) = 5^{3}/3!$ without $e^{-5}$ | The Poisson pmf always includes the factor $e^{-\lambda}$. |
| Confusing $P(X \ge 1)$ with $5 \cdot P(X=1)$ | Use $1 - P(X=0)$ or sum $P(X=k)$ for $k \ge 1$. |
