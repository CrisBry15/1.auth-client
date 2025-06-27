import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql-container')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3307'))  # Convierte el puerto a entero
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Brytib+1906')
    MYSQL_DB = os.getenv('MYSQL_DB', 'auth_database')
