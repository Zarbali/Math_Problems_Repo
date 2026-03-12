# Task 8 — Events and Probabilities in Card Drawing

This task continues the card experiment introduced in **Task 3**.

We draw cards from a **standard 52-card deck**.

The deck is assumed to be **well shuffled**, so every ordered sequence of draws is **equally likely**.

Because of that we again use the **classical probability formula**

$$
P(A) = \frac{|A|}{|\Omega|}
$$

where

- $|A|$ = number of favorable outcomes  
- $|\Omega|$ = total number of possible outcomes.

Standard deck structure:

- 52 cards total  
- 4 suits: hearts, diamonds, clubs, spades  
- 13 ranks in each suit  
- face cards = J, Q, K (3 per suit → 12 total)

---

# Probabilities of elementary outcomes

First we determine the probabilities of **individual outcomes** in each sample space.

| Sample space | Outcomes | Probability of each |
|--------------|----------|----------------------|
| Ω₁ | 52 possible cards | $P(\omega) = \frac{1}{52}$ |
| Ω₂ (with replacement) | $52 \times 52$ ordered pairs | $P(\omega) = \frac{1}{2704}$ |
| Ω₂′ (without replacement) | $52 \times 51$ ordered pairs | $P(\omega) = \frac{1}{2652}$ |

**Reasoning**

- With replacement the second draw still has **52 possibilities**.
- Without replacement the second draw has **51 possibilities** because one card has already been removed.

---

# One card drawn

The sample space is

$$
\Omega_1
$$

which contains the **52 individual cards**.

---

## $A_1$ — card is a heart

There are **13 hearts** in the deck.

So

$$
|A_1| = 13
$$

$$
P(A_1) = \frac{13}{52} = \frac{1}{4}
$$

**Note**

One quarter of the deck belongs to each suit.

---

## $B_1$ — card is a king

There are **4 kings** in the deck.

$$
|B_1| = 4
$$

So

$$
P(B_1) = \frac{4}{52} = \frac{1}{13}
$$

---

## $C_1$ — card is not a face card

Face cards are

J, Q, K.

There are **3 per suit**, so

$$
12 \text{ face cards}
$$

Non-face cards:

$$
52 - 12 = 40
$$

So

$$
P(C_1) = \frac{40}{52} = \frac{10}{13}
$$

---

# Two cards drawn (with replacement)

Here the card is returned to the deck before the second draw.

So the two draws are **independent**.

Total outcomes:

$$
|\Omega_2| = 52 \times 52 = 2704
$$

---

## $A_2$ — both cards are hearts

First draw: 13 hearts  
Second draw: 13 hearts

Number of outcomes

$$
13 \times 13 = 169
$$

So

$$
P(A_2) = \frac{169}{2704}
$$

This simplifies to

$$
P(A_2) = \frac{1}{16}
$$

**Alternative reasoning**

Since each draw has probability $\frac{13}{52}=\frac{1}{4}$

and the draws are independent

$$
P(A_2) = \left(\frac{1}{4}\right)^2
$$

---

## $B_2$ — both cards have the same rank

There are **13 possible ranks**.

For each rank:

- 4 choices for the first card
- 4 choices for the second card

So

$$
4 \times 4 = 16
$$

ordered pairs per rank.

Therefore

$$
13 \times 16 = 208
$$

outcomes.

So

$$
P(B_2) = \frac{208}{2704}
$$

which simplifies to

$$
\frac{1}{13}
$$

---

## $C_2$ — at least one card is an ace

Instead of counting directly it is easier to use the **complement rule**.

At least one ace =

$$
1 - P(\text{no ace})
$$

Non-aces:

$$
52 - 4 = 48
$$

So

$$
48 \times 48 = 2304
$$

ordered pairs with no ace.

Therefore

$$
P(C_2) = 1 - \frac{2304}{2704}
$$

$$
P(C_2) = \frac{400}{2704}
$$

which simplifies to

$$
\frac{25}{169}
$$

---

# Two cards drawn (without replacement)

Now the first card is **not returned to the deck**.

Total outcomes:

$$
|\Omega_2'| = 52 \times 51 = 2652
$$

---

## $A_3$ — both cards are hearts

First draw:

13 possible hearts.

Second draw:

12 remaining hearts.

So

$$
13 \times 12 = 156
$$

outcomes.

Therefore

$$
P(A_3) = \frac{156}{2652}
$$

which simplifies to

$$
\frac{1}{17}
$$

---

## $B_3$ — both cards have the same rank

For each rank:

First card → 4 choices  
Second card → 3 remaining cards of that rank

So

$$
4 \times 3 = 12
$$

pairs per rank.

Since there are 13 ranks

$$
13 \times 12 = 156
$$

outcomes.

So

$$
P(B_3) = \frac{156}{2652}
$$

which again simplifies to

$$
\frac{1}{17}
$$

---

## $C_3$ — one king and one queen (in any order)

Two possibilities:

(K,Q) or (Q,K)

Number of kings = 4  
Number of queens = 4

So

$$
4 \times 4 = 16
$$

pairs of type (K,Q)

and

$$
4 \times 4 = 16
$$

pairs of type (Q,K)

Total

$$
16 + 16 = 32
$$

So

$$
P(C_3) = \frac{32}{2652}
$$

which simplifies to

$$
\frac{8}{663}
$$

---

# Additional event on $\Omega_2'$

Let

$$
D
$$

be the event that **both cards have the same suit**.

For one suit:

First card → 13 choices  
Second card → 12 remaining cards of that suit

So

$$
13 \times 12 = 156
$$

pairs.

Since there are **4 suits**

$$
4 \times 156 = 624
$$

outcomes.

Therefore

$$
P(D) = \frac{624}{2652}
$$

which simplifies to

$$
\frac{4}{17}
$$

---

# Final remark

This problem illustrates how probabilities in card experiments are computed by **counting outcomes in the sample space**, taking into account whether draws are **with replacement or without replacement**.