a = 1
while a!=0:
	print("1. Lista de Frutas")
	print("0. Cerrar")
	a=int(input("Selecciona una opción: "))
	if a==1:
		frutas=["Sandia", "Fresa", "Uva", "Pera", "Manzana", "Maracuya"]

		for fr in frutas:
			print(fr)
	else:
		print("Saliendo...")
