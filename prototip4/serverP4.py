import newDades as server
from newDades import User, Child, Tap, Role, Status, Treatment
from flask import Flask, request, jsonify

app = Flask(__name__)

#Classes DAO
class DAO_User:
    def __init__(self):
        self.listUsers = server.users

    def getUserByCredentials(self, username, password):
        for user in self.listUsers:
            if (username == user.username and password == user.password): 
                return user
            
        return None

class DAO_Child:
    def __init__(self):
        self.listChildren = server.children
        self.listTaps = server.taps
    
    def getChildByUser(self, user_id):
        # print(type(server.relation_user_child[0])) -> comprovar si els continguts de la llista són diccionaris per saber cridar els atributs
        users_children = [relation["child_id"]for relation in server.relation_user_child if user_id == relation["user_id"]]

        if users_children:
            children_data = [child for child in self.listChildren if child.id in users_children]
            return children_data
        else:
            return None
                         

    def getAllTaps(self, child_id):
        taps_data = [tap for tap in self.listTaps if child_id == tap.child_id]        
        
        if taps_data: 
            return taps_data
        else: 
            return None

    def getTapById(self, tap_id):
        for tap in self.listTaps:
            if tap_id == tap.id:
                return tap
        return tap

DAOUser = DAO_User()
DAOChild = DAO_Child()

@app.route("/prototip2/login/<string:username>/<string:password>", methods=["GET"])
def login(username, password):
    try: 
        """data = request.json  # Recibe un JSON con username y password
        username = data.get("username")
        password = data.get("password")""" #POST?

        user = DAOUser.getUserByCredentials(username, password)

        if user:
            return jsonify(user.__dict__), 200
        else:
            return jsonify({"error":"Credencials incorrectes."}), 404
    except Exception as e:
        return jsonify({"error":"Error inesperat del sistema", "detalls:":str(e)})

@app.route('/prototip2/children/', defaults={'user_id': None}, methods=['GET'])
@app.route("/prototip2/children/<int:user_id>", methods=["GET"])
def getChildByUser(user_id): 
    if user_id is None:
        return jsonify({"error":"No s'ha introduit cap parametre"}), 400
    
    children = DAOChild.getChildByUser(user_id)

    if children:
        return jsonify([child.__dict__ for child in children]), 200
    else:
        return jsonify({"error":"Aquest usuari no té cap nen al seu càrrec"}), 404

@app.route('/prototip2/taps/', defaults={'child_id': None}, methods=['GET'])
@app.route("/prototip2/taps/<int:child_id>", methods=['GET'])
def getAllTaps(child_id): 
    if child_id is None:
        return jsonify({"error":"No s'ha introduit cap parametre"}), 400
    
    taps = DAOChild.getAllTaps(child_id)

    if taps:
        return jsonify([tap.__dict__ for tap in taps]), 200
    else:
        return jsonify({"error":"Aquest nen no té cap tap enregistrat"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")