#!/usr/bin/env python
# coding: utf-8

# # 10: Solutions
# 

# 1. Create a class named `Vehicle`.
#     * Give the class attributes `max_speed` and `mileage`.
#     * Instantiate an object `car` with:
#         * `max_speed` of 120,
#         * `mileage` of 10,000
#     * Print these attributes _via an object reference._

# In[8]:


# Solution
class Vehicle :
    def __init__(self, max_speed, mileage) :
        self.max_speed = max_speed
        self.mileage = mileage
        
car = Vehicle(120, 10000)
print(f"The car has max speed {car.max_speed} and mileage {car.mileage}")


# 2. Create a child class `Bus` that:
#     * Inherits all of the variables and methods of the Vehicle class,
#     * Has another attribute: `capacity`, representing the number of people a bus object can seat.
#     * Make the `capacity` attribute have a default value of 60.
#     * Instantiate an object `megabus` with:
#         * Top speed 100,
#         * Mileage 100,000 and
#         * Capacty 80.
#     * Print these attributes _via an object reference._
#     * Print the _type_ of the `megabus` object (hint: use the `type()` method)
#     * Find out whether `megabus` is an instance of the parent `Vehicle` class (hint: use the `isinstance()` method)

# In[9]:


# Solution
class Bus(Vehicle) :
    def __init__(self, max_speed, mileage, capacity=60) :
        super().__init__(max_speed, mileage)
        self.capacity = capacity
        
megabus = Bus(100, 100000, 80)
print(f"The megabus has max speed {megabus.max_speed}, mileage {megabus.mileage} and capacity {megabus.capacity}.")
print(f"Megabus is of type {type(megabus)}") 
print(f"Megabus is an instance of Vehicle: {isinstance(megabus, Vehicle)}") # True


# In[ ]:




