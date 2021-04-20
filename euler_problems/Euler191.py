from math import comb,ceil
import numpy as np

def fill(o,s):
    return 100

def get_sequences(n):

    # Key is the # of tokens in the sequence, values is the number of possibles sequences under this constraint
    sequences = {}

    if n == 0:
        return {0:1} 

    a = ceil(n/2)
    
    if n > 15:
        b = (30-n)+1
    else:
        b = n

    for i in range(a,b+1):
        dbls = n-i
        singles = i-dbls
        sequences[i] = comb(i,singles)

    return sequences



fill_cache = np.zeros((31,16))

total_strings = 0

for a in range(21):
    o = 30-a
    sequences = get_sequences(a)
    for i_tokens in sequences:
        # The number of possible sequences of JUST letter A made up of i_tokens amount of tokens, where a token is A or AA
        m_ways = sequences[i_tokens]
        
        # The number of possible ways to fill the gaps of the As, when given a string of i_tokens length A tokens
        n_ways = fill_cache[o,i_tokens]
        if n_ways == 0:
            n_ways = fill(o,i_tokens)
            fill_cache[o,i_tokens] = n_ways
        
        n_ways *= m_ways
        n_ways *= o

        total_strings += n_ways

print('done')
# print(fill_cache)
print(total_strings)

print(get_sequences(5))
print(get_sequences(6))
print(get_sequences(7))
print(get_sequences(8))
print(get_sequences(20))
print(get_sequences(19))