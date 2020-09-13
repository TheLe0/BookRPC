import psycopg2

from settings import HOST, DB_USER, PASSWORD, DBNAME, PORT, SERVER_PORT

def connect_db():

    try:
        conn = psycopg2.connect(
            user = DB_USER,
            password = PASSWORD,
            host = HOST,
            port = PORT,
            dbname = DBNAME)
    except:
        print("Failed to connect to the database")
    
    return conn

def insert_book(code, name):

    conn = connect_db()

    cursor = conn.cursor()

    query = "INSERT INTO livros (codigo, titulo) VALUES ("+str(code)+",'"+name+"');" 

    cursor.execute(query)
	
    conn.commit()
    count = cursor.rowcount
    
    if(conn):
        cursor.close()
        conn.close()
    
    if (count > 0):
        print(str(count)+" registro adicionado com sucesso")
    else:
        print("Erro ao adicionar o registro")

def delete_book(name):

    conn = connect_db()

    cursor = conn.cursor() 

    query = "DELETE FROM livros WHERE TITULO = '"+name+"';"

    cursor.execute(query)

    conn.commit()
    count = cursor.rowcount 

    if(conn):
        cursor.close()
        conn.close()

    if (count > 0):
        print(str(count)+" registro removido com sucesso")
    else:
        print("Erro ao remover o registro")  
