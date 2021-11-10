#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from pandas import ExcelWriter
df = pd.DataFrame({'Funcion': [1, 2,3,4,5],
                   'Definicion': ['Scandir Esta funcion devuelve un iterador de archivos y recibe como parametro la ruta de acceso.','Times retorna los tiempos generales de los procesos.', 'Mkdir Esta funcion retorna la ruta del archivo que se va a crear.', 'Listdir Esta fucnion devuelve la lista de de subcarpetas de una carpeta dada.','Getlogin Devuelve el nombre de usuario asociado a la terminal de un proceso .'],
                   })
df = df[['Funcion', 'Definicion']]
writer = ExcelWriter('Funciones.xls')
df.to_excel(writer, 'Datos', index=False)
writer.save()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




