#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[10]:


# Write a function that, given a 2d numpy array, returns (write all functions to hw1/q7/main.py )
##write your example/test case 2D array
x = np.array([(1.255,-1.55,-1.888), (4,5,6)], dtype = float)
x


# In[6]:


# 7.1 A 2d array with rows of magnitude>1
##square each element and then add them and sqrt
def Q7_1(X):
    return X[np.linalg.norm(X, axis=1)>1]
Q7_1(x)


# In[10]:


# 7.2 A 1d array with all elements of the matrix in a column-major way
def Q7_2 (X):
    return X.flatten(order='F')
print(Q7_2(x))


# In[18]:


# 7.3 A 2d array with all the negative values replaced by zero
def Q7_3 (X):
    #this works b/c python is passing by reference, changing/assigning at this point will change original data (not a copy)
    X[X<0]= 0 
    return X
print(Q7_3(x))


# In[62]:


# 7.4 A 3x4 Block Matrix (2d array) with each block as the input 2d array
def Q7_4 (a):
    Y=np.block([[a, a, a, a],
                [a, a, a, a],
                [a, a, a, a],
                [a, a, a, a]])
    return Y
print(Q7_4(x))


# In[15]:


# 7.5 A 2d array with all elements of the input array rounded to the nearest hundred
def Q7_5(X):
    X=np.round(X, decimals=2) ## note, this performs "bankers" rounding, not always rounding 0.5 up. check if your implementation NEEDS rounding up as a req, because many cases its won't be good to anyways
    return X
print(Q7_5(x))


# In[16]:


# 7.6 A 2d array with each number converted to a python string
def Q7_6 (X):
    return X.astype(str)

print(Q7_6(x))


# In[17]:


# 7.7 Median of all entries in the array
def Q7_7 (X):
    return np.median(X)

print(Q7_7(x))

