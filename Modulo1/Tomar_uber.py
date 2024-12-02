def mostrar_instrucciones():
    print("Instrucciones para tomar un Uber:")
    print("1. Abre la aplicación de Uber en tu teléfono.")
    print("2. Ingresa tu destino en la barra de búsqueda.")
    print("3. Selecciona el tipo de viaje que deseas (UberX, UberXL, etc.).")
    print("4. Confirma tu ubicación de recogida.")
    print("5. Revisa el costo estimado y el tiempo de llegada.")
    print("6. Haz clic en 'Solicitar Uber'.")
    print("7. Espera que el conductor llegue a tu ubicación.")
    print("8. Sube al vehículo y disfruta del viaje.")
    print("9. Al llegar, paga a través de la aplicación y califica tu viaje.")

def preguntar_usuario():
    nombre = input("¿Cuál es tu nombre? ")
    destino = input("¿A dónde te gustaría ir? ")
    print(f"\nHola, {nombre}! Vamos a ayudarte a tomar un Uber hacia {destino}.")

def main():
    mostrar_instrucciones()
    preguntar_usuario()

if __name__ == "__main__":
    main()
