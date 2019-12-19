import math
primes = []
num = 2

while len(primes) < 100001:
    checker = True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            checker = False
            continue
    if checker == True:
        primes.append(num)
    num += 1

smolList = []
for pp in primes:
    if pp < 1000000:
        smolList.append(pp)

print(smolList)
