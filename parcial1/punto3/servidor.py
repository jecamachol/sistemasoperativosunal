#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

misocket = socket.socket()
misocket.bind (("localhost",7000))
misocket.listen(5)

text = "soy el servidor"
while True:
    conexion, addr = misocket.accept()
    print ("la conexion se establecio")
    print (addr)
    
    peticion = conexion.recv(1024)
    print (peticion)
    
    conexion.send(text.encode("ascii"))
    conexion.close()
    


# In[ ]:





# In[ ]:





# In[ ]:




