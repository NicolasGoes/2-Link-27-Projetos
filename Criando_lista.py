#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random 
cidades = ['Ceara', 'São Paulo', 'Rio de Janeiro', 'Porto Alegre']
escolhida = random.choice(cidades)
print('A cidade escolhida é:', escolhida)


# In[17]:


a = [1, 2, 3] 


# In[18]:


a.append(15)


# In[19]:


print(a)


# In[20]:


b = [7, 8, 9]


# In[21]:


for item in b:
    a.append(item)
print(a)


# In[ ]:




