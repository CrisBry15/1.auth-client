# este archivo se configuro para que este disponible en todo el microservicio.
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret_default")  
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")


    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"

    # Configuración de la aplicación
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    PORT = int(os.getenv("PORT", 5000))
    
    # Configuración de rate limiting
    RATELIMIT_DEFAULT = os.getenv("RATELIMIT_DEFAULT", "100 per minute")
    RATELIMIT_STORAGE_URL = os.getenv("RATELIMIT_STORAGE_URL", "memory://")
    
    # Configuración de logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    # Configuración de CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
    
    # Validación de configuración crítica
    @classmethod
    def validate_config(cls):
        """Valida que las variables críticas estén configuradas"""
        required_vars = [
            "MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", 
            "MYSQL_DB", "JWT_SECRET_KEY"
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Variables de entorno requeridas faltantes: {', '.join(missing_vars)}")
        
        return True