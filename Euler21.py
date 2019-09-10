
def divisorSum(x):
    factors = []
    for ii in range(1,(x//2)+1):
        if x%ii == 0:
            factors.append(ii)
    summ = sum(factors)
    return summ

bigList = [0]
for pp in range(1,10001):
    bigList.append(divisorSum(pp))

amicableSum = 0
for dd in range(1,10001):
    check = bigList[dd]
    if check < 10001 and bigList[check] == dd and dd != bigList[dd]:
        print(dd,bigList[dd])
        amicableSum += dd
print(amicableSum)
