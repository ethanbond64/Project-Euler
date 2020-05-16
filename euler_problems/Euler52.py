i = 1
def tryIt(x,j):
    return sorted(str(x)) == sorted(str(x*j))

while True:
    if tryIt(i,2):
        print(i)
        found = True
        for k in range(3,7):
            if tryIt(i,k) == False:
                found = False
                break
        
        if found:
            print('Found It',i)
            break
    # if i == 1000000:
    #     break
    i += 1
