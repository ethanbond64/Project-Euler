nums = [x for x in range(1000000)]
nums[1] = 0
for i in range(2,len(nums)):
    cur = nums[i]
    if cur != 0:
        for j in range(i*2,len(nums),i):
            nums[j] = 0

print('primes are ready')
primes = list(filter(lambda x: x != 0 and x > 100, nums))

circs = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

for p in primes:
    if p not in circs:
        p = str(p)
        temp = []
        for c in range(1,len(p)):
            if int(p[c:] + p[:c]) in primes:
                temp.append(int(p[c:] + p[:c]))
            else:
                break
        if len(temp) == (len(p)-1):
            circs.append(int(p))
            circs += temp
            print(circs)
print(len(circs))
