## Task 3 — Drawing Cards

Experiment: drawing cards from a standard 52-card deck.

Important assumption: the order of outcomes matters.  
Each outcome is treated as an ordered sequence of drawn cards.

Note: A standard deck contains 52 cards:
- 4 suits (♠, ♥, ♦, ♣)
- 13 ranks (A,2,...,10,J,Q,K)

Total = 52 cards.


## 1. Sample space Ω₁ (drawing one card)

If we draw one card, any card from the deck may appear.

So the sample space contains all 52 cards.

Examples of outcomes:

| Example |
|---|
| A♠ |
| 7♥ |
| Q♦ |
| 10♣ |

We can write the sample space symbolically as

$$
\Omega_1 = \{c_1, c_2, ..., c_{52}\}
$$

Number of elementary outcomes:

$$
|\Omega_1| = 52
$$

Note: I first thought whether we should list every card explicitly,  
but since there are 52 cards it is easier to represent them as  
\(c_1,c_2,...,c_{52}\).

Each outcome simply means **one specific card drawn from the deck**.


## 2. Sample space Ω₂ (two draws with replacement)

Now we draw two cards **with replacement**.

That means:
1. draw a card
2. record it
3. put it back into the deck
4. draw again

So the second draw is again from the full deck of 52 cards.

Note: I reminded myself that replacement means the first card does not affect the second draw.

Each outcome is therefore an **ordered pair of cards**.

Examples:

| First draw | Second draw | Outcome |
|---|---|---|
| A♠ | K♥ | (A♠,K♥) |
| 7♦ | 7♦ | (7♦,7♦) |
| Q♣ | 2♠ | (Q♣,2♠) |

Note: outcomes like (7♦,7♦) are possible here because the card is returned to the deck.

Mathematically:

$$
\Omega_2 = \{(c_i,c_j) : i,j \in \{1,...,52\}\}
$$

Number of elementary outcomes:

$$
|\Omega_2| = 52 \times 52 = 2704
$$

Note: I used the multiplication rule:  
52 choices for the first draw and 52 for the second.


## 3. Sample space Ω₂′ (two draws without replacement)

Now we draw two cards **without replacement**.

That means the first card is removed from the deck.

So after the first draw there are only **51 cards left**.

Note: this was the key difference from the previous case.

Examples:

| First draw | Second draw | Outcome |
|---|---|---|
| A♠ | K♥ | (A♠,K♥) |
| Q♦ | 10♣ | (Q♦,10♣) |

But outcomes like

(A♠,A♠)

are impossible because the card is not returned to the deck.

Mathematically we write

$$
\Omega_2' = \{(c_i,c_j) : i,j \in \{1,...,52\}, i \ne j\}
$$

Number of elementary outcomes:

$$
|\Omega_2'| = 52 \times 51 = 2652
$$

Note: I also checked that the order still matters.

For example

(A♠,K♥)

and

(K♥,A♠)

are different outcomes because the first card drawn is different.


## 4. Number of elementary outcomes

| Case | Formula | Count |
|---|---|---|
| With replacement | 52 × 52 | 2704 |
| Without replacement | 52 × 51 | 2652 |

Note: with replacement we have more outcomes because the same card can appear twice.


## 5. Meaning of an elementary outcome

An elementary outcome represents one complete result of the experiment.

Examples:

A♠  
→ one card drawn.

(A♠,K♥)  
→ first card A♠, second card K♥.

(Q♦,10♣)  
→ first card Q♦, second card 10♣.

Note: an elementary outcome describes exactly one possible way the experiment could happen.