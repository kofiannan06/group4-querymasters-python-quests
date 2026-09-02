#!/usr/bin/python3
# A club bouncer requires guests to be 18+ AND have 20+ gold coins. Ask the user for their age and gold, and tell them if they can enter.
# Variables needed.
age = int(input("Enter age:"))
gold_coins = int(input("Enter amount of gold coins you have:"))
# The conditions to be met.
if age >= 18 and gold_coins >= 20:
    print("You can enter!")
else:
    print("Access denied. Please come back when you meet the standards of our club")
