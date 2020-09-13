import sys
import xmlrpc.client

from settings import IP, SERVER_PORT

with xmlrpc.client.ServerProxy(('http://' + IP + ':'+ SERVER_PORT), allow_none=True) as proxy:

    ## proxy.insert_book(10006, 'The Stand') 
    proxy.delete_book('The Stand')