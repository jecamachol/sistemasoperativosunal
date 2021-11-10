#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket

misocket = socket.socket()
misocket.connect(("localhost",7000))

f = open("index.html", "rb")
contenido = f.read(1024)
misocket.send(contenido)
respuesta = misocket.recv(1024)

print (respuesta)
misocket.close()


