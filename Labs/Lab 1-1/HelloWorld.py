
print("Hello world")
print("Python is awesome")

print("Hello world. " + "Goodbye")
print("Hello world.","Goodbye") #comma adds a space

# want "Hello world. Python is awesome" to print on the same line.
print("Hello world.", end="") #replace newline with no space at all
print("Python is awesome")

# example of end=
print("Hello world", end="!! ")  # replace newline w/ "!! "
print("Python is awesome")

#using escape character "\"
print("\"Python\" comes from a comedy troupe")

"""
backslash \ means "no seriously put this character"
sometimes certain characters are action items, \ is an 'escape' from that
BTW this is a multi-line comment 
"""
print("\"Python\" comes from \n a comedy troupe")

#can comment out certain sections of code by using control + slash (/)

"""" 
to declare a variable + dont need to declare the type like in c++, python will assume for you
variable = value

eg: 
age = 16
catchphrase = "Hello World"
"""


x = "20"
y = "10"
print(x)
print(y)

x = int(x) #cast x from a string to an int
y = int(y) #same for y
print(x+y)

#x and y are operands and + is the operation in x+y

age = input("what is your age?")
print(age)
