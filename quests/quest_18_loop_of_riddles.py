#!/usr/bin/python3

secret_number = 7

guess = int(input("Guess the secret number: "))

while guess != secret_number:
   guess = int(input("Try again: "))

print("Correct! You guessed the secret number.")
   
