
# start with a prime
i = 13

primes = [2,3,5,7,11]
truncs = []

def isTrunc(i,primes):
    i = str(i)
    passing = True
    for dig in range(1,len(i)):
        if int(i[dig:]) not in primes or int(i[:dig]) not in primes:
            passing = False
            break

    return passing

# while loop that increments
while len(truncs) <= 10:

    if i % 10000 == 0:
        print('i: ',i)

    prime = True
    for j in primes:
        if i % j == 0:
            prime = False
            break

    if prime == True:
        if isTrunc(i,primes) == True:
            print(i,len(truncs))
            truncs.append(i)
        primes.append(i)

    i += 1

print('Total: ',sum(truncs))
