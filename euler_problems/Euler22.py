letters = {'A':1,
'B':2,
'C':3,
'D':4,
'E':5,
'F':6,
'G':7,
'H':8,
'I':9,
'J':10,
'K':11,
'L':12,
'M':13,
'N':14,
'O':15,
'P':16,
'Q':17,
'R':18,
'S':19,
'T':20,
'U':21,
'V':22,
'W':23,
'X':24,
'Y':25,
'Z':26}

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

count = 0
final = 0
with open('p022_names.txt','r') as file:
    for line in file:
        currentLine = line.split(',')
        print(len(currentLine))
        currentLine = bubbleSort(currentLine)
        for word in range(len(currentLine)):
            count += 1
            name = currentLine[word][1:-1]
            val = 0
            for let in name:
                val += letters[let]
            final += count * val

print(final)

temp = ''
swaps = 1
