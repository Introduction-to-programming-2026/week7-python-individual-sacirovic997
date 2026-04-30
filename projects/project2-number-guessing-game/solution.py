# Project 2 - Number Guessing Game
# Author: Sacirovic
# Date: 30.04.2026

import random

secret_number = random.randint(1, 10)
guesses = 0

guess = int(input("Guess a number between 1 and 10: "))
guesses += 1

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))
    guesses += 1

print(f"Correct! You guessed it in {guesses} guesses!")
