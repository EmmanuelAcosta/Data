import psycopg2

try:
	conn = psycopg2.connect(host="localhost", port = 5433, database="base_original", user="mati", password="mati")

	# create a psycopg2 cursor that can execute queries
	cursor = conn.cursor()

	sql = "SELECT * FROM personas;"
	cursor.execute(sql)
	conn.commit()
	rows = cursor.fetchall()

	print(rows)

	cursor.close()
	conn.close()

except:
	print("Error conectando a la base de datos")