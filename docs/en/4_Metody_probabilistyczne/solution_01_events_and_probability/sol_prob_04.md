# Problem 04 – Parallel Elements

Two elements $a_1$ and $a_2$ are connected in parallel.

$A_i$ = event that element $a_i$ works for at least time $t$.

From the problem:

$P(A_1) = P(A_2) = p$

$P(A_1 \cap A_2) = p^2$

We need the probability that current flows through the system for at least time $t$.

---

## Understanding the circuit

note: since the elements are connected in parallel, the current can pass if **at least one of the elements works**.

So the system works if

$A_1$ works  
or  
$A_2$ works.

That corresponds to the event

$$
A = A_1 \cup A_2
$$

note: this is the same idea as in the previous circuit problem — parallel connection means union of events.

---

## Using the probability formula

To compute the probability of the union of two events I use the formula

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

note: the intersection is subtracted because otherwise the case where both events occur would be counted twice.

Applying this to our events:

$$
P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 \cap A_2)
$$

---

## Substituting the given values

From the problem:

$P(A_1) = p$  
$P(A_2) = p$  
$P(A_1 \cap A_2) = p^2$

So

$$
P(A_1 \cup A_2) = p + p - p^2
$$

$$
= 2p - p^2
$$

note: this can also be written as $p(2-p)$.

---

## Result

The probability that the current flows through the system is

$$
P = 2p - p^2
$$

---

## Quick check

note: it is useful to check extreme cases.

If $p = 0$  
→ both elements fail  
→ current cannot flow  
→ $P = 0$

If $p = 1$  
→ both elements always work  
→ current always flows  
→ $P = 1$

So the expression behaves correctly.

note: $P(A_1 \cap A_2) = p^2$ suggests independence, but here I just use the value given in the problem.