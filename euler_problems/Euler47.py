nums = [x for x in range(10000)]
nums[1] = 0
for i in range(2,len(nums)):
    n = nums[i]
    if n != 0:
        for j in range(i*2,len(nums),i):
            nums[j] = 0

primes = list(filter(lambda x: x != 0, nums))

consecutives = []
for i in range(1000000):
    if i % 10000 == 0:
        print(i)
    factors = []
    x = i
    valid = False
    for p in primes:
        if p > i or x == 1:
            break
        if x % p == 0:
            x = x/p
            factors.append(p)
    if len(set(factors)) == 4:
        valid = True
    consecutives.append(valid)
    if consecutives[-4:] == [True,True,True,True]:
        print('Found It')
        print(i-3)
        break

