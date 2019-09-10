import math
primes = [0]
num = 2
while primes[-1] < 10000:
    checker = True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            checker = False
            continue
    if checker == True:
        primes.append(num)
    num += 1
primes.remove(primes[-1])
nuPrimes = []
for x in primes:
    if x >= 1000:
        nuPrimes.append(x)

def permList()
