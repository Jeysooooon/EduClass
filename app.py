import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de la conexión a la base de datos
DB_HOST = os.environ.get('MYSQLHOST', 'localhost')
DB_USER = os.environ.get('MYSQLUSER', 'root')
DB_PASSWORD = os.environ.get('MYSQLPASSWORD', '')
DB_NAME = os.environ.get('MYSQLDATABASE', 'EduClass')
DB_PORT = os.environ.get('MYSQLPORT', 3306)

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

@app.route("/")
def index():
    return render_template('index.html')

# ================= CRUD: ESTUDIANTE =================
@app.route("/estudiante/")
def estudiante_index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Estudiante")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('estudiante/index.html', lista_estudiantes=datos)

@app.route("/estudiante/agregar", methods=["GET", "POST"])
def estudiante_agregar():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        nombre = request.form['EstNombre']
        apellido = request.form['EstApellido']
        dni = request.form['EstDNI']
        correo = request.form['EstCorreo']
        
        cursor.execute("INSERT INTO Estudiante (EstNombre, EstApellido, EstDNI, EstCorreo) VALUES (%s, %s, %s, %s)", 
                       (nombre, apellido, dni, correo))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('estudiante_index'))
    return render_template('estudiante/agregar.html')

@app.route("/estudiante/editar/<int:codigo>", methods=["GET", "POST"])
def estudiante_editar(codigo):
    if request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Estudiante WHERE EstCodigo = %s", (codigo,))
        estudiante = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('estudiante/editar.html', estudiante=estudiante)
    elif request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        nombre = request.form['EstNombre']
        apellido = request.form['EstApellido']
        dni = request.form['EstDNI']
        correo = request.form['EstCorreo']
        
        cursor.execute("UPDATE Estudiante SET EstNombre=%s, EstApellido=%s, EstDNI=%s, EstCorreo=%s WHERE EstCodigo=%s", 
                       (nombre, apellido, dni, correo, codigo))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('estudiante_index'))

@app.route("/estudiante/eliminar/<int:codigo>", methods=["GET", "POST"])
def estudiante_eliminar(codigo):
    if request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Estudiante WHERE EstCodigo = %s", (codigo,))
        estudiante = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('estudiante/eliminar.html', estudiante=estudiante)
    elif request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Estudiante WHERE EstCodigo=%s", (codigo,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('estudiante_index'))

# ================= CRUD: DOCENTE =================
@app.route("/docente/")
def docente_index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Docente")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('docente/index.html', lista_docentes=datos)

@app.route("/docente/agregar", methods=["GET", "POST"])
def docente_agregar():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        nombre = request.form['DocNombre']
        apellido = request.form['DocApellido']
        especialidad = request.form['DocEspecialidad']
        telefono = request.form['DocTelefono']
        
        cursor.execute("INSERT INTO Docente (DocNombre, DocApellido, DocEspecialidad, DocTelefono) VALUES (%s, %s, %s, %s)", 
                       (nombre, apellido, especialidad, telefono))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('docente_index'))
    return render_template('docente/agregar.html')

@app.route("/docente/editar/<int:codigo>", methods=["GET", "POST"])
def docente_editar(codigo):
    if request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Docente WHERE DocCodigo = %s", (codigo,))
        docente = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('docente/editar.html', docente=docente)
    elif request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        nombre = request.form['DocNombre']
        apellido = request.form['DocApellido']
        especialidad = request.form['DocEspecialidad']
        telefono = request.form['DocTelefono']
        
        cursor.execute("UPDATE Docente SET DocNombre=%s, DocApellido=%s, DocEspecialidad=%s, DocTelefono=%s WHERE DocCodigo=%s", 
                       (nombre, apellido, especialidad, telefono, codigo))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('docente_index'))

@app.route("/docente/eliminar/<int:codigo>", methods=["GET", "POST"])
def docente_eliminar(codigo):
    if request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Docente WHERE DocCodigo = %s", (codigo,))
        docente = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('docente/eliminar.html', docente=docente)
    elif request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Docente WHERE DocCodigo=%s", (codigo,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('docente_index'))

if __name__ == "__main__":
    app.run(debug=True)