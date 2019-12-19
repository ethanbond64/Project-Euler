import math
summ = 0
num = 2
primeIndex = 0
while num < 2000000:
    checker = True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            checker = False
            continue
    if checker == True:
        summ += num
        primeIndex += 1
    num += 1

print(summ)
