import math

def nextPoint(a,b,m):
    c = a - m*b
    # Quadratic terms
    A = m**2 + 4
    B = 2*c*m
    C = c**2 - 100
    print(A,B,C)

    X1 = (-B + (B**2 - 4*A*C)**.5)/(2*A)
    X2 = (-B - (B**2 - 4*A*C)**.5)/(2*A)

    if abs(X1-a) > abs(X2-a):
        X = X1
    else:
        X = X2

    Y = m*(X - b) + a

    return X, Y

# m = old slope
def newSlope(m,x,y):
    tangent = -(4*x)/y
    normal = y / (4*x)


oldX = 0.0
oldY = 10.1
newX = 1.4
newY = -9.6
firstSlope = -1.5914673561732418

print(nextPoint(1.4,-9.6, -1.5914673561732418))
