import socket

conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexion.bind((socket.gethostname(),7000))
conexion.listen(5)

while True:
	clientsocket, direccion = conexion.accept()
	print(f"la conexion de la {direccion} esta establecida")
	clientsocket.send(bytes("este es el servidor"))
