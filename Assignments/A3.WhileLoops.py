# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 2

# Description: Finding the average, smallest number, and largest numbers from user input. 

def main():
    import math
    choice = "y"
    while choice == "y":
        num = 0
        sum = 0
        counter = 0
        largest = 0
        while num != -1 and num >= 0:
            num = int(input("Write a number greater than or equal to zero. Or input -1 to quit. "))

            if num != -1:
                smallest = num

            #find largest and smallest as going thru loop
            if largest < num and num!= -1:
                largest = num
            elif smallest > num and num!= -1:
                smallest = num

            #find sum
            if num != -1:
                sum = num + sum

            # take count of how many numbers added
            if num != -1:
                counter = counter + 1

            #find average
            average = sum/counter # why wont the average work

        print("The largest number is " + str(largest))
        print("The smallest number is "+ str(smallest))
        print("The average number is " + str(average))

        choice = input("Would you like to input another set of numbers? (y/n) ").lower()

    if choice == "n":
        print("Goodbye!")

main()
