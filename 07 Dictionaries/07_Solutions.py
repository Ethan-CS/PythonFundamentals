#!/usr/bin/env python
# coding: utf-8

# # 7: Dictionaries Solutions
# 
# 1. Below are two lists, `keys` and `values`. Combine these into a single dictionary.
# 
# ```python
# keys = ['Ben', 'Ethan', 'Stefani']
# values = [1, 29, 28]
# ```
# Expected output:
# ```python
# {'Ben': 1, 'Ethan': 29, 'Stefani': 28}
# ```
# _Hint: look up the `zip()` function..._

# In[1]:


keys = ['Ben', 'Ethan', 'Stefani']
values = [1, 29, 28]

# Cheat way of doing it - if you thought of a clever way, good on you!
my_dict = dict(zip(keys, values))
print(my_dict)


# 2. Below are two dictionaries. Merge them into a single dictionary.
# 
# ```python
# dict1 = {'Ben': 1, 'Ethan': 29}
# dict2 = {'Stefani': 28, 'Madonna': 16, "RuPaul": 17}
# ```
# Expected output:
# ```python
# {'Ben': 1, 'Ethan': 29, 'Stefani': 28, 'Madonna': 16, 'RuPaul': 17}
# ```

# In[6]:


dict1 = {'Ben': 1, 'Ethan': 29}
dict2 = {'Stefani': 28, 'Madonna': 16, "RuPaul": 17}

'''
In Python 3.9+, we can use `dict3 = dict1 | dict2`
In Python 3.5+ we can use `dict3 = {**dict1, **dict2}`
But I'll show you the long, non-cheat way anyway
'''

def merge_two_dicts(x, y) :
    z = x.copy()  # Start with all entries in x
    z.update(y)   # Then, add in the entries of y
    return z      # Return

dict3 = merge_two_dicts(dict1, dict2)
print(dict3)


# 3. From the dictionary given below, extract the keys `name` and `salary` and add them to a new dictionary.
# 
# Dictionary:
# ```python
# sample_dict = {
#     "name": "Ethan",
#     "age": 21,
#     "salary": 1000000,
#     "city": "Glasgow"
# }
# ```
# Expected output:
# ```python
# {'name': 'Ethan', 'salary': 1000000}
# ```

# In[14]:


sampleDict = { 
    "name": "Ethan",
    "age": 21,
    "salary": 1000000,
    "city": "Glasgow" 
}

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)


# In[ ]:




