def practicar_regularmente():
    print("1. Practica regularmente: La programación es una habilidad que mejora con la práctica.")

def aprender_fundamentos():
    print("2. Aprende los fundamentos: Asegúrate de entender bien los conceptos básicos.")

def leer_codigo():
    print("3. Lee código de otros: Estudia el código de programadores experimentados para aprender buenas prácticas.")

def trabajar_proyectos():
    print("4. Trabaja en proyectos: Aplica tus conocimientos en proyectos reales o personales.")

def mantenerse_actualizado():
    print("5. Mantente actualizado: La tecnología cambia rápidamente; sigue aprendiendo.")

def colaborar_otros():
    print("6. Colabora con otros: Trabajar en equipo te ayudará a mejorar y aprender de los demás.")

def no_temas_errores():
    print("7. No temas a los errores: Aprende de tus errores y busca soluciones.")

def escribir_documentacion():
    print("8. Escribe documentación: Mantén tu código claro y documentado para ti y otros.")

def mostrar_menu():
    print("\nSelecciona un consejo para ser un buen programador:")
    print("1. Practicar regularmente")
    print("2. Aprender los fundamentos")
    print("3. Leer código de otros")
    print("4. Trabajar en proyectos")
    print("5. Mantenerse actualizado")
    print("6. Colaborar con otros")
    print("7. No temer a los errores")
    print("8. Escribir documentación")
    print("9. Salir")

def main():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"\nHola, {nombre}! Aquí tienes algunos consejos para ser un buen programador:\n")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-9): ")

        if opcion == '1':
            practicar_regularmente()
        elif opcion == '2':
            aprender_fundamentos()
        elif opcion == '3':
            leer_codigo()
        elif opcion == '4':
            trabajar_proyectos()
        elif opcion == '5':
            mantenerse_actualizado()
        elif opcion == '6':
            colaborar_otros()
        elif opcion == '7':
            no_temas_errores()
        elif opcion == '8':
            escribir_documentacion()
        elif opcion == '9':
            print("¡Gracias por usar el programa! ¡Buena suerte en tu camino como programador!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
