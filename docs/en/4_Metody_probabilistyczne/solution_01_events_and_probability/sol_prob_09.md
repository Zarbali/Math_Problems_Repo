# Problem 09 – Three Plants

A product can come from one of three plants.

The probabilities that a product from each plant is first-quality are:

Plant 1 → 0.97  
Plant 2 → 0.90  
Plant 3 → 0.86

From each plant one item is taken, so we have three items total.

One of these three items is then selected randomly.

We need the probability that the selected item is first-quality.


## Setting up the events

Let

$H_1$ = the selected item came from plant 1  
$H_2$ = the selected item came from plant 2  
$H_3$ = the selected item came from plant 3  

$F$ = the selected item is first-quality

note: since one item from each plant is placed together and we choose randomly among the three, each plant has the same chance of being selected.

Therefore

$$
P(H_1)=P(H_2)=P(H_3)=\frac{1}{3}
$$

note: the three events $H_1,H_2,H_3$ form a partition of the sample space, because the item must come from exactly one of the plants.


## Using the total probability formula

To find the probability that the selected item is first-quality, I combine the probabilities from each possible plant.

The total probability formula gives

$$
P(F)=P(F|H_1)P(H_1)+P(F|H_2)P(H_2)+P(F|H_3)P(H_3)
$$

note: this works because the product must come from one of the three plants, and these cases cover all possibilities.

## Substituting the values

$$
P(F)=0.97\cdot\frac{1}{3}+0.90\cdot\frac{1}{3}+0.86\cdot\frac{1}{3}
$$

Factor out $\frac{1}{3}$:

$$
P(F)=\frac{0.97+0.90+0.86}{3}
$$

$$
=\frac{2.73}{3}
$$

$$
=0.91
$$

## Final result

$$
P(F)=0.91
$$

note: this value is essentially the average of the three quality probabilities, because each plant has equal weight 1/3 in the selection.