# app/utils.py

import bcrypt

def hash_password(password):
    """Hashea una contraseña utilizando bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def validate_password(password, hashed_password):
    """Verifica si la contraseña proporcionada coincide con el hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

