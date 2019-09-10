# Euler Project 42 Triangle numbers and words

wordList = open("eulerWords.txt")

def checkTriangle(numero):
    val = False
    x = (-1 + (1 + 8*numero)**(.5))/2
    if x % 1 == 0.0:
        val = True
    return val

letterValues = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,\
'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,\
'V':22,'W':23,'X':24,'Y':25,'Z':26,',':11}

count = 0
triangleTest = 0
tempword = ''
for container in wordList:
    for char in container:
        if char == "\"" :
            print(tempword)
            if checkTriangle(triangleTest) == True and tempword != ",":
                count += 1
            triangleTest = 0
            tempword = ""
        else:
            triangleTest += letterValues[char]
            tempword += char
print(checkTriangle(11))
print(count)
