# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 6-1

def main():
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



main()