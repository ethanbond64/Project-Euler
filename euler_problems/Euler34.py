# 9999999 is tenative cap
import math
total = 0
for i in range(3,9999999):
    temp = 0
    # if i % 100000 == 0:
        # print('hundk')
    for x in str(i):
        temp += math.factorial(int(x))
    if temp == i:
        total += i
        print(i)
print(total)
