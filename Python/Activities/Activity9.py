firstlist = [1, 2, 3, 4, 5]
secondlist = [6, 7, 8, 9, 10]

thirdlist =[]
for i in firstlist:
    if (i % 2 != 0):
        thirdlist.append(i)

for i in secondlist:
    if (i % 2 == 0):
        thirdlist.append(i)

print(thirdlist)