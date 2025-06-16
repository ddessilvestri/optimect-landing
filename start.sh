#!/bin/bash

# Navegar al directorio del backend (opcional si ya estás ahí)
cd "$(dirname "$0")"

# Activar el entorno virtual
source venv/bin/activate

# Ejecutar la app en el puerto 5050
python3 app.py

# How to execute
# chmod +x start.sh 
# ./start.sh


