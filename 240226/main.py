from bd import productos

def regProductos():
	idP = 1
	for i in productos:
		if i['id']==0:
			idP = 1
		else:
			idP = i['id']+1
	nom = input("Ingresa el nombre del producto: ")
	pr = input("Precio del producto: ")
	return {'id': idP, 'nombre': nom, 'precio': pr}

def consProductos():
	for i in productos:
		print(f'{i['id']}, {i['nombre']}, {i['precio']}')

def deleatProd():
	consProductos()
	prod = int(input('Ingresa el id del producto a eliminar: '))
	for n in productos:
		if n == prod:
			print('Producto eliminado: ', n['id'])
			productos.remove(n)

def editProd():
	prodN = int(input('Ingresa el id a editar: '))
	for k in productos:
		if k['id'] == prodN:
			nom = input('Ingresa el nombre del producto: ')
			k['nombre']=nom
			prc = input('Ingresa el nuevo precio: ')
			k['precio']=prc

while True:
	print('1. Registrar producto')
	print('2. Consultar producto')
	print('3. Eliminar producto')
	print('4. Editar producto')
	print('0. Salir')
	r = int(input('Elige una opción: '))
	if r==1:
		productos.append(regProductos())
	if r==2:
		consProductos()
	if r==3:
		deleteProd()
	if r==4:
		editProd()
	if r==0:
		print('Saliendo...')
		break
