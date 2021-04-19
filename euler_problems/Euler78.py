import numpy as np


# def p(n):
#     sum = 0
#     a = n //2
    
#     # sum of 1 for range(1,a)
#     sum += (a-1)

#     # Middle number
#     if n % 2 == 1:
#         sum += (n-1)-a
#     else:
#         sum += n-a
    
#     # between n/2 and n
#     for i in range(a+1,n):
#         sum += n-i
    
#     # Case no spaces
#     sum += 1

#     return sum

f_mat = np.zeros((1001,1001))

def f(a,b):
    if f_mat[a,b] != 0:
        return f_mat[a,b]

    if b == 0 or b == 1:
        f_mat[a,b] = 1
        return 1

    if a > b:
        # print(a,b)
        f_mat[a,b] = f(b,b)
        return f_mat[a,b]
        
    new_sum = 0
    x = 0
    y = 0
    if a == b:
        new_sum += 1
        x = b-1
        y = 1
    else:
        x = a
        y = b-a
    
    while x > 0:
        # print('while',a,b)
        new_sum += f(x,y)
        x -= 1
        y += 1
    # print(a,b,new_sum)
    f_mat[a,b] = new_sum
    return new_sum

def p(n):
    main_sum = 0
    for k in range(n):
        main_sum += f(n-k,k)
        # print(n-k,k,'=',f(n-k,k))
    # print(k,p(k))
    return main_sum


# print(5,p(5))
# print(6,p(6))
# print(7,p(7))
# print(8,p(8))
# print(100,p(100))

for i in range(8,1001):
    # print(p(i)/1000000)
    if (p(i) / 1000000) % 1.0 == 0.0:
        print('ANSWER',i,p(i))
        break
    
    if i % 20 == 0:
        print(i)

# print(f_mat)
# print(f(2,2))
# print(f(5,2))