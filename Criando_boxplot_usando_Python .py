#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
dados = pd.read_csv('C: /Users/Nicolas/Documentos/Atividade/athlete_events.csv')


# In[ ]:


dados.head()


# In[ ]:


import matplotlib.pyplot as plt
dados.boxplot(column='Age','Height', 'Weight')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




