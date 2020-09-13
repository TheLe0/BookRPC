import re
import SimpleXMLRPCServer
import sys

from lib import insert
from settings import HOST, SERVER_PORT

server = SimpleXMLRPCServer.SimpleXMLRPCServer((HOST, int(SERVER_PORT)))
server.register_function(insert, "insert")
server.serve_forever()

