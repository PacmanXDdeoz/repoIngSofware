from base import getConnection

if getConnection:
	con=getConnection()
	cursor = con.cursor()
	while True:
		try:
			print('2. Insertar')
			print('3. Actualizar')
			print('4. Eliminar')
			print('0. Cerrar')
			op = int(input('Elige una opcion: '))
			match op:
				case 1:
					cursor.execute('select * from users')
					cursor.execute('select * from users')
					consulta = cursor.fetchall()
					for us in consulta:
						print(us)
				case 2:
					nombre = input('Ingresa el nombre: ')
					apellido = input('Ingresa el apellido: ')
					edad = int(input('Ingresa la edad: '))
					print('1. true')
					print('2. false')
					st = int(input('Elige una opc: '))
					if st == 1:
						status = True
					if st == 2:
						status = False
					cursor.execute('insert into users (nombre, apellido, edad, status) values (%s, %s, %s, %s)', (nombre, apellido, edad, status))
					con.commit()
				case 3:
					id = int(input('Ingresa el id a actualizar: '))
					nom = input('nombre nuevo: ')
					apll = input('Apellido nuevo: ')
					ad = int(input('Edad nueva: '))
					cursor.execute('update users set nombre=%s, apellido=%s, edad=%s where id=%s', (nom, apll, ad, id))
					con.commit()
					print('Usuario actualizado con éxito')
				case 4:
					idD = int(input('Ingresa el id a dar de baja: '))
					cursor.execute('update users set status=false where id=%s', (idD,))
					con.commit()
					print('Usuario dado de baja')
				case 0:
					print('saliendo...')
					break
				case _:
					print('Ingresa un dato correcto')
		except Exception as e:
			print(e)
