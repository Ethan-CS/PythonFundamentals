#!/usr/bin/env python
# coding: utf-8

# # Exercises 9: Functions
# 
# There are some tricky questions in here - don't be afraid to ask for help. You might find it useful to work out a rough structure or process on paper before going to code.
# 
# ## Task 1: Regular functions
# 
# 1. Write a function to find the maximum of three numbers

# In[14]:


# Solution

# This is a 'helper' function that will help the main function
def max_of_two(x, y) :
    if x > y :
        return x
    return y

# Main function - finds max of two, then finds max of that max and the third number
def max_of_three(x, y, z) :
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(31, 67, -10))


# 2. Write a function that sums all numbers in a list

# In[15]:


# Solution

def sum(numbers_list) :
    total = 0  # Initialise this to zero - it'll end up as the result
    for x in numbers_list :
        total += x  # Increase the total sum by each element in the list
    return total

print(sum([1, 2, 5, 10, 25]))


# 3. Write a function that reverses a string
# 
# E.g. "123abcde" becomes "edcba321".
# Hint: you can use `len(string)` as the starting index and work backwards

# In[16]:


# Solution

def string_reverse(string) :
    rev_string = ""  # initialise an empty string
    index = len(string)  # Start by looking at the last element
    while index > 0 :
        rev_string += string[index - 1]
        index -= 1  # Decrease index to move backwards through the string
    return rev_string


string = "123abcde"
print(string)
print(string_reverse(string))


# ## Task 2: Recursive Functions
# 
# For the next three exercises, try thinking first about your base case and then your recursive case. Write your code on paper first if it helps!
# 
# 1. Write a functio called `recursive_exponent(base, exp)` that takes a `base` and an `exp` as parameters and _recursively_ computes base ^ exp. You are not allowed to use the `**` operator!

# In[17]:


# Solution

def recursive_exponent(base, exp):
    # Base case 1 - this is how we know we're finished recursing
    if exp == 1:
        return base
    else:
        return base * recursive_exponent(base, exp - 1)

print("2^6 =", recursive_exponent(2, 6))


# 2. Write a function called `recursive_countdown(n)` that uses recursion to print numbers from `n` to `0`, where `n` will be a positive integer parameter.

# In[18]:


# Solution

def recursive_countdown(n):
    # Base case 0 - how we know we're finished recursing
    if n == 0:
        print(n)
    else:
        print(n, end=', ')
        recursive_countdown(n-1)
        
recursive_countdown(10)


# # Task 3: Higher-Order Function
# 
# A higher-order function is a function that either contains other functions as parameters or returns a function as an output.
# 
# For this exercise, we will write a function named `apply_fun_on_dict(a, my_fun)`. This function will apply a given function `my_fun` on the values of the dictionary `a`. For example, it could calculate the square of each value.
# 
# The function `my_fun` that we want to apply to the dictionary in the main function will be defined as:
# ```python
# def my_fun(element):
#     return element**2
# ```
# 
# Then, the dictionary `a` will be:
# ```python
# a = {"apple": 6,
#      "banana": 2,
#      "hello": 5,
#      "world": 4}
# ```
# and so `apply_fun_on_dict(a, my_fun)` should give the result `{"apple": 36, "banana": 4, "hello": 25, "world": 16}`.

# In[19]:


# Solution

def apply_fun_on_dict(a, my_fun):
    return {k: my_fun(v) for k, v in a.items()}

def my_fun(n):
    return n**2

a = {'apple': 6, 'banana': 2, 'hello': 5, 'world': 4}
print(apply_fun_on_dict(a, my_fun))


# In[ ]:




