#W3 schools tutorial 'Hello world' intro
print("Hello, World!")

# W3 schools Indentation
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

# W3 schools Variables
x = 5
y = "Hello, World"
print(x)
print(y)

# W3 schools Comments #
# this is a comment and is not code. used to explain code and make it more readable.
print("Hello, World") # this is a comment

# Multiline string """ (triple quotes), also used in code as comments and comment placed inside it.
"""
This also is a comment 
written in more than one line, 
this saves time using # at start of each line. 
"""
# as long as a string is not assigned a variable, python will read the code but ignore it

# Python variables
x = 5
y = "John"
print(x)
print(y)

x = 4 # x is of type integer
x = "Sally" # x is now of type string
print(x)

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# get the data type by using type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# ' and " are same
# case sensitive variable names, a = 4 A = "Sally" are different variable names.

#variable names. Must not start with number and are case sensitive for example.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multiple variables
x, y, z = "orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#same value to multiple variables
x = y = z = "orange"
print(x)
print(y)
print(z)
#unpacking a list
fruits = ["apple", "banana", "cherry"]
x , y, z = fruits
print(x)
print(y)
print(z)

