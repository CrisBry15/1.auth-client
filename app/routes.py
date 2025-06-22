from flask import Blueprint, request, jsonify
from .auth import login_user, create_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() # Obtener los datos del cuerpo de la solicitud
    username = data.get("username")
    password = data.get("password")
    return login_user(username, password)

# Ruta para registrar un nuevo usuario (opcional)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    return create_user(username, password)