from base import getConnection

def talla():
	while True:
		try:
			print('Que talla es la que tiene esta prenda?')
			print('1. S')
			print('2. M')
			print('3. L')
			print('4. XL')
			pr = int(input('Elige una opc: '))
			match pr:
				case 1:
					return 'S'
				case 2:
					return 'M'
				case 3:
					return 'L'
				case 4:
					return 'XL'
				case _:
					print('Elige una opc correcta')
		except Exception as e:
			print(e)

if getConnection:
	con = getConnection()
	cursor = con.cursor()

	while True:
		try:
			print('1. Consultar')
			print('2. Registrar')
			print('3. Actualizar')
			print('4. Eliminar')
			print('0. Salir')
			op = int(input('Elige una opc: '))
			match op:
				case 1:
					cursor.execute('select * from dama.catalogo where status = true')
					cons = cursor.fetchall()
					for us in cons:
						print(us)
				case 2:
					prenda = input('Que prenda vas a registrar?: ')
					talla = talla()
					cursor.execute('insert into dama.catalogo (nombre, talla, status) values (%s, %s, true)', (prenda, talla,))
					con.commit()
					print('Registrado con éxito')
				case 3:
					upd = int(input('Ingresa el id a actualizar: '))
					prenda = input('Cual es la nueva prenda?: ')
					tallaupd = talla()
					cursor.execute('update dama.catalogo set nombre = %s, talla=%s where id=%s', (prenda, tallaupd, upd,))
					con.commit()
					print('Registrado con éxito')
				case 4:
					delid = int(input('Ingresa el id a eliminar: '))
					cursor.execute('update dama.catalogo set status = false where id=%s', (delid,))
					con.commit()
					print('Eliminado con éxito')
				case 0:
					print('Saliendo...')
					break
				case _:
					print('Elige una opción correcta')
		except Exception as e:
			print(e)
