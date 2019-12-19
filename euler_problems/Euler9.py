n = 1000

for b in range(2,n/2):
    for a in range(1,n/3):
        c = n-a-b
        if c < b :
            break
        if c == ((a**2)+(b**2))**(0.5):
            print (a*b*c)
