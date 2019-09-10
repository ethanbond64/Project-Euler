import numpy as np
import math

def angle(v1, v2):
  return math.acos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

count = 0

#open file
with open('p102_triangles.txt','r') as file:
    for line in file:
        currentLine = line.split(',')
        one = [int(currentLine[0]),int(currentLine[1])]
        two = [int(currentLine[2]),int(currentLine[3])]
        three = [int(currentLine[4]),int(currentLine[5])]
        print(one,two,three)

        top = np.array(one)
        bottom = np.array(one)
        mid = np.array(one)
        for x in [two,three]:
            if x[1] > top[1]:
                top = np.array(x)
            if x[1] < bottom[1]:
                bottom = np.array(x)
            else:
                mid = np.array(x)

        mainVec = top-bottom

        botVec = mid-bottom
        botRefVec = -1*bottom

        topVec = mid-top
        topRefVec = -1*top

        if np.linalg.norm(botVec) > np.linalg.norm(botRefVec) and abs(angle(botVec,mainVec)) > abs(angle(botRefVec,mainVec)):
            count += 1

        if np.linalg.norm(topVec) > np.linalg.norm(topRefVec) and abs(angle(topVec,(mainVec*(-1)))) > abs(angle(topRefVec,(mainVec*(-1)))):
            count += 1

        print(coun)

print(count)
