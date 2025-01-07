"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

import random

def title():
    print("Welcome to Number Guessing Extravaganza!, guess a number between 1 and 10, see if you can guess it right!")

def game():
    x = random.randint(1,10)
    y = input("Guess a number: ")
    try:
        y = int(y)
    except:
        print("Invalid input")
        exit()
    if y > 10:
        print("Number too large")
    else:
        if x == y:
            print(f"Correct!, the number was {x}")
        else:
            print(f"Incorrect, the number was {x}")

title()

game()