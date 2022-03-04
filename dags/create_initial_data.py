import psycopg2

try:
	conn = psycopg2.connect(host="localhost", port = 5433, database="base_original", user="mati", password="mati")

	# create a psycopg2 cursor that can execute queries
	cursor = conn.cursor()


	sql = """DROP TABLE personas"""
	try:
		cursor.execute(sql)
		conn.commit()
	except:
		print("error consulta drop")


	sql = """CREATE TABLE personas (
		id serial PRIMARY KEY,
		nombre VARCHAR ( 100 ) NOT NULL,
		apellido VARCHAR ( 100 ) NOT NULL,
		mail VARCHAR ( 100 ) NOT NULL,
		telefono VARCHAR ( 30 ) NOT NULL,
	    last_login TIMESTAMP 
	);"""
	try:
		cursor.execute(sql)
		conn.commit()
	except:
		print("error consulta create")

	sql = """INSERT INTO personas (nombre, apellido, mail, telefono) VALUES
	('matias', 'rodriguez', 'matias@ucu', '123456'),
	('agustin', 'lorenzo', 'agustin@ucu', '24534'),
	('felipe', 'corderi', 'matias@ucu', '993483'),
	('dana', 'castroman', 'dana@ucu', '42342')
	"""
	try:
		cursor.execute(sql)
		conn.commit()
	except:
		print("error consulta insert")


	cursor.close()
	conn.close()

except:
	print("Error conectando a la base de datos")