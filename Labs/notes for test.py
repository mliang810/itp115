# any word (can put numbers in variable name) can be the name of a variable + is caps sensitive
#       - hello is different from Hello
# can't put symbols in names of variables (Eg ! - * most punctuation really, no spaces)
# variable must start with a letter (Eg 1variable wouldnt work)

'''
hello there = not a variable name
hello_there = is a variable name
hello1 = works
128hello = doesnt work
hello-there = not a variable name
'''

# python is an interpretative language - python tells you errors happening live, not before it runs
# other languages are compilers - eg C++ tells you before running if there's an error as it compiles

'''
word = "hello world"
# print(word[0]) # error, can't use index with string
# print(word[5]) # error, can't use index with string
print(word.find("o")) # 4 - will print index of the letter o
print(word.find("x")) # return -1 because can't find the letter x

foundL = word.find("l")
restofword = word[foundL:] # this is called slicing
print(restofword)

# slicing
word = "hello world"
firstWord = word[0:5]
print(firstWord)
secondWord = word[6:]
print(secondWord)


# slice index into list
# word[0] = "H" # cant do this, strings are immutable - cant change individual members of the string
myList = ["H" , "E" , "L", "L", "O"]
myList[0] = "h"
print(myList)

# or to change first letter of Hello
newWord = word.capitalize() # can do this becuase it creates a new string, it isn't modifying the old string
print(word) # see, didn't actually change word, just created new string and stuck it in newWord
print(newWord)

# or
word1 = "hi there"
word1 = "H" + word1[1:]
print(word1)

# REPLACE - the string function
newWord = newWord.replace("o", "x") #replace o with x
print(newWord)

if "l" in newWord:
    print("Found one")
if "world" in newWord:
    print("Found one")
'''

'''
# not supppperrr efficient but
newText = "Hi 1234"
numbers = "0123456789"
for number in numbers:
    newText = newText.replace(number, "!")
print(newText)
'''
'''
#Exercise put an "s" in the middle of "desert"
word = "desert"
middleWord = len(word)//2
word = word[:middleWord] + "s" + word[middleWord:]
print(word)
'''

# append and remove things from list, [can also use find, in, not in like we do for strings]
    # if "hello" not in list:
    # if "hello" in list:
    # if("hello" in list) == False:
