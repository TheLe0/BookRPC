import re
import sys

from lib import insert_book, delete_book, find_book, list_books_by_author, list_books_per_year_edition, update_book
from settings import HOST, SERVER_PORT
from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer((HOST, int(SERVER_PORT))) as server:

    server.register_function(insert_book, "insert_book")
    server.register_function(delete_book, "delete_book")
    server.register_function(find_book, "find_book")
    server.register_function(list_books_by_author, "list_books_by_author")
    server.register_function(list_books_per_year_edition, "list_books_per_year_edition")
    server.register_function(update_book, "update_book")

    try:
        print("The server was started!")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutdown by keyboard exit!")
        sys.exit(0)

