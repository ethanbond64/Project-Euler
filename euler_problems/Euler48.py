total = 0
for k in range(1,1001):
    total += k**k
print(str(total)[len(str(total))-10:])
