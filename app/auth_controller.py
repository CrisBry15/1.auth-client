from flask import request, jsonify
from app.models import User
from app.utils import validate_password
from config import Config
import jwt
import datetime

# Controlador de autenticación
def login():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email y contraseña son requeridos"}), 400

    email = data.get('email')
    password = data.get('password')

    # Simulación de búsqueda de usuario en la base de datos
    # Aquí en producción deberías hacer una consulta real
    dummy_user = User(email="admin@example.com", password="$2b$12$YwO87s7tT5dNkJJXStwCMevaFw4gUx1/h5kUmFYvwuxn4Zugprb6a")  # hash para "admin123"

    if dummy_user.email != email:
        return jsonify({"error": "Usuario no encontrado"}), 404

    if not validate_password(password, dummy_user.password):
        return jsonify({"error": "Contraseña incorrecta"}), 401

    try:
        payload = {
            'email': dummy_user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
        return jsonify({"token": token}), 200

    except Exception as e:
        return jsonify({"error": "Error al generar el token"}), 500