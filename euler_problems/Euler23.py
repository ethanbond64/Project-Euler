import math
def isAbundent(k):
    divs = [1]
    s = math.sqrt(k)
    if s % 1 == 0:
        s = int(s + 1)
    else:
        s = int(math.ceil(s))
    for j in range(2,s):
        if k % j == 0:
            divs.append(j)
            divs.append(int(k/j))

    # print(k,' Factors: ',set(divs))
    if sum(set(divs)) > k:
        return True
    else:
        return False
#
# inputnum = int(input('Enter a number: '))
# print(isAbundent(inputnum))
#
#







abundents = [12]

for g in range(13,28124):
    if isAbundent(g) == True:
        print(g)
        abundents.append(g)

print('Abundents found')
# print(abundents)
diffs = []
for k in range(len(abundents)-1):
    diffs.append(abundents[k+1]-abundents[k])
print(diffs)

nums = []
for n in range(1,28124):
    if n % 1000 == 0:
        print(n)
    good = True
    for a in abundents[:int((len(abundents)/2)+1)]:
        if n != a:
            if (n - a)/abs(n - a) == -1:
                break
            elif (n - a) in abundents:
                good = False
                break
    if good == True:
        nums.append(n)

print('Answer: ',sum(nums))
