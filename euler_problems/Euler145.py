import math
import time

sumation = 0
n = 10000000
checks = [0]*(n+1)
t0 = time.time()
for i in range(n):
    # print(i)s
    # Check for leading/trailing zero
    if i % 10 == 0:
        continue
    rev = int(str(i)[::-1]) 
    if checks[i] == 1: 
        # print('WOooooooooooooooooooooooooooooo')
        continue
    comp = i + rev
    # print(i,int(str(i)[::-1]))
    cont = False
    # print(comp)
    for j in str(comp):
        if int(j)%2 == 0 :
            cont = True
            break
    if cont:
        continue

    checks[rev] = 1
    sumation += 2
    # print('yee',i)

t1 = time.time()
print(sumation)
print(t1-t0)