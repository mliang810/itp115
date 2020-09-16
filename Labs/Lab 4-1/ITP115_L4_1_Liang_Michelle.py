# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 4-1

def main():
    keepgoing = "y"
    while keepgoing == "y":
        print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!\n(Welcome to the Pig Elvish translator!)")
        word = input("Please enter a word you would like to translate: ").lower()

        #step 1, move first letter to end
        firstletter = ""
        newword = ""
        count = 0
        for letter in word:
            count +=1
            if count == 1:
                firstletter = letter
            if count >= 2:
                newword = newword + letter
        newword = newword + firstletter
        #print(newword)

        #step 2 - add random vowel to end if more than 4 letters
        if len(word) >= 4:
            import random
            randvowel = random.choice("aeiou")
            newword = newword + randvowel
        #print(newword)

        #step 3 - if word has less/= 3 letters, put en at back
        if len(word) <= 3:
            newword = newword + "en"
            #print(newword)


        #step 4 - if k, change to c
        temp = ""
        for letter in newword:
            if letter == "k" or letter == "K":
                letter = "c"
            temp = temp + letter
            newword = temp
        #print(newword)

        #step 4 - if e change to ë
        temp = ""
        count = 0
        for letter in newword:
            count+=1
            if count == len(newword) and letter == "e":
                letter = "ë"
            temp = temp + letter
        newword = temp
        #print(newword)

        #capt. the first letter
        firstletter = ""
        count = 0
        temp = ""
        for letter in newword:
            count += 1
            if count == 1:
                firstletter = letter.upper()
            if count >= 2:
                temp = temp + letter.lower()
        newword = firstletter + temp

    # print final statement
        print("\'" + word + "\'" + "in elvish is: " + newword)
        keepgoing = input("Would you like to translate another word? (y/n) ").lower()

main()