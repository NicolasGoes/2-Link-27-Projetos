#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
dados = pd.read_csv('C: /Users/Nicolas/Documentos/Atividade/athlete_events.csv')


# In[ ]:


dados.head()


# In[ ]:


dados.drop('ID', axis = 1, inplace = True)
dados.drop('Season', axis = 1, inplace = True)
dados.drop('City', axis = 1, inplace = True)


# In[ ]:


dados.head()


# In[ ]:




