nombres = []
while True:
    nombre = input("Ingrese un nombre (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    nombres.append(nombre)
nombres.sort(key=len)
print("Nombres organizados por tamaño:", nombres)
