asesor_tienda_melia = "Buenas tarde señorita, bienvenida a Melia, Veleas con Memoria, en que la puedo asesorar el dia de hoy"
print(asesor_tienda_melia)

cliente = "Muchas gracias, tengo un evento y estoy buscando un recordatorio que llene a cada persona y que para mi sea inolvidable"
print(cliente)

asesor_tienda_Melia = "haz llegado al lugar indicado, los momentos mas bellos de la vida se pasan volando, pero el sentido del olfato tiene el poder magico de traernos de vuelta. en Melia no solo elaboramos velas; creamos detalles de memoria olfativa para que viajesa tu dia mas feliz, permiteme te muestro el catalogo"
print(asesor_tienda_Melia)

cliente = "wow me has dejado sin palabras, es justo lo que estoy buscando, haz tocado mi corazon"
print(cliente)

asesor_tienda_Melia = "nos alegra mucho que haya tomado una decision, necesito los siguientes datos"
print(asesor_tienda_Melia)

nombre_cliente_melia = input("nos regalas tu nombre por favor")
fecha_tentativa_para_entrega = input("para que dia necesita el pedido")
cantidad_de_recordatorios = int(input("¿cuanta cantidad necesita?"))
print(f"Señorita {nombre_cliente_melia} su pedido ha sido agendado con exito para el dia {fecha_tentativa_para_entrega} con una cantidad de {cantidad_de_recordatorios} recordatorios")

if cantidad_de_recordatorios >= 70:
    print("Oh! su compra ha sido nivel oro! tienes un descuento del 20% y envio gratis")

elif cantidad_de_recordatorios >=40:
    print(" Su compra ha sido nivel plata! tiene usted un descuento del 10% y envio gratis ")

else:
    print("Muchas gracias por su compra! su pedido se procesara al precio regular")

