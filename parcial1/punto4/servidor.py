#!/usr/bin/env python
# coding: utf-8

# In[2]:


from asyncio.base_events import Server
import socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind(("localhost",8000))
servidor.listen(128)
conexion, addr = servidor.accept()
f = open(r"C:\Users\Kike\Desktop\parcial\punto4\pulp fiction.jpg", "wb")
    
while True:
        try:
            input_data = conn.recv(1024)
        except TypeError:
            print("error")
            break
        else:
            if indata:
                if isinstance(indata, bytes):
                    a = indata[0] == 1
                else:
                    a = indata == chr(1)
                if not a:
                    f.write(indata)
                else:
                    break
    
print("se recibio el archivo")
f.close()


# In[ ]:





# In[ ]:




