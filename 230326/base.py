import psycopg2

def getConnection():
	try:
		return psycopg2.connect(user='admin_zara', password='123456', host='localhost', port='5432', database='zara_db')
	except Exception as e:
		print(e)
		return None
