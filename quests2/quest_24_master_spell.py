#!/usr/bin/python3
# Create ask_for_age() which returns an age, and can_they_vote(age) which prints a message. Call the first, then pass its result to the second.
# Create ask_for_age().
def ask_for_age():
    age = int(input("Enter your age:"))
    return age
# Create can_they_vote(age).
def can_they_vote(age):
    if age >= 18:
        print("Can vote")
    else:
        print("Cannot vote")
# Call first function and use the result for the second one.
age = ask_for_age()
can_they_vote(age)
