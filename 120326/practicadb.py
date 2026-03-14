import psycopg2
try:
	con = psycopg2.connect(user='admin', password='123456', host='localhost', database='db0', port='5432')
	print('conexión exitosa')
	cursor = con.cursor()
	cursor.execute("select * from colores")
	registros = cursor.fetchall()
	for color  in registros:
		print(color)
	con.close()
except Exception as e:
	print(e)
