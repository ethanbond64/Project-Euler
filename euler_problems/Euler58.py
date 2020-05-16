# i*2 + 1 = ans

# generate primes

def isPrime(x):
    for i in range(2, int((x)**0.5)+1):
        if x % i == 0:
            return False
    return True 

# round 1 complete
diag = [1,3,5,7,9]

k = 8

a = 3
b = 5

for i in range(2,14000):
    # s_diag = []
    for j in range(4):
    #     s_diag.append(diag[j-4]+k+2*(1+j))
    # diag += s_diag
        k += 2
        diag.append(diag[-4]+k)
        if isPrime(diag[-1]):
            a += 1
    b += 4
    # print(a/b)
    if a/b < 0.1:
        print(i*2 +1)
        break
# print(diag)
