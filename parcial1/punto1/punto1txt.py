#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
archivo = "funciones"
def escribir():
    with open (archivo, 'w', encoding = "utf-8" ) as f:
        f.write("1) Scandir Esta funcion devuelve un iterador de archivos y recibe como parametro la ruta de acceso. \n")
        f.write("2) Times retorna los tiempos generales de los procesos. \n")
        f.write("3) Mkdir Esta funcion retorna la ruta del archivo que se va a crear. \n")
        f.write("4) Listdir Esta fucnion devuelve la lista de de subcarpetas de una carpeta dada. \n")
        f.write("5) Getlogin Devuelve el nombre de usuario asociado a la terminal de un proceso . \n")
        
escribir()            
              


# In[ ]:





# In[ ]:




