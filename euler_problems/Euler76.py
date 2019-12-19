# iter = 4
# f1 = 2
# f2 = 2
# for ii in range(100):
#     next = f1 +f2
#     f2 = f1
#     f1 = next
#     print(iter,f1)
#     iter += 1
iter = 3
q = 2
sum = 2
for ii in range(100):
    if iter%2 ==1:
        sum += (iter-1)
    else:
        sum += iter/2
    iter += 1
    print(iter,sum)
