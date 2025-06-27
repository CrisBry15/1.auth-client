import re
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import current_app

# Función para validar un correo electrónico
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

# Función para encriptar una contraseña
def encrypt_password(password):
    return generate_password_hash(password)

# Función para verificar la contraseña (al comparar con la base de datos)
def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

# Función para generar un token JWT
def generate_token(user_id):
    expiration = timedelta(hours=1)  # El token expirará en 1 hora
    payload = {
        'sub': user_id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + expiration
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Función para verificar la validez del token
def verify_token(token):
    try:
        decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # El token es inválido
