from itertools import permutations
megaList = []
def permMaker(digs):
    print(digs)
    elif len(digs) == 1:
        pass
    else:
        for i in range(len(digs)):
            removedList = digs[:i] + digs[i+1:]
            z = permMaker(removedList)
            print(digs)
            print(digs[:i]," ",digs[i+1:])

        megaList.append(digs[i] + z)
print('beginning')
f = ['0','1','2','3','4','5','6','7','8','9']
permMaker(f)

def bubbleSort(liz):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for ii in range(len(liz)-1):
            if liz[ii] > liz[ii+1]:
                temp = liz[ii]
                liz[ii] = liz[ii+1]
                liz[ii+1] = temp
                swaps += 1
    return liz
print("sorting time")
megaList = bubbleSort(megaList)
print('Millionth! is: ',megaList[999999])
