def gcf(a,b):

    factorlist = []
    for ii in range(1,a + 1):
        if a % ii == 0:
            if b % ii == 0:
                factorlist.append(ii)
    return factorlist[-1]
def lcm(a,b):

    fin = a*b/gcf(a,b)

    return int(fin)
change = False
for jj in range(11,100):
    # print(kk)
    for kk in range(11,100):
        newk = kk
        newj = jj
        oldDiv = kk/jj
        # if (int(str(newk)[-1]) and int(str(newj)[-1])) == 0:
        if int(str(newk)[-1]) == int(str(newj)[0]):
            newk = int(str(newk)[0])
            newj = int(str(newj)[-1])
            change = True
            # print('2')
        elif int(str(newk)[0]) == int(str(newj)[-1]):
            newk = int(str(newk)[-1])
            newj = int(str(newj)[0])
            change = True
            # print('3')
        elif int(str(newk)[0]) == int(str(newj)[0]) and int(str(newk)[-1]) != int(str(newj)[-1]):
            newk = int(str(newk)[-1])
            newj = int(str(newj)[-1])
            change = True
            # print('4')
        else:
            pass
        if newj == 0:
            break
        else:
            newDiv = newk/newj
        if oldDiv == newDiv and change == True and kk != jj:
            print(oldDiv,newDiv)
            print(kk,'/',jj)
        change = False

# 16 / 64
1/4
# 26 / 65
2/5
# 19 / 95
1/5
# 49 / 98
1/2
# for bb in [64,64,95,98]:

# print(lcm(lcm(64,65),lcm(95,98)))
print(lcm(64,65))
print(lcm(64,95))
print(lcm(64,98))
print(lcm(4160,6080))
print(lcm(3136,79040))
