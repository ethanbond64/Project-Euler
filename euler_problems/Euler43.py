import numpy as np
bot = 123456789
top = 9876543210

div = np.array([2,3,5,7,11,13,17])

res = [0,0,0,0,0,0,0]
sum = 0
for n in range(bot,top+1):
    if (top-n)%100000000 == 0:
        print(n) 
    n = str(n)
    if ''.join(sorted(n)) == '123456789' or ''.join(sorted(n)) == '0123456789':
        slices = []
        if len(n) == 9:
            n = '0' + n
        for k in range(1,8):
            slices.append(int(n[k]+n[k+1]+n[k+2]))
        slices = np.array(slices) / div
        if list(slices % 1) == res:
            sum += int(n)
            print('+1')
print('final answer',sum)
