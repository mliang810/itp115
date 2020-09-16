# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 7

# Description:
# Playing rock, paper, scissors
import random
def displaymenu():
    print("Welcome! Let's play rock, paper, scissors.\nThe rules of the game are:"
          "\nRock smashes scissors\nScissors cut paper\nPaper covers rock\nIf both the choices are the same, it's a tie")
def playRound(cpu, person):
    if person == 0:
        print("You chose rock")
    if person == 1:
        print("You chose paper")
    if person == 2:
        print("You chose scissors")
    if cpu == 0: # rock
        print("The computer chose rock")
        if person == 0: # tie
            return 0
        if person == 1: # win
            return 1
        if person == 2: # lose
            return -1
    elif cpu == 0: # paper
        print("The computer chose paper")
        if person == 0: # lose
            return -1
        if person == 1: # tie
            return 0
        if person == 2: # win
            return 1
    else: # scissors
        print("The computer chose scissors")
        if person == 0: # win
            return 1
        if person == 1: # lose
            return -1
        if person == 2: # tie
            return 0
def continueGame():
    choice = input("Would you like to play again? (Y/N): ")
    asking = True
    while asking == True:
        asking = False
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            asking = True
            choice = input("Invalid input, would you like to play again? (Y/N)")
def getComputerChoice():
    return random.randrange(3)

def main():
    counterPlayer = 0
    counterComp = 0
    keepPlaying = True

    while keepPlaying:
        # get rock paper scissor choice for player and comp
        displaymenu()
        player = int(input("Please choose a number to play. (0) for Rock, (1) for Paper, and (2) for Scissors: "))
        comp = getComputerChoice()
        result = playRound(comp, player)
        if player == 0 or player == 1 or player == 2:
            if result == 1:
                print("You Win")
                counterPlayer+=1
            elif result == -1:
                print("You Lose")
                counterComp += 1
            else:
                print("Tie")
        else: # when none of the choices are valid
            ask = True
            while ask == True:
                choice = input("Invalid input, would you like to try again? (Y/N)")
                ask = False
                if choice.lower() == "y":
                    keepPlaying = True
                if choice.lower() == "n":
                    keepPlaying = False
                else:
                    ask = True

        # play again?
        if continueGame() == False:
            keepPlaying = False

    # print score when they quit
    print("Here are the final scores:\nYou:", counterPlayer, "Computer:", counterComp)
    print("Goodbye!")

main()
