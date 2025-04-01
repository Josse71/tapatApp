import requests
import tkinter as tk
from tkinter import messagebox

class DAOUser:
    @staticmethod
    def getUserByCredentials(username, password):
        response = requests.post("http://localhost:10050/prototip2/login", json={"username": username, "password": password})

        if response.status_code == 200:
            userData = response.json()
            return userData  # Devuelve un diccionario con ID, username, email y token
        else:
            return None

class DAOChild:
    @staticmethod
    def getChildren(user_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"http://localhost:10050/prototip2/children/{user_id}", headers=headers)

        if response.status_code == 200:
            return response.json()  # Devuelve la información de los niños
        else:
            return None

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")
        self.root.geometry("1280x720")  # Tamaño de la ventana

        # Etiqueta y entrada para el username
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=10)

        # Etiqueta y entrada para el password
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=10)

        # Botón para iniciar sesión
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        # Área de texto para mostrar la información del usuario y de los niños
        self.user_info_text = tk.Text(root, height=30, width=100, state="disabled")
        self.user_info_text.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Por favor, introduce username y password.")
            return

        user = DAOUser.getUserByCredentials(username, password)
        if user:
            self.display_user_info(user)
            self.get_children_info(user)  # Llamar al método para obtener la información de los niños
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def display_user_info(self, user):
        self.user_info_text.config(state="normal")
        self.user_info_text.delete(1.0, tk.END)
        self.user_info_text.insert(tk.END, "✅ Inicio de sesión correcto!\n")
        self.user_info_text.insert(tk.END, " --- User Info --- \n")
        self.user_info_text.insert(tk.END, f"ID: {user['id']}\n")
        self.user_info_text.insert(tk.END, f"Username: {user['username']}\n")
        self.user_info_text.insert(tk.END, f"Email: {user['email']}\n")
        self.user_info_text.insert(tk.END, f"Token: {user['token']}\n")
        self.user_info_text.config(state="disabled")

    def get_children_info(self, user):
        user_id = user['id']
        token = user['token']
        children = DAOChild.getChildren(user_id, token)

        self.user_info_text.config(state="normal")
        if children:
            self.user_info_text.insert(tk.END, "\n👶 --- Children Info --- \n")
            for child in children:
                self.user_info_text.insert(tk.END, f"ID: {child['id']}\n")
                self.user_info_text.insert(tk.END, f"Nombre: {child['child_name']}\n")
                self.user_info_text.insert(tk.END, f"Promedio de sueño: {child['sleep_average']} horas\n\n")
        else:
            self.user_info_text.insert(tk.END, "\n❌ ERROR: No hay niños asociados a este usuario.\n")
        self.user_info_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()