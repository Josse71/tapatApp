from flask import Flask, jsonify, request

app = Flask(__name__)

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        print(self.username+":"+self.password+":"+self.email)

# Dades d'exemple
users = [
    User(id=1, username="mare", password="mare", email="prova@gmail.com"),
    User(id=2, username="pare", password="pare", email="prova2@gmail.com")
]

# Classes DAO
class UserDAO:
    def __init__(self):
        self.users = users

    def get_all_users(self):
        result = []
        for user in self.users:
            result.append(user.__dict__)
        return result

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

# Inicialitzar DAOs
user_dao = UserDAO()

# Rutes del Servei Web
# --------------------
# Mètodes GET
# /users: retorna tots els usuaris.
# /users/username/<string:username>: retorna la informació d'un usuari específic pel seu username.

@app.route('/prototip1/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.get_all_users())

@app.route('/prototip1/getuser', methods=['GET'])
def get_user_by_username():
    username=request.args.get('username', default="", type=str)
    print("+"+username+"+")
    user = user_dao.get_user_by_username(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": f"User with username {username} not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)