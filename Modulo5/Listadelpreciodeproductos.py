lista_compras = {}
while True:
    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if producto.lower() == 'salir':
        break
    precio = float(input(f"Ingrese el precio de {producto}: "))
    lista_compras[producto] = precio
total = sum(lista_compras.values())
print("Precio total de los productos:", total)
