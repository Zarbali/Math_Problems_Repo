# Problem 05 – Water Volume

We consider the water flow through a concrete culvert (in dm³/s).

Two intervals are given.

$A$ = the water volume lies in the interval $\langle125,250\rangle$  

$P(A)=0.6$

$B$ = the water volume lies in the interval $(200,300\rangle$

$P(B)=0.7$

We also know:

$$
P(A \cup B)=0.8
$$

We need to compute:

$P(A')$  
$P(A \cap B)$  
$P(A' \cap B')$

---

## First observations

note: the two intervals overlap because the range 200–250 belongs to both intervals.  
This means that the events $A$ and $B$ are **not disjoint**, so their intersection is not zero.

note: since the probability of the union $P(A \cup B)$ is given, the standard union formula will be useful for finding the intersection.

---

## 1. Complement of A

The complement $A'$ means the event that the water volume **does not lie in interval A**.

In probability theory the complement rule states:

$$
P(A') = 1 - P(A)
$$

This works because an event and its complement cover the whole sample space and cannot occur simultaneously.

Substituting the value from the problem:

$$
P(A') = 1 - 0.6
$$

$$
=0.4
$$

note: this means there is a 40% chance that the water volume is outside the interval $\langle125,250\rangle$.

---

## 2. Intersection of A and B

Now we need the probability that the volume lies in **both intervals simultaneously**.

That corresponds to the intersection event $A \cap B$.

To find this value I use the union formula:

$$
P(A \cup B)=P(A)+P(B)-P(A\cap B)
$$

note: the intersection must be subtracted because when we add $P(A)$ and $P(B)$, the overlapping region would be counted twice.

Now substitute the known values:

$$
0.8 = 0.6 + 0.7 - P(A \cap B)
$$

Rearranging to isolate the intersection:

$$
P(A \cap B) = 0.6 + 0.7 - 0.8
$$

$$
=0.5
$$

note: this value represents the probability that the water volume lies in the overlapping part of the two intervals (between 200 and 250).

---

## 3. Neither A nor B

The event $A' \cap B'$ means the water volume lies in **neither interval A nor interval B**.

Instead of calculating this directly, it is easier to use De Morgan's rule:

$$
(A \cup B)' = A' \cap B'
$$

This means that “not (A or B)” is the same as “not A and not B”.

So the probability we want is simply the complement of the union.

$$
P(A' \cap B') = P((A \cup B)')
$$

Using the complement rule:

$$
P(A' \cap B') = 1 - P(A \cup B)
$$

Substituting the value:

$$
=1 - 0.8
$$

$$
=0.2
$$

note: this corresponds to the probability that the water volume lies outside both given intervals.

---

## Final results

$P(A') = 0.4$

$P(A \cap B) = 0.5$

$P(A' \cap B') = 0.2$

---

## Consistency checks

note: probabilities must always lie between 0 and 1.

All results satisfy this condition.

Also the complement rule holds:

$P(A)+P(A')=0.6+0.4=1$

Finally the intersection must be smaller than each individual probability:

$P(A \cap B) \le P(A)$  
$0.5 \le 0.6$

$P(A \cap B) \le P(B)$  
$0.5 \le 0.7$

So the values are consistent with probability rules.