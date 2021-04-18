
# start n from 94745
# do prime factorization on n
# get set of prime factors
# make list ranging from 1 to n-1
# iterate over prime factors
# go through list mentioned and if number % factor == 0, number = -1
# remove all -1s from the list and get the length
# winner has length less than 15499

# from stackoverflow
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return set(factors)


def nToNumerator(n):
    factors = prime_factors(n)
    k = n-1
    for f in factors:
        g = k//f
        k -= g
    return k

n = 94746
mint = 100

while True:

    if n % 10000 == 0:
        print(n)
        print("Thres", str(15499/94744))
        print("Mint",mint)

    # prime factors
    numerator = nToNumerator(n)
    if (numerator/(n-1)) < mint:
        mint = (numerator/(n-1))

    if (numerator/(n-1)) < (15499/94744):
        print('ANS')
        print(n)
        break
    
    n += 2


