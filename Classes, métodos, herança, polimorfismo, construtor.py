#!/usr/bin/env python
# coding: utf-8

# In[1]:


def teste(v, i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado


# In[2]:


a = teste(10,1)


# In[3]:


a


# In[10]:


class DidaticaTech:
    
    def incrementa(self, v, i):
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado


# In[11]:


a = DidaticaTech()


# In[12]:


b = a.incrementa(10, 1)


# In[13]:


b


# In[14]:


a = DidaticaTech().incrementa(10, 1)


# In[15]:


a


# In[16]:


class DidaticaTech:
    
    def incrementa(self, v, i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado


# In[17]:


a = DidaticaTech()


# In[18]:


b = a.incrementa(10, 1)


# In[19]:


b


# In[21]:


a.valor


# In[22]:


class DidaticaTech:
    
    def __init__(self, v: int, i:int):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor += + self.incremento
        


# In[23]:


a = DidaticaTech(10, 1)


# In[24]:


a.incrementa()


# In[25]:


a.valor


# In[26]:


a.incrementa()


# In[27]:


a.valor


# In[28]:


b = DidaticaTech(10, 1)


# In[29]:


b.incrementa()


# In[30]:


b.valor


# In[31]:


class DidaticaTech:
    
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor = self.valor + self.incremento


# In[32]:


a = DidaticaTech()


# In[33]:


a.incrementa()


# In[34]:


a.valor


# In[35]:


class DidaticaTech:
    
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print("Ultrapassou 12")
        else:
            print("Não Ultrapassou 12")
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)
            


# In[36]:


a = DidaticaTech()


# In[37]:


a.incrementa()


# In[38]:


a.valor


# In[39]:


a.verifica()


# In[40]:


a.exponencial(3)


# In[41]:


a.valor_exponencial


# In[42]:


a.incrementa_quadrado()


# In[43]:


a.valor


# In[44]:


a.valor_exponencial


# In[47]:


class Calculos(DidaticaTech):
    pass


# In[48]:


c = Calculos()


# In[49]:


c.incrementa()


# In[50]:


c.valor


# In[51]:


class Calculos(DidaticaTech):
    def decrementa(self):
        self.valor = self.valor - self.incremento


# In[52]:


c = Calculos()


# In[53]:


c.incrementa()


# In[54]:


c.valor


# In[56]:


c.decrementa()


# In[57]:


c.valor


# In[71]:


class Calculos(DidaticaTech):
    def __init__(self, d=5):
        super().__init__(v=10, i=1)
        self.divisor = d
    def decrementa(self):
        self.valor = self.valor - self.incremento
    def divide(self):
        self.valor = self.valor/self.divisor


# In[72]:


c = Calculos()


# In[73]:


c.incrementa()


# In[80]:


c.valor


# In[77]:


c.decrementa()


# In[79]:


c.divide()


# In[ ]:




