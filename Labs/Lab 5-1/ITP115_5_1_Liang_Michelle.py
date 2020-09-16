# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 4-1
def main():
    articles = ['a', 'the']
    nouns = ['person', 'place', 'thing']
    verbs = ['danced', 'ate', 'frolicked']
    word = ""
    ask = True
    import random
    while ask == True:
        print("Welcome to the Sentence Generator\nMenu\n1) View Words\n2) Add Words\n3) Remove Words\n"
              "4) Generate Sentence\n5) Exit")
        choice = input("Please select a number choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("articles: ", articles)
                print("nouns: ", nouns)
                print("verbs: ", verbs)
                ask = False

            elif choice == 2:
                nounorVerb = int(input("Enter 1 for nouns or 2 for verbs: "))
                if nounorVerb == 1: #chose to add a noun
                    word = input("Enter the word ")
                    nouns.append(word)
                    print("nouns updated: ", nouns)
                elif nounorVerb == 2: #chose to add a verb
                    word = input("Enter the word ")
                    verbs.append(word)
                    print("verbs updated: ", verbs)
                ask = False

            elif choice == 3:
                nounorVerb = int(input("Enter 1 for nouns or 2 for verbs: "))
                if nounorVerb == 1:  # chose to remove a noun
                    word = input("Enter the word to remove ")
                    if word in nouns:
                        nouns.remove(word)
                        print("nouns updated: ", nouns)
                    else:
                        print("The word isn't in the list")
                elif nounorVerb == 2:  # chose to add a verb
                    word = input("Enter the word to remove ")
                    if word in verbs:
                        verbs.remove(word)
                        print("verbs updated: ", verbs)
                    else:
                        print("The word isn't in the list")

                ask = False

            elif choice == 4:
                print(random.choice(articles), random.choice(nouns), random.choice(verbs))
                ask = False

            elif choice == 5:
                print("Program will exit.\n Have a great day!")
                ask = False
            else: #will trigger if the digit isnt between 1 and 5
                print("error. Try again")

        else: #if the input isnt even a digit
            print("!!!error. Try again!!!")

main()