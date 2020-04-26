#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
alunosDIC = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 'Nota': [4, 7, 5.5, 9], 'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}


# In[2]:


alunosDF = pd.DataFrame(alunosDIC)


# In[3]:


print(alunosDF)


# In[4]:


primeiraslinhas = alunosDF.loc[0:2]


# In[5]:


print(primeiraslinhas)


# In[9]:


novoDF = alunosDF.loc[alunosDF['Nota']!=9]


# In[10]:


print(novoDF)


# In[11]:


alu_repro = alunosDF.loc[alunosDF['Aprovado']=='Sim']


# In[12]:


print(alu_repro)


# In[ ]:




