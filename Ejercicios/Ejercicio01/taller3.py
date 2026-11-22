archivo = open("datos.txt", "rb") 

datos = archivo.read(20) 

print("Datos:", datos) 

print("Cantidad leída:", len(datos)) 


archivo.close() 