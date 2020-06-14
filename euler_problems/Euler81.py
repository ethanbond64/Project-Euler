import csv

NROWS = 80
NCOLS = 80


Matrix = []
with open('E81matrix.txt','r') as matrrix:
    filereader = csv.reader(matrrix,delimiter=',')
    for row in filereader:
        newRow = []
        # print(row[0])
        for ii in row:
            newRow.append(int(ii))

        Matrix.append(newRow)
# print(Matrix)
trMat = []
for r in Matrix:
    trMat += r
Matrix = trMat
# print(Matrix)
def toRow(idx):
    return idx // (NROWS)

def toCol(idx):
    return idx % (NCOLS)

# row and col are 0 indexed
def toIdx(row,col):
    return row*NROWS + col

parentPointers = [None]*(NCOLS*NROWS)
minPathWeights = [0]*(NCOLS*NROWS)
for i in range(len(Matrix)):
    r = toRow(i)
    c = toCol(i)

    parentWeights = 0

    if r == 0 and c == 0:
        parentWeights = 0
    elif r == 0:
        parentWeights = minPathWeights[i-1]
        parentPointers[i] = i-1

    elif c == 0:
        parentWeights = minPathWeights[i-NCOLS]
        parentPointers[i] = i-NCOLS

    else:
        leftParent = minPathWeights[i-1]
        upParent = minPathWeights[i-NCOLS]  
        
        if upParent < leftParent:
            parentWeights = upParent
            parentPointers[i] = i-NCOLS
        else:
            parentWeights = leftParent
            parentPointers[i] = i-1

    minPathWeights[i] = parentWeights+Matrix[i]

print(minPathWeights[-1])
# print(parentPointers)
    

    
