i = 1
sum = 0
while True:
    i = i+1
    if i >= 1000:
        break
    if i%3 == 0:
        print(i)
        sum = sum + i
    elif i%5 == 0:
        print(i)
        sum = sum + i
    continue
print(sum)
