#Use sieve to generate all primes less than 987654321
import numpy as np
n = 987654321
largeModified = int((n)**(.5))
booleanlist = np.zeros(largeModified)
PrimeList = []
PrimeFactors = []


# creates list of boolean values for the sieve function
for kk in range(0, largeModified):
    booleanlist[kk] = True

booleanlist[0] = 0
booleanlist[1] = 0

# this is the main component of the sieve function, removes all multiples of
#prime values
for n in range( len(booleanlist)):
    if booleanlist[n] == True:
        for ii in range(0, largeModified+1, n):
            index1 = n**2 + ii*n
            booleanlist[index1] = False

#This loop makes a list of all the indexes of the booleanlist that are prime
for ll in range(0,len(booleanlist)):
    if booleanlist[ll] == True:
        PrimeList.append(ll)

finlist = []
for prime in PrimeList:
    prime = str(prime).split()
    print(prime)
    checker = False
    for dig in range(1,len(prime)):
        if prime.count(dig) == 1:
            checker = True
        else:
            checker = False
            break
    if checker == True:
        finlist.append(prime)
print(finlist)
