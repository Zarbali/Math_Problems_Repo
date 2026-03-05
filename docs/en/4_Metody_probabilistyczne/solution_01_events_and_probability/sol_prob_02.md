# Problem 02 – Circuit

## Given

Element $a_1$ is connected in series with a block.  
The block consists of elements $a_2$ and $a_3$ connected in parallel.

Let

$A_i$ = "element $a_i$ works at time $t$".

We need to describe the event

$A$ = "the current through the circuit is not interrupted".


## How I thought about it

At first I drew the circuit to understand how the current flows.

The current first passes through $a_1$, and then reaches the block where $a_2$ and $a_3$ are connected in parallel.

In the block the current can go through $a_2$ **or** $a_3$ (two possible paths).

So the block works if at least one of these elements works.

That corresponds to the union of events.

For the whole circuit to work, element $a_1$ must work **and** the block must work.

Because $a_1$ is in series — if it fails, the current stops completely.

The rule I use is:

series connection → all elements must work $\cap$
parallel connection → at least one works $\cup$


## Block

The block works when either $a_2$ or $a_3$ works.

$$
A_2 \cup A_3
$$


## Whole circuit

The circuit works when $a_1$ works and the block works

Therefore

$$
A = A_1 \cap (A_2 \cup A_3)
$$


## Answer

$$
A = A_1 \cap (A_2 \cup A_3)
$$

This means that element $a_1$ works and at least one of the elements $a_2$ or $a_3$ works


## Check

- if $a_1$ fails the current stops 
- if both $a_2$ and $a_3$ fail there is no path in the block 
- if $a_1$ works and at least one of $a_2$ or $a_3$ works current flows 


series = $\cap$, parallel = $\cup$ (note to remember the rule)