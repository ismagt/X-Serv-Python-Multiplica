#!/usr/bin/python3

rango=range(1,11)
for numero in rango:
	print ("Tabla del " + str(numero))
	for elemento in rango:
		producto=numero*elemento
		print (str(numero)+ " x", str(elemento), "=", str(producto)+"\n")
