import psycopg2
def getconnection():
	try: 
		return psycopg2.connect(user='admin',password = '123456',host='localhost',port = 5432, database = 'db0')
	except Expection as e:
		print(e)
		return None


