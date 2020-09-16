# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 5

# Description:
# This program should jumble words and have the user guess what it is and should be able to encrypt words.

def main():
# Part 1:
    import random
    wordList = ["jumbled", "word", "candy", "python", "nugget"]
    jumbled = random.choice(wordList)
    word = jumbled # keeps track of original word
    # now, we jumble the word
    count = 0
    while count < 5:
        num = random.randrange(0,len(jumbled))
        jumbled = jumbled[num:] + jumbled[:num]
        count+=1

    if jumbled == word: # if chance makes the jumbled word unjumbled
        num = random.randrange(1, len(jumbled))
        jumbled = jumbled[num:] + jumbled[:num]

    print("The jumbled word is " + jumbled)

    # begin guessing for the word
    correct = False
    counter = 0
    points = True
    score = 0
    while correct == False:
        guess = input("Please enter your guess: ")
        counter +=1
        if guess.lower() == word:
            correct = True
            print("You got it!")
            if points == True:
                score +=1
            print("Score: " + str(score))
        elif counter > 2: # if three wrong attempts, give out hints
            hint = input("Would you like a hint? (y/n) ")
            if hint.lower() == "y":
                points = False
                if word == "jumbled":
                    print("Hint: The function of this program is to ____ the words")
                if word == "word":
                    print("Hint: What are you unjumbling?")
                if word == "candy":
                    print("Hint: Something sweet you get on Halloween.")
                if word == "python":
                    print("Hint: Programming language.")
                if word == "nugget":
                    print("I love the chicken ___ at McDonald's!")

    print("It took you " + str(counter) + " tries")

# Part 2:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o","p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
    message = input("Enter a message: ")
    shift = int(input("Enter a number to shift by (0-25): "))
    print("Encrypting message.......")

    # shift alphabet
    newAlpha = []
    for index in range(shift, 26):
        append = alphabet[index]
        newAlpha.append(append)
    for index in range(0, shift):
        newAlpha.append(alphabet[index])

    # now convert word to new alphabet
    messageList = list(message)
    count0 = 0
    for letter in messageList:
        for index in range(len(alphabet)):
            if letter == alphabet[index]:
                messageList[count0] = newAlpha[index]
        count0 +=1
    print("Encrypted message: ")
    print("".join(messageList))

    # convert new word to old alphabet --> DECRYPTION
    print("Decrypting message.......")

    counts = 0
    messageList1 = list(message)
    for letter in messageList:
        for index in range(26):
            if letter == newAlpha[index]:  # why isn't decryption registering
                messageList1[counts] = alphabet[index]
        counts += 1
    print("Decrypted message: ")
    print("".join(messageList1))
    print("Original message: " + message)

main()

