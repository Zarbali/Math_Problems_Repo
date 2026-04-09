# Task 3 — Geometric Model (Waiting for the First Event)

Pages are checked one by one. Each page is a **Bernoulli trial**: either a **printing error** occurs (with probability $p$) or it does not (with probability $1-p$). Trials are **independent** and $p$ is the same every time. The process **stops** when the **first** error is observed. This is the classical **geometric** waiting-time model (version “number of trials until the first success,” where “success” is defined as seeing an error — see Section 4).

---

## Setting and notation

| Symbol | Meaning |
|--------|---------|
| $p$ | Probability of a **printing error** on a single page, $p \in (0,1]$ (for $p=0$ there is no error almost surely; for $p=1$ the first page always fails) |
| $q$ | $q = 1-p$, probability of **no error** on one page |
| $T$ | Index of the page on which the **first** error appears (trial number of the first “error” outcome) |

---

## 1. Description of the random experiment

The experiment proceeds as follows:

- Inspect pages in order: page $1$, page $2$, page $3$, …  
- The outcomes on different pages are **independent**; each page has probability $p$ of containing an error.  
- As soon as a page **with** an error is found, observation **stops**. The recorded result is **where** that first error occurred.  
- If one were to imagine continuing forever when no error ever appears, that would be a zero-probability event when $p>0$; in the standard geometric model with $p>0$, the first error appears **almost surely** after finitely many pages.

So this is an **indefinite sequence of independent Bernoulli trials** stopped at the **first** occurrence of the event of interest (error). The randomness is in **how many** pages must be inspected — not a fixed sample size as in the binomial model.

---

## 2. Sample space $\Omega$

Each outcome is completely described by **on which page the first error appears**.

Let $T \in \{1,2,3,\ldots\}$ be that page number. Then

$$
\Omega = \{1,\, 2,\, 3,\, \ldots\} = \mathbb{N}.
$$

**Interpretation:** $T = k$ means: pages $1,\ldots,k-1$ have **no** error, and page $k$ has an error. (For $k=1$, only page $1$ must have an error.)

Equivalently, one could encode outcomes as finite prefixes of an infinite string of “clean” ($C$) and “error” ($E$) symbols, each valid outcome ending with the **first** $E$: e.g. $E$, $CE$, $CCE$, $CCCE$, … The cardinality of $\Omega$ is **countably infinite**.

---

## 3. Probability distribution

### 3.1 Mass function for $T$

For the first error to occur exactly on page $k$:

- pages $1$ through $k-1$ must each have **no** error: probability $q^{\,k-1} = (1-p)^{k-1}$;
- page $k$ must have an error: probability $p$.

By **independence** of pages,

$$
P(T = k) = (1-p)^{k-1}\, p, \qquad k = 1,2,3,\ldots
$$

This is the **geometric distribution** on $\{1,2,\ldots\}$ (sometimes denoted $\mathrm{Geom}(p)$ in the “first success on trial $k$” convention).

### 3.2 Sum to one

$$
\sum_{k=1}^{\infty} P(T=k) = \sum_{k=1}^{\infty} (1-p)^{k-1} p = p \sum_{j=0}^{\infty} (1-p)^{j} = p \cdot \frac{1}{1-(1-p)} = 1,
$$

for $p \in (0,1]$ (geometric series).

### 3.3 Alternative convention (optional)

Some texts define $Y = T - 1$ = **number of error-free pages before** the first error. Then $Y \in \{0,1,2,\ldots\}$ and

$$
P(Y = k) = (1-p)^{k}\, p, \qquad k = 0,1,2,\ldots
$$

The problem asks for the distribution of “waiting until the first error”; the table above uses $T$ (page number of first error). When reading other sources, always check whether “geometric” means $T$ or $Y = T-1$.

---

## 4. What is considered a success?

In Bernoulli trials, **success** is whichever of the two outcomes is labeled as the “interesting” event for the geometric law.

The task is to wait for the **first printing error**. Therefore the natural identification is:

$$
\boxed{\text{Success} = \text{a page contains a printing error}}, \qquad P(\text{success}) = p.
$$

Then $T$ is the **trial number** of the first success, and $P(T=k)$ takes the form $(1-p)^{k-1} p$.

If “success” were instead defined as a **clean** page, the waiting time for the first “success” would follow the same geometric **shape** but with $p$ replaced by $1-p$ in the formulas above. The problem ties $p$ to **error**, so the boxed convention matches the statement.

---

## Final result

- **Experiment:** independent Bernoulli pages with $P(\text{error})=p$; observe until the first error.  
- **$\Omega$:** $\{1,2,3,\ldots\}$ — the index of the page where the first error occurs.  
- **Distribution:** $P(T=k) = (1-p)^{k-1} p$ for $k=1,2,\ldots$ (geometric).  
- **Success:** a page with a printing error (probability $p$ per trial).

---

## Quick sanity checks

1. **$p=1$:** $P(T=1)=1$ (error on the first page with certainty).  
2. **Small $p$:** most mass shifts to larger $k$; mean waiting time is $1/p$.  
3. **Memoryless property** (for this geometric version): given $T>n$, the extra wait $(T-n)$ has the same geometric distribution as $T$ — characteristic of the geometric law on $\{1,2,\ldots\}$.

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Treating the number of pages as fixed $n$ like a binomial count | Here the sample size is **random** (stop at first error). |
| Using $\binom{n}{k} p^k(1-p)^{n-k}$ | That is **binomial** for a fixed number of trials, not waiting for the first event. |
| Mixing two geometric conventions ($T$ vs $T-1$) | Always state whether $k$ counts **trials until** first success or **failures before** first success. |
