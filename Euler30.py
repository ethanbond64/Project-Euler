test = 2
answers = []
finalans = 0
while len(answers) < 6:
    teststr = str(test)
    tempSum = 0
    for kk in range(len(teststr)):
        tempSum += int(teststr[kk]) ** 5
    if tempSum == test:
        answers.append(test)
        print(answers)
    test += 1
for ii in range(0,len(answers)):
    finalans += answers[ii]
print(finalans)
