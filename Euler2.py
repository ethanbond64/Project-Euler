fib = 1
fib2 = 2
temp = 0
total = 0

while temp <=4000000:
    temp = fib2
    if temp % 2 == 0:
        total += temp
    temp = fib + fib2
    fib = fib2
    fib2 = temp

print (total)
