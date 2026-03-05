# Problem 04 – Parallel Elements

Two elements $a_1$ and $a_2$ are connected in parallel.

$A_i$ = event that element $a_i$ works for at least time $t$.

Given:

$P(A_1) = P(A_2) = p$

$P(A_1 \cap A_2) = p^2$

Need: probability that current flows through the system for at least time $t$.

---

## Understanding the system

note: since the elements are connected in parallel, the current can pass if **at least one element works**.

So the system works if

$A_1$ works  
or  
$A_2$ works.

That corresponds to the event

$A = A_1 \cup A_2$

note: this is the same idea as in the previous circuit task — parallel → union.

---

## Computing the probability

To find the probability of a union of two events I use the formula

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

note: the intersection must be subtracted because otherwise the case where both events occur would be counted twice.

Applying this to our events:

$$
P(A_1 \cup A_2)
=
P(A_1) + P(A_2) - P(A_1 \cap A_2)
$$

---

## Substituting the values

From the problem:

$P(A_1) = p$  
$P(A_2) = p$  
$P(A_1 \cap A_2) = p^2$

So

$$
P(A_1 \cup A_2)
=
p + p - p^2
$$

$$
= 2p - p^2
$$

note: this can also be written as $p(2 - p)$.

---

## Result

Probability that the current flows for at least time $t$:

$$
P = 2p - p^2
$$

---

## Quick check

note: check extreme cases to see if the formula makes sense.

If $p = 0$  
→ both elements always fail  
→ no current flows  
→ $P = 0$

If $p = 1$  
→ both elements always work  
→ current always flows  
→ $P = 1$

note: so the result behaves correctly.

Also $P(A_1 \cap A_2) = p^2$ looks like the elements are independent, but here I just use the value given in the problem.