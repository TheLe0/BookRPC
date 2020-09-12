import psycopg2

from settings import HOST, DB_USER, PASSWORD, DBNAME, PORT, SERVER_PORT

conn = psycopg2.connect(
    user = DB_USER,
    password = PASSWORD,
    host = HOST,
    port = PORT,
    dbname = DBNAME)

cursor = conn.cursor()

query = "SELECT nome FROM autor LIMIT 10;"

cursor.execute(query);
records = cursor.fetchall()

for row in records:
    print(row[0])

if(conn):
    cursor.close()
    conn.close()
    print("PostgreSQL connection is closed")

