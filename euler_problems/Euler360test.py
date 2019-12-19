import math
r = 45

sq = [i**2 for i in range(r+1)]

# sq = list(filter(lambda a: a > ((45**2)/3)-1, sq))
# print(sq)
# print(sq)

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
for c in sq:
    iters += 1

    #Find the highest b can be, which is c
    i = sq.index(c)
    bMin = ((r**2)-c)//2

    if i != len(sq)-1:
        i += 1

    for b in sq[:i]:
        if b < bMin or (b+c) > (r**2):
            continue
        a = (r**2) - (b + c)
        if (a**.5) % 1 == 0:
            mag = (a+b+c)**.5
            if r == mag:
                print('----')
                print('a',a,'b',b,'c',c)
                if a == b and b == c:
                    print('Triple!')
                    threeEq += abs((a**.5)) + abs((b**.5)) + abs((c**.5))
                elif a == b or b == c:
                    print('Double!')
                    twoEq += abs((a**.5)) + abs((b**.5)) + abs((c**.5))
                    print(3*8*(abs((a**.5)) + abs((b**.5)) + abs((c**.5))))
                else:
                    regSum += abs((a**.5)) + abs((b**.5)) + abs((c**.5))
                    print(6*8*(abs((a**.5)) + abs((b**.5)) + abs((c**.5))))

#use multipliers
twoEq *= 3
regSum *= 6


finalTotal = regSum + twoEq + threeEq
finalTotal *= 8

print('final:',finalTotal)
print('off by ',abs(finalTotal-34518))
