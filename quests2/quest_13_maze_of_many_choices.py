#!/usr/bin/python3
# Write a grading program. Ask for a score (0-100). Print "A" for 90+, "B" for 80-89, "C" for 70-79, and "Needs Improvement" otherwise.
# Variable used.
score = int(input("Enter score:"))
# Conditions for print.
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")
