from ExamenL import personas

def regPersonas():
	while True:
		try:
			id = len(personas)+1
			name = input('Ingresa el nombre: ')
			age = int(input('Ingresa tu edad: '))
			break

		except ValueError:
			print('')
			print('Error al ingresar la edad!')
			print('')
	return {'id':id, 'name':name, 'age':age}

def consPersonas():
	for cons in personas:
		print('')
		print(f'{cons['id']}, {cons['name']}, {cons['age']}')

def updPersonas():
	while True:
		try:
			idUp = int(input('Ingresa el id a actualizar: '))
			for upd in personas:
				if idUp == upd['id']:
					upd['name'] = input('Ingresa el nombre: ')
					upd['age'] = int(input('Ingresa la edad: '))
					return
				else:
					print('La persona que buscas no existe!')
					while True:
						try:
							print('1. Volver a intentar')
							print('0. Menu principal')
							opcUp = int(input('Elige una opc: '))
							match opcUp:
								case 1:
									break
								case 0:
									return
								case _:
									print('Elige una opción valida')
						except ValueError:
							print('Dato no admitido!')
		except ValueError:
			print('Dato no admitido!')

def delPersonas():
	while True:
		try:
			idDel = int(input('Ingresa el id que quieres eliminar: '))
			for dp in personas:
				if idDel == dp['id']:
					personas.remove(dp)
					return
				else:
					print('La personas que buscas no existe!')
					while True:
						print('')
						print('1. Volver a intentar')
						print('0. Menu principal')
						try:
							opcDel = int(input('Elige una opc: '))
							match opcDel:
								case 1:
									break
								case 0:
									return
								case _:
									print('Selecciona una opción valida')
						except ValueError:
							print('')
							print('Dato no admitido!')
							print('')
		except ValueError:
			print('Dato no admitido!')

while True:
	print('1. Registrar')
	print('2. Consultar')
	print('3. Actualizar')
	print('4. Eliminar')
	print('0. Salir')

	try:
		op = int(input("Elige una opc: "))
		match op:
			case 1:
				personas.append(regPersonas())
				print("Registro exitoso!")
				print('')
			case 2:
				consPersonas()
				print('')
			case 3:
				updPersonas()
				print('')
			case 4:
				delPersonas()
				print('')
			case 0:
				print('Saliendo...')
				break
			case _:
				print('Selecciona una opc valida')

	except ValueError:
		print('')
		print('Dato no admitido!')
		print('')
