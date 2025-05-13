# 📸 Gestor de Imágenes con Login de Usuarios
Este proyecto es una aplicación desarrollada en Python que permite la gestión dinámica de imágenes a través de una interfaz sencilla y personalizada según el usuario que inicia sesión.

## 🛠️ Características principales
- 🔐 Autenticación de usuarios con nombre de usuario y contraseña encriptada usando MD5.

- 👥 Soporte para múltiples roles de usuario (por ejemplo, user1, admin), con acceso diferenciado a contenidos.

- 🖼️ Visualización de imágenes según el usuario autenticado.

- 📂 Navegación intuitiva mediante una barra de navegación integrada.

- 🗄️ Base de datos MySQL para almacenar la información de usuarios y rutas de imágenes.

## 💡 Objetivo
Ofrecer una solución simple pero eficaz para mostrar imágenes personalizadas según el perfil del usuario, ideal como base para sistemas de gestión de contenido, portafolios privados o dashboards con contenido multimedia restringido.

# ⚙️ Requisitos Técnicos
- Lenguaje: Python 3.x

- Base de datos: MySQL

- Backend: Flask (ideal peara aplicaciones web y gestión de sesiones)

- Frontend: Wireframes básicos

- Entorno de desarrollo: Visual Studio Code

- Control de versiones: Git + GitHub

- Tests: unittest (validar la funcionalidad del codigo)

## Modelo E/R

![image](https://github.com/user-attachments/assets/08b09712-ac63-47d3-8a7c-5863d0c34d0d)

## Diagrama de arquitectura

![image](https://github.com/user-attachments/assets/5fbce81d-b65b-4aa4-a21b-0b4a8b30139d)

# 🔌 End-points WebService

| **Método** | **Endpoint**       | **Función**                                                   |
|------------|--------------------|----------------------------------------------------------------|
| `POST`     | `/login`           | Inicia sesión de usuario con nombre de usuario y contraseña (MD5). |
| `POST`     | `/register`        | Registra un nuevo usuario en la base de datos.                |
| `GET`      | `/imagenes`        | Lista imágenes visibles según el usuario autenticado.         |
| `POST`     | `/imagenes`        | Sube una nueva imagen (requiere permisos especiales, ej. admin). |
| `GET`      | `/perfil`          | Devuelve la información del perfil del usuario actual.        |
| `PUT`      | `/perfil`          | Permite modificar los datos del perfil del usuario.           |
| `POST`     | `/logout`          | Cierra la sesión del usuario actual.                          |

## Diagrama de clases BackEnd

![image](https://github.com/user-attachments/assets/0414979f-b52f-47a8-bf16-11d8c52ce316)


### Creado por Daniel Montes y Jose Gomez - 2025
