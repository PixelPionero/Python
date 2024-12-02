notas = []
cantidad = int(input("¿Cuántas notas desea ingresar? "))
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
promedio = sum(notas) / cantidad
print(f"El promedio es: {promedio}")
