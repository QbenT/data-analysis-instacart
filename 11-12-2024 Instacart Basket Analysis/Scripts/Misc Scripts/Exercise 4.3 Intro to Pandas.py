#!/usr/bin/env python
# coding: utf-8

#  # Exercise 4.3 Intro to Pandas

# # 01. Importing libraries

# In[38]:


# step 3
# Import libraries
import pandas as pd
import numpy as np
import os


# # Importing Data (orders.csv)

# In[40]:


# step 4 and 5
# import orders.csv (column eval_set omitted)
path = r'C:\Users\kthav\My Pc\Desktop\Career Foundry\Data Immersion\Python Fundamentals for Data Analytics\11-12-2024 Instacart Basket Analysis'


# In[41]:


path


# In[42]:


df =pd.read_csv(os.path.join(path, 'Data', 'Original Data', 'orders.csv'), index_col = False)


# In[43]:


df.info()


# In[44]:


vars_list = ['order_id', 'user_id', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order']


# In[45]:


df = pd.read_csv(os.path.join(path, 'Data', 'Original Data', 'orders.csv'), usecols = vars_list)


# In[47]:


# step 6
# print first 5 rows of df
df.head(5)


# # Importing Data (products.csv)

# In[54]:


# step 7
# import products.csv as df_prods
df_prod = pd.read_csv(os.path.join(path, 'Data', 'Original Data', 'products.csv'), index_col = False)


# In[56]:


df_prod.info()


# In[58]:


# step 5 
# print first 20 rows of df_prod
df_prod.head(20)


# In[62]:


# print last 35 rows of df_prod
df_prod.tail(35)


# In[66]:


# step 9
# print df_prod column names
df_prod.columns


# In[68]:


# step 10
# print df_prod number of rows and columns
df_prod.shape


# ## 49693 rows and 5 columns

# In[79]:


# step 11
# print pd_prod max value
max_aisle_id = df_prod['aisle_id'].max()
print(max_aisle_id)


# In[81]:


## Max value of 'aisle_id' = 134


# In[85]:


# step 11
# print pd_prod data type
department_id_dtype = df_prod['department_id'].dtype
print(department_id_dtype)


# ## Data type of 'department_id' = int64

# In[ ]:




