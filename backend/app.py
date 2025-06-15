
from flask import Flask, request, jsonify
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    telefono = request.form.get("telefono")
    mensaje = request.form.get("mensaje")
    archivo = request.files.get("archivo")

    archivo_nombre = None
    archivo_path = None

    if archivo:
        if archivo.filename.endswith(('.pdf', '.doc', '.docx', '.xls', '.xlsx')):
            archivo_nombre = archivo.filename
            archivo_path = os.path.join(UPLOAD_FOLDER, archivo_nombre)
            archivo.save(archivo_path)
        else:
            return jsonify({"error": "Extensión de archivo no permitida"}), 400

    conn = psycopg2.connect(
    host="localhost",
    database="optimec",
    user="postgres",
    password="postgres" 
    )
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO contactos (nombre, email, telefono, mensaje, archivo_nombre, archivo_path, fecha_envio)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nombre, email, telefono, mensaje, archivo_nombre, archivo_path, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
