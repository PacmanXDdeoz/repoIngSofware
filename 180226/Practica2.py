lista=[]
for i in range(5):
	lista.append(input("Ingresa una fruta: "))

for u in lista:
	print(u)

lista.remove(lista[0])
lista.remove(lista[3])

for x in lista:
	print(x)
