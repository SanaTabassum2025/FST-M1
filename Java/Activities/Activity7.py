list = input("Enter your sequence of list with commas:").split(",")

sumofList = 0
for number in list:
    sumofList += int(number)

print("Sum of the numbers of list:" +str(sumofList))
