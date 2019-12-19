lizz = []
for ii in range(2,101):
    for jj in range(2,101):
        lizz.append(ii**jj)
print(len(set(lizz)))
