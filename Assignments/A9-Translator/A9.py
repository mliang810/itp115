# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 9

# Description:
# Reading in a csv file and using its contents to translate english words into various other languages. The results
# will get outputted to a file of the user's choice

def getLanguages(fileName="languages.csv"):
    # read in only first line and put those values in a list
    fileIn = open(fileName, "r") # what to do when the file fails?

    # extracts first line, aka header with the languages
    languages = fileIn.readline().split(",")
    fileIn.close()
    return languages


def getSecondLanguage(langList):
    keepAsking = True
    while keepAsking:
        print("Translate English words to one of the following languages: ")
        print("\t", langList)
        secondLang = input("Enter a language: ")
        if secondLang.lower().capitalize() in langList:
            return secondLang.lower().capitalize()

def readFile(langList, langstr="English", fileName="languages.csv"):
    fileIn = open(fileName, "r")

    # figuring out the index of the language in question (0 for english, 1 for danish, etc)
    count = 0
    for entry in langList:
        if entry == langstr:
            index = count
        else:
            count+=1

    # making the list for the language in question (usually english)
    wordsinLang = []
    count = 0
    for line in fileIn:
        if count > 0:
            temp = line.split(",")
            wordsinLang.append(temp[index])
        count += 1
    fileIn.close()
    return wordsinLang


def createResultsFile(language, resultsFile):
    fileOut = open(resultsFile, "w")
    print("Words translated from English to " + language, file=fileOut)
    fileOut.close()

def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile, "a")
    tryAgain = True
    while tryAgain:
        askForAnotherGo = False
        word = input("Enter a english word to translate: ")
        if word.lower() in englishList:
            # find index of that word and apply it to the second list, return that
            count = 0
            for entry in englishList:
                if word.lower() == entry:
                    result = secondList[count]
                    if result == "-":
                        print(word + " did not have a translation")
                    else:
                        print(word + " is translated to " + result)
                        print(word, "=", result, file=fileOut)
                        askForAnotherGo = True
                count +=1

        # asking if the user wants to do more words
        if askForAnotherGo:
            askAgain = True
            while askAgain:
                choice = input("Would you like to translate another word? (y/n): ")
                if choice.lower() == "n" or choice.lower() == "y":
                    askAgain = False
                    if choice.lower() == "n":
                        tryAgain = False

        else:
            asking = True
            while asking:
                again = input(word + " is not in the English list, try again? (y/n): ")
                if again.lower() == "n" or again.lower() == "y":
                    asking = False
                    if again.lower() == "n":
                        tryAgain = False

    fileOut.close()

def main():

    langList = getLanguages()
    secondLanguage = getSecondLanguage(langList)
    englishList = readFile(langList)
    secondLangList = readFile(langList, secondLanguage)
    resultsFile = input("Enter a name for the results file (return key for " + secondLanguage + ".txt): ")
    if resultsFile.strip() == "":
        resultsFile = secondLanguage + ".txt"
    createResultsFile(secondLanguage,resultsFile)

    translateWords(englishList, secondLangList, resultsFile)


main()
