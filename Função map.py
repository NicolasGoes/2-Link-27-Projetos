#!/usr/bin/env python
# coding: utf-8

# In[1]:


kph = [40, 50, 30, 100, 120, 85, 57, 98]


# In[2]:


mph = []
for i in kph:
    mph.append(i/1.61)
print(mph)


# In[3]:


mph2 = list(map(lambda x: x/1.61,kph))
print(mph2)


# In[ ]:




