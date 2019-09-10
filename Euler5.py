import time
def smallest_multiple(n):
    tick = time.time()
    factors = list(range(1, n + 1))

    number = 1

    smallMultiple = 0

    state = True

    while state == True:
         for i in factors:
            if number % i == 0 :
                if i == n :
                    smallMultiple = number
                    state = False
            else:
                number += 1
                break
    tock = time.time()
    totaltime = tock -tick
    print(totaltime)
    return smallMultiple
smallest_multiple(20)
