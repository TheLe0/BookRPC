import sys
import xmlrpc.client

from settings import IP, SERVER_PORT

with xmlrpc.client.ServerProxy(('http://' + IP + ':'+ SERVER_PORT), allow_none=True) as proxy:

    try:
        ## print(proxy.insert_book(10006, 'The Stand'))
        ## print(proxy.delete_book('The Outsider'))
        ## print(proxy.find_book('%Dark Tales'))
        ## print(proxy.list_books_by_author('Roberto Nogueira%'))
        ## print(proxy.list_books_per_year_edition(2013, '1'))
        print(proxy.update_book('Solvansku%', 'Slovansky Dekline', 2013, '2'))
    except:
        print("Error while calling the server!")