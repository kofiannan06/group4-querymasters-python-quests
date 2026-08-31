#!/usr/bin/python3

def personalized_greeting(name ,quest):
    print(f"Hello {name} ! Your quest is to {quest}.")


name = input("What is your name? ")
quest = input("What ia your quest? ")

personalized_greeting(name, quest)    
