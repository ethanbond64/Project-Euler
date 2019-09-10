shorts = {1:1}
def collatzLen(n):
    count = 0
    while True:
        if n in shorts:
            return shorts[n] + count
        elif n % 2 == 0:
            count += 1
            n = n/2
        else:
            count += 1
            n = 3*n + 1
max = 0
best = 0
for i in range(2,1000000):
    j = collatzLen(i)
    if i not in shorts:
        shorts[i] = j
    if j > max:
        max = j
        best = i

print('Longest chain from starting number: ',best, ' With chain length: ', max)
