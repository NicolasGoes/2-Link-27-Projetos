#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
arquivo = pd.read_csv('/home/nicolas/Documentos/wine_dataset.csv')


# In[2]:


arquivo.head()


# In[14]:


arquivo['style'] = arquivo['style'].replace('red',0)


# In[15]:


arquivo['style'] = arquivo['style'].replace('white',1)


# In[16]:


y = arquivo['style']
x = arquivo.drop('style', axis = 1)


# In[17]:


from sklearn.model_selection import train_test_split


# In[18]:


x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)


# In[20]:


from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()
modelo.fit(x_treino,y_treino)
resultado = modelo.score(x_teste, y_teste)
print("Acurácia:", resultado)


# In[21]:


previsoes = modelo.predict(x_teste[400:403])


# In[22]:


previsoes


# In[23]:


y_teste[400:403]


# In[ ]:




