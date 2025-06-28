import bcrypt

def validate_password(plain_password, hashed_password):
    """
    Compara una contraseña en texto plano con una contraseña hasheada.
    """
    if not plain_password or not hashed_password:
        return False

    try:
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    except Exception as e:
        print(f"Error al validar contraseña: {e}")
        return False