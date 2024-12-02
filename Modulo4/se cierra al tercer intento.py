intentos = 0
while intentos < 3:
    respuesta = input("Ingrese 'salir' para cerrar el programa: ")
    if respuesta.lower() == 'salir':
        print("Programa cerrado.")
        break
    intentos += 1
else:
    print("Has alcanzado el máximo de intentos. Programa cerrado.")
