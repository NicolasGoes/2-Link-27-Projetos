#!/usr/bin/env python
# coding: utf-8

# In[1]:


kph = [40, 50, 30, 100, 120, 85, 57, 98]


# In[8]:


mph = []
for i in kph:
    mph.append(i/1.61)
print(mph)


# In[9]:


mph2 = list(map(lambda x: x/1.61,kph))
print(mph2)


# In[10]:


mph3 = [x/1.61 for x in kph]
print(mph3)


# In[11]:


caracteres = [i for i in 'Didatica Tech']


# In[12]:


print(caracteres)


# In[ ]:




