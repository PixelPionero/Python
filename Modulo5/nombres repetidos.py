nombres = set()
while True:
    nombre = input("Ingrese un nombre (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    if nombre in nombres:
        print("Este nombre ya ha sido ingresado.")
    else:
        nombres.add(nombre)
print("Nombres ingresados:", nombres)
