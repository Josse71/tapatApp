CREATE DATABASE IF NOT EXISTS gestor_imagenes;
USE gestor_imagenes;

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasena_md5 VARCHAR(32) NOT NULL,
    email VARCHAR(100),
    rol VARCHAR(10)
);

-- Puedes añadir más tablas luego, como `imagenes`
