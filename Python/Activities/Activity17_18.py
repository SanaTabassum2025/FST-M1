import pandas

#create a dataset
data = {
    "usernames": ["admin", "Charles", "Deku"],
    "passwords" : ["password", "charl13", "AllMight"]
}
#Convert te data into DataFrame
df = pandas.DataFrame(data)

#write the dataframe to a file
df.to_csv("./sample.csv")

#Activity18
input_file = pandas.read_csv("./sample.csv")

#Print the values only in the Usernames column
print(input_file["usernames"])

#Print the username and password of the second row
print("second row values:", input_file["usernames"][1], input_file["passwords"][1])

#Sort the Usernames column data in ascending order and print data
print(input_file.sort_values("usernames"))

#Sort the Passwords column in descending order and print data
print(input_file.sort_values("passwords"), ascending= False)