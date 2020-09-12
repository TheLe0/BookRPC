import datetime
import psycopg2
import re
import SimpleXMLRPCServer
import sys

from lib import validate_cpf
from settings import HOST, DB_USER, PASSWORD, DBNAME, PORT, SERVER_PORT

try:
    conn = psycopg2.connect(
        user = DB_USER,
        password = PASSWORD,
        host = HOST,
        port = PORT,
        dbname = DBNAME)

    cursor = connection.cursor()

    query = "SELECT nome FROM autor LIMIT 10;"

    records = cursor.fetchall()

    for row in records:
        print(row[0])
    
    print "The Server was Started"

    server = SimpleXMLRPCServer.SimpleXMLRPCServer((HOST, int(SERVER_PORT)))
    server.register_function(validate_cpf, "validate_cpf")
    server.serve_forever()
except:
    print("Failed to connect to the database")
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
