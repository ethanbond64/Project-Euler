# try brute force

def calc_triangle(x):
    return int(x*(x+1)/2)

def rev_pentagon(x):
    return (1 + (1 + 24*x)**(.5))/6
    

def rev_hexagon(x):
    return (1 + (1 + 8*x)**(.5))/4


for i in range(286,100000):
    if i % 100 == 0:
        print(i)
    x = calc_triangle(i)
    a = rev_hexagon(x) % 1 
    b = rev_pentagon(x) % 1
    if a == 0 and b == 0:
        print(i,x)
        break