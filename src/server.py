import datetime
import psycopg2
import re
import SimpleXMLRPCServer
import sys

from lib import validate_cpf
from settings import HOST, USER, PASSWORD, DBNAME, PORT, SERVER_PORT

try:
    conn = psycopg2.connect(
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT,
        dbname = DBNAME)
    
    print "The Server was Started"

    server = SimpleXMLRPCServer.SimpleXMLRPCServer((HOST, int(SERVER_PORT)))
    server.register_function(validate_cpf, "validate_cpf")
    server.serve_forever()
except:
    print("Failed to connect to the database")
