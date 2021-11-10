#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket

url = "www.buda.com"
puerto = 443
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((url, puerto))
client1.connect((url, puerto))
client2.connect((url, puerto))

def getbitcoin():
    request = "GET /api/v2/markets/btc-clp HTTP/1.1\r\nHost: %s\r\n\r\n" % url
    client.send(request.encode())
    file = open("bitcoin.txt", "w")
    respuesta = client.recv(1024)
    datos = respuesta.decode()
    file.write(datos + "\n")
    file.close()
getbitcoin()    

def getorderbook():
    request1 = "GET /api/v2/markets/btc-clp/order_book HTTP/1.1\r\nHost: %s\r\n\r\n" % url
    client1.send(request1.encode())
    file1 = open("orderbook.txt", "w")
    respuesta1 = client1.recv(1024)
    datos1 = respuesta1.decode()
    file1.write(datos1 + "\n")
    file1.close()
getorderbook()    

def gettrades():
    request2 = "GET /api/v2/markets/btc-clp/trades HTTP/1.1\r\nHost: %s\r\n\r\n" % url
    client2.send(request2.encode())
    file2 = open("orderbook.txt", "w")
    respuesta2 = client2.recv(1024)
    datos2 = respuesta2.decode()
    file2.write(datos2 + "\n")
    file2.close()
gettrades() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




