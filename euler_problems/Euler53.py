x = 1
facs = [1]
for i in range(1,101):
    x *= i
    facs.append(x)

total = 0
for n in range(1,101):
    for r in range(n+1):
        if (facs[n]/facs[r])/facs[n-r] > 1000000:
            total += 1
print(total)