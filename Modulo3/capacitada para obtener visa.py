edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
if edad >= 18 and ingresos >= 30000:
    print("Está capacitado para obtener visa.")
else:
    print("No está capacitado para obtener visa.")
