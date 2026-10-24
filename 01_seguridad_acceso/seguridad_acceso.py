clave_correcta = "melia2026"
clave_ingresada = input("¿ Cual es la contraseña?")
while clave_correcta != clave_ingresada:
    print("clave incorrecta, intenta de nuevo")
    clave_ingresada = input("intenta nuevamente, cual es la contraseña?")
    print("-" * 40)
print("Acceso concedido al sistema Melia!")
