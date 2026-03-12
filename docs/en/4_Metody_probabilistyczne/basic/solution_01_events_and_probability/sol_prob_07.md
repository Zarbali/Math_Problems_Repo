# Task 7 — Events and Probabilities in Die Rolling

This task continues the experiment introduced in **Task 2**, where we defined the sample spaces for rolling a fair six-sided die one, two, and three times.

Since the die is **fair**, every elementary outcome has the **same probability**.  
Because of that we can use the **classical definition of probability**:

$$
P(A) = \frac{|A|}{|\Omega|}
$$

where

- $|A|$ is the number of favorable outcomes  
- $|\Omega|$ is the total number of elementary outcomes.

So in each part the strategy is the same:

1. describe the **sample space**
2. describe the **event**
3. count the outcomes
4. divide by the total number of outcomes.

---

# Probabilities of elementary outcomes

First we assign probabilities to the elementary outcomes in each sample space.

| Sample space | Outcomes | Probability of each |
|--------------|----------|----------------------|
| Ω₁ | 1, 2, …, 6 | $P(\omega) = \frac{1}{6}$ |
| Ω₂ | (1,1), (1,2), …, (6,6) | $P(\omega) = \frac{1}{36}$ |
| Ω₃ | (1,1,1), …, (6,6,6) | $P(\omega) = \frac{1}{216}$ |

**Note**

The number of outcomes increases by multiplication because every roll is independent:

- one roll → $6$ outcomes  
- two rolls → $6^2 = 36$ outcomes  
- three rolls → $6^3 = 216$ outcomes.

Therefore every ordered triple in $\Omega_3$ has probability $\frac{1}{216}$.

---

# One die roll

The sample space is

$$
\Omega_1 = \{1,2,3,4,5,6\}
$$

---

## $A_1$ — result is even

Even numbers on the die are

$$
A_1 = \{2,4,6\}
$$

Number of favorable outcomes:

$$
|A_1| = 3
$$

Therefore

$$
P(A_1) = \frac{3}{6} = \frac{1}{2}
$$

**Note**

Exactly half of the faces of the die are even.

---

## $B_1$ — result greater than 4

Numbers greater than 4 are

$$
B_1 = \{5,6\}
$$

Number of outcomes

$$
|B_1| = 2
$$

So

$$
P(B_1) = \frac{2}{6} = \frac{1}{3}
$$

---

## $C_1$ — result at most 3

Numbers less than or equal to 3 are

$$
C_1 = \{1,2,3\}
$$

$$
|C_1| = 3
$$

Therefore

$$
P(C_1) = \frac{3}{6} = \frac{1}{2}
$$

---

# Two die rolls

Now we roll the die twice.

The sample space consists of **ordered pairs**

$$
\Omega_2 = \{(i,j) : i,j \in \{1,\ldots,6\}\}
$$

Total number of outcomes:

$$
|\Omega_2| = 36
$$

**Important**

Order matters.

For example $(1,6)$ and $(6,1)$ are different outcomes because the results occur in different order.

---

## $A_2$ — sum equals 7

We list all pairs whose sum equals 7.

$$
A_2 = \{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}
$$

Number of outcomes

$$
|A_2| = 6
$$

So

$$
P(A_2) = \frac{6}{36} = \frac{1}{6}
$$

---

## $B_2$ — both results are the same

These are pairs where the same number appears twice:

$$
B_2 = \{(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)\}
$$

$$
|B_2| = 6
$$

Therefore

$$
P(B_2) = \frac{6}{36} = \frac{1}{6}
$$

---

## $C_2$ — sum at least 10

We consider sums 10, 11 and 12.

Possible outcomes:

- sum 10 → $(4,6),(5,5),(6,4)$  
- sum 11 → $(5,6),(6,5)$  
- sum 12 → $(6,6)$  

So

$$
|C_2| = 6
$$

Therefore

$$
P(C_2) = \frac{6}{36} = \frac{1}{6}
$$

---

# Three die rolls

Now the die is rolled three times.

The sample space contains ordered triples:

$$
|\Omega_3| = 6^3 = 216
$$

Each triple has probability

$$
\frac{1}{216}
$$

---

## $A_3$ — sum equals 10

We need triples $(a,b,c)$ such that

$$
a+b+c = 10
$$

with $1 \le a,b,c \le 6$.

We count the possibilities using partitions of 10.

| Partition | Permutations | Count |
|-----------|--------------|-------|
| 6+3+1 | $3!$ | 6 |
| 6+2+2 | $\frac{3!}{2!}$ | 3 |
| 5+4+1 | $3!$ | 6 |
| 5+3+2 | $3!$ | 6 |
| 4+4+2 | $\frac{3!}{2!}$ | 3 |
| 4+3+3 | $\frac{3!}{2!}$ | 3 |

Total

$$
|A_3| = 27
$$

Therefore

$$
P(A_3) = \frac{27}{216} = \frac{1}{8}
$$

---

## $B_3$ — exactly two rolls give the same number

One number appears twice and another number appears once.

Steps:

- choose the repeated number → 6 possibilities  
- choose the different number → 5 possibilities  
- choose the position of the different number → 3 possibilities  

So

$$
|B_3| = 6 \times 5 \times 3 = 90
$$

Therefore

$$
P(B_3) = \frac{90}{216} = \frac{5}{12}
$$

---

## $C_3$ — two twos and one three

Possible outcomes are

$$
C_3 =
\{(2,2,3),(2,3,2),(3,2,2)\}
$$

Number of outcomes

$$
|C_3| = 3
$$

So

$$
P(C_3) = \frac{3}{216} = \frac{1}{72}
$$

---

# Additional event on $\Omega_3$

Let

$$
D_3
$$

be the event that **the first roll equals 6**.

The remaining two rolls can be any numbers.

So

$$
D_3 = \{(6,j,k) : j,k \in \{1,\ldots,6\}\}
$$

Number of outcomes

$$
|D_3| = 1 \times 6 \times 6 = 36
$$

Therefore

$$
P(D_3) = \frac{36}{216} = \frac{1}{6}
$$

**Note**

This equals the probability of rolling a 6 on a single die because the rolls are independent.