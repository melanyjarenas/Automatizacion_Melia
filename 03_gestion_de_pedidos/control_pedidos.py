saludo = "Buen día bienvenidos a control de pedidos Melia, para agendar tu pedido, necesito los siguientes datos"
print(saludo)

Nombre_del_cliente_2 = input("Cual es tu nombre?")
while Nombre_del_cliente_2 != "salir":
    print(f"pedido registrado exitosamente para {Nombre_del_cliente_2}")
    print("-" * 40)
    Nombre_del_cliente_2 = input("siguiente cliente (o 'salir' para terminar):")
print("¡Registro de pedidos finalizado por hoy!")
print("Gracias por usar el control de pedidos Melia")
