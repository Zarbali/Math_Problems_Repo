# Task 4 — Poisson Model (Arrival of Events)

Error reports arrive at a web service over time. The problem fixes the **average rate** at **3 reports per hour** and assumes that the **count** of reports in a chosen time interval has a **Poisson distribution**. The goal is to describe the experiment, identify the sample space for that count, write the probability mass function, and interpret the parameter $\lambda$ for a **one-hour** window.

---

## Setting and notation

| Symbol | Meaning |
|--------|---------|
| $X$ | Number of error reports in the **time interval under study** (below: one hour) |
| $\lambda$ | Poisson parameter for that interval (mean of $X$, see Section 4) |
| $k$ | Possible values of $X$, here $k \in \{0,1,2,\ldots\}$ |

The **rate** stated in the problem is $3$ reports **per hour**. For an interval of length $t$ hours, one often writes $\lambda = (\text{rate}) \times t$ when the process is homogeneous in time.

---

## 1. Description of the random experiment

Fix a **one-hour** time window (for example, a specific clock hour or any contiguous hour of observation). During that hour, **error reports** arrive at random instants; only the **total count** $X$ of reports in that hour is modeled.

The experiment is: **observe the service for one hour and record how many error reports arrive** in that period.

The problem assumes that $X$ follows a **Poisson law**. Informally, this matches “rare” independent arrivals in continuous time; formally, a full Poisson **process** would add assumptions (independent increments, etc.). For this task it is enough that the **count in a fixed interval** is Poisson with a parameter tied to the length of the interval and the given rate.

---

## 2. Sample space $\Omega$

The random variable of interest is the **number** of reports in the fixed hour. That number is a **non-negative integer** and there is **no finite upper bound** in the Poisson model (any $k=0,1,2,\ldots$ has positive probability).

Thus, for this experiment,

$$
\Omega = \{0,\, 1,\, 2,\, 3,\, \ldots\} = \mathbb{N}_0.
$$

Each elementary outcome $\omega = k$ means: “exactly $k$ error reports in the chosen hour.”

*(If one modeled exact arrival times as continuous, the underlying space would be different; the problem asks for the distribution of the **count**, so $\Omega$ is the support of that count.)*

---

## 3. Probability distribution

Let $X \sim \mathrm{Poisson}(\lambda)$ for the one-hour interval. The **probability mass function** is

$$
P(X = k) = \frac{e^{-\lambda}\, \lambda^{k}}{k!}, \qquad k = 0,1,2,\ldots
$$

**Properties used everywhere:**

$$
\sum_{k=0}^{\infty} P(X=k) = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{-\lambda} e^{\lambda} = 1,
$$

$$
\mathbb{E}[X] = \lambda, \qquad \mathrm{Var}(X) = \lambda.
$$

---

## 4. Interpretation of $\lambda$ and its value for one hour

**Meaning of $\lambda$:** for a Poisson count on a fixed interval, $\lambda$ is the **expected number of events** in that interval. It is also the **variance** of $X$. In arrival modeling, $\lambda$ is often written as

$$
\lambda = (\text{intensity}) \times (\text{length of interval}),
$$

when the intensity (average rate per unit time) is constant over the interval.

**Numerical value for one hour:** the average rate is **3 reports per hour**. For a **one-hour** observation window,

$$
\lambda = 3 \times 1 = 3.
$$

So, for the count $X$ in one hour,

$$
P(X = k) = \frac{e^{-3}\, 3^{k}}{k!}, \qquad k = 0,1,2,\ldots
$$

and $\mathbb{E}[X] = \mathrm{Var}(X) = 3$.

If the interval were $t$ hours instead, with the same rate $3/\text{hour}$, one would use $\lambda = 3t$ for that interval.

---

## Final result

- **Experiment:** count error reports during a fixed **one-hour** period; the count is modeled as Poisson.  
- **$\Omega$:** $\{0,1,2,\ldots\}$ — possible values of the number of reports.  
- **Distribution:** $P(X=k) = e^{-\lambda} \lambda^k / k!$; for **one hour**, $\lambda = 3$.  
- **$\lambda$:** mean (and variance) of the count in the chosen interval; for one hour at rate $3/\text{hour}$, $\lambda = 3$.

---

## Quick sanity checks

1. **$P(X=0) = e^{-3} \approx 0.050$** — a chance of no reports in an hour.  
2. **$P(X=3) = e^{-3} 3^3 / 3!$** — probability of exactly the “average” count (not the maximum of the pmf in general; the mode is $\lfloor\lambda\rfloor$ or nearby).  
3. **Sum** of all $P(X=k)$ equals $1$ (exponential series).

---

## Pitfalls to avoid

| Mistake | Why it is wrong |
|--------|------------------|
| Setting $\lambda = 3$ for **any** interval regardless of length | $\lambda$ scales with the **duration** of the interval if the rate is per hour. |
| Using a **finite** $\Omega$ like $\{0,\ldots,n\}$ without justification | Poisson allows arbitrarily large $k$ with positive (though tiny) probability. |
| Confusing **rate** (3 per hour) with **probability** $p$ of a Bernoulli trial | Poisson models **counts in continuous time**, not a fixed number of Bernoulli trials (unless as a limit). |
