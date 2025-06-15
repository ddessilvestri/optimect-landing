
CREATE TABLE IF NOT EXISTS contactos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    email TEXT,
    telefono TEXT,
    mensaje TEXT,
    archivo_nombre TEXT,
    archivo_path TEXT,
    fecha_envio TIMESTAMP
);
