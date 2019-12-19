#solved in a way that will solve euler 67
import statistics as s

with open('p067_triangle.txt') as f:
    tri = f.readlines()
tri = [list(map(int,x.strip().split())) for x in tri]

i = 0
totalSum = tri[0][0]
#iterate on the row to decide on
for row in range(1,len(tri)-3):
    leftSum = 0
    rightSum = 0
    # tempSum = 0

    # differenceA = abs(tri[row][i] - tri[row][i+1])/100#(tri[row][i] + tri[row][i+1])

    for k in range(4):
        leftSum += tri[row+k][i] * (6-k)

        rightSum += tri[row+k][i+k+1] * (6- k)
        # tempSum += tri[row+k][i] + tri[row+k][i+k]

    # differenceB = abs(leftSum - rightSum)/tempSum#(leftSum + rightSum)

    # print(differenceA)
    # print(differenceB)
    # if differenceA > differenceB:
    #     if tri[row][i] < tri[row][i+1]:
    #         i += 1
    # else:
    if leftSum < rightSum and tri[row][i] < tri[row][i+1]:
        i += 1
    # else if (leftSum < rightSum and tri[row][i] > tri[row][i+1]) or (leftSum > rightSum and tri[row][i] < tri[row][i+1]):

    # print(tri[row][i])
    totalSum += tri[row][i]
    # print('---')

bpoint = len(tri)-4
final8 = []
for j in range(2):
    for k in range(2):
        for l in range(2):
            final8.append(tri[bpoint+1][i+j]+tri[bpoint+2][i+j+k]+tri[bpoint+3][i+j+k+l])
totalSum += max(final8)

print(totalSum)
