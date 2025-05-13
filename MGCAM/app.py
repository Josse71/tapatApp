from flask import Flask, render_template, request, redirect, session, url_for
import hashlib
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Conexión a MySQL
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    if 'usuario' in session:
        return render_template('home.html', usuario=session['usuario'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario=%s AND contrasena_md5=%s", (usuario, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Credenciales incorrectas')
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect('/login')
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre_usuario = %s", (session['username'],))
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM imagenes WHERE id_usuario = %s", (user['id_usuario'],))
    imagenes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('home.html', imagenes=imagenes)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre_usuario, contrasena_md5, email, rol) VALUES (%s, %s, %s, %s)", 
                       (usuario, password, email, 'User'))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
