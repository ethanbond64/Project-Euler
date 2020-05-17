# a^2 + b^2 = c^2

n = 1000
for n in range(11,1000):
    sq = False
    for b in range(2, int(n/2)+1):
        for a in range(1, int(n/3)+1):
            c = n-a-b
            if c < b:
                break
            if c == ((a**2)+(b**2))**(0.5):
                # print(a,b,c)
                print(a+b+c)
                sq = True
                break
        if sq:
            break
