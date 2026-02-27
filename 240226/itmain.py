from itdb  import alumnos
def registrarA():
	a=int(input("ingresa id: "))
	b=input("ingresar nombre del alumno: ")
	c=int(input("ingresar edad del alumnos: "))
	d=input("ingresa direccion: ")
	return{"id":a, "name":b, "age":c, "adress":d}

def consultarA():
	for i in alumnos:
		print(f"{i['id']}, {i['name']},{i['age']},{i['adress']}")
	
def eliminarA():
	a=int(input("eliminar el id: "))
	for e in alumnos:
		if e['id'] == a:
			print("eliminado:",e ['id'])
			producto.remove(e)

def editarA():
	b=int(input("ingresa id a editar: "))
	for u in alumnos:
		if u ['id'] ==b:
			p=input("nuevo alumno name:  ")
			u['alumnos']=p
def menu():
	r=int(input("ingresa una op: "))
	while True:
	print("1.registra\n 2.consultar\n3.eliminar\n4.editar")
		if r==1:
			alumnos.append(registarA())
		elif r==2:
			consultarA()
		elif r==3:
			eliminarA()
	elif r==4:
		editarA()
	elif r==0:
		print ("Saliendo...")
	break:
