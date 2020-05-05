nums = [x for x in range(1000000)]
nums[1] = 0
for i in range(2,len(nums)):
    n = nums[i]
    if n != 0:
        for j in range(i*2,len(nums),i):
            nums[j] = 0

primes = list(filter(lambda x: x != 0, nums))
print(len(primes))

# try first 1000 primes dp strategy
prev = primes[0]
cache = [[prev]]

for p in primes[1:1000]:
    prev += p
    cache[0].append(prev)

for idx, p in enumerate(primes[:5]):
    row = [i-p for i in cache[idx]]
    cache.append(row)

# print(len(cache))
# print(len(cache[-1]))

mx = 0
best = 0
start = 0
for i1, row in enumerate(cache):
    for i2, el in enumerate(row):
        z = i2 - i1
        if z > mx:
            if el in primes and el < 1000000:
                mx = z
                start = i1
                best = el
                print(mx,i1,el)

print('fin')
print(mx,best)
