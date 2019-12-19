import math

num = 21
add = 7
while True:
    if num % 1000 == 0:
        print(num)

    count = 2
    top = math.floor(math.sqrt(num))
    for i in range(2,top+1):
        if num % i == 0:
            count += 2
    if count > 500:
        print('Answer: ',num)
        break

    num += add
    add += 1
