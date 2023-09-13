# Strings are alphanumeric and all characters. are surrounded in " " or ''

#name = 'John'
#myname = "ng'ang'a"

first_name = 'John'
last_name = "Ng'ang'a"

full_name = first_name +" "+ last_name

#print(full_name)

#Operations or methods are available to use/ Use dots to access the methods 

#print(full_name.lower()) is okay but the data has not been stored anywhere. 
#Instead do to store the data, declare outside the print()
#All methods end with the () this is the data to be 'functioned' .method()

#full_name = full_name.split("a")
print(full_name)

#Dealing with numbers that are strings

num1 = "7"
num2 = "8"
t = int(num1)+int(num2)
print(t)

##### Indexing and Slicing:

# This is used when you want to get a part of a string
#Indexing is when you want to access one character
#Slice is when you want to access multiple characters


#indexing to find the position of h// 2 and =11
#print(full_name[])

#Slicing from the position you want to start : position you want to end your slice.

print(full_name[5:13]) # when slicing the name john from the rest of the name-string

#Finding the length of a string

print(len("John"))




