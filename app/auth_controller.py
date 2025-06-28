from flask import request, jsonify
from config import Config
from app.utils import hash_password, validate_password
import mysql.connector
import jwt
import datetime

# Función para registrar un nuevo usuario
def register():
    data = request.get_json(silent=True)
    
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        cursor = conn.cursor()

        # Verificar si el email ya está registrado
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            return jsonify({"error": "Email already registered"}), 409

        # Hashear la contraseña antes de guardar
        hashed_pwd = hash_password(password)

        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_pwd))
        conn.commit()

        return jsonify({"message": "User registered successfully"}), 201

    except mysql.connector.Error as err:
        return jsonify({"error": f"MySQL Error: {err}"}), 500
    finally:
        if 'conn' in locals():
            try:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
            except:
                pass




# Función para login real desde base de datos
def login():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, email, password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if not user or not validate_password(password, user["password"]):
            return jsonify({"error": "Invalid email or password"}), 401

        token = jwt.encode({
            "user_id": user["id"],
            "email": user["email"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)

        return jsonify({"token": token})

    except mysql.connector.Error as err:
        return jsonify({"error": f"MySQL error: {err}"}), 500
    finally:
        if 'conn' in locals():
            try:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
            except:
                pass