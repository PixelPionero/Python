usuario_correcto = "admin"
clave_correcta = "12345"
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")
if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
