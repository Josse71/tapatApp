from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

def __str__(self):
    return "Usuario:" + self.username + " contra:" + self.password + " correo:" + self.email

listUsers= [
    User(id=1, username="usuari1", password="12345", email="usuari1@gmail.com"),
    User(id=2, username="usuari2", password="123", email="usuari2@gmail.com"),
    User(3,"usuari3","00","Miscos@gmail.com")
]

for u in listUsers:
    print(u)


class DAOUsers:
    def __init__(self):
        self.users=listUsers

def getUserByUsername(self,username):

#encontrar usuario
    for u in self.users:
        if u.username == username:
            return u
        return None

daousers = DAOUsers()

'''print(daousers.getUserbyUsername("usuario1"))
u=daousers.getUserByUsername("noencontrao")
if (u):
print(u)
else:
print("No encontrao")"'''

app = Flask(__name__)

@app.route('/tapatapp/getUser',methods=['GET'])
def getUser():
    n = str(request.args.get('name'))
    email = str(request.args.get('email'))
    return "Hello World Nombre: " + n + " Email: " + email

@app.route('/prototip/getuser/<string:username>',methods=['GET'])
def prototipGetUser(username):
    return "Prototip 1, user: " + username

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="10050")