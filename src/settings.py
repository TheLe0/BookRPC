import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")
IP = os.getenv("IP")
SERVER_PORT = os.getenv("SERVER_PORT")