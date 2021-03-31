#!/usr/bin/env python
# coding: utf-8

# # 02: Numbers and Strings Solutions
# 
# These exercises are to help you become more familar working with numbers and strings in Python.
# 
# ## Ex. 1: Guessing Game
# 
# 1. Generate a random number between 1 and 10.
# 2. Ask the user to guess the number and tell them whether they guessed too high/low or guessed the number.
# 3. Keep the game going until the user guesses the number or types `exit` (hint: `while True:`
# 4. Keep track of how many guesses the user takes and when the game ends, print this to the console.


# Solution

import random

# Generate a random number between 1 and 10
rand = random.randint(1, 10)

# Initialise guess and count variables - random number can't be 0.
guess = 0
count = 0

while guess != rand and guess != "exit":
    guess = input("Please make a guess.\n")
    
    # If the user types exit, break the loop
    if guess == "exit":
        break
        
    # Cast guess to an integer and increase the guess counter
    guess = int(guess)
    count += 1
    
    if guess < rand:
        print("Go higher!")
    elif guess > rand:
        print("Go lower!")
    else:
        print(f"That's it!\nYou got it in {count} guesses, well done!")


# ## Ex. 2: String List
# 
# 1. Ask the user for a string (this can be anything) and print whether the string is a palindrome or not.


# Solution

word = input("Please enter a word.\n").lower()
reverse = word[::-1]
print(f"Your word reversed is {reverse}")

if word == reverse:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")


# ## Ex. 3: Rock, Paper, Scissors
# 
# 1. Make a two-player rock-paper-scissors game.
# 
# Hint: ask for each player to input a play, compare, print a message of congratulations to the winner and ask if they want to start a new game. Remember: rock > scissors > paper > rock.


# Solution

# LotR version: Orc beats Hobbit, Hobbit beats Elf, Elf beats Orc.
print('''Please pick one:
            Orc
            Hobbit
            Elf''')

while True:
    game_dict = {'Orc': 1, 'Hobbit': 2, 'Elf': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game (y/n)?\n').lower()) == 'y':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game (y/n)?\n').lower) == 'y':
            continue
        else:
            print('Game over. Thanks for playing!')
            break
    else:
        print('Draw.Please continue.')
        print('')


# ## Ex. 4: Fibonacci
# 
# 1. Write a program that asks the user how many Fibonacci numbers to generate and then generate that many.
# 2. Try and use functions to complete this task.
# 
# Hint: the Fibonacci sequence is a sequence of numbers where the next number is the sum of the previous two. It begins at 1, then 1 again, then 1+1=2 so the next number is 2, 2+1=3 so then we move to 3, then 5, etc. so we have 1, 1, 2, 3, 5, 8, 13, ...

# Solution


def fibonacci():
    num = int(input("How many numbers to generate?\n"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(fibonacci())


# ## Ex. 5: Reverse word
# 
# 1. Write a program (with functions) that gets a long string containing multiple words from the user.
# 2. Print the same string back to the user with the _words_ in the _reverse order._ For instance, "My name is Ethan" becomes"Ethan is name My".

# Solution


# Here are some possible ways you may have solved this

# method 0: to make me look clever
def reverse_v0(w):
  return ' '.join(w.split()[::-1])

# method 1: loop through the words and insert each word 
# at the begining of the result list
def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)

# method 2
def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])
  
# method 3
def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))

# method 4
def reverse_v4(x):
  y = x.split()
  y.reverse()
  return " ".join(y)

# test code - to make sure all methods work
test1 = input("Enter a sentence: ")
print(reverse_v0(test1))
print(reverse_v1(test1))
print(reverse_v2(test1))
print(reverse_v3(test1))
print(reverse_v4(test1))


# ## Ex. 6: Password generator
# 
# 1. Write a program that generates passwords. Be creative - use a mix of lowercase and uppercase letters, numbers and symbols. 
# 2. Make sure passwords are random and a new one is generated each time you run the program.

# Solution


# generate a password with length "passlen" with no  
# duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 12
p =  "".join(random.sample(s,passlen ))
print(p)


# ## Ex. 7: Check for Primality
# 
# Every good prime number generator starts with code that can check whether a given number is prime or not (so it knows which numbers to output and which to ignore).
# 
# 1. Ask the user for a number and determine whether it is prime or not.
# 2. To do this, you might write code that asks the user for a number and then prints out a list of all the numbers that divide evenly into that number (e.g. 18/9 gives a whole number, so 9 is a divisor of 18 and it would be printed). 
# 3. Recall that a prime number's only divisors are 1 and itself - you can then perform a logical test to see whether this is true of a given number, thereby seeing if it is prime or not.

# Solution


def get_number(prompt):
    # Returns integer value for input. Prompt is displayed text
    return int(input(prompt))    
    
def is_prime(number):
    # Returns True for prime numbers, False otherwise
    #Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes    
    else:
        prime = True
        for check_number in range(2, int((number / 2)+1)):
            if number % check_number == 0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number," is ", descriptor, "prime.", sep = "", end = "\n\n")
    

print_prime(get_number("Enter a number to check."))





