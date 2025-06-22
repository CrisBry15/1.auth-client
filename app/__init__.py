from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from .config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)
    CORS(app)  # Permitir peticiones CORS

    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
