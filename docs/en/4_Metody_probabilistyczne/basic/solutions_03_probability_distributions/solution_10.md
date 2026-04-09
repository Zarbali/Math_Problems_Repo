# Task 10 — Multinomial Model (Candy Flavors)

Each selection is **independent** and the box composition is unchanged because draws are **with replacement**. On a single draw:

- strawberry (S): $p_{1} = 0.4$  
- lemon (L): $p_{2} = 0.35$  
- mint (M): $p_{3} = 0.25$

Check: $0.4 + 0.35 + 0.25 = 1$.

There are **$n = 6$** trials. Let $(N_{1}, N_{2}, N_{3})$ be the counts of strawberry, lemon, and mint in those six draws. Then

$$
(N_{1}, N_{2}, N_{3}) \sim \mathrm{Multinomial}\bigl(n;\, p_{1}, p_{2}, p_{3}\bigr).
$$

---

## Required probability

We want $N_{1} = 3$, $N_{2} = 2$, $N_{3} = 1$ (note $3+2+1=6=n$).

The multinomial pmf gives

$$
P(N_{1}=3,\, N_{2}=2,\, N_{3}=1) = \frac{n!}{n_{1}!\, n_{2}!\, n_{3}!}\, p_{1}^{n_{1}} p_{2}^{n_{2}} p_{3}^{n_{3}}
$$

$$
= \frac{6!}{3!\, 2!\, 1!}\, (0.4)^{3}\, (0.35)^{2}\, (0.25)^{1}.
$$

**Multinomial coefficient:**

$$
\frac{6!}{3!\, 2!\, 1!} = \frac{720}{6 \cdot 2 \cdot 1} = 60.
$$

So

$$
P = 60 \cdot (0.4)^{3} \cdot (0.35)^{2} \cdot 0.25.
$$

Compute step by step:

- $(0.4)^{3} = 0.064$  
- $(0.35)^{2} = 0.1225$  
- $0.064 \cdot 0.1225 = 0.00784$  
- $0.00784 \cdot 0.25 = 0.00196$  
- $P = 60 \cdot 0.00196 = \mathbf{0.1176}$.

So about **$11.76\%$**.

---

## Final result

$$
\boxed{
P(N_{1}=3,\, N_{2}=2,\, N_{3}=1)
= \frac{6!}{3!\,2!\,1!}\,(0.4)^{3}(0.35)^{2}(0.25)
= 0.1176
}
$$

---

## Quick sanity checks

1. **Orderings:** $60$ is the number of distinct sequences of six letters with three S, two L, one M (permutations of a multiset).  
2. **Product of probabilities:** $(0.4)^{3}(0.35)^{2}(0.25)$ is the probability of **one** fixed order (e.g. SSSLLM); multiplying by $60$ sums over all orders.  
3. **Sum over all $(n_{1},n_{2},n_{3})$ with $n_{1}+n_{2}+n_{3}=6$** equals $1$ — multinomial theorem: $(p_{1}+p_{2}+p_{3})^{6}=1$.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $\binom{6}{3}(0.4)^{3}(0.6)^{3}$ | That is **binomial** for “strawberry vs not strawberry”; it ignores the split between lemon and mint. |
| Omitting $6!/(3!2!1!)$ | Without the multinomial coefficient, only **one** ordering of outcomes is counted. |
| Sampling **without** replacement from a finite box | The problem states **with replacement**, so category probabilities stay $0.4,\,0.35,\,0.25$ each trial. |
