import pandas

#create a dataset
data = {
    "firstname": ["Satvik", "Avinash", "Lahri"],
    "lastname" : ["Shah", "Kati", "Rath"],
    "email": ["satshah@example.com", "avinashk@example.com", "lahri.rath@example.com"],
    "phonenumber": ["4537829158", "5892184058", "4528727830"]
}
#Convert data into draframe
df = pandas.Dataframe(data)
#Write dataframe into excel file
writer = ExcelWriter("./sample1.xlsx")
df.to_excel(writer, "Sheet1", index = False)


#Activity20
input_file = pandas.read_excel("./sample.xlsx", "Sheet1")

#print the number of rows and columns
print(input_file.shape)

#Print the data in the emails column only

#Sort the data based on FirstName in ascending order and print the data