import psycopg2

try:
	conn = psycopg2.connect(host="localhost", port = 5433, database="base_original", user="mati", password="mati")
	connStaging = psycopg2.connect(host="localhost", port = 5433, database="base_destino", user="mati", password="mati")

	# create a psycopg2 cursor that can execute queries
	cursor = conn.cursor()
	cursorStaging = connStaging.cursor()

	sql = "SELECT * FROM personas;"
	cursor.execute(sql)
	conn.commit()
	rows = cursor.fetchall()

	for persona in rows:
		nombre = persona[1]

		sql = "INSERT INTO personas (nombre, apellido, mail, telefono) VALUES ('"+persona[1]+"', '"+persona[2]+"', '"+persona[3]+"', '"+persona[4]+"')"
		try:
			cursorStaging.execute(sql)
			connStaging.commit()
		except:
			print("error consulta insert")

	cursor.close()
	conn.close()
	cursorStaging.close()
	connStaging.close()

except:
	print("Error conectando a la base de datos")