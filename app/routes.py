from flask import Blueprint, jsonify
from app.auth_controller import login, register

# Definir blueprint para el microservicio auth-client
auth_bp = Blueprint('auth', __name__)

# Ruta de prueba (GET)
@auth_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Auth Client Microservice funcionando correctamente"})

# Ruta de login (POST)
@auth_bp.route('/login', methods=['POST'])
def login_route():
    return login()

# Ruta de registro (POST)
@auth_bp.route('/register', methods=['POST'])
def register_route():
    return register()
