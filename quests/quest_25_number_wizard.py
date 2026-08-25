#!/usr/bin/python3

secret_number = 7

while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("Correct! You found the secret number.")
        break
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
