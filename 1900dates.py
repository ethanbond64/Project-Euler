dayCount = 0
sundayCount = 0

for jan in range(31):
    dayCount += 1
    if jan == 0 and dayCount%7 == 0:
        sundayCount += 1
for feb in range(28):
    dayCount += 1
    if feb == 0 and dayCount%7 == 0:
        sundayCount += 1
for mar in range(31):
    dayCount += 1
    if mar == 0 and dayCount%7 == 0:
        sundayCount += 1
for apr in range(30):
    dayCount += 1
    if apr == 0 and dayCount%7 == 0:
        sundayCount += 1
for may in range(31):
    dayCount += 1
    if may == 0 and dayCount%7 == 0:
        sundayCount += 1
for jun in range(30):
    dayCount += 1
    if jun == 0 and dayCount%7 == 0:
        sundayCount += 1
for jul in range(31):
    dayCount += 1
    if jul == 0 and dayCount%7 == 0:
        sundayCount += 1
for a in range(31):
    dayCount += 1
    if a == 0 and dayCount%7 == 0:
        sundayCount += 1
for s in range(30):
    dayCount += 1
    if s == 0 and dayCount%7 == 0:
        sundayCount += 1
for o in range(31):
    dayCount += 1
    if o == 0 and dayCount%7 == 0:
        sundayCount += 1
for n in range(30):
    dayCount += 1
    if n == 0 and dayCount%7 == 0:
        sundayCount += 1
for d in range(31):
    dayCount += 1
    if d == 0 and dayCount%7 == 0:
        sundayCount += 1

print(dayCount)
print(sundayCount)
