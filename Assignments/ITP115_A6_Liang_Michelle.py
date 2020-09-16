# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 6

# Description:
# This program will assign 10 seats on a plane - first class and economy class

def main():
    # TOTAL SEATS VARIABLE NOT HERE TO ACCOUNT FOR FIRST CLASS AND SECOND CLASS
    # seatsLeft variable replaces total_seats and numFilledSeats variables
    FCseatsLeft = 4
    ECseatsLeft = 6
    FCseats = []
    ECseats = []

    # Menu
    print("1: Assign Seat\n2: Print Seat Map\n3: Print Boarding Pass\n-1: Quit\n")
    loop = True
    while loop == True:
        choice = input("What is your choice?: ")
        # assign
        if choice == '1':
            name = input("Please enter your first name: ")
            looper = True
            while looper == True:
                looper = False
                tier = input("Type 1 for First Class or type 2 for Economy: ")
                if tier == '1':
                    if FCseatsLeft > 0:
                        FCseats.append(name.capitalize())
                        FCseatsLeft -= 1
                    else:
                        alt = input("Would you like to be placed in Economy instead? (y/n)")
                        if alt.lower() == "y":
                            if ECseatsLeft > 0:
                                ECseats.append(name.capitalize())
                                ECseatsLeft -= 1
                        else:
                            print("Next flight leaves in 3 hours")
                elif tier == '2':
                    if ECseatsLeft > 0:
                        ECseats.append(name.capitalize())
                        ECseatsLeft -= 1
                    else:
                        alt = input("Would you like to be placed in First Class instead (y/n)?")
                        if alt.lower() == "y":
                            if FCseatsLeft > 0:
                                FCseats.append(name.capitalize())
                                FCseatsLeft -= 1
                        else:
                            print("Next flight leaves in 3 hours")
                else:
                    print("Please enter a valid value?")
                    looper = True

        # print seat
        elif choice == '2':
            seatnum = 0
            if len(FCseats) > 0:
                for index in range(0, len(FCseats)):
                    seatnum += 1
                    print("FC", seatnum, end="")
                    print(":", FCseats[index], end="    ")
            if FCseatsLeft != 0:
                for num in range(0, FCseatsLeft):
                    seatnum += 1
                    print("FC", seatnum, end="")
                    print(": EMPTY", end="    ")
            if len(ECseats) > 0:
                seatnum = 4
                for index in range(0, len(ECseats)):
                    seatnum += 1
                    print("ECO", seatnum, end="")
                    print(":", ECseats[index], end="    ")
            if ECseatsLeft != 0:
                for num in range(0, ECseatsLeft):
                    seatnum += 1
                    print("ECO", seatnum, end="")
                    print(": EMPTY", end="    ")
            print()

        # Print Boarding Pass
        elif choice == '3':
            FCseatstemp = []
            ECseatstemp = []
            # making the ACTUAL full list (isn't dependent on option 1 or 2 happening)
            if FCseatsLeft != 0:
                for num in range(0, FCseatsLeft):
                    FCseatstemp = FCseats
                    FCseatstemp.append("EMPTY")
            if ECseatsLeft != 0:
                for num in range(0, ECseatsLeft):
                    ECseatstemp = ECseats
                    ECseatstemp.append("EMPTY")
            allSeats = FCseatstemp + ECseatstemp
            del FCseatstemp
            del ECseatstemp
            # print(allSeats)

            # can now check if input is within the seat list
            look = input("What is your name or seat number? We will check if you have a seat: ")
            if look.isdigit():
                look = int(look)
                if look in range(1, 11):
                    if allSeats[look - 1] != "EMPTY":
                        print("======= BOARDING PASS =======")
                        print("Seat Number:", look)
                        print("Passenger Name:", allSeats[look - 1])
                        print("=============================")
                    else:
                        if look in range(1, 11):
                            print("Nobody sits here.")
                        else:
                            print("Invalid seat number.")

            elif look.lower().capitalize() in allSeats:
                index = allSeats.index(look.lower().capitalize())
                print("======= BOARDING PASS =======")
                print("Seat Number:", (index + 1))
                print("Passenger Name:", look.capitalize())
                print("=============================")
            else:
                print("No passenger with name", look.capitalize(), "was found")

        # quit, stops the loop
        elif choice == '-1':
            print("You quit.")
            loop = False


        # happens if none of the menu choices are chosen, will cause it to loop and keep asking
        else:
            print("Error, please enter a proper value from the menu above")
            loop = True  # make loop continue


main()
