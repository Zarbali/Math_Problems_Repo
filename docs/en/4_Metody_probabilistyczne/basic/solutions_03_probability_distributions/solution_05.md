# Task 5 — Multinomial Model (Categories of Outcomes)

A fair die is rolled **5 times**; each roll is classified into one of **three** categories (small 1–2, medium 3–4, large 5–6), each category having probability **$1/3$** on a single roll. Rolls are independent. This is the standard setup for a **multinomial** distribution with $n=5$ trials and $r=3$ outcome types with equal probabilities.

---

## Setting and notation

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of rolls (trials), here $n = 5$ |
| $r$ | Number of categories, here $r = 3$ |
| $p_{1}, p_{2}, p_{3}$ | Probabilities of small / medium / large on **one** roll; here $p_{1}=p_{2}=p_{3}=1/3$ |
| $(N_{1}, N_{2}, N_{3})$ | Counts: how many of the $5$ rolls fall in category $1$, $2$, $3$ |

On each roll, exactly one category occurs, so $p_{1}+p_{2}+p_{3}=1$.

---

## 1. Description of the random experiment

The experiment consists of **five independent** repetitions of the same random trial:

- **Trial:** roll a fair six-sided die once.  
- **Outcome of interest:** not only the face $1,\ldots,6$, but its **category** — small ($1$ or $2$), medium ($3$ or $4$), or large ($5$ or $6$).  
- Each category has two faces out of six, so $P(\text{small}) = P(\text{medium}) = P(\text{large}) = 2/6 = 1/3$.  
- The five rolls do not affect each other (**independence**).

The **multinomial** model describes the **joint distribution of the three counts** $(N_{1}, N_{2}, N_{3})$ over the five rolls.

---

## 2. Sample space $\Omega$

Two levels are useful.

### 2.1 Fine outcomes (every face visible)

Each roll has a face in $\{1,2,3,4,5,6\}$. An outcome of the full experiment is a **5-tuple**

$$
\omega = (\omega_{1},\omega_{2},\omega_{3},\omega_{4},\omega_{5}), \qquad \omega_{i} \in \{1,\ldots,6\}.
$$

So

$$
\Omega_{\text{full}} = \{1,\ldots,6\}^{5}, \qquad |\Omega_{\text{full}}| = 6^{5} = 7776.
$$

This is the sample space if elementary outcomes are **all** sequences of five faces.

### 2.2 Category counts (multinomial state)

For the multinomial law, the random **vector** is $(N_{1}, N_{2}, N_{3})$ with

$$
N_{1} + N_{2} + N_{3} = 5, \qquad N_{j} \in \{0,1,\ldots,5\}.
$$

The **support** of the multinomial vector is

$$
\bigl\{ (n_{1},n_{2},n_{3}) \in \mathbb{N}_{0}^{3} : n_{1}+n_{2}+n_{3} = 5 \bigr\}.
$$

This set has $\binom{5+3-1}{5} = \binom{7}{5} = 21$ triples (stars-and-bars count of nonnegative integer solutions).

---

## 3. Multinomial distribution

Let $(N_{1}, N_{2}, N_{3})$ be the counts of rolls in the three categories. Under **independent** trials with category probabilities $p_{1}, p_{2}, p_{3}$,

$$
P(N_{1}=n_{1},\, N_{2}=n_{2},\, N_{3}=n_{3}) = \frac{n!}{n_{1}!\, n_{2}!\, n_{3}!}\, p_{1}^{n_{1}} p_{2}^{n_{2}} p_{3}^{n_{3}},
$$

whenever $n_{1}+n_{2}+n_{3}=n$ and $n_{j}\ge 0$; otherwise the probability is $0$.

Here $n=5$ and $p_{1}=p_{2}=p_{3}=1/3$, so

$$
P(N_{1}=n_{1},\, N_{2}=n_{2},\, N_{3}=n_{3}) = \frac{5!}{n_{1}!\, n_{2}!\, n_{3}!}\left(\frac{1}{3}\right)^{5}, \qquad n_{1}+n_{2}+n_{3}=5.
$$

**Note:** the factor $(1/3)^{5} = (1/3)^{n_{1}+n_{2}+n_{3}}$ is constant over all such triples; only the multinomial coefficient $\dfrac{5!}{n_{1}!\,n_{2}!\,n_{3}!}$ changes with $(n_{1},n_{2},n_{3})$.

**Sum to one:** summing over all $21$ triples gives $1$ (multinomial theorem expansion of $(p_{1}+p_{2}+p_{3})^{5}=1^{5}=1$).

---

## 4. Interpretation of the parameters

| Parameter | Role |
|-----------|------|
| $n$ | **Number of independent trials** (here rolls). Each trial contributes exactly one count to the category in which it falls. |
| $r$ (here $3$) | **Number of categories** (types of outcome). |
| $(p_{1}, p_{2}, p_{3})$ | **Category probabilities** on a **single** trial. They must be nonnegative and sum to $1$. Here they are **equal** ($1/3$ each), so each category is symmetric in the formula. |

**Marginals:** for each $j$, $N_{j} \sim \mathrm{Binomial}(n,p_{j})$ (e.g. $N_{1} \sim \mathrm{Binomial}(5,\,1/3)$), but $N_{1},N_{2},N_{3}$ are **not** independent because $N_{1}+N_{2}+N_{3}=5$.

---

## Final result

- **Experiment:** five independent die rolls; each roll is labeled small / medium / large with probabilities $1/3$ each.  
- **$\Omega$ (fine):** $6^{5}$ sequences of faces; **$\Omega$ (counts):** triples $(n_{1},n_{2},n_{3})$ of nonnegative integers with $n_{1}+n_{2}+n_{3}=5$.  
- **Distribution:** $P(N_{1}=n_{1},N_{2}=n_{2},N_{3}=n_{3}) = \dfrac{5!}{n_{1}!n_{2}!n_{3}!}(1/3)^{5}$ on that support.  
- **Parameters:** $n=5$ trials; $r=3$ categories; $(p_{1},p_{2},p_{3})=(1/3,1/3,1/3)$.

---

## Quick sanity checks

1. **Binomial special case:** if only two categories mattered, the multinomial would reduce to a **binomial** for one of the counts.  
2. **Equal $p_{j}$:** when $p_{1}=p_{2}=p_{3}$, the formula is symmetric in permutations of $(n_{1},n_{2},n_{3})$.  
3. **$\mathbb{E}[N_{j}] = n p_{j}$:** here $\mathbb{E}[N_{j}] = 5/3$ for each $j$.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Using $\binom{5}{n_{1}} p_{1}^{n_{1}}(1-p_{1})^{5-n_{1}}$ for $N_{1}$ alone as if the other categories did not matter | That ignores the **three-way** structure; the **joint** law is multinomial. |
| Forgetting $n_{1}+n_{2}+n_{3}=n$ | The three counts are **linked**; they cannot vary independently. |
| Claiming $N_{1},N_{2},N_{3}$ are independent | They sum to $5$; they are **dependent** (multinomial vs product of binomials). |
