import xmlrpclib
import sys

from settings import IP, SERVER_PORT

server = xmlrpclib.ServerProxy('http://' + IP + ':'+ SERVER_PORT)

## print str(server.validate_cpf("03661861085"))