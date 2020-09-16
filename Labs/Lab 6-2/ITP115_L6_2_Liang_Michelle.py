# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 6-2

def main():

    wordState = input("Please enter a word or statement: ")
    wordState2 = input("Please enter a second word or statement: ")

    wordState = wordState.lower().replace(" ", "")
    wordState2 = wordState2.lower().replace(" ", "")

    # convert wordState 1 and 2 to lists so that we can sort it
    wordStateI = []
    wordState2I = []
    for character in wordState:
        wordStateI = wordStateI + [character]
    for character in wordState2:
        wordState2I = wordState2I + [character]

    # checking if word 1 and 2 are anagrams
    anagram = False
    if len(wordState2) == len(wordState):
        wordState2I = wordState2I.sort()
        wordStateI = wordStateI.sort()
        if wordStateI == wordStateI:
            anagram = True

    if anagram == True:
        print("The two words you entered are anagrams")
    else:
        print("The two words you entered are not anagrams")

    # Palindrome 1
    if wordState == wordState[::-1]:
        print("The first word is a palindrome")
    else:
        print("The first word is not a palindrome")

    # Palindrome 2
    if wordState2 == wordState2[::-1]:
        print("The second word is a palindrome")
    else:
        print("The second word is not a palindrome")

# can reverse a sring with reverse
#string = string.reverse()

main()