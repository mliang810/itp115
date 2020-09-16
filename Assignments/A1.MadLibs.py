# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 1

# Description:
# This program creates a Mad Libs story by taking the players input and printing it out.

def main():
    # Gather input in string form
    number = input("Enter an integer: ") # needs converting to integer and then back to string
    animal = input("Enter an animal (plural if number entered is greater than 1): ")
    verb = input("Enter a verb that ends with -ing: ")
    place = input("Enter a place: ")
    name = input("Enter a name: ")
    adjective = input("Enter an adjective: ")
    number2 = input("Enter another integer: ")
    number3 = input("Enter another integer: ")
    number4 = input("Enter another integer that is smaller than the previous one: ")
    decimal = input("Enter a number that includes a decimal: ")

    # math
    result = int(number3) - int(number2)

    # convert integers and floats to string
    number = str(number)
    number2 = str(number2)
    number3 = str(number3)
    decimal = str(decimal)
    result = str(result)

    # Print the statement - filled in
    print("\nThere were \"" + number + "\" young \"" + animal + "\" that loved going out and \"" + verb + "\" around"
           " \"" + place + "\". \nOne day they saw Mrs.\"" + name + "\" and decided to stop to ask her a question. \n"
           "They asked: \"Why are you not \"" + adjective + "\"?\" \n"
           "She replied: \"Back in my day, when I was born \""
          + number2 + "\" years ago, only \"" + number3 + "\" people dared to ask me this question."
          "\nNow only \"" + number4 + "\" of them still live today. That means that I got rid of \"" + result +
          "\" of them.\" \nThe children paled in fear and promised to stay a minimum of \""
          + decimal + "\" kilometers away from her forever.")

main()
