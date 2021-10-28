import socket

punto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
punto.connect((socket.gethostname(),6000))
mensaje = punto.recv(1024)
print(mensaje.decode("utf-8"))
