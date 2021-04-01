#!/usr/bin/env python
# coding: utf-8

# # Exercises 9: Functions
# 
# There are some tricky questions in here - don't be afraid to ask for help. You might find it useful to work out a rough structure or process on paper before going to code.
# 
# ## Task 1: Regular functions
# 
# 1. Write a function to find the maximum of three numbers

# In[6]:


# Your solution goes here


# 2. Write a function that sums all numbers in a list

# In[7]:


# Your solution goes here


# 3. Write a function that reverses a string
# 
# E.g. "123abcde" becomes "edcba321".
# Hint: you can use negative indices, where the index `-1` gives the last element in the string, `-2` gives the second last, etc.

# In[8]:


# Your solution goes here


# ## Task 2: Recursive Functions
# 
# For the next three exercises, try thinking first about your base case and then your recursive case. Write your code on paper first if it helps!
# 
# 1. Write a functio called `recursive_exponent(base, exp)` that takes a `base` and an `exp` as parameters and _recursively_ computes base ^ exp. You are not allowed to use the `**` operator!

# In[9]:


# Your solution goes here


# 2. Write a function called `recursive_countdown(n)` that uses recursion to print numbers from `n` to `0`, where `n` will be a positive integer parameter.

# In[10]:


# Your solution goes here


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

# In[ ]:




