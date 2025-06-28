# app/routes.py

from flask import Blueprint, jsonify
from app.auth_controller import login

auth_bp = Blueprint('auth', __name__)  # Blueprint con prefijo /auth

@auth_bp.route('/', methods=['GET'])   # La ruta raíz del blueprint
def home():
    return jsonify({"message": "Auth Client Microservice funcionando correctamente"})

# Ruta de login (POST)
@auth_bp.route('/login', methods=['POST'])
def login_route():
    return login()