# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 4

# Description: Create a program that simulates a 20 sided die rolling and a character counter of the user's input

def main():
    # character counter #
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    countC = 0
    countL = 0
    # oldFocus = []
    ast = "*"
    sentence = input("Please enter a sentence: ")
    print("Here is the character distribution: ")

    # counting special characters
    for character in sentence.lower():
        if character != " " and character not in alphabet:
            countC+=1
    print("Special Character: " + str(countC*ast))

    for letter in alphabet: # will go through the alphabet and count will change based on whats in sent.
        focus = letter
        for letter in sentence.lower(): # cycle thru sentence to see how many times the letter is there
            if focus == letter: # and oldFocus[:] != focus:
                countL+=1
        if countL!=0: # normal ast. count
            print(focus + ": " + str(countL*ast))
        if countL == 0: # print NONE in empty counts
            print(focus + ": NONE")
        # oldFocus = oldFocus + [focus]
        countL = 0

# dice game
    import random
    score = 0
    count = 0
    for count in range(0,10):
        winornot = False
        # cases
        caseNum = random.randrange(1,6)
        print("You're playing for Case " + str(caseNum) + ". Here are the winning numbers: ")
        if caseNum == 1:
            for num in range(2,21,2):
                print(num, end=" ")
        if caseNum == 2:
            for num in range(1,20,2):
                print(num, end=" ")
        if caseNum == 3:
            for num in range(5,11):
                print(num, end=" ")
        if caseNum == 4:
            for num in range(10,21,2):
                print(num, end=" ")
        if caseNum == 5:
            for num in range(3,19,3):
                print(num, end=" ")

        # Then roll the die. get a num between 1-20
        print("Now rolling...")
        result = random.randrange(1,21)
        print("You rolled a " + str(result))
        # check if result matches number in winning case
        if caseNum == 1:
            for num in range(2,21,2):
                if result == num:
                    print("You won 50 points!")
                    score+=50
                    winornot = True
            if winornot == False:
                print("You didn't win")

        if caseNum == 2:
            for num in range(1,20,2):
                if result == num:
                    print("You won 50 points!")
                    score += 50
                    winornot = True
            if winornot == False:
                print("You didn't win")

        if caseNum == 3:
            for num in range(5,11):
                if result == num:
                    print("You won 50 points!")
                    score += 50
                    winornot = True
            if winornot == False:
                print("You didn't win")

        if caseNum == 4:
            for num in range(10,21,2):
                if result == num:
                    print("You won 50 points!")
                    score += 50
                    winornot = True
            if winornot == False:
                    print("You didn't win")

        if caseNum == 5:
            for num in range(3,19,3):
                if result == num:
                    print("You won 50 points!")
                    score += 50
                    winornot = True
            if winornot == False:
                print("You didn't win")

        if count == 9:
            print("Your total score is " + str(score))

main()