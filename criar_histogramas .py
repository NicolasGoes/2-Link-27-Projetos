#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
dados = pd.read_csv('C: /Users/Nicolas/Documentos/Atividade/athlete_events.csv')


# In[ ]:


dados.head()


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


dados.hist(column= 'Age', bins = 10)
plt.show()


# In[ ]:


dados.hist(column= 'Weight', bins = 1000)
plt.show()


# In[ ]:




