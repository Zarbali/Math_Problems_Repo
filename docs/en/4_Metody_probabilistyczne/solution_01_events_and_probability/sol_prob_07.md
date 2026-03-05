# Problem 07 – Signal Transmission

Two signals can be sent through the communication line:

111 or 000.

Prior probabilities:

P(sent 111) = 0.65  
P(sent 000) = 0.35

During transmission interference may flip symbols.

1 → 0 with probability 0.2  
0 → 1 with probability 0.2

So the probability that a symbol stays correct is 0.8.

Symbols are affected independently.

We need the probability of receiving:

111  
000  
010

## First observations

note: even if the receiver sees a certain code, it might not be the same as the one that was sent because each bit can flip.

note: since we don't know which signal was sent, we must consider both possibilities (111 and 000) and combine them using total probability.

To keep things clear I wrote the transition probabilities for one symbol:

| sent | received | probability |
|-----|-----|-----|
|1|1|0.8|
|1|0|0.2|
|0|0|0.8|
|0|1|0.2|

note: because the symbols are independent, the probability of a full code is the product of the probabilities of its three symbols.


## 1. Probability of receiving 111

Two situations can lead to receiving 111.

First case: 111 was sent and all three bits stayed correct.

$$
0.8^3 = 0.512
$$

Second case: 000 was sent but all three bits flipped.

$$
0.2^3 = 0.008
$$

Now apply total probability.

$$
P(111)=0.512\cdot0.65+0.008\cdot0.35
$$

$$
=0.3328+0.0028
$$

$$
=0.3356
$$

note: most of the probability comes from the case where 111 was actually sent.


## 2. Probability of receiving 000

Again we consider both possible transmitted signals.

If 111 was sent:

all three bits must flip.

$$
0.2^3 = 0.008
$$

If 000 was sent:

all three bits remain correct.

$$
0.8^3 = 0.512
$$

Total probability:

$$
P(000)=0.008\cdot0.65+0.512\cdot0.35
$$

$$
=0.0052+0.1792
$$

$$
=0.1844
$$


## 3. Probability of receiving 010

Now we look at the pattern 010.

If 111 was sent:

first bit correct  
second bit flipped  
third bit correct

$$
0.8\cdot0.2\cdot0.8=0.128
$$

If 000 was sent:

first bit flipped  
second bit correct  
third bit flipped

$$
0.2\cdot0.8\cdot0.2=0.032
$$

Now combine both cases.

$$
P(010)=0.128\cdot0.65+0.032\cdot0.35
$$

$$
=0.0832+0.0112
$$

$$
=0.0944
$$

## Final results

P(receive 111) = 0.3356

P(receive 000) = 0.1844

P(receive 010) = 0.0944

## Quick check

note: all probabilities lie between 0 and 1.

note: receiving 111 is most likely because the signal 111 is sent more often and the probability of correct transmission (0.8) is higher than the probability of flipping (0.2).