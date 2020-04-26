#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
dados = pd.read_csv('C: /Users/Nicolas/Documentos/Atividade/athlete_events.csv')


# In[ ]:


dados.rename(columns = {'Name':'Name', 'Sex': 'Sexo'}, inplace = True)


# In[ ]:


dados.head()


# In[ ]:


altura = dados['Height']


# In[ ]:


type(altura)


# In[ ]:


dados['City'].value_counts()


# In[ ]:





# In[ ]:




