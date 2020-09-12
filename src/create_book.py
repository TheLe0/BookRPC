import psycopg2

from settings import HOST, DB_USER, PASSWORD, DBNAME, PORT, SERVER_PORT

conn = psycopg2.connect(
    user = DB_USER,
    password = PASSWORD,
    host = HOST,
    port = PORT,
    dbname = DBNAME)

cursor = conn.cursor()

query = """ INSERT INTO public.livros(codigo, titulo) VALUES (%s, %s);"""
record_to_insert = (10000, "Everything Is Eventual: 14 Dark Tales")

cursor.execute(query, record_to_insert)
	
cursor.execute(query);
records = cursor.fetchall()

connection.commit()
count = cursor.rowcount
print (count, "Record inserted successfully into mobile table")

if(conn):
    cursor.close()
    conn.close()
    print("PostgreSQL connection is closed")