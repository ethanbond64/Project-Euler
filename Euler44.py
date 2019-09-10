def pentafunction(x):

    x = int(x)

    pentanum = (3 * (x**2) - x) / 2

    return pentanum

def subtFunction(n, d):
    # n is the index of the smaller pentagonal number
    # d is the difference d = m - n, where m is the larger pentagonal number

    subt = (d * 3) * n + pentafunction(d)

    return subt

def backwardsPentfunction(pentanum):

    xx = (1 + (1 + 24 * pentanum)**(.5))/6

    return xx

print(backwardsPentfunction(145))

# checker = True
# while checker == True:
#     point = 2
#     for dd in range(0, point):
#         if backwardsPentfunction(subtFunction(point, dd)) % 1 == 0:
#             print(subtFunction(point,dd))
