#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
dados = pd.read_csv('C: /Users/Nicolas/Documentos/Atividade/athlete_events.csv')


# In[ ]:


dados.head()


# In[ ]:


dados2 = dados.dropna()


# In[ ]:


dados2.shape


# In[ ]:


dados.chape


# In[ ]:


enulo = dados.isnull()
enulo.head(100)


# In[ ]:


faltantes = dados.isnull().sum()
print(faltantes)


# In[ ]:


faltantes_percentual = (dados.isnull().sum() / len(dados['ID']))*100


# In[ ]:


print(faltantes_percentual)


# In[ ]:


dados['Metal'].fillna('Nenhuma', inplace = True)
dados['Metal'].fillna(dados['Age'].mean(), inplace = True)


# In[ ]:





# In[ ]:





# In[ ]:




