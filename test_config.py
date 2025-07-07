# test_config.py
from config import Config

print("Host:", Config.MYSQL_HOST)
print("Base de datos:", Config.MYSQL_DB)
print("Clave secreta:", Config.SECRET_KEY)
print("Algoritmo JWT:", Config.JWT_ALGORITHM)
