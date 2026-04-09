# Task 7 — Hypergeometric Model (Light Bulbs)

The box has **$12$** working bulbs and **$3$** defective bulbs, so **$N = 15$** in total. **$5$** bulbs are drawn **without replacement**. The number $X$ of defective bulbs in the sample follows a **hypergeometric** law with parameters $(N,K,n) = (15,\,3,\,5)$.

---

## Model

Let $X$ = number of defective bulbs among the $5$ drawn. Then $X$ can take values $\max(0,\, n-(N-K)) \le X \le \min(n,\,K)$:

$$
\min(5,3) = 3, \qquad n - (N-K) = 5 - 12 = -7 \Rightarrow X \in \{0,1,2,3\}.
$$

The hypergeometric probability mass function is

$$
P(X = k) = \frac{\displaystyle \binom{K}{k}\binom{N-K}{\,n-k\,}}{\displaystyle \binom{N}{n}}, \qquad k = 0,1,\ldots,\min(n,K).
$$

Here $K = 3$ (defectives), $N-K = 12$ (working), $n = 5$.

---

## Probability of exactly 2 defective bulbs

Set $k = 2$. Then $n-k = 3$ working bulbs must be chosen from $12$:

$$
P(X = 2) = \frac{\displaystyle \binom{3}{2}\binom{12}{3}}{\displaystyle \binom{15}{5}}.
$$

**Factorials / binomials:**

$$
\binom{3}{2} = 3, \qquad \binom{12}{3} = \frac{12\cdot 11\cdot 10}{3\cdot 2\cdot 1} = 220.
$$

$$
\binom{15}{5} = \frac{15\cdot 14\cdot 13\cdot 12\cdot 11}{5\cdot 4\cdot 3\cdot 2\cdot 1} = 3003.
$$

So

$$
P(X = 2) = \frac{3 \cdot 220}{3003} = \frac{660}{3003}.
$$

Simplify: divide numerator and denominator by $3$:

$$
\frac{660}{3003} = \frac{220}{1001}.
$$

Divide by $\gcd(220,1001)=11$:

$$
\frac{220}{1001} = \frac{20}{91}.
$$

**Decimal:** $\displaystyle \frac{20}{91} \approx 0.21978$ (about **$22.0\%$**).

---

## Final result

$$
\boxed{P(X = 2) = \frac{\binom{3}{2}\binom{12}{3}}{\binom{15}{5}} = \frac{20}{91} \approx 0.220 }.
$$

---

## Quick sanity checks

1. **$P(X=2)$** is between $0$ and $1$; with only $3$ defectives in the box, $P(X=3)$ is also possible but smaller than $P(X=2)$ in typical balances — here $\binom{3}{3}\binom{12}{2}/3003 = 66/3003 \approx 0.022$.  
2. **Mean** $\mathbb{E}[X] = n \cdot (K/N) = 5 \cdot (3/15) = 1$; observing $2$ defectives is plausible.  
3. **Replacing without replacement** by a binomial $\mathrm{Binomial}(5,\,3/15)$ would be only an approximation; the problem requires the exact hypergeometric formula.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $\binom{5}{2} p^{2}(1-p)^{3}$ with $p = 3/15$ | That is **binomial** (sampling **with** replacement or independent trials), not drawing without replacement from a finite box. |
| Using $\binom{3}{2}$ without $\binom{12}{3}$ | The sample must contain **both** defectives **and** enough working bulbs to fill the sample of $5$. |
| Wrong $N$ | Total bulbs are $12+3=15$, not $12$. |
