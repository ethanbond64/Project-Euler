twoPowers = []
for ii in range(21):
    twoPowers.append(2**ii)
twoPowers = twoPowers[::-1]


def toBin(num):
    #check first 20 binary bits
    standard = []
    for l in range(20):
        standard.append(0)
    if num % 2 == 1.0:
        standard[0] = 1
    for pp in range(len(twoPowers)):
        if num >= twoPowers[pp]:
            standard[20 - pp] = 1
            num -= twoPowers[pp]
    standard = standard[::-1]
    on = True
    binStr = ''
    for kk in standard:
        if kk != 1 and on == True:
            pass
        else:
            binStr += str(kk)
            on = False

    return binStr


pList = []

ran = list(range(1,1000001))
for i in ran:
    forward = str(i)
    reverse = forward[::-1]
    if forward == reverse:
        pList.append(i)

summ = 0
for tt in pList:
    bin = toBin(int(tt))
    if bin == bin[::-1]:
        print(bin,tt)
        summ += int(tt)
print(summ)
