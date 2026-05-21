import psycopg2

def getConnection():
	try:
		return psycopg2.connect(user='admin', password='123456', host='localhost', port=5432, database='multiapp')
	except Exception as e:
		print(e)
		return None
