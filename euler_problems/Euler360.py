import math
import time
r = 10**10
tic = time.time()
sq = [i**2 for i in range(1,10**8)]
toc = time.time()
print('Time taken to generate 10^8 primes: ',toc-tic)
sq2 = list(filter(lambda a: a > ((10**10/3)-1), sq))

# A summation where there are two equivalent paramters, ex a=b or b=c
# SPECIFIC MULTIPLIER = 3
twoEq = 0

# A summation where all parameters are equal a=b=c
# SPECIFIC MULTIPLIER = 1 ,, NO SPECIFIC MULITIPLIER
threeEq = 0



# The regular summation for when a<b<c
# SPECIFIC MULTIPLIER = 6
regSum = 0

# POSITIVE NEGATIVE MULTIPLIER = 8


# Loop through c, which is each val in sq
# Add to the three storage variables on a case basis
# Add local multipliers
# sum the 3
# Add global multiplier
# EL FIN
iters = 0
for c in sq2:
    iters += 1
    if iters % 1000 ==0:
        print(iters)

    i = sq.index(c)
    bMin = (r-c)//2

    if i != len(sq)-1:
        i += 1

    for b in sq[k:i]:
        if b < bMin:
            continue
        a = r - (b + c)
        if math.sqrt(a) % 1 == 0:
            if a == b and b == c:
                threeEq += abs(math.sqrt(a)) + abs(math.sqrt(b)) + abs(math.sqrt(c))
            elif a == b or b == c:
                twoEq += abs(math.sqrt(a)) + abs(math.sqrt(b)) + abs(math.sqrt(c))
            else:
                regSum += abs(math.sqrt(a)) + abs(math.sqrt(b)) + abs(math.sqrt(c))


#use multipliers
twoEq *= 3
regSum *= 6


finalTotal = regSum + twoEq + threeEq
finalTotal *= 8

print('final:',finalTotal)
