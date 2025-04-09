import mysql.connector

# Clase DAO para gestionar las operaciones con la tabla User
class UserDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    # Conectar a la base de datos
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error al conectar: {err}")

    # Desconectar de la base de datos
    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Conexión cerrada.")

    # Obtener todos los usuarios
    def get_all_users(self):
        try:
            self.cursor.execute("SELECT * FROM User")
            users = self.cursor.fetchall()
            return users
        except mysql.connector.Error as err:
            print(f"Error al obtener usuarios: {err}")
            return []

# Uso de la clase UserDAO
if __name__ == "__main__":
    # Parámetros de conexión con los detalles proporcionados
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'tapatapp'

    # Crear instancia del DAO
    user_dao = UserDAO(host, user, password, database)

    # Conectar a la base de datos
    user_dao.connect()

    # Obtener y mostrar todos los usuarios
    users = user_dao.get_all_users()
    if users:
        for user in users:
            print(f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")

    # Desconectar de la base de datos
    user_dao.disconnect()
