archivo = open("prueba.txt", "r")

parte1 = archivo.read(5)
print("Primera Parte", parte1)

parte2 = archivo.read(5)
print("Segunda Parte", parte2)

parte3 = archivo.read(5)
print("Tercera Parte", parte3)

archivo.close()