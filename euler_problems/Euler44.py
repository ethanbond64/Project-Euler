def pentafunction(x):

    x = int(x)

    pentanum = (3 * (x**2) - x) / 2

    return pentanum


def backwardsPentfunction(pentanum):

    xx = (1 + (1 + 24 * pentanum)**(.5))/6

    return xx


for i in range(100):
    print(pentafunction(i))
    if (backwardsPentfunction(pentafunction(i)) == i):
        print(True)