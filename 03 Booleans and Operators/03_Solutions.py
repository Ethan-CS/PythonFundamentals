#!/usr/bin/env python
# coding: utf-8

# # 03: Booleans and Operators Solutions
# 
# ## Task 1: Variables and Booleans

# 1. Declare a variable named `yep` and give it the string value "It is less than 2"
# 2. Write a comment above that variable (e.g. "Assign the string to a variable")


# Solution

# Assign "It is less than 2" to the variable yep
yep = "It is less than 2."


# 3. Create a variable `i` that takes the integer value 1. Again, write a suitable comment.
# 4. Create a variable named `check` assigned to the logic test `i < 2`.
# 5. Write an `if` statement that checks if the variable `i` is less than two using the variable `check`. If this is true, print the variable `yep` that you assigned before. _TIP: You don't need to declare `yep` again, you can think of all code cell in a notebook as being one Python file._

# Solution

# Assign integer value 1 to variable i
i = 1
check = i < 2

# if statement
if check :
    print(yep)


# ## Task 2: Boolean practice
# 
# Below are some boolean statements that evaluate to `True` or `False`. Write them out on paper and, for each one, write down whether it evaluates to `True` or `False`. Once you've done that, we're going to open a Python _terminal_ to see if you got it right.
# 
# 1. `True and True`
# 2. `False and True`
# 3. `1 == 1 and 2 == 1`
# 4. `"test" == "test"`
# 5. `1 == 1 or 2 != 1`
# 6. `True and 1 == 1`
# 7. `False and 0 != 0`
# 8. `True or 1 == 1`
# 9. `"test" == "testing"`
# 10. `1 != 0 and 2 == 1`
# 11. `"test" != "testing"`
# 12. `"test" == 1`
# 13. `not (True and False)`
# 14. `not (1 == 1 and 0 != 1)`
# 15. `not (10 == 1 or 1000 == 1000)`
# 16. `not (1 != 10 or 3 == 4)`
# 17. `not ("testing" == "testing" and "Ethan" == "Cool Guy")`
# 18. `1 == 1 and not ("testing" == 1 or 1 == 0)`
# 19. `"chunky" == "bacon" and not (3 == 4 or 3 == 3)`
# 20. `3 == 3 and not ("testing" == "testing" or "Python" == "Fun")`
# 
# Here is a process you might like to follow:
# * Find any equality tests (`==` or `!=`) and replace with truth value (`True`/`False`).
# * Find each `and`/`or` inside brackets and solve that first, again replacing by truth values.
# * Find each negation (`not`) and replace with the appropriate truth value.
# * Find any remaining `and`/`or` and replace with truth values.
# * You should have a single truth value now.
# 
# E.g.
# ```python
# 3 != 4 and not ("testing" != "test" or "Python" == "Python")
# ```
# Find equality tests and replace:
# 
# ```python
# True and not (True or True)
# ```
# Find `and`/`or` inside brackets:
# ```python
# True and not (True)
# ```
# Find negations and evaluate:
# ```python
# True and False
# ```
# Find remaining `and`/`or` and evaluate:
# ```python
# False
# ```
# And indeed, I'm just left with a single truth value - `False`.

# __Solution:__
# 
# ```python
# >>> print(True and True) #1
# True
# >>> print(False and True) #2
# False
# >>> print(1 == 1 and 2 == 1) #3
# False
# >>> print("test" == "test") #4
# True
# >>> print(1 == 1 or 2 != 1) #5
# True
# >>> print(True and 1 == 1) #6
# True
# >>> print(False and 0 != 0) #7
# False
# >>> print(True or 1 == 1) #8
# True
# >>> print("test" == "testing") #9
# False
# >>> print(1 != 0 and 2 == 1) #10
# False
# >>> print("test" != "testing") #11
# True
# >>> print("test" == 1) #12
# False
# >>> print(not True and False) #13
# True
# >>> print(not (1 == 1 and 0 != 1)) #14
# False
# >>> print(not (10 == 1 or 1000 == 1000)) #15
# False
# >>> print(not (1 != 10 or 3 == 4)) #16
# False
# >>> print(not ("testing" == "testing" and "Ethan" == "Cool Guy")) #17
# True
# >>> print(1 == 1 and not ("testing" == 1 or 1 == 0)) #18
# True
# >>> print("chunky" == "bacon" and not (3 == 4 or 3 == 3)) #19
# False
# >>> print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun")) #20
# False
# ```




