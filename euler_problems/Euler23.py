import math
def isAbundent(k):
    divs = [1]
    for j in range(2,math.ceil(math.sqrt(k))):
        if k % j == 0:
            divs.append(j)
            divs.append(int(k/j))
    if sum(divs) > k:
        return True
    else:
        return False

abundents = [12]

for g in range(13,28124):
    if isAbundent(g) == True:
        abundents.append(g)

print('Abundents found')
print(abundents[:10])
nums = []
for n in range(1,28124):
    if n % 1000 == 0:
        print(n)
    good = True
    for a in abundents:
        if n != a:
            if (n - a) in abundents:
                good = False
                break
            elif (n - a)/abs(n - a) == -1:
                break
    if good == True:
        nums.append(n)

print('Answer: ',sum(nums))
