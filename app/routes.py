from flask import Blueprint, jsonify, request
from app.auth_controller import login, register
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

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

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    claims = get_jwt()
    return jsonify({
        "message": "Token válido",
        "user_id": get_jwt_identity(),  # solo el ID
        "email": claims.get("email")    # extraído del token
    }), 200


