#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]


# In[4]:


plt.scatter(x,y)
plt.show()


# In[11]:


import numpy as np
x1 = np.arange(-1000, 1000, 1)
print(x1)


# In[13]:


plt.plot(x1, -x1**3+4)
plt.show()


# In[ ]:




