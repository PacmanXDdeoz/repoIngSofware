alumnos=[]
def regAlumnos():
	a=input('Ingresa nombre: ')
	b=int(input('Ingresa tu numero de control: '))
	return {'nombre': a, 'control': b}

def consUsuario():
	for al in alumnos:
		print(al)
		print(al['nombre'], al['control'])

while True:
	print('1. Registrar')
	print('2. Consultar')
	print('0. Cerrar')
	a = int(input('Elige una opc: '))
	if a==1:
		alumno=regAlumnos()
		alumnos.append(alumno)
	elif a==2:
		consUsuario()
	elif a==0:
		print('Saliendo...')
		break
	else:
		print('Elige una opc valida')
