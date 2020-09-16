"""
LIST FUNCTION NOTES
"""

# can sort lists - will sort the actual list, not create a new one
numbers = [3, 5, -12, 40]
numbers.sort() # sort from least to greatest
print(numbers)

numbers1 = ["coffee" , "boba"]
numbers1.sort() # sort from alphabetical order, each letter has a numerical value assigned
print(numbers1)

# can also reverse a list
numbers3 = ["o" , "j" , "l"]
numbers3.reverse() # will just swap order
print(numbers3)

# can remove elements someList.remove()
numbers2 = [1, 2, 3, 4]
numbers2.remove(2) # remove the number 2 from numbers2
print(numbers2)

# can also delete elements  someList.del() --> EMPTIES the slot, not just removes, clears memory
numbers4 = [1, 2, 3, 4]
del numbers4[2] # delete number at index 2 (so thats 3 in this case)
print(numbers4)
del numbers4[2] # delete number at index 2 (so thats 4 in this case)
print(numbers4)

# someList.index(someValue) -- ON TEST
numbers6 = [3, 5, -12]
found = numbers6.index(5) # if it cant find the number 5, it'll crash. Supposed to return index of 5
print(found)
# rather use find because it wont crash if the number isnt in the list

# slicing lists someList[start:end], will return a list
animals = ["dog" , "cat", "emu", "bird"]
slice = animals[1:3]
print(slice) #prints cat and emu
slice = animals[0:1] # even tho its one element, its NOT a string, its a list with 1 item

item = animals[0] # will just print dog, its a string, because you're just pulling out the ELEMENT of the list

# changing lists by slicing
nums = [12, -3, 5]
nums[0:2] = [7,9] # change spots 0 and 1 (12, -3) to 7 and 9
nums[0:2] = [13] # will get rid of spots 0,1 and replace it with just 13. so end product is 13, 5

# note
a = nums # a IS the list, so any edits to a will result in edits to nums overall. it becomes the original
b = nums[:] # b is a COPY of the list




# can use find on either strings or lists, can only sort lists
# convert string to list
word = "stir"
ltrList = list(word)
ltrList[1] = "p" # will now say spir
ltrList.append("e") # will now say spire

# convert list to string (can use for loop OR a function --> newString = delimiter.join(aList))
# delimiter refers to what seperates each character/member of a list, so what do you want to seperate
# each member when you convert to a string
word = "^-".join(ltrList)

# split --> seperates a string that contains delimiters into a list
namestring = "a,b,c"
nameList = namestring.split(",") #splits into list, each value seperated by comma
# nameList now equals ["a" ,"b" , "c"]

# strip --> removes whitespace from beginning and end of the string
line = "    Hello my name is Rob\nn"
astring = line.strip()
print(astring) # "Hello my name is Rob"