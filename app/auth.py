from flask_jwt_extended import create_access_token
from flask_mysqldb import MySQL
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from . import mysql

def login_user(username, password):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    
    if user and check_password_hash(user[2], password):  # user[2] es el campo de la contraseña
        access_token = create_access_token(identity=user[1])  # user[1] es el nombre de usuario
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401
    
def create_user(username, password):
    cursor = mysql.connection.cursor()
    hashed_password = generate_password_hash(password)  # Hash de la contraseña
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
    mysql.connection.commit()
    return jsonify({"message": "Usuario creado exitosamente"}), 201
