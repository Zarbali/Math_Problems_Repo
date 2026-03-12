# Task 9 — Events and Probabilities in Weekly Weather Observation

This task builds on **Task 4**, where we defined the sample space $\Omega_7$
for observing weather over seven consecutive days.

Each day is in exactly one of three states: Sunny ($S$), Cloudy ($C$),
or Rainy ($R$). The days are **independent**, and each state occurs with
equal probability $\frac{1}{3}$.

*Convention: Day 1 = Monday, Day 2 = Tuesday, ...,
Day 6 = Saturday, Day 7 = Sunday.*

---

## Sample space and probability formula

Since there are 7 independent days and 3 possible states per day,
the total number of outcomes is:

$$|\Omega_7| = 3^7 = 2187$$

I multiply — not add — because the days are independent.
Every combination of states across all seven days is a valid outcome.

Because all outcomes are equally likely (each state has probability
$\frac{1}{3}$ on every day), I can use the **classical probability formula**
throughout this task:

$$P(A) = \frac{|A|}{|\Omega_7|}$$

This formula applies here precisely because all elementary outcomes
are equally likely. If the states had different probabilities,
I would need a different approach.

---

## Event A — entire weekend is sunny

The weekend consists of Saturday (day 6) and Sunday (day 7).

$$A = \{(w_1,\ldots,w_7) : w_6 = S,\, w_7 = S\}$$

Days 6 and 7 are fixed as $S$. The remaining 5 days (Monday–Friday)
can each be any of the three states freely.

$$|A| = 3^5 = 243$$

$$P(A) = \frac{243}{2187} = \frac{1}{9}$$

**Why $3^5$?** Because 5 days are unconstrained and each has 3 choices,
giving $3 \times 3 \times 3 \times 3 \times 3 = 3^5$ combinations.

**Verification using independence:** Since the days are independent,
I can multiply the probabilities of the individual conditions directly:

$$P(A) = P(w_6 = S) \cdot P(w_7 = S) = \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9} \checkmark$$

---

## Event B — Wednesday, Thursday, Friday all rainy

Wednesday = day 3, Thursday = day 4, Friday = day 5.

$$B = \{(w_1,\ldots,w_7) : w_3 = R,\, w_4 = R,\, w_5 = R\}$$

Days 3, 4 and 5 are fixed as $R$. The remaining 4 days
(days 1, 2, 6, 7) are free.

$$|B| = 3^4 = 81$$

$$P(B) = \frac{81}{2187} = \frac{1}{27}$$

**Verification using independence:**

$$P(B) = \left(\frac{1}{3}\right)^3 = \frac{1}{27} \checkmark$$

---

## Event C — at least one day is sunny

Counting directly would require handling cases with exactly 1 sunny day,
exactly 2 sunny days, and so on — which is tedious.

Instead I use the **complement rule**:

$$P(C) = 1 - P(\text{no sunny day at all})$$

I can use the complement here because the events "at least one sunny day"
and "no sunny day" together cover all possible outcomes and cannot
both occur at the same time.

If no day is sunny, then each day must be either $C$ or $R$ —
that gives 2 choices per day.

$$|\text{no sunny}| = 2^7 = 128$$

$$P(C) = 1 - \frac{128}{2187} = \frac{2059}{2187}$$

**Verification using independence:**

$$P(\text{no sunny}) = \left(\frac{2}{3}\right)^7 = \frac{128}{2187}$$

$$P(C) = 1 - \frac{128}{2187} = \frac{2059}{2187} \checkmark$$

---

## Event D — no rainy day during the week

If no day is rainy, then each day must be either $S$ or $C$ —
that gives 2 choices per day.

$$D = \{(w_1,\ldots,w_7) : w_i \in \{S, C\} \text{ for all } i\}$$

$$|D| = 2^7 = 128$$

$$P(D) = \frac{128}{2187}$$

**Note:** Events $C$ and $D$ both produce $2^7 = 128$ favorable outcomes,
but they describe completely different situations. In $C$ we exclude
the state $S$ from each day; in $D$ we exclude the state $R$.
The count happens to be the same by symmetry of the model.

---

## Event E — exactly two days are sunny

I split this into two independent choices:

**Step 1 — choose which 2 days out of 7 are sunny.**

The order of the sunny days does not matter here —
I am choosing positions, not arranging them.
So I use the binomial coefficient:

$$\binom{7}{2} = \frac{7!}{2!\,5!} = 21$$

**Step 2 — assign states to the remaining 5 days.**

Each of the remaining 5 days must be $C$ or $R$ (not $S$,
since exactly two days are sunny).
That gives 2 choices per day:

$$2^5 = 32$$

**Combining:** I multiply because the choice of positions and
the assignment of states to remaining days are independent of each other.

$$|E| = 21 \times 32 = 672$$

$$P(E) = \frac{672}{2187} = \frac{224}{729}$$

To simplify: both 672 and 2187 are divisible by 3.
$672 \div 3 = 224$ and $2187 \div 3 = 729$.

---

## Additional event — Monday is rainy

Let $F$ be the event that Monday (day 1) is rainy.

$$F = \{(w_1,\ldots,w_7) : w_1 = R\}$$

Day 1 is fixed as $R$. The remaining 6 days are free.

$$|F| = 1 \times 3^6 = 729$$

$$P(F) = \frac{729}{2187} = \frac{1}{3}$$

This result makes complete sense: Monday is a single independent day
with three equally likely states, so the probability of any one
specific state is exactly $\frac{1}{3}$.