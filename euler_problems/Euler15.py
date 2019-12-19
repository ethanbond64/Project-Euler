l1 = [3,3]
l2 = []
while len(l1) < 39:
    l2.append(l1[0] + 1)
    for ii in range(1,len(l1)):
        l2.append(l1[ii] + l1[ii-1])
    l2.append(l1[-1] + 1)
    print(l2)
    l1 = l2
    l2 = []
print(l1[18])
print(l1[19])
print(l1[20])
