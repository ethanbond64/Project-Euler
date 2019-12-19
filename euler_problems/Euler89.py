with open('p089_roman.txt') as f:
    romans = f.readlines()
romans = [x.strip() for x in romans]

charKey = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def romanToInt(roman):
    n = 0
    for let in range(len(roman)-1):
        if charKey[roman[let]] >= charKey[roman[let+1]]:
            n += charKey[roman[let]]
        else:
            n -= charKey[roman[let]]
    n += charKey[roman[-1]]
    return n

total = 0
for numeral in romans:
    ogLength = len(numeral)

    val = list(str(romanToInt(numeral)))[::-1]
    new = ''
    for loc in range(len(val)):
        dig = int(val[loc])
        if loc == 0:
            if dig > 0:
                moded = dig % 5
                if 0 < moded and moded < 4:
                    new = moded*'I' + new
                    if dig > 5:
                        new = 'V' + new
                elif moded == 0:
                    new = 'V' + new
                else:
                    if dig > 5:
                        new = 'IX' + new
                    else:
                        new = 'IV' + new

        elif loc == 1:
            if dig > 0:
                moded = dig % 5
                if 0 < moded and moded < 4:
                    new = moded*'X' + new
                    if dig > 5:
                        new = 'L' + new
                elif moded == 0:
                    new = 'L' + new
                else:
                    if dig > 5:
                        new = 'XC' + new
                    else:
                        new = 'XL' + new
        elif loc == 2:
            if dig > 0:
                moded = dig % 5
                if 0 < moded and moded < 4:
                    new = moded*'C' + new
                    if dig > 5:
                        new = 'D' + new
                elif moded == 0:
                    new = 'D' + new
                else:
                    if dig > 5:
                        new = 'CM' + new
                    else:
                        new = 'CD' + new
        else:
            new = dig*'M' + new
    print('-------')
    print(numeral)
    print(romanToInt(numeral))
    print(new)
    newLen = len(new)
    # print(ogLength-newLen)
    total += ogLength-newLen
print('fin: ',total)
