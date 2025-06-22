from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Brytib+1906'
app.config['MYSQL_DB'] = 'auth_database'

mysql = MySQL(app)

@app.route('/')
def test_connection():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        return f"Conexión exitosa a la base de datos: {db_name[0]}"
    except Exception as e:
        return f"Error al conectar: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
