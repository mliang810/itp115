# Michelle Liang
# ITP 115, Spring 2020
# Lab 1-1
# liangmic@usc.edu

# Description:
# This program prints a box, a monty python quote, and the date

def main():
    #print box
    print(" ___ ", end= "\n\n")
    print("|   " + "|", end= "\n\n")
    print("|   " + "|", end= "\n\n")
    print("|___" + "|", end= "\n\n")

    #print quote
    print("You don't frighten us, English pig-dogs! \nGo and boil your bottoms, sons of a silly person! "
          "\n\t -\"Monty Python and the Holy Grail\"")
    print("\n")

    #print date
    month = input("What month are we in?: ")
    day = input("What day is it?: ")
    dayofmonth = input("What day of the month is today?: ")

    dayofmonth = int(dayofmonth)
    nextday = dayofmonth + 1

    nextday = str(nextday)
    dayofmonth = str(dayofmonth)

    print("Today is " + day + " " + month + " " + dayofmonth + " " + "and Tomorrow will be " + month + " " + nextday)
    # Code will not work if it is new years/end of any month because it will create a date that doesn't exist.
    # Leap years also do not work.

main()