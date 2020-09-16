# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 8

# Description:
# This is a program that uses functions to simulate a 2p game of Tic Tac Toe. Note: printPrettyBoard function is located
# within the Tic-Tac-Toe Helper

import TicTacToeHelper
import random

def isValidMove(boardList, spot):
    if spot.isdigit():
        spot = int(spot)
        if 0 <= spot < 10:
            if boardList[spot] != 'x' and boardList[spot] != 'o':
                return True
        else:
            print("Invalid move, please pick again")
            return False
    else:
        print("Invalid entry, please pick again (between 0 and 8)")
        return False

def updateBoard(boardList, spot, playerLetter):
    spot = int(spot)
    boardList[spot] = playerLetter.lower()

def playGame():
    print("Welcome to Tic Tac Toe!")
    # initialize the list
    boardList = []
    for number in range(0,9):
        boardList.append(str(number))

    # Asks user to pick X or O
    keepAsking = True
    while keepAsking:
        whoStarts = input("Would you like to play as player 'X', or 'O'? (x/o): ")
        if whoStarts.lower() == "x" or whoStarts.lower() == "o":
            keepAsking = False
        else:
            print("Invalid input")

    # sets letter of other player based on input
    if whoStarts.lower() == "x":
        otherPlayer = "o"
    else:
        otherPlayer = "x"

    #Asks user whether to play against computer
    keepAsking = True
    while keepAsking:
        computerPlays = input("Would you like to play against the computer? (y/n): ")
        if computerPlays.lower() == "y" or computerPlays.lower() == "n":
            keepAsking = False
        else:
            print("Invalid input")

    # chose spot to place x or o
    counter = 0
    gameIsOn = True
    while gameIsOn:
        # printing the board
        TicTacToeHelper.printPrettyBoard(boardList)

        # placing the x's and o's
        if counter%2 == 0: # if even turn number, it is the first player's turn
            repeat = True
            while repeat:
                play = input("Player " + whoStarts + " pick a spot: ")
                if isValidMove(boardList, play):
                    repeat = False
                    updateBoard(boardList, play, whoStarts.lower())

        elif counter%2 != 0: # if odd turn number, it is other player's turn
            repeat = True
            while repeat:
                if computerPlays == "n":
                    play = input("Player " + otherPlayer + " pick a spot: ")
                    if isValidMove(boardList, play):
                        repeat = False
                        updateBoard(boardList, play, otherPlayer.lower())
                else:
                    print("It's the computer's turn")
                    play = str(random.randrange(0, 9))
                    if isValidMove(boardList, play):
                        repeat = False
                        updateBoard(boardList, play, otherPlayer.lower())
        counter+=1

        # check for winner and ask whether to keep playing
        result = TicTacToeHelper.checkForWinner(boardList, counter)
        if result == 'x' or result=='o' or result == 's':
            TicTacToeHelper.printPrettyBoard(boardList)
            print("Game over!")
            if result == 'x':
                print("Player x is the winner!")
            elif result == 'o':
                print("Player o is the winner!")
            elif result == 's':
                print("Stalemate reached!")

            # Ask whether to keep playing after the game ends
            keepAsking = True
            while keepAsking:
                keepPlaying = input("Would you like to play another round? (y/n): ")
                if keepPlaying.lower() == "y" or keepPlaying.lower() == "n":
                    keepAsking = False
                    if keepPlaying.lower() == "n":
                        gameIsOn = False
                    else:
                        # initialize the list since they still wanna play
                        boardList = []
                        for number in range(0, 9):
                            boardList.append(str(number))
                        # reset the counter as well
                        counter = 0

def main():
    playGame()

main()