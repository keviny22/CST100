#!/usr/bin/env python
#Rock, Paper, Scissor:
#
#Write a program to simulate the paper-rock-scissor game. Each of the two players type in P, R, or S.
# The program then announces the winner based on the rule: Paper covers Rock, Rock breaks Scissors, Scissors cut Paper, or Nobody wins.
# Be sure to allow the players to use lowercase as well as uppercase letters.  
#
#You MUST implement a function that takes the choices that both the players made and returns 1 if the player 1 won and 2 if the player 2 won and 0 if it is a tie.
# So the logic of deciding who won based on the rock, paper, scissor rule must be programmed inside this function.
#
#You MUST call this function to decide who won and you must display the result of the game based on the return value of the function.
#
#Sample run:
#
#Player 1: Please enter either (R)ock, (P)aper, or (S)cissors: P
#
#Player 2: Please enter either (R)ock, (P)aper, or (S)cissors: s
#
#Player 2 wins.
#
#Optional: Your program can allow the users to play repeatedly say 5 times. Your program should then keep a score for each player and display that after each play.
#
#Sample run (with optional part):
#
#Player 1: Please enter either (R)ock, (P)aper, or (S)cissors: P
#
#Player 2: Please enter either (R)ock, (P)aper, or (S)cissors: s
#
#Player 2 wins.
#
#Scores after this play:
#
#Player 1: 0
#
#Player 2: 1
#
#Thanks!!


# function to decide winner of rock paper scisors
def game(str_player1, str_player2):
    if str_player1 == str_player2:
        return 0
    elif str_player1 == "p" and str_player2 == "r":
        return 1
    elif str_player1 == "r" and str_player2 == "s":
        return 1
    elif str_player1 == "s" and str_player2 == "p":
        return 1
    elif str_player1 == "r" and str_player2 == "p":
        return 2
    elif str_player1 == "s" and str_player2 == "r":
        return 2
    elif str_player1 == "p" and str_player2 == "s":
        return 2
    else:
        exit() #exit program on anyhing else (catch all)

str_player1 = input("Player 1: Please enter either (R)ock, (P)aper, or (S)cissors: ")
str_player2 = input("Player 2: Please enter either (R)ock, (P)aper, or (S)cissors: ")

winner = game(str_player1.lower(),str_player2.lower()) #call the game function
print("Player " + str(winner) + " wins")


