#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
from scipy.stats import skew


# In[2]:


df=pd.read_csv('fuel_data.txt')


# In[3]:


df.head()


# In[5]:


A = [1,2,3,4,5,6]
B = [13, 21, 34]
A.extend(B)
print(A)


# In[6]:


np.identity(3)


# In[15]:


df.isnull().sum()


# In[16]:


df['fuel_unit'].fillna('mcf', inplace=True)


# In[18]:


df.isnull().sum()


# In[26]:


ca = df.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean().nsmallest()
ca


# In[33]:


a = df['fuel_mmbtu_per_unit'].std()
a


# In[34]:


df.describe()


# In[43]:


b = df['fuel_qty_burned'].skew().round(2)
d = df['fuel_qty_burned'].kurt().round(2)
print(b,d)


# In[40]:





# In[41]:


##please revert to in15 above


# In[42]:


## categorical mode inputation


# In[44]:


df.corr().loc['fuel_cost_per_unit_burned']  ##2nd and 3rd correlation is found in fuel_mmb_per_unit, fuel_qty_burned


# In[51]:


df([['report_year'==1998] & ['report_year'==1994]]).pct_change()
df


# In[52]:


p = df.groupby('report_year')['fuel_cost_per_unit_delivered'].mean().nlargest() ##highest is 1997
p


# In[ ]:




