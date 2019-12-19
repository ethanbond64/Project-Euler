def digitSquares(x):
    y = str(x)
    sum = 0
    while y not in ['1','89']:
        for ii in y:
            sum += int(ii)**2
        y = str(sum)
        sum = 0
    return y

# print(digitSquares(13))
# print(digitSquares(37))
count = 0
for ii in range(1,10000001):
    if digitSquares(ii) == '89':
        count += 1

print(count)
