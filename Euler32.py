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

for a in range(1,9999):
    for b in range(1,999):
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
        c = a*b
        if c not in pans:
            s = str(a) + str(b) + str(c)
            if '0' in s:
                continue
            for char in s:
                counts[char] += 1
            if counts == correct:
                print(s)
                pans.append(c)

print(sum(pans))























            #bottom
