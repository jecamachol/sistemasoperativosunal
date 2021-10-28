

ruta = 'archivo.txt'

def leer():
	file = open(ruta,"r")
	print(file.read())

def escritura():
	texto = "este es un texto"
	ruta = 'archivo1.txt'
	file = open(ruta,"w")
	file.write(texto)


def lectoescritura(): 
	leer()
	escritura()



lectoescritura()