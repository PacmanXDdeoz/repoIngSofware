import psycopg2
def getConnection():
	try:
		return psycopg2.connect(user='admin', password='123456', host='localhost', database='c2db', port='5432')
	except Exception as e:
		print(e)
		return None
