import math
checker = True
num = int(input("print a number: "))
for i in range(2,int(math.sqrt(num))+1):
    if num%i == 0:
        checker = False
        break
print(checker)
# prints True if the value is prime, False if non-prime, does not work for 1
