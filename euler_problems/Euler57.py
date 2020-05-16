a = 3
b = 2

total = 0

for i in range(1000):
    if len(str(a)) > len(str(b)):
        total += 1

    c = a + b
    a = c + b
    b = c

print(total)