import psycopg2

def getConnection():
	try:
		return psycopg2.connect(user='mvp_tienda', password='123456', host='localhost', port=5432, database='tienda')
	except Exception as e:
		print(e)
		return None
