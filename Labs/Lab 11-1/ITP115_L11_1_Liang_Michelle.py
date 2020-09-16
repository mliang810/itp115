# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 11-1
import random
class Die():
    def __init__(self, numSides=6):
        self.rollValue = 0
        self.sides = numSides

    def roll(self):
        self.rollValue = random.randrange(1, self.sides + 1)

    def __str__(self):
        result = "Die has " + str(self.sides) + " sides and rolled a " + str(self.rollValue)
        return result

def calculateSum(die1, die2):
    die1.roll()
    die2.roll()

    print(die1)
    print(die2)

    sum = die1.rollValue + die2.rollValue
    print("The sum of Dice 1 and Dice 2 is", sum)
    return sum

def main():
    # die 1 questions - default side? and how many sides
    keepAsking = True
    while keepAsking:
        dieSideDecide = input("Would you like to use the default number of sides(6) for the first die? (y/n): ")
        if dieSideDecide.lower() == "y" or dieSideDecide.lower() == "n":
            keepAsking = False
            if dieSideDecide.lower() == "n":
                again = True
                while again:
                    sides1 = input("How many sides for die 1?: ")
                    if sides1.isdigit():
                        again = False
                        die1 = Die(int(sides1))
            else: # default
                die1 = Die()

    # die 2 questions - default side? and how many sides
    keepAsking = True
    while keepAsking:
        dieSideDecide = input("Would you like to use the default number of sides(6) for the second die? (y/n): ")
        if dieSideDecide.lower() == "y" or dieSideDecide.lower() == "n":
            keepAsking = False
            if dieSideDecide.lower() == "n":
                again = True
                while again:
                    sides2 = input("How many sides for die 2?: ")
                    if sides2.isdigit():
                        again = False
                        die2 = Die(int(sides2))
            else: # default
                die2 = Die()

    # number of rolls for each die
    keepAsking = True
    while keepAsking:
        rolls = input("How many times do you want to roll the die?: ")
        if rolls.isdigit():
            keepAsking = False
            rolls = int(rolls)
            while rolls >0:
                rolls-=1
                calculateSum(die1, die2)


main()