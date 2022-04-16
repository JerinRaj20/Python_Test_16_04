#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd


# In[13]:


os.chdir(r'C:\Users\JERIN RAJ')


# In[3]:


df = pd.read_csv('Auto_Python_Test.csv')


# In[4]:


df


# In[6]:


## Part 1
Maximum_Price = df['price'].max()
x = df.loc[(df['price'] ==Maximum_Price)]
x


# In[7]:


## Part 3

df.groupby(['make'], sort=False)['price'].max()


# In[12]:


# Part 2

print(df.groupby(['make']).size())



# In[11]:


#Part 5

df.groupby(['make'],['fuel-type'],['body_style'] sort=False)['city_mpg'].avg()
df.groupby(['make'],['fuel-type'],['body_style'] sort=False)['highway_mpg'].avg()


# In[ ]:


#Part 4

