'''
range(10)   # will print 0-9
range(0,10) # will print 0-9
range(1,11) # will print 1-10

range(10,0, -1) # will count down from 10


for num in range(10, 0, -1):
    print(num)

for letter in "Hello World":
    print(letter)

print(len("Hello World"))
print(len(range(10)))

count = 0
for letter in "Artwork":
    if letter.lower() == "a": # or if letter in "Aa":
        count+=1
        print("Found " + str(count))

age = input("how old are u")
while age.isdigit() == False:   #or false == age.isdigit()
    age = input("how old are u, please input an integer value ")
age = int(age)
print(age)

# operator for random access
text = "Hello World"
print("The first letter is \"" + text[0] + "\"")
#going off the end of the string
print(text[17])
'''
'''
text = "Nothing"
first = text[0]
second = text[1]
third = text[2]
word = first + second +third
print(word)
word = text[0:3]
print(word)
# reverse = text[1:len(text)] + text[0]
reverse = text[1:] + text[0] # putting nothing at begining or end means start from beigining or end
print(reverse)
print(text[:])
'''
'''
# find
text = "Hello world"
oIndex = text.find("o")
print(oIndex)
print(text[oIndex:]) #will print last part of string
nIndex = text.find("i")
print(nIndex) # returning -1 means it couldnt find it
'''
'''
text = "Hello World"
helloIndex = text.lower().find("hello")
print(helloIndex)
print(text[helloIndex:])


#text[0] = "H" #cant do
text = "H" + text[1:]
print(text)
text = "H" + text[0:]
print(text)
'''

'''
name1 = "Steve"
name2 = "Michael"
name3 = "Michelle"
name4 = "Alex"
name5 = "Clarissa"

names = ["Steve", "Michael", "Michelle","Alex","Clarissa"]
print(names)
print(names[0])
print("There are " + str(len(names)) + " names in this list")

for name in names:
    print(name)

print("\n")
for index in range(len(names)):
    print(names[index])
    index+=1
print("\n")
# names = names + "Grace" #cant add a string to a list of strings, but can add a list of strings to a list of strings
names = names + ["Melody"]
for index in range(len(names)):
    print(names[index])
    index+=1

print("\nThe first two names are:")
for name in names[:2]:
    print(name)

print("\nThe first two names are:")
for index in range(2):
    print(names[index])
'''
'''
nameList = [] #or nameList = list() #this is how to make an empty list
for count in range(5):
    nameList = nameList + [input("Gimme your name: ")]
    count += 1
print(nameList)
'''
'''
nameList = [""] * 5 #times 5 to make a list of 5 empty spots #or [None]*5
for index in range(5): #5 means i want to make a list of 5 names (0-4)
    nameList[index] = input("Gimme your name: ")
print(nameList)

'''
#change first name in nameList
nameList = ["a", "b", "michelle", "d", "e"]
for name in nameList[:1]:
    nameList[:1] = input("new replacement name")
    print(nameList)

'''
#remove michelle sfrom namelist
nameList = ["a", "b", "michelle", "d", "e"]
nameList.remove("michelle")
print(nameList)
'''