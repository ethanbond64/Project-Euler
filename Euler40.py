dec = ''
for k in range(1,200000):
    dec += str(k)
x = int(dec[0])*int(dec[9])*int(dec[99])*int(dec[999])*int(dec[9999])*int(dec[99999])*int(dec[999999])
print(x)
