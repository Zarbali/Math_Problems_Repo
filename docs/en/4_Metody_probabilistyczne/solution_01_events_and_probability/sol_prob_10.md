# Problem 10 – Letter Sequences

Only three possible sequences can be transmitted:

AAAA with probability 0.4  
BBBB with probability 0.3  
CCCC with probability 0.3

During transmission every letter can be received incorrectly because of interference.

The probabilities for one letter are given in the table.

| sent \ received | A | B | C |
|---|---|---|---|
| A |0.8|0.1|0.1|
| B |0.1|0.8|0.1|
| C |0.1|0.1|0.8|

We assume the errors of different letters are independent.

We want the probability of receiving:

AAAA  
ACAA

## First observations

note: even if we receive a certain sequence, it might not be the same as the one that was originally transmitted because letters can change during transmission.

note: since we do not know which sequence was sent, we must consider all three possibilities (AAAA, BBBB, CCCC) and combine them using the total probability idea.

note: because the letters are independent, the probability of receiving a full sequence is the product of the probabilities for the individual letters.

## 1. Probability of receiving AAAA

First consider the case where AAAA was sent.

Each A must be received correctly.

Probability for one letter:

A → A = 0.8

For four letters:

$$
0.8^4 = 0.4096
$$

Next consider the case where BBBB was sent.

Each B must change into A.

B → A = 0.1

For four letters:

$$
0.1^4 = 0.0001
$$

The same happens if CCCC was sent.

Each C must change into A.

$$
0.1^4 = 0.0001
$$

Now combine the three possibilities using their prior probabilities.

$$
P(AAAA)=0.4096\cdot0.4+0.0001\cdot0.3+0.0001\cdot0.3
$$

$$
=0.16384+0.00003+0.00003
$$

$$
=0.1639
$$


## 2. Probability of receiving ACAA

Now we analyze the sequence position by position.

### If AAAA was sent

The received sequence must be A C A A.

Position probabilities:

A > A = 0.8  
A > C = 0.1  
A > A = 0.8  
A > A = 0.8

Multiply them:

$$
0.8\cdot0.1\cdot0.8\cdot0.8=0.0512
$$

### If BBBB was sent

B > A = 0.1  
B > C = 0.1  
B > A = 0.1  
B > A = 0.1

$$
0.1^4=0.0001
$$

### If CCCC was sent

C > A = 0.1  
C > C = 0.8  
C > A = 0.1  
C > A = 0.1

$$
0.1\cdot0.8\cdot0.1\cdot0.1=0.0008
$$

Combine all three possibilities.

$$
P(ACAA)=0.0512\cdot0.4+0.0001\cdot0.3+0.0008\cdot0.3
$$

$$
=0.02048+0.00003+0.00024
$$

$$
=0.02075
$$


## Final results

P(receive AAAA) = 0.1639

P(receive ACAA) = 0.02075


## Quick check

note: receiving AAAA is much more likely than ACAA because AAAA can occur when AAAA is transmitted correctly, which already has relatively high probability.