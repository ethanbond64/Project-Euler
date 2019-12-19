
def relativePrimes(input):
    rps = []
    for kk in range(input):
        if (kk/input)%1 == 0:
            rps.append(kk)

    return rps

divDict = {}
sortList = []
for pp in range(2,1000000):
    if pp % 1000 in [1,10,100,1000]:
        print(pp)
    nums = relativePrimes(pp)
    for ii in nums:
        sentence = str(ii) + '/' + str(pp)
        divDict[sentence] = (ii/pp)
        sortList.append(ii/pp)
sortList = sortList.sort()
indec = 0
useDis = 0
for gg in sortList:
    if gg == (3/7):
        print(indec)
        useDis = indec -1
        break
    indec += 1
for dd in divDict:
    if dd == sortList[useDis]:
        print(dd)
