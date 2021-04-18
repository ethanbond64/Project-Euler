import os
import math

def get_exp(a,n):
    return math.log(a,2) * n

file = open(os.path.split(os.path.abspath(__file__))[0] + '/p099_base_exp.txt','r')

lines = file.readlines()

max_val,max_i = 0, 0

for i, line in enumerate(lines):
    a = int(line.split(',')[0])
    n = int(line.split(',')[1])
    val = get_exp(a,n)

    if val > max_val: 
        # print(i,': ',a,n,' = ',val)
        max_val = val 
        max_i = i

# Line numbers index starts at 1
max_i += 1
print(max_i,max_val)