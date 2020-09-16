print("Welcome to the Sentence Generator\nMenu\n1) View Words\n2) Add Words\n3) Remove Words\n4) Generate Sentence"
      "\n5) Exit")

choice = input("Please select a number choice: ")
while choice.isdigit() == False:
    choice = input("Error. Please select a number choice between 1-5: ")
if choice.isdigit():
    choice = int(choice)
    while int(choice)>5 or int(choice)<1:
        choice = input("Error! Please select a number choice between 1-5: ")

if 0<choice<6:
        if choice == 1:
            print(articles)
            print(nouns)
            print(verbs)
        elif choice == 2:
            print("hey")
        elif choice == 3:
            print("hey")
        elif choice == 4:
            print("hey")
        elif choice == 5:
            print("hey")



