import csv

Matrix = []
with open('E81matrix.txt','r') as matrrix:
    filereader = csv.reader(matrrix,delimiter=',')
    for row in filereader:
        newRow = []
        # print(row[0])
        for ii in row:
            newRow.append(int(ii))

        Matrix.append(newRow)

#True if side, False if down
def directionToGo(top3,mid2,bottom):
    sideDecision = True
    sideside = top3[1] + top3[2]
    sidedown = top3[1] + mid2[1]
    downside = mid2[0] + mid2[1]
    downdown = mid2[0] + bottom
    best = min([sideside,sidedown,downside,downdown])
    if best == downside or best == downdown:
        sideDecision = False
    return sideDecision

def edgeDirection(top2,mid2,bottom):
    edgeDecision = True
    sidedown = top2[1] + mid2[1]
    downside = mid2[0] + mid2[1]
    downdown = mid2[0] + bottom
    best = min([sidedown,downside,downdown])
    if best == downside or best == downdown:
        edgeDecision = False
    return edgeDecision

def bottomDirection(top3,mid2):
    sideDecision = True
    sideside = top3[1] + top3[2]
    sidedown = top3[1] + mid2[1]
    downside = mid2[0] + mid2[1]

    best = min([sideside,sidedown,downside,downdown])
    if best == downside or best == downdown:
        sideDecision = False
    return sideDecision

roww = 0
coll = 0
summ = 0
while roww != 79 and coll != 79:
    print(roww,coll)
    val = Matrix[roww][coll]
    summ += val
    if roww < 78 and coll < 78:
        if (directionToGo(Matrix[roww][coll:(coll+3)],Matrix[roww+1][coll:(coll+2)],Matrix[roww+2][coll])) == True:
            coll += 1
        else:
            roww += 1
    elif roww == 78 and coll < 78:
        if (bottomDirection(Matrix[roww][coll:(coll+3)],Matrix[roww+1][coll:(coll+2)])) == True:
            coll += 1
        else:
            roww += 1
    elif roww < 78 and coll == 78:
        if (edgeDirection(Matrix[roww][coll:(coll+2)],Matrix[roww+1][coll:(coll+2)],Matrix[roww+2][coll])) == True:
            coll += 1
        else:
            roww += 1
    elif roww == 79 and coll != 79:
        coll += 1
    elif roww != 79 and coll == 79:
        roww += 1
    else: #roww == 78 and coll == 78
        if Matrix[roww][coll+1] > Matrix[roww+1][coll]:
            summ += Matrix[roww+1][coll] + Matrix[roww+1][coll+1]
        else:
            summ += Matrix[roww][coll+1] + Matrix[roww+1][coll+1]
        break
print(summ)
