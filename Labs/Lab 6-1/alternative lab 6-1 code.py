# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 6-1

# Description: In this alternative version, I used the replace function so that i did not need to
# create 2 more lists to hold the hyphenated strings



sentence = input("Please enter a sentence (including numbers): ")
# create list to hold indices for letter and number position
isLetter = []
isNumber = []
count = 0 # for rolling through indices in for loop

'''
convert input to a list.
make two sep lists to store different version of sentence after you black out the letters or numbers with "-".
'''
sentenceLetter = sentence
sentenceNum = sentence
# for loop to check if character
for letter in sentence:
    if letter.isalpha():
        sentenceLetter = sentenceLetter.replace(letter, "-")
        isLetter = isLetter + [count]
        count += 1
    elif letter.isdigit():
        sentenceNum = sentenceNum.replace(letter, "-")
        isNumber = isNumber + [count]
        count += 1
    else:
        count += 1

print("Here is the sentence breakdown:\n")

# print letters outcome
print("LETTERS:")
print(sentenceLetter)
print("\nLetters occur at the following positions: ")
if(len(isLetter)) > 0:
    for index in range(len(isLetter)):
        print(isLetter[index], end=" ")
else:
    print("NONE")


# print numbers outcome
print("\n\nNUMBERS:")
print(sentenceNum)
print("\nNumbers occur at the following positions:")

if(len(isNumber)) > 0:
    for index in range(len(isNumber)):
        print(isNumber[index], end=" ")
else:
    print("NONE")


"""
----------------------------------------------------------------------------------------------------------------
"""

# this is the longer version that has the two extra lists
sentence = input("Please enter a sentence (including numbers): ")
# create list to hold indices for letter and number position
isLetter = []
isNumber = []
count = 0 # for rolling through indices in for loop


'''
convert input to a list.
make two sep lists to store different version of sentence after you black out the letters or numbers with "-".
'''
sentenceListLetter = []
sentenceListNum = []

# add each character 1 by 1, so 1 character occupies 1 spot
for character in sentence:
    sentenceListLetter = sentenceListLetter + [character]
    sentenceListNum = sentenceListNum + [character]

# for loop to check if character
for letter in sentence:
    if letter.isalpha():
        sentenceListLetter[count] = "-"
        isLetter = isLetter + [count]
        count += 1
    elif letter.isdigit():
        sentenceListNum[count] = "-"
        isNumber = isNumber + [count]
        count += 1
    else:
        count += 1

print("Here is the sentence breakdown:\n")

# print letters outcome
print("LETTERS:")
for index in range(len(sentenceListLetter)):
    print(sentenceListLetter[index], end = "")
print("\nLetters occur at the following positions: ")
if(len(isLetter)) > 0:
    for index in range(len(isLetter)):
        print(isLetter[index], end=" ")
else:
    print("NONE")


# print numbers outcome
print("\n\nNUMBERS:")
for index in range(len(sentenceListNum)):
    print(sentenceListNum[index], end = "")
print("\nNumbers occur at the following positions:")

if(len(isNumber)) > 0:
    for index in range(len(isNumber)):
        print(isNumber[index], end=" ")
else:
    print("NONE")
