def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicitar un número al usuario
numero = int(input("Introduce un número para verificar si es primo: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
