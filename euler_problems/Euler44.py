def pentafunction(x):

    pentanum = (3 * (x**2) - x) / 2

    return pentanum


def backwardsPentfunction(pentanum):

    xx = (1 + (1 + 24 * pentanum)**(.5))/6

    return xx

pent_nums = []
for i in range(10000):
    pent_nums.append(pentafunction(i))


for i in range(1,len(pent_nums)):
    for j in range(i,len(pent_nums)):
        x = pent_nums[j] - pent_nums[i]
        if backwardsPentfunction(x) % 1 == 0:
            # print('diff')
            y = pent_nums[i] + pent_nums[j]
            if backwardsPentfunction(y) % 1 == 0:
                print(pent_nums[j]-pent_nums[i])
                break
