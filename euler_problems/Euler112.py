

# make a dict to store previous results but store them as a string
res = {
"0":"ID",
"1":"ID",
"2":"ID",
"3":"ID",
"4":"ID",
"5":"ID",
"6":"ID",
"7":"ID",
"8":"ID",
"9":"ID",
"0":"ID"
}

# for each check that the int(the rest) != 0 else set D

# Enum-like 
# I (check that next is less than or equal)
# D (check that next is greater than or equal)
# B (convert to bouncy)
# ID (check less than, check greater than, then check equal to)
g = 0
i = 10

while True:
    
    print(i)
    s = str(i)
    x = int(s[0])
    a = s[1:]
    k = int(a[0])
    

    # if all others are zero its increasing
    if int(a) == 0:
    	res[s] = "D"
    elif "0" in a and res.get(a) is None:
	res[s] = "B"
	g += 1
    elif res[a] == "I":
	if x <= k:
	    res[s] = "I"
        else:
	    res[s] = "B"
	    g += 1
    elif res[a] == "D":
	if x >= k:
            res[s] = "D"
        else:
            res[s] = "B" 
	    g += 1
    elif res[a] == "ID":
	if x > k:
	    res[s] = "D"
	elif x < k:
	    res[s] = "I"
    	else:
	    res[s] = "ID"
    
    else:
	res[s] = "B"	
	g += 1
    i += 1
     
    if float(g)/float(i) == 0.5:
    	print(float(g)/float(i))
	print("this")
	print(i-1)
	break


    	    



