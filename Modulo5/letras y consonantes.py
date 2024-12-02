palabra = input("Ingrese una palabra: ")
cantidad_letras = len(palabra)
cantidad_consonantes = sum(1 for letra in palabra if letra.isalpha() and letra not in 'aeiouAEIOU')
print(f"La palabra '{palabra}' tiene {cantidad_letras} letras y {cantidad_consonantes} consonantes.")
