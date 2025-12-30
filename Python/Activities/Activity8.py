list = input("Enter your sequence of list with commas:").split(",")

firstnumber = list[0].strip() #.strip() removes any whitespace around the item
lastnumber = list[-1].strip()

if (firstnumber == lastnumber):
    print(True)
else:
    print(False)
