# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 10-1

def readDictionaryFile(fileName):
    dictionary = []
    try:
        fileIn = open(fileName, "r") # what to do when the file fails?
    except FileNotFoundError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")
    for line in fileIn:
        dictionary = dictionary + [line.strip()]
    fileIn.close()
    return dictionary

def checkWord(dictionaryList,word):
    if word in dictionaryList:
        return True
    else:
        return False

def main():
    print("Welcome to Spell Check!")
    run = True
    while run:
        fileName = input("Please enter the dictionary file you wish to read in: ")
        word = input("Please enter the word you wish to spell check: ").lower()
        run = False
        dictionaryList = readDictionaryFile(fileName)
        if checkWord(dictionaryList, word) == True: # in there
            run = False
            print("That word is in the dictionary")
        else:
            print("That word is NOT in the dictionary, so it must be spelled wrong.")

main()