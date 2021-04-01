#!/usr/bin/env python
# coding: utf-8

# # 4: Lists Solutions
# 
# 1. Reverse a given list, e.g. if you get the list `[10, 20, 30, 40, 50]` you should print `[50, 40, 30, 20, 10]`.
#     * There are two possible ways you might try this. The first is using the `reverse()` function (which is a bit like cheating), and the second is using a _scicing operator._ If you can't find anything to help online, have a look at the solutions.

# In[21]:


# Solution
input_list = [10, 20, 30, 40, 50]
print(input_list)
# Using slicing operator
input_list = input_list[::-1]
print(input_list)


# 2. Square every number in a given list of numbers, e.g. if you're given the list `[1, 2, 3, 4, 5]` you should return `[1, 4, 9, 16, 25]`.

# In[22]:


# Solution
input_list1 = [1, 2, 3, 4, 5]
# first way to do this
for i in range(len(input_list1)) :
    input_list1[i] **= 2
    
print(input_list1)

# second way
input_list2 = [1, 2, 3, 4, 5]
input_list2 = [x * x for x in input_list2]

print(input_list2)


# 3. Write a program that counts the number of times a specified element occurs within a given list. You should try writing this inside a function.

# In[23]:


# Solution
def find_elem_in_list(elem, my_list) :
    count = 0
    for x in my_list :
        if x == elem :
            count += 1
    return count

my_list = [10, 15, 20, 3, 9, 99, 20, 20, 17, 20, "Star Wars", 30, 20]
print(find_elem_in_list(20, my_list))


# 4. Write a program that, given a list of numbers, removes any even numbers and returns a list of all the odd numbers

# In[24]:


# Solution
def remove_even(my_next_list) :
    to_return = []
    for x in my_next_list :
        if x % 2 != 0 :
            to_return.append(x)
    return to_return

my_next_list = [1, 2, 3, 5, 7, 8, 9, 10, 12, 14, 22, 23, 27, 99]
print(remove_even(my_next_list))


# In[ ]:




