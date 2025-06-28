import bcrypt

# Función para hashear contraseñas
def hash_password(password: str) -> str:
    # bcrypt genera una sal aleatoria internamente
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # Almacenamos como string

# Función para validar contraseñas
def validate_password(input_password: str, stored_hashed_password: str) -> bool:
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
