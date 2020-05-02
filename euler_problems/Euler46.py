

# use sieve function to generate a list of primes and a list on non primes
# then go through the odd non prime numbers and check with the primes
# recycled sieve logic from Euler41.py

nums = [x for x in range(10000)]
nums[1] = 0
for i in range(2,len(nums)):
    n = nums[i]
    if n != 0:
        for j in range(i*2,len(nums),i):
            nums[j] = 0

primes = list(filter(lambda x: x != 0, nums))
odd_composite = [idx for idx, a in enumerate(nums) if a == 0 and idx % 2 == 1 and idx >1]
# print(odd_composite[:20])

for k in odd_composite:
    valid = False
    for j in primes:
        if j > k:
            break
        d = ((k - j)/2)**0.5
        if d % 1 == 0:
            valid = True
            break
    if valid == False:
        print('Found it')
        print(k)
        break
        