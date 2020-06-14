#ks = [1,2k,1 for k in range50][:98] 
ks = []
for i in range(1,50):
    ks.append(1)
    ks.append(2*i)
    ks.append(1) 


n = 9
num = [2,3,8,11,19,87,106,193]
den = [1,1,3,4,7,32,39,71]



#break when n == 100
while True:
    if n > 100:
	break
    
    num.append((ks[n-2]*num[-1])+num[-2])
    den.append((ks[n-2]*den[-1])+den[-2])

    n += 1

print(num)
print(len(num))

print('ans')
ans = sum([int(a) for a in list(str(num[-1]))])
print(ans)
