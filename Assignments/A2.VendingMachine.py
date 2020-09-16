# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 2

# Description:
# This program creates a harry potter vending machine.
# It determines change and gives a discount.

def main():
    #options + choose item
    print("a)Butterbeer: 58 knuts\nb)Quill: 10 knuts\nc)The Daily Prophet: 7 knuts\nd)Book of Spells: 400 knuts\n")
    itemchoice = input("What would you like from the vending machine: a, b, c, or d? ")

    ingalleons = input("How many galleons would you like to insert? Enter integer value: ")
    insickles = input("How many sickles would you like to insert? Enter integer value: " )
    inknuts = input("How many knuts would you like to insert? Enter integer value: ")

    #payment calculation
    #figuring out original cost of item
    cost = 0
    if itemchoice == "a":
        itemchoice = "Butterbeer"
        cost = 58
    elif itemchoice == "b":
        itemchoice = "Quill"
        cost = 10
    elif itemchoice == "c":
        itemchoice = "copy of The Daily Prophet"
        cost = 7
    elif itemchoice == "d":
        itemchoice = "Book of Spells"
        cost = 400
    else:
        print("Your input does not match our options, thus you have been assigned a default option " 
            "- the Book of Spells")
        cost = 400

    # ask discount?
    sharechoice = input("Would you like to share your purchase on instagram?"
                        " You will get a 5 knut discount for doing so. (y/n) ")

    #subtract discount or not, only go thru if yes
    if sharechoice == "y":
        print("Thanks! You get 5 knuts off your purchase.")
        cost = cost - 5
        sharechoice = "true"
    elif sharechoice == "Y":
        print("Thanks! You get 5 knuts off your purchase.")
        cost = cost - 5
        sharechoice = "true"

    #decide change
    moneyin = (int(ingalleons) * 493) + (int(insickles) * 29) + int(inknuts)
    change = moneyin - cost

    #convert knuts (change) into sickles and knuts
    origchange = change
    galleons = change//493
    change = change - (galleons*493)
    sickles = change//29
    knuts = change%29

    #return change
    print("You bought a " + itemchoice + " for " + str(cost) + " knuts", end = " ")
    if(sharechoice == "true"):
        print("(with a coupon of 5 knuts)", end = " ")
    print("and paid with " + str(ingalleons) + " galleon(s) "+ str(insickles) + " sickle(s) " + str(inknuts) + " knut(s).\n")

    print("Here is your change (" + str(origchange) + " knuts)")
    print("Galleons: " + str(galleons))
    print("Sickles: " + str(sickles))
    print("Knuts: " + str(knuts))

main()
