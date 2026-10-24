Planta_de_produccion = "Control de Calidad de Fragancias en Melia"
print(Planta_de_produccion)
revisar = "si"
while revisar == "si":
    auxiliar_de_produccion = input("Nombre del aroma en la vela? ")
    print(f"Aprobado el control de calidad para la vela de {auxiliar_de_produccion}")
    print("-" * 40)
    revisar = input("Desea revisar otra Vela? (Si/No)").lower()
print("control de calidad finalizado por hoy!")
