#!/usr/local/bin/python3
#Python 3.5.0
#Daniel A. Christie ©2015
#Portland Tech Academy Assignment

'''Need to import the functions I will call from other files for access'''
from Call_function_from_another_file2 import commandThrall_A, rollTheDie
from Call_function_from_another_file3 import commandThrall_B
import sys


askForNum = None 

def getNum():
    guess = input("Please type in a number between 1 and 10 or type 0 to quit: ")
    return guess

def checkNum():
    print("\nWe are going to play a game. You will need to guess the random number.")
    ranNum = rollTheDie() #Calling function from another file with random generator
    count = 0
    while count != 1:
        guess = int(getNum())
        if guess == ranNum:
            print("\n{} was the right number, good job!".format(ranNum))
            count += 1
        elif guess == 0:
            print("\nOK, you don't want to play right now. Maybe later...")
            count += 1
        else:
            print("\n{} is not right. Guess again...".format(guess, ranNum))
    

def command_Thralls(): ##<---did not require an argument)#
    #Calling these functions from other files to get their returns and storing
    #their returns to a variable for future use.
    getA = commandThrall_A()
    getB = commandThrall_B()
    print(getA) #Decided to print the values stored as well.
    print(getB)

    #demonstrating that I have sucessfully grabed the data from these functions
    #and stored their value to do other things with their data.
    x = getA + " " + getB
    print(x)

    y = checkNum()

if __name__ == '__main__':

    command_Thralls()
