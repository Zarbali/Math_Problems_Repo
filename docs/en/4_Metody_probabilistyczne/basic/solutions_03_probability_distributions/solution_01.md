# Task 1 — Binomial Model (Quality Control)

A factory inspects screws one after another. Each trial has two outcomes; probability $p$ of a defect is fixed and trials do not influence each other. Below we fix notation once, then answer all four sub-questions, and finally connect the **eight elementary outcomes** to the **binomial law** for the number of defects.

---

## Setting and notation

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of trials (here $n = 3$) |
| $G$ | “Good” screw |
| $D$ | “Defective” screw |
| $p$ | $P(D)$ on a single trial, $p \in [0,1]$ |
| $q$ | $P(G) = 1-p$ (often convenient to write $q = 1-p$) |
| $\omega_{i}$ | Outcome of trial $i$; $\omega_{i} \in \{G,\, D\}$ |

**Assumptions (given in the problem):**

$$
P(\omega_{i} = D) = p, \qquad P(\omega_{i} = G) = 1-p .
$$

For distinct trials with $i \neq j$, events that depend only on $\omega_{i}$ and on $\omega_{j}$ are **independent**. Equivalently, the joint probability of any pattern equals the **product** of the three one-trial probabilities.

---

## 1. What is the random experiment?

We observe a **sequence of three independent Bernoulli trials**:

- Trial $i$ = inspection of the $i$-th screw in the sequence.  
- Each trial has sample space $\{G,\, D\}$ with probabilities $1-p$ and $p$ as above.  
- The **compound experiment** is the triple $(\omega_{1},\omega_{2},\omega_{3})$.

Formally, this is a **Bernoulli scheme** of length $n=3$ with “failure/success” coding fixed in **Section 4** below. The model is the standard setup for a **binomial** count when we later define “success” as a defective item and aggregate the three trials.

---

## 2. Sample space $\Omega$

Elementary outcomes are **ordered** triples (order = which screw in the sequence), so

$$
\Omega = \{G,\, D\}^3 = \bigl\{ (\omega_{1},\omega_{2},\omega_{3}) \mid \omega_{k} \in \{G,\, D\},\ k \in \{1,2,3\} \bigr\}.
$$

Listing all elements:

$$
\Omega = \{\, GGG,\, GGD,\, GDG,\, DGG,\, GDD,\, DGD,\, DDG,\, DDD \,\}.
$$

**Cardinality:**

$$
|\Omega| = 2^n = 2^3 = 8.
$$

Different orders are **different** outcomes: e.g. $GGD \neq GDG$ because the defective screw is the third vs the second in the line.

---

## 3. Probabilities of every elementary outcome

### 3.1 Independence → product rule

Write an elementary outcome as a single symbol $\omega = (\omega_{1},\omega_{2},\omega_{3})$, with $\omega \in \Omega$. For each such $\omega$,

$$
P(\{\omega\}) = P_{1}(\omega_{1})\, P_{1}(\omega_{2})\, P_{1}(\omega_{3}),
$$

where $P_{1}(G)=1-p$ and $P_{1}(D)=p$. So each **specific** sequence with exactly $k$ defects and $(3-k)$ good screws has probability

$$
p^k (1-p)^{3-k}.
$$

### 3.2 All eight probabilities in closed form

Writing $q = 1-p$:

| Outcome | Factorization | Probability |
|---------|-----------------|---------------|
| $GGG$ | $q\cdot q\cdot q$ | $q^3 = (1-p)^3$ |
| $GGD$ | $q\cdot q\cdot p$ | $p q^2 = p(1-p)^2$ |
| $GDG$ | $q\cdot p\cdot q$ | $p q^2$ |
| $DGG$ | $p\cdot q\cdot q$ | $p q^2$ |
| $GDD$ | $q\cdot p\cdot p$ | $p^2 q = p^2(1-p)$ |
| $DGD$ | $p\cdot q\cdot p$ | $p^2 q$ |
| $DDG$ | $p\cdot p\cdot q$ | $p^2 q$ |
| $DDD$ | $p\cdot p\cdot p$ | $p^3$ |

So there are **four** distinct numerical values, each repeated according to how many sequences share the same $k$.

### 3.3 Grouping by the number of defectives

Let $k \in \{0,1,2,3\}$ be the number of letters $D$ in the sequence. There are $\binom{3}{k}$ distinct orders (choose which $k$ positions are defective):

$$
P(\text{exactly } k \text{ defects in the sample of 3}) = \binom{3}{k} p^k (1-p)^{3-k}.
$$

This is exactly the **binomial probability mass function** $\mathrm{Bin}(n,p)$ at $n=3$. It is obtained by summing $\binom{3}{k}$ elementary outcomes, each of probability $p^k(1-p)^{3-k}$.

### 3.4 Sum to one (algebraic check)

Grouping the eight terms:

$$
\sum_{\omega \in \Omega} P(\{\omega\})
  = \sum_{k=0}^{3} \binom{3}{k} p^k (1-p)^{3-k}.
$$

By the **binomial theorem**,

$$
\sum_{k=0}^{3} \binom{3}{k} p^k (1-p)^{3-k} = \bigl(p + (1-p)\bigr)^3 = 1^3 = 1.
$$

So the assignment is a valid probability law on $\Omega$.

---

## 4. What is a “success” here?

In a Bernoulli trial, **success** is whichever of the two outcomes we **count** when we form the binomial random variable.

The problem defines $p$ as the probability of a **defective** screw. The natural choice for quality control is therefore:

$$
\boxed{\text{Success} = \text{a defective screw}}, \qquad P(\text{success}) = p.
$$

Let $X$ = number of defective screws among the three inspected. Then

$$
X \sim \mathrm{Binomial}(n,p) \quad \text{with } n = 3,
$$

$$
P(X = k) = \binom{3}{k} p^k (1-p)^{3-k}, \quad k = 0,1,2,3.
$$

**Alternative convention (consistent but swaps the parameter):** if we called “success” a **good** screw, we would set $p_{\text{success}} = 1-p$ and the same formulas would use $1-p$ wherever $p$ appears above. The problem statement ties $p$ to **defective**, so the boxed convention matches the given $p$.

---

## Final result

Answers to the four tasks in one place:

1. **Random experiment.** Inspect three screws in sequence; each inspection is an independent Bernoulli trial with $P(D)=p$, $P(G)=1-p$.

2. **Sample space.** $\Omega = \{G,\, D\}^3$ — all ordered triples of length $3$; $|\Omega|=8$, listed explicitly in **Section 2** above.

3. **Probabilities on $\Omega$.** For $\omega=(\omega_{1},\omega_{2},\omega_{3})$,
   $$
   P(\{\omega\}) = p^{k}(1-p)^{3-k},
   $$
   where $k$ is the number of defective outcomes $D$ in $\omega$. Grouping by $k$ gives $P(X=k)=\binom{3}{k}p^k(1-p)^{3-k}$ for the number of defectives $X$.

4. **Success.** Take **success = defective screw** (probability $p$ per trial). Then $X \sim \mathrm{Binomial}(3,p)$.

**Compact summary:** three independent trials, eight elementary outcomes with product probabilities, and defect count $X \sim \mathrm{Binomial}(3,p)$ with success probability $p$.

---

## Extra: expectation and variance of $X$

For $X \sim \mathrm{Binomial}(n,p)$ with $n=3$:

$$
\mathbb{E}[X] = np = 3p, \qquad \mathrm{Var}(X) = np(1-p) = 3p(1-p).
$$

These formulas are not required by the task statement but follow immediately once $X$ is defined.

---

## Quick sanity checks

1. **Boundary values:** if $p=0$, only $GGG$ has probability 1; if $p=1$, only $DDD$ has probability 1.  
2. **Symmetry of roles:** replacing $p$ by $1-p$ swaps “counting defects” and “counting good items”.  
3. **Equal one-eighth:** all eight sequences are equally likely **only** when $p = q = \tfrac{1}{2}$; then each has probability $(\tfrac{1}{2})^3 = \tfrac{1}{8}$.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Listing only $k \in \{0,1,2,3\}$ as $\Omega$ | That describes the **count** $X$, not the full sequential experiment; tasks (2)–(3) ask for elementary outcomes in $\Omega = \{G,\, D\}^3$. |
| $P = 1/8$ for each sequence for every $p$ | Only true for $p = \tfrac{1}{2}$. |
| Calling “success” = good while keeping $p = P(D)$ | Then the Bernoulli probability for “success” would be $1-p$, not $p$. |
