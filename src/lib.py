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

def insert(code, name):

    conn = connect_db()

    cursor = conn.cursor()

    query = "INSERT INTO livros (codigo, titulo) VALUES ("+str(code)+",'"+name+"');" 

    cursor.execute(query)
	
    conn.commit()
    count = cursor.rowcount
    
    if(conn):
        cursor.close()
        conn.close()
    
    return True if count > 0 else False
