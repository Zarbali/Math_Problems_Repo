## Task 1 — Coin Tossing

Experiment: tossing a fair coin.

Important: **the order of outcomes matters**, so sequences like HT and TH represent different results.

---

## 1. Sample space Ω₁ (one coin toss)

For one coin toss there are only two possible outcomes.

| Outcome | Meaning |
|-------|--------|
| H | Heads |
| T | Tails |

$$
\Omega_1 = \{H, T\}
$$

Number of elementary outcomes:

$$
|\Omega_1| = 2
$$

Note: an elementary outcome represents one complete result of the experiment.

---

## 2. Sample space Ω₂ (two coin tosses)

For two tosses we must consider **ordered pairs of outcomes**.

First toss can be H or T.  
Second toss can also be H or T.

| First toss | Second toss | Outcome |
|------------|-------------|--------|
| H | H | HH |
| H | T | HT |
| T | H | TH |
| T | T | TT |

$$
\Omega_2 = \{HH, HT, TH, TT\}
$$

Number of elementary outcomes:

$$
|\Omega_2| = 4
$$

Note: HT means **heads on the first toss and tails on the second toss**.

---

## 3. Sample space Ω₃ (three coin tosses)

For three tosses we extend the same idea.

Each outcome from Ω₂ can be followed by either H or T.

| From Ω₂ | Add H | Add T |
|--------|-------|-------|
| HH | HHH | HHT |
| HT | HTH | HTT |
| TH | THH | THT |
| TT | TTH | TTT |

$$
\Omega_3 =
\{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

Number of elementary outcomes:

$$
|\Omega_3| = 8
$$

Observation: each additional toss doubles the number of possible outcomes.

---

## 4. Number of elementary outcomes

| Sample space | Number of tosses | Outcomes |
|---------------|-----------------|---------|
| Ω₁ | 1 | 2 |
| Ω₂ | 2 | 4 |
| Ω₃ | 3 | 8 |

We observe the rule:

$$
|\Omega_n| = 2^n
$$

because each coin toss has two possible results.

---

## 5. Meaning of an elementary outcome

An **elementary outcome** represents one complete possible result of the experiment.

Examples:

| Outcome | Interpretation |
|--------|---------------|
| H | Heads in one toss |
| HT | Heads first, tails second |
| HTH | Heads, tails, heads in three tosses |

Each elementary outcome describes **exactly one possible sequence of results**.