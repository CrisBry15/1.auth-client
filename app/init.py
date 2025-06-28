from flask import Flask
from config import Config
from app.routes import auth_bp

from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)  # Corrección aquí

    # Carga de configuración desde config.py
    app.config.from_object(Config)

    # Inicializar JWTManager
    jwt = JWTManager(app)

    # Registro del blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app