from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulación de usuarios en memoria
users = [
    {"id": 1, "username": "mare", "password": "12345", "email": "prova@gmail.com", "role_id": 2},
    {"id": 2, "username": "pare", "password": "123", "email": "prova2@gmail.com", "role_id": 1}
]

# Endpoint /login (POST)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Buscar al usuario
    user = next((u for u in users if (u["username"] == username or u["email"] == username) and u["password"] == password), None)

    if user:
        token = str(uuid.uuid4())  # Generamos un token aleatorio
        return jsonify({
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "token": token,
            "idrole": user["role_id"],
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400


# Endpoint Login por Token (POST)
@app.route('/login', methods=['POST'])
def login_by_token():
    token = request.headers.get('Authorization')

    if token == "token12345":  # Validamos si el token es válido
        user = {"id": 1, "username": "mare", "email": "prova@gmail.com", "role_id": 2}
        return jsonify({
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "token": token,
            "idrole": user["role_id"],
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400


# Simulación de datos de children
children = [
    {"id": 1, "child_name": "Carol Child", "sleep_average": 8, "treatment_id": 1, "time": 6},
    {"id": 2, "child_name": "Jaco Child", "sleep_average": 10, "treatment_id": 2, "time": 6}
]

# Endpoint /child (POST)
@app.route('/child', methods=['POST'])
def get_children():
    user_id = request.get_json().get("iduser")
    # Simulamos que siempre hay dos hijos para el usuario
    if user_id:
        return jsonify({
            "msg": "2",
            "coderesponse": "1",
            "children": children
        }), 200
    else:
        return jsonify({
            "msg": "1",
            "coderesponse": "1",
            "children": []
        }), 200


# Simulación de datos de taps
taps = [
    {"id": 1, "child_id": 1, "status_id": 1, "user_id": 1, "init": "2024-12-18T19:42:43", "end": "2024-12-18T20:42:43"},
    {"id": 2, "child_id": 1, "status_id": 2, "user_id": 1, "init": "2024-12-18T20:42:43", "end": "2024-12-18T22:42:43"}
]

# Endpoint /taps (POST)
@app.route('/taps', methods=['POST'])
def get_taps():
    child_id = request.get_json().get("idchild")
    
    if child_id == 1:  # Simulamos que el niño con id 1 tiene taps
        return jsonify({
            "msg": "2",
            "coderesponse": "1",
            "taps": taps
        }), 200
    else:
        return jsonify({
            "msg": "0",
            "coderesponse": "1",
            "taps": []
        }), 200


# Inicia la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
