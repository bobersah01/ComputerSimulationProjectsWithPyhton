#!/usr/bin/env python
# coding: utf-8

# In[27]:


#hit or miss method
import random
import numpy
import numpy as np

# constant numbers
a = 1
b = 3
N = 1000000 # number of random points to generate

def takingIntegral(x):
    M = 2
    theta = 4
    return 1/(np.sqrt(2*np.pi)*theta)*np.exp(-(x-M)**2/(2*theta**2))
    #return x**2
    
# Find the maximum value of takingIntegral(x) in the interval [a, b]
x_values = np.linspace(a, b, N)
max_y = np.max(takingIntegral(x_values))
print("Maximum Y value: {}".format(max_y))

# generating random (x,y) pairs
index = 0
for i in range(N):
    x = random.uniform(a, b)
    y = random.uniform(0, max_y)
    if y <= takingIntegral(x):
        index += 1

integralResult = (b-a) * max_y * index / N
print(integralResult)


# In[ ]:





# In[ ]:




