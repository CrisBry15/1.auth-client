from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from .config import Config
from flask_jwt_extended import JWTManager

jwt = JWTManager()

mysql = MySQL() #se crea la conexion a la base de datos.

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Cargar la configuración desde el archivo Config

    mysql.init_app(app) # Inicializar MySQL con la aplicación Flask
    jwt.init_app(app)
    
    CORS(app)  # Permitir peticiones CORS

    # Registrar las rutas
    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
