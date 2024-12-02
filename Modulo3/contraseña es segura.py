contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and any(char.isdigit() for char in contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")
