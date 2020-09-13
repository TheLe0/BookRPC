import re
import sys

from lib import insert_book, delete_book, find_book
from settings import HOST, SERVER_PORT
from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer((HOST, int(SERVER_PORT))) as server:

    server.register_function(insert_book, "insert_book")
    server.register_function(delete_book, "delete_book")
    server.register_function(find_book, "find_book")

    try:
        print("The server was started!")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutdown by keyboard exit!")
        sys.exit(0)

