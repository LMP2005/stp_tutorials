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

# output variables
x = "python is awesome"
print(x)
# can use print() to output multiple variables seperated by a comma or a + sign. Although comma is better as it supports different data types.
# remember to include a space after python and is otherwise the 3 words would be pythonisawesome.
x = "python "
y = "is "
z = "awesome"
print(x, y, z)

# + sign also works as a mathematical operator. you cannot use it with a number and "" string.
x = 5
y = 10
print(x+y)

# Global variables are variables created outside of a function. Can be used inside the function.
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " +x)
myfunc()
# myfunc() will now print "Python is fantastic". Note indentation.

print("Python is " + x)
# the above will print "Python is awesome", as x = awesomme. X = fantastic is under def myfunc().

# Data Types
# type() function will tell you data type
x = 5
print(type(x))
# data type is set when you assign a value to a variable
# x = "hello world" is str
# x = 20 is int
# x = 20.5 is float
# x = ["apple", "banana", "cherry"] is list
# x = ("apple", "banana", "cherry"] is tuple
# x = range (6) is range
# x = {"name" : "John", "age" : 36} is dict
# x = {"apple", "banana", "cherry:} is set

# Setting specific data type
x = str("hello world")
print(x)
y = int(20)
print(y)
z = float(20.5)
print(z)

# NUMBERS: numeric types
x = 1 # int is a whole number, pos neg without decimals
y = 2.8 # float is floating point, can also be e to indicate to the power of 10.
z = 1j # complex numbers are written with "j" as imaginary part
# convert from one type to another (not complex)
x = 1
y = 2.8
z = 1j
#convert from int to float
a = float(x)
print(a)
print(type(a))
# x has now been converted from int to float i.e 1 to 1.0

# Built in module called "random" can generate random numbers
import random
print(random.randrange(1,10))

#STRINGS:
a = "hello" # can be double or single '"
print(a) # assigns string to a variable i.e.a

#assign multiline string to a variable using three quotes, can be double or single.
a = """lorem ipsum dolor
consectetur adipiscing
elit sed do"""
print(a)


b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5 (not included). The first character has index 0.

b = "Hello, World!"
print(b[:5]) #Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[2:]) #Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[-5:-2]) #Get characters "o" in "World!" (position -5), to, but not included: "d" in "World!" (position -2):

a = "Hello, World!"
print(a.upper()) #upper() method returns the string in upper case:

a = "Hello, World!"
print(a.lower()) #lower() method returns the string in lower case:

a = "Hello, World!"
print(a.replace("H", "J")) #replace() method replaces a string with another string:

#To concatenate, or combine, two strings you can use the + operator.
a = "hello"
b = "world"
c = a + b
print(c)

a = "hello"
b = "world"
c = a + " " + b
print(c)

#cannot combine strings and numbers, use format(). This takes the passed arguments, formats them and places in the string where placeholders {} are.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#BOOLEANS: represent one of two values- TRUE or FALSE

print(10 > 9)
print(10 == 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("hello"))
print(bool(15))

x = "hello"
y = 15
print(bool(x))
print(bool(y))
#almost all values are true
# not many values are false, except empty values [] {} () "", 0 , value NONE, False.

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

#create functions that return a Boolean value (i.e. true or false)
def myfunction() :
    return True #ensure capital
#print(myfunction())
if myfunction() :
    print("YES!")
else:
    print("NO!")

#OPERATORS
print(100+5*3)
#LISTS: used to store muliple items in single variable. Ordered and changable [].
thislist = ["apple", "banana", "cherry"]
print(thislist)

list1 = ["1, 3, 7, 9"]
list2 = [True, False]

#TUPLES: used to store multiple items in single variable. Ordered and unchangable ().
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#sets: Used to store multiple items in single variable. Unordered, unchangeable, unindexed {}.
#once set created cannot change items, but can delete or add new.
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#DICTIONARIES: store data values in key:value pairs. Ordered changeable and no dups.
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
print(thisdict)

for x in thisdict:
    print(x) #this prints all key names
for x in thisdict:
    print(thisdict[x]) #this prints all values

#if...else
a = 33
b = 200
if b > a:
    print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")


#else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")


#WHILE LOOP: can execute set of statements as long as one is true
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#exit loop when x is banana, break is before print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#loop through set of code a specified number of times using range(). starts at 0 increments of 1.
for x in range(6):
    print(x)

for x in range(2, 30, 3):#this increments the sequence by 3 (default is 1).
    print(x)

for x in range(6):
    print(x)
else:
    print("finally finished")


