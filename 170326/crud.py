from base import getConnection

if getConnection:
	conn=getConnection()
	cursor = conn.cursor()
	while True:
		try:
			print('1. Agregar usuario')
			print('2. Agregar producto')
			print('3. Consultar usuarios')
			print('4. Consultar productos')
			print('5. Salir')
			op = int(input('Elige una opción: '))
			match op:
				case 1:
					usuario = input('Ingresa el nombre del usuario: ')
					cursor.execute('insert into usuarios (nombre) values (%s)',(usuario,))
					conn.commit()
					print('Registrado con éxito')
				case 2:
					producto = input('Ingresa el nombre del producto: ')
					cursor.execute('insert into productos (nombre) values (%s)',(producto,))
					conn.commit()
					print('Registrado con éxito')
				case 3:
					cursor.execute('select * from usuarios')
					resultado = cursor.fetchall()
					for us in resultado:
						print(us)
				case 4:
					cursor.execute('select * from productos')
					resultado = cursor.fetchall()
					for prd in resultado:
						print(prd)
				case 5:
					print('Saliendo...')
					break
				case _:
					print('')
					print('Elige una opc correcta')
		except Exception as e:
			print(e)
	conn.close()
else:
	print('No hubo conexión a la base de datos')
	print('No hay datos que mostrar')
