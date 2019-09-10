sm = 0
nat = list(range(0,101))
for x in nat:
    sm = sm+(x**2)

ms = 0
tan = list(range(0,101))
for x in tan:
    ms = ms+x
tot = ms**2

fin= tot-sm
print(fin)
