maxx = 0
bestP = 0
for p in range(12,1000):
    count = 0
    for c in range(p//3,p//2):
        for a in range(1,min(p//3,c//2)):
            # print('x')
            # if c == 5:
                # print(a,(p-c-a),c)
            if a**2 + (p-c-a)**2 == c**2:
                count += 1
                # if p == 420:
                #     print(a,(p-c-a),c)
    if count > maxx:
        maxx = count
        bestP = p
print(bestP,maxx)
