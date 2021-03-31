#!/usr/bin/env python
# coding: utf-8

# # 01: Syntax and Variables Exercises
# 
# These exercises should help you become more familiar with Python syntax and variables generally.

# ## Ex. 1: Character Input
# 
# 1. Create a program that asks the user to enter their name and age (think about how you will format these - two separate input variables for instance) and returns a message with their name and age.
# 2. Print a message that tells the user the year in which they will turn 100 years old.



# Solution
import datetime 

# Gets the current year
now = datetime.datetime.now()

# Get name and age
name = input("What is your name?\n ")
age = int(input("How old are you?\n "))

# Year they will turn 100 (either that year or year before, depending on DOB)
year = str((now.year - age)+100)
print(f"{name} will be 100 years old in either {year} or {int(year)-1}")


# ## Ex. 2: Odd or Even?
# 
# 1. Get a _number_ from the user and assign it to a variable `num`.
# 2. Determine whether the number is odd or even and then print an appropriate message (hint: use the operator `%` - remainder).
# 
# __Extras:__
# 
# 3. Print another message if the number is a multiple of four.
# 4. Ask the user for two numbers (instead of just one):
#     * One number to check, other to divide by the number to check.
#     * If the first divides evenly into the second, tell the user. Otherwise, print another appropriate message.



# Solution

# Get an int from the user
num = int(input("Please enter a number.\n"))

# Work out if it's divisible by four, by two (even) or odd.
if num % 4 == 0:
    print(f"{num} is divisible by four.")
elif num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# 
