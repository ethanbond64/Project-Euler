max = 0
for i in range(1,100):
    if i % 10 == 0:
        print(i)
    for k in range(1,100):
        num = i ** k
        num = str(num)
        total = 0
        for j in num:
            total += int(j)
        if total > max:
            max = total
print(max)
