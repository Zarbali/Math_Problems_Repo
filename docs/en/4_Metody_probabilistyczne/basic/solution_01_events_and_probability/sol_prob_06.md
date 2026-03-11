# Task 6 — Events and Probabilities in Coin Tossing

This task builds on the sample spaces Ω₁, Ω₂ and Ω₃ from Task 1.

In Task 1 we only described the **possible outcomes** of the experiment.  
Now we start assigning **probabilities to events**.

Since the coin is **fair**, every elementary outcome is equally likely.  
Because of this we can use the classical probability rule.

Note: this means the probability of an event is simply the number of favorable outcomes divided by the total number of outcomes.

---

## Probabilities of elementary outcomes

If all outcomes are equally likely, the probability of a single elementary outcome ω is

$$
P(\omega) = \frac{1}{|\Omega|}
$$

This means: one outcome divided by the total number of outcomes in the sample space.

Applying this to the sample spaces from Task 1:

| Sample space | Outcomes | Probability of each |
|--------------|----------|----------------------|
| Ω₁ | H, T | $P(\omega) = \frac{1}{2}$ |
| Ω₂ | HH, HT, TH, TT | $P(\omega) = \frac{1}{4}$ |
| Ω₃ | HHH, HHT, …, TTT | $P(\omega) = \frac{1}{8}$ |

Note: the more tosses we have, the larger the sample space becomes, so the probability of each individual outcome gets smaller.

---

# One coin toss

The sample space is

Ω₁ = {H, T}

So there are two possible outcomes.

---

### Event A₁ — heads

Event A₁ contains all outcomes where we get heads.

$$
A_1 = \{H\}
$$

Number of favorable outcomes = 1  
Total number of outcomes = 2

$$
P(A_1) = \frac{1}{2}
$$

---

### Event B₁ — tails

Event B₁ contains all outcomes where we get tails.

$$
B_1 = \{T\}
$$

$$
P(B_1) = \frac{1}{2}
$$

---

### Event C₁ — not tails

If the result is **not tails**, then it must be heads.

$$
C_1 = \{H\}
$$

$$
P(C_1) = \frac{1}{2}
$$

Note: events $A_1$ and $C_1$ are actually the same event.  
They describe the same outcome but using different wording.

---

# Two coin tosses

The sample space is

Ω₂ = {HH, HT, TH, TT}

There are four outcomes and each has probability $\frac{1}{4}$.

To find probabilities of events, we count how many outcomes satisfy the condition.

---

### Event A₂ — exactly one head

Exactly one head means one H and one T.

Possible outcomes:

$$
A_2 = \{HT, TH\}
$$

Number of favorable outcomes = 2

$$
P(A_2) = \frac{2}{4} = \frac{1}{2}
$$

Note: outcomes HH and TT are excluded because they do not contain exactly one head.

---

### Event B₂ — at least one head

This means we get one or more heads.

Possible outcomes:

$$
B_2 = \{HH, HT, TH\}
$$

Number of favorable outcomes = 3

$$
P(B_2) = \frac{3}{4}
$$

Note: it is sometimes easier to compute this using the complement.

The only outcome with **no heads** is TT.

So

$$
P(B_2) = 1 - P(TT) = 1 - \frac{1}{4} = \frac{3}{4}
$$

---

### Event C₂ — both tosses give the same result

This means both tosses match.

Possible outcomes:

$$
C_2 = \{HH, TT\}
$$

Number of favorable outcomes = 2

$$
P(C_2) = \frac{2}{4} = \frac{1}{2}
$$

---

# Three coin tosses

The sample space is

Ω₃ = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}

There are eight outcomes, each with probability $\frac{1}{8}$.

---

### Event A₃ — exactly two heads

Possible outcomes:

$$
A_3 = \{HHT, HTH, THH\}
$$

Number of favorable outcomes = 3

$$
P(A_3) = \frac{3}{8}
$$

Note: outcome HHH is excluded because it has three heads, not two.

---

### Event B₃ — at least one tail

Possible outcomes:

$$
B_3 = \{HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

Number of favorable outcomes = 7

$$
P(B_3) = \frac{7}{8}
$$

Again it is easier to think using the complement.

The only outcome with **no tails** is HHH.

So

$$
P(B_3) = 1 - \frac{1}{8} = \frac{7}{8}
$$

---

### Event C₃ — all three tosses give the same result

Possible outcomes:

$$
C_3 = \{HHH, TTT\}
$$

Number of favorable outcomes = 2

$$
P(C_3) = \frac{2}{8} = \frac{1}{4}
$$

---

# Additional event on Ω₃

Let

$$
D_3
$$

be the event that the **first toss is heads**.

We simply list all outcomes that start with H.

$$
D_3 = \{HHH, HHT, HTH, HTT\}
$$

Number of favorable outcomes = 4

$$
P(D_3) = \frac{4}{8} = \frac{1}{2}
$$

Note: this makes sense intuitively because the first toss of a fair coin has probability $\frac{1}{2}$ of being heads, regardless of what happens later.