import time
import pickle
tic = time.time()

# Create the list of primes from 10M to 20M
nums = [x for x in range(2*10**7)]
nums[1] = 0
for i in range(2,len(nums)):
    if i % (5*10**6) == 0:
        print(i)
    cur = nums[i]
    if cur != 0:
        for j in range(i*2,len(nums),i):
            nums[j] = 0

primes = list(filter(lambda x: x != 0 and x > 10**7, nums))
toc = time.time()
timee = (toc-tic)/60
print('Minutes: ',timee)
# with open('primesTo20M.pkl','wb') as file:
#     pickle.dump(primes,file)
# print('pickled!')
print(primes[:100])


# Use storage in a 8X6 matrix to find transitions, sum for sam, array for max
# C4 convention for the first four which are vertical 5,6,7 are top bottom middle
transitions = {
    '0':[1,1,1,1,1,0,1],
    '1':[1,0,0,1,0,0,0],
    '2':[1,0,1,0,1,1,1],
    '3':[1,0,0,1,1,1,1],
    '4':[1,1,0,1,0,1,0],
    '5':[0,1,0,1,1,1,1],
    '6':[0,1,1,1,1,1,1],
    '7':[1,1,0,1,1,0,0],
    '8':[1,1,1,1,1,1,1],
    '9':[1,1,0,1,1,1,1]
}

# xor for LISTS a and b
def xor(a,b):
    total = 0
    for k in range(len(a)):
        if a[k] == b[k]:
            total += a[k]
    return total

# returns a list of the digital roots down to a single digit (includes original)
def roots(x):
    s = str(x)
    r = [s]
    while len(s) > 1:
        new = 0
        for dig in s:
            new += int(dig)
        s = str(new)
        r.append(s)
    return r

def numToMaxmat(num):
    num = str(num)
    mat = []
    if len(num) == 8:
        for dig in num:
            mat.append(transitions[dig])
    else:
        for k in range(8-len(num)):
            mat.append([-1,-1,-1,-1,-1,-1,-1,])
        for g in range(len(num)):
            mat.append(transitions[num[g]])
    return mat

samTotal = 0
maxTotal = 0
iters = 0

print('Beginning the clocks')
# loop through the primes
for feed in primes:

    iters += 1
    if iters % 10000 == 0:
        print(iters)

    # fullFeed is a list of strings
    fullFeed = roots(feed)
    # print(feed)
    # print(fullFeed)

    # loop through the second to last numer in fullfeed
    lastSave = 0
    nextMat = numToMaxmat(fullFeed[0])
    for disp in range(len(fullFeed)-1):
        samCurrent = 0

        for dig in fullFeed[disp]:
            samCurrent += sum(transitions[dig])
        # print('sam:',samCurrent)
        samTotal += 2*samCurrent

        # Compute maxOn by finding the sum of all the positive ones in the matrix
        maxOn = 0
        maxmat = nextMat
        for place in maxmat:
            digOn = sum(place)
            if digOn > 0:
                maxOn += digOn
        # Set max off to the total number of segments that are turned on
        maxOff = maxOn
        # Subtract the amount that carried over from maxOn
        maxOn -= lastSave

        # find maxSave as the number of positive digits that are the same as the next in fullFeed
        maxSave = 0
        nextMat = numToMaxmat(fullFeed[disp+1])
        for p in range(8-len(fullFeed[disp+1]),8):
            if nextMat[p][0] != -1:
                maxSave += xor(nextMat[p],maxmat[p])

        maxOff -= maxSave
        # print('maxOn:',maxOn)
        # print('maxOff:',maxOff)

        maxTotal += maxOn + maxOff

        lastSave = maxSave

    # add the transitions from the final display to max,
    finMat = numToMaxmat(fullFeed[-1])
    finalMaxOn = 0
    for place in finMat:
        digOn = sum(place)
        if digOn > 0:
            finalMaxOn += digOn
    finalMaxOff = finalMaxOn
    finalMaxOn -= lastSave
    # print('maxOn:',finalMaxOn)
    # print('maxOff:',finalMaxOff)

    maxTotal += finalMaxOn +finalMaxOff

    #final sam
    samCurrent = 0
    for dig in fullFeed[-1]:
        samCurrent += sum(transitions[dig])
    samTotal += 2*samCurrent

print('Finished!')
difference = samTotal - maxTotal
print('Difference: ',difference)






























# bottom
