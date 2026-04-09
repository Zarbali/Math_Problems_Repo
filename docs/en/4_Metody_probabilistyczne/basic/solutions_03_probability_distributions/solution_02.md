# Task 2 — Hypergeometric Model (Sampling from a Batch)

A finite batch contains known numbers of defective and functional components. A **simple random sample without replacement** is drawn: each subset of a fixed size is equally likely. This is the standard setup for the **hypergeometric** distribution — unlike the binomial model, successive draws are **not** independent because the composition of the remaining batch changes.

---

## Setting and notation

| Symbol | Meaning |
|--------|---------|
| $N$ | Population size (total components), here $N = 20$ |
| $K$ | Number of **defective** items in the batch, here $K = 5$ |
| $N-K$ | Number of **functional** items, here $15$ |
| $n$ | Sample size (drawn without replacement), here $n = 4$ |
| $X$ | Number of defective items in the sample |

All unordered samples of size $n$ from $N$ distinct items are equally likely (simple random sampling).

---

## 1. Description of the random experiment

The experiment consists of **one** act of sampling:

- From $N = 20$ distinguishable components ($5$ defective, $15$ functional), **exactly $n = 4$** are selected **without replacement**.
- “Without replacement” means: no component appears twice in the sample; after each conceptual draw the remaining pool shrinks (equivalently: choose a subset of $4$ distinct items uniformly at random from all $\binom{20}{4}$ subsets).

This is **not** a sequence of four independent Bernoulli trials: the probability that the next draw is defective **depends** on what was already drawn. The correct model for the count of defectives is **hypergeometric**, not binomial.

---

## 2. Random variable $X$

Define

$$
X = \text{the number of defective components among the $4$ selected}.
$$

So $X$ is a function of the random sample: it counts how many of the $4$ positions are filled by items from the defective subpopulation of size $K$.

---

## 3. Possible values of $X$

The sample contains $4$ items. It cannot contain more defectives than exist in the batch or than places in the sample:

$$
0 \le X \le \min(n,\, K) = \min(4,\, 5) = 4.
$$

It also cannot contain more defectives than the sample size, and cannot force more functional items than available: the number of functionals in the sample is $n-X$, and we need $n-X \le N-K$, i.e. $X \ge n - (N-K) = 4 - 15 = -11$, which is automatic, and $X \ge 0$.

Thus the **support** of $X$ is

$$
X \in \{0,\, 1,\, 2,\, 3,\, 4\}.
$$

(Every integer from $0$ to $4$ is achievable: there are enough functional items to fill the sample when $X$ is small, and enough defectives when $X \le 4$.)

---

## 4. Probability distribution of $X$

### 4.1 General hypergeometric formula

Among all $\binom{N}{n}$ equally likely samples, the event $\{X = k\}$ occurs exactly when the sample contains $k$ defectives and $n-k$ functionals. Choosing such a sample means:

- choose $k$ defectives from $K$: $\binom{K}{k}$ ways;
- choose $n-k$ functionals from $N-K$: $\binom{N-K}{\,n-k\,}$ ways.

Hence

$$
P(X = k) = \frac{\displaystyle \binom{K}{k}\binom{N-K}{\,n-k\,}}{\displaystyle \binom{N}{n}},
$$

for integers $k$ for which all binomial coefficients are defined (nonzero), i.e. $\max(0,\, n-(N-K)) \le k \le \min(n,\, K)$.

Here $N=20$, $K=5$, $n=4$:

$$
P(X = k) = \frac{\displaystyle \binom{5}{k}\binom{15}{\,4-k\,}}{\displaystyle \binom{20}{4}}, \qquad k = 0,1,2,3,4.
$$

### 4.2 Total number of samples

$$
\binom{20}{4} = \frac{20\cdot 19\cdot 18\cdot 17}{4\cdot 3\cdot 2\cdot 1} = 4845.
$$

### 4.3 Probabilities (exact and approximate)

| $k$ | $\binom{5}{k}\binom{15}{4-k}$ | $P(X=k)$ (exact) | $\approx$ |
|:---:|:-----------------------------:|:-----------------|:----------|
| $0$ | $1 \cdot 1365 = 1365$ | $\dfrac{1365}{4845} = \dfrac{91}{323}$ | $0.282$ |
| $1$ | $5 \cdot 455 = 2275$ | $\dfrac{2275}{4845} = \dfrac{455}{969}$ | $0.470$ |
| $2$ | $10 \cdot 105 = 1050$ | $\dfrac{1050}{4845} = \dfrac{70}{323}$ | $0.217$ |
| $3$ | $10 \cdot 15 = 150$ | $\dfrac{150}{4845} = \dfrac{10}{323}$ | $0.031$ |
| $4$ | $5 \cdot 1 = 5$ | $\dfrac{5}{4845} = \dfrac{1}{969}$ | $0.001$ |

**Check:** $1365 + 2275 + 1050 + 150 + 5 = 4845$, so the probabilities sum to $1$.

---

## 5. What does “success” mean here?

In sampling models, **success** usually denotes the outcome type that is **counted** by the random variable of interest.

Here $X$ counts **defective** components. A natural convention is:

$$
\boxed{\text{Success} = \text{drawing a defective item in a single draw}}
$$

when one describes the underlying dichotomy (defective vs functional). The hypergeometric law then describes the total number of “successes” in $n$ draws without replacement from a population with $K$ success-type items.

Alternatively, one could label functional items as “success” for a different problem; then the count of interest would be $n-X$ and the same hypergeometric structure would apply with the roles of $K$ and $N-K$ swapped. The problem fixes attention on **defectives in the sample**, so aligning “success” with **defective** matches $X$ as defined.

---

## Final result

- **Experiment:** choose a uniform random subset of $4$ components from $20$ without replacement ($5$ defective, $15$ functional).  
- **$X$:** number of defectives in that sample; $X \in \{0,1,2,3,4\}$.  
- **Distribution:** $P(X=k) = \binom{5}{k}\binom{15}{4-k}\big/\binom{20}{4}$ (hypergeometric).  
- **Success (conventional):** a defective item, so $X$ counts successes in the sampling-without-replacement sense.

---

## Quick sanity checks

1. **Symmetry of roles:** $P(X=k)$ uses $\binom{K}{k}\binom{N-K}{n-k}$ — defective and functional enter symmetrically in the combinatorial structure.  
2. **Extreme batches:** if $K < n$, the upper bound on $X$ would be $K$ instead of $n$; here $K=5 \ge 4$, so $X=4$ is possible.  
3. **Large-$N$ intuition:** if $N$ were huge compared to $n$, sampling with vs without replacement would be close; here $n=4$ and $N=20$ are comparable, so the hypergeometric correction matters.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $\mathrm{Binomial}(n,\, K/N)$ for $X$ | Ignores **without replacement**; trials are dependent. |
| Allowing $X > 4$ or impossible $k$ | Must satisfy $k \le \min(n,K)$ and $n-k \le N-K$. |
| Forgetting the denominator $\binom{N}{n}$ | Probabilities must be normalized over **all** samples of size $n$. |
