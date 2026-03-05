# Problem 06 – Two Machines

Two automated machines produce identical products.

Production ratio:

machine 1 : machine 2 = 3 : 2

Machine 1 produces 65% first-grade products.  
Machine 2 produces 85% first-grade products.

We randomly select one product from the conveyor.

We need:

1. probability that the product is first-grade
2. probability that a first-grade product came from machine 1


## Setting up the events

Let

$H_1$ = product was produced by machine 1

$H_2$ = product was produced by machine 2

$F$ = product is first-grade

note: the production ratio is 3:2, so if I imagine 5 products total,
3 would come from machine 1 and 2 from machine 2.

This allows me to convert the ratio into probabilities.

$$
P(H_1)=\frac{3}{5}=0.6
$$

$$
P(H_2)=\frac{2}{5}=0.4
$$

note: these must add up to 1 because every product must come from one of the two machines.

Now the quality probabilities are given directly in the problem.

$$
P(F|H_1)=0.65
$$

$$
P(F|H_2)=0.85
$$

note: this means machine 2 produces higher quality products on average.

## 1. Probability that a product is first-grade

A randomly chosen product can come either from machine 1 or from machine 2.

So to compute the probability of event $F$ I use the total probability formula.

$$
P(F)=P(F|H_1)P(H_1)+P(F|H_2)P(H_2)
$$

note: this formula works because the events $H_1$ and $H_2$ form a partition of the sample space.

Now substitute the values.

$$
P(F)=0.65\cdot0.6 + 0.85\cdot0.4
$$

First term:

$$
0.65\cdot0.6=0.39
$$

Second term:

$$
0.85\cdot0.4=0.34
$$

Add them together:

$$
P(F)=0.39+0.34
$$

$$
=0.73
$$

note: this means about 73% of all products on the conveyor are first-grade.


## 2. Probability that a first-grade product came from machine 1

Now the situation is reversed.

We already know that the product is first-grade and we want to know which machine most likely produced it.

This is exactly the situation where Bayes' theorem is used.

$$
P(H_1|F)=\frac{P(F|H_1)P(H_1)}{P(F)}
$$

note: the numerator represents the probability that the product both came from machine 1 and is first-grade.

Compute the numerator:

$$
0.65\cdot0.6=0.39
$$

Now divide by $P(F)$:

$$
P(H_1|F)=\frac{0.39}{0.73}
$$

$$
=\frac{39}{73}
$$

$$
\approx0.534
$$

note: even though machine 2 produces better quality products, machine 1 still produces more items overall, so the probability remains slightly above 0.5.


## Final results

Probability that a random product is first-grade:

$$
P(F)=0.73
$$

Probability that a first-grade product came from machine 1:

$$
P(H_1|F)=\frac{39}{73}\approx0.534
$$


## Quick consistency checks

note: probabilities must lie between 0 and 1.

$0.73$ and $0.534$ satisfy this.

Also

$$
P(H_1)+P(H_2)=0.6+0.4=1
$$

so the model is consistent.