#!/usr/bin/python3
# Variables needed are City_name, Year, and Your_name.
City_name = "Metropolis"
Year = 1938
Your_name = "Clark Kent"
# Print the following line using strings and variables.
if isinstance(City_name, str) and isinstance(Your_name, str) and isinstance(Year, int):
    print("Welcome to {}! The year is {}, and our newest resident is {}.".format(City_name, Year, Your_name))
else:
    print("error")
