import copy
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

dic = {}
for idx, k in enumerate(nuPrimes):
    x = sorted(str(k))
    for j in nuPrimes[idx+1:]:
        if sorted(str(j)) == x:
            t = str(x)[1:-1].replace(', ','').replace("'",'')
            if t in dic:
                dic[t].append(j)
            else:
                dic[t] = [k,j]

d = copy.deepcopy(dic)

for key in d:
    if len(dic[key]) < 3:
        del dic[key]
    else:
        dic[key] = list(set(dic[key]))
        dic[key] = sorted(dic[key])
        ll = dic[key]
        for el in ll:
            diffs = []
            for el2 in ll:
                if el == el2:
                    pass
                if abs(el-el2) in diffs:
                    print(ll,abs(el-el2))
                diffs.append(abs(el-el2))

# print(dic)

