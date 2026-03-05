# Problem 08 – Seven Pulses

We have 7 pulses total.

Types:

A : 4 pulses  
B : 2 pulses  
C : 1 pulse

The arrangement of pulses is random.

We want the probability of several events related to the first positions.



## First observation

note: since the arrangement is random, every pulse has the same chance to appear in the first position.

So for the first pulse I can simply count how many of each type exist out of the total 7 pulses.



## 1. Probability that the first pulse is A

There are 4 pulses of type A out of 7 total pulses.

So the probability that the first position contains A is

$$
P(\text{first}=A)=\frac{4}{7}
$$

note: this works because any of the 7 pulses could appear first with equal probability.


## 2. Probability that the first pulse is A or C

Now the first pulse can be either A or C.

There are

4 pulses of A  
1 pulse of C

So in total 5 pulses that satisfy the condition.

$$
P(\text{first}=A \text{ or } C)=\frac{5}{7}
$$

note: this is larger than the previous probability because now we allow two different pulse types instead of only A.


## 3. Probability that the first two pulses are A then C

Now the order matters.

We want the first pulse to be A and the second pulse to be C.

It is easier to compute this step by step.

First compute the probability that the first pulse is A.

$$
P(\text{first}=A)=\frac{4}{7}
$$

If the first pulse is A, one A is already used.

So there are 6 pulses left:

3 A  
2 B  
1 C

The probability that the second pulse is C under this condition is

$$
P(\text{second}=C \mid \text{first}=A)=\frac{1}{6}
$$

Since these steps happen sequentially, we multiply the probabilities.

$$
P=\frac{4}{7}\cdot\frac{1}{6}
$$

$$
=\frac{4}{42}
$$

$$
=\frac{2}{21}
$$

note: the probability becomes smaller because we require a very specific order of pulses.

## Final results

$P(\text{first}=A)=\frac{4}{7}$

$P(\text{first}=A \text{ or } C)=\frac{5}{7}$

$P(\text{first}=A, \text{second}=C)=\frac{2}{21}$


## Quick check

note: all probabilities are between 0 and 1.

Also

$$
\frac{5}{7}>\frac{4}{7}
$$

which makes sense because the event "A or C" includes more possibilities than just "A".