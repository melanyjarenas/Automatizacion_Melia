continuar = "si"

print("---SISTEMA DE PEDIDOS MELIA---")

while continuar == "si":
  nombre_cliente_Melia = input(" ¿Como te llamas?")
  fecha_de_entrega = input(" ¿ Para que día necesitas el pedido? ")
  cantidad_de_recordatorios = int(input(" ¿ Cuanta cantidad de recordatorios necesitas? "))
  if cantidad_de_recordatorios >= 70:
    print(f"""Señorita {nombre_cliente_Melia} su compra ha sido nivel oro! 
    tiene un descuento del 20% mas domicilio gratis, su pedido sera entregado el dia {fecha_de_entrega} 
    con una cantidad de {cantidad_de_recordatorios} recordatorios""")
  elif cantidad_de_recordatorios >= 40:
    print(f""" Señorita {nombre_cliente_Melia } su pedido ha sido agendado con exito para el dia {fecha_de_entrega}
    con una cantidad de {cantidad_de_recordatorios} recordatorios, y su compra se ha registrado 
    como nivel plata por lo tanto tiene un descuento del 10% mas domicilio gratis""")
  else:
    print(f"""Señorita {nombre_cliente_Melia} muchas gracias por su compra, esta ha sido efectuada con el precio regular, 
    se le estará haciendo la entrega el dia {fecha_de_entrega} con la cantidad de {cantidad_de_recordatorios} 
    recordatorios """)
  print("-" * 40) 

  continuar = input("Desea registar otro pedido? (Si/No): ").lower()
  
print("Gracias por usar el sistema de Melia! Que tengas un excelente dia")
