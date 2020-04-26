#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


alunos = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 'Nota': [4, 7, 5.5, 9], 'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}


# In[3]:


dataframe = pd.DataFrame(alunos)


# In[4]:


print(dataframe)


# In[5]:


objeto1 = pd.Series([2, 6, 9, 10, 5])
print(objeto1)


# In[8]:


import numpy as np
array1 = np.array([6, 12, 8, 3, 4]) 
array2 = np.array([(2, 6, 9, 10, 5), (4, 6, 5, 7, 8)])
print(array1)
print(array2)


# In[9]:


objeto2 = pd.Series(array1)
print(objeto2)


# In[ ]:




