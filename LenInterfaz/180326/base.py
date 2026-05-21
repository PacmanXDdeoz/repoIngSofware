import psycopg2

def getConnection():
	try:
		return psycopg2.connect(user='admin_db0', password='123456', host='localhost', port='5434', database='mindbx')
	except Exception as e:
		print(e)
		return None
