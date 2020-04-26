#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd 
alunosDIC = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 'Nota': [4, 7, 5.5, 9], 'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}


# In[20]:


alunosDF = pd.DataFrame(alunosDIC)


# In[21]:


print(alunosDF)


# In[22]:


alunosDF['Nome']


# In[23]:


alunosDF.loc[[0,1,3]]


# In[ ]:


alunosDF.loc[alunoDF['Aprovado'] == 'Sim']


# In[ ]:





# In[ ]:




