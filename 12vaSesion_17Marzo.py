#!/usr/bin/env python
# coding: utf-8

# # Enfoque clásico de series de tiempo 

# **Estadistica aplicada**
# 
# **Lizbeth Ramos Saucedo**
# 
# 
# **Sesión 12 a 17 de Marzo del 2023**

# En el enfoque clásico de series del tiempo, se considera que una serie se puede descomponer en cuatro elementos:
# 
# 1. Tendencia "T"
# 2. Ciclo "C"
# 3. Estacional "S"
# 4. Irregular "E"
# 
# Usualmente se considera que no es posible separar la tendencia del ciclo, por lo que se presentan junto en lo que se llama tendencia-ciclo (tendencia)
# 

# In[22]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


pip install statsmodels


# In[24]:


#Modelo ETS (eror- trend-seasonally)
#modelo de tendencia (ciclo)-estacional-irregular
from statsmodels.tsa.api import seasonal_decompose 


# In[25]:


pasajeros = pasajeros=pd.read_csv ('https://raw.githubusercontent.com/jimmyzac/Estadistica-Aplicada-FCFM-UANL/main/bases_datos/airline_passengers.csv')


# In[26]:


pasajeros


# In[27]:


pasajeros=pasajeros.rename(columns={'Month':'mes', 'Thousands of Passengers':'miles de pasajeros'})


# In[28]:


pasajeros 


# In[29]:


pasajeros['mes']=pd.to_datetime(pasajeros['mes']) #para que mes se reconozca como variable de fecha 


# In[30]:


pasajeros


# In[31]:


pasajeros= pasajeros.set_index('mes') #mes sea el index


# In[35]:


pasajeros 


# In[32]:


pasajeros.index.freq = ' MS'
#index tiene frecuencia mensual montly frecuency 


# In[33]:


pasajeros.index


# In[41]:


pasajeros ['miles de pasajeros' ].plot(figsize=(12,6));
plt.title('Miles de pasajeros de avión en EE.UU. \n 1949-1960');


#la grafica es estacionaria cada junio se dan mas vuelos


# In[40]:


pasajeros ['miles de pasajeros' ].plot(figsize=(12,6));
plt.title('Miles de pasajeros de avión en EE.UU. \n 1960');
plt.xlim('1960-01', '1960-12'); # serie solo de 1960


# In[42]:


serieETS = seasonal_decompose (pasajeros['miles de pasajeros'], model='mult')


# In[43]:


serieETS.plot()
plt.show()


# Una serie destacionalizada ( Seasonally Adjusted) es una serie sin su componente estacional 

# In[44]:


#acceder a su componente estacional 
serieETS.seasonal

#acceder a su componente de tendencia (ciclo )
serieETS.trend

#acceder al componente irregular 
serieETS.resid


# In[49]:


pasajeros['destacionalizada']=pasajeros['miles de pasajeros']/serieETS.seasonal


# In[50]:


pasajeros['destacionalizada'].plot();


# Covid en México 

# In[59]:


confirmados = pd.read_excel('C:/Users/sauce/Downloads/covid_mex.xlsx')


# In[60]:


confirmados.head()


# In[61]:


confirmados['fecha']=pd.to_datetime(confirmados['fecha'])


# In[62]:


confirmados = confirmados.set_index('fecha')


# In[63]:


confirmados.index.freq = 'D'


# In[71]:


confirmados['nacional'].plot(figsize=(24,8));
plt.xlim('2021-07', '2022-10')


# In[73]:


serie2 = seasonal_decompose(confirmados['nacional'], model='ad')


# In[74]:


confirmados['tendencia nacional'] = serie2.trend


# In[75]:


confirmados['tendencia nacional'].plot(figsize=(18,6))
plt.title('Tendencia de casos confirmados Covid 19')
plt.show();


# In[ ]:





# In[ ]:




