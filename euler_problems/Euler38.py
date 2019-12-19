correct = {
'1':1,
'2':1,
'3':1,
'4':1,
'5':1,
'6':1,
'7':1,
'8':1,
'9':1
}
pans = []

for i in range(99999):
    counts = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
    }
    s = ''
    k = 1
    while True:
        s += str(k*i)
        if len(s) > 9 or '0' in s:
            break
        elif len(s) == 9:
            for char in s:
                counts[char] += 1
            if counts == correct:
                print(s)
                pans.append(int(s))
            break
        k += 1

print('max: ',max(pans))
