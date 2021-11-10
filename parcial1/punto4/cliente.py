#!/usr/bin/env python
# coding: utf-8

# In[2]:


import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",8000))

while True:
        file = open(r"C:\Users\Kike\Desktop\parcial\punto4\korn.png", "rb")
        cont = file.read(1024)
        while cont:
            client.send(cont)
            content = file.read(1024)
        break

try:
        client.send(chr(1))
except TypeError:
       client.send(bytes(chr(1), "utf-8"))
    
    
client.close()
file.close()


# In[ ]:





# In[ ]:




