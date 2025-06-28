from app.init import create_app
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Usar la app definida en app/__init__.py
app = create_app()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


