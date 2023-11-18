from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime
import hashlib
from claseValidaLogin import ValidationLogin
from claseOperadores import Operadores

app = Flask(__name__)

app.secret_key = "digitalforge"

# AGREGAR UN CONTROL DE TIEMPO DE LA SESION, (SOLO SI ES REQUERIDO)

mysql = MySQL()

""" app.config['MYSQL_DATABASE_HOST'] = 'gymcontrol.mysql.database.azure.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'horux69'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gym_control2525'
app.config['MYSQL_DATABASE_DB'] = 'gym_control' """

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'gym_control'

mysql.init_app(app)

conexion = mysql.connect()
cursor = conexion.cursor()

validaLogin = ValidationLogin(mysql)
losOperadores = Operadores(mysql)



@app.route('/')
def login():
    return render_template('auth/login.html')

# OPERADORES --------------------------------------------------------------------------------------------

@app.route('/operadores')
def consultaOperadores():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        resultado = losOperadores.consultaOperadores()
        return render_template('dashboard/operadores.html', operadores = resultado)
    
    elif session.get("logueado") and session.get("rol") == 'operador':
        return redirect('/inicio')
    else:
        return redirect('/')

@app.route('/operadores/agregarOperador', methods= ["POST"])
def agregarOperadores():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form ['cedula']
        telefono = request.form['celular']
        correo = request.form['correo']
        contrasena = request.form['password']
        rol = request.form['rol']
        estado = 'activo'

        if not losOperadores.validarDatosOpe(usuario, cedula, correo, telefono):

            losOperadores.agregarOperador([usuario, nombre, apellido, cedula, telefono, correo, contrasena,  rol,  estado], session['user_name'])

            return redirect('/operadores')
        else:
            return render_template('dashboard/operadores.html', mensaje = 'Cedula, Correo o Telefono no disponible.')
    else:
        return redirect('/')
    
@app.route('/operadores/desactivar/<usuario>')
def desactivarOperador(usuario):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        losOperadores.desactivarOpe(usuario)
        return redirect('/operadores')
    else:
        return redirect('/')
    
@app.route('/operadores/eliminar/<usuario>')
def eliminarOperador(usuario):
    if session.get("logueado") and session.get("rol") == 'super_admin':
        losOperadores.eliminarOpe(usuario)
        return redirect('/operadores')
    else:
        return redirect('/')
    
@app.route('/operadores/info/<usuario>', methods = ['GET'])
def infoOperadores(usuario):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':

        resultado = losOperadores.infoOperadores(usuario)

        return render_template('/dashboard/infoperador.html', operadores = resultado[0])
    else:
        return redirect('/')

# -------------------------------------------------------------------------------------------

@app.route('/validationAuth', methods = ['GET', 'POST'])
def validacionLogin():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['password']

        resultados = validaLogin.validaLogin(usuario, contrasena)

        print(resultados)

        if len(resultados) > 0:
            if contrasena == resultados[0][2]:
                session["logueado"] = True
                session["user_name"] = resultados[0][0] 
                session["rol"] = resultados[0][3]

                if session["rol"] == 'administrador' or session["rol"] == 'super_admin' or session["rol"] == 'entrenador':
                    return render_template('dashboard/index.html')
                else:
                    return redirect('/')
        else:
            return render_template('auth/login.html', mensaje = "Acesso denegado")


@app.route('/dashboard/cerrar')
def cerrarSesion():
    session.clear()
    return redirect('/')

# ----------------------------- INVENTARIO ------------------------------------#

@app.route('/inventario')
def inventario():
    return render_template('/dashboard/inventario_productos.html')

@app.route('/inventario/categorias')
def categorias():
    return render_template('/dashboard/categoria_productos.html')



@app.route('/inicio')
def inicio():
    if session.get("logueado"):
        return render_template('dashboard/index.html')
    else:
        return redirect('/')

""" @app.route('/operadores')
def operadores():
    return render_template('dashboard/operadores.html') """




def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializador_app():
    app.register_error_handler(404, pagina_no_encontrada)
    return app