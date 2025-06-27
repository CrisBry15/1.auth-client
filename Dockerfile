# Usa una imagen de Python 3.9
FROM python:3.9-slim

# Instala las dependencias necesarias para compilar mysqlclient
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código al contenedor
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "run.py"]
