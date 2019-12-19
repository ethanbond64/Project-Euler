ran = list(range(1, 999))
list.reverse(ran)
largest = 0
for i in ran:
    for n in range(2,i) :
        forward = str(i*n)
        reverse = forward[::-1]
        if forward == reverse:
            if largest < (i*n):
                largest = (i*n)
print(largest)
