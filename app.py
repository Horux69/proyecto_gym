from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime, timedelta
import hashlib
from claseValidaLogin import ValidationLogin
from claseOperadores import Operadores
from claseMembresias import Membresias
from claseAfiliados import Afiliados
from claseInvProductos import InventarioProductos

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
lasMembresias = Membresias(mysql)
LosAfiliados = Afiliados(mysql)
InvProductos = InventarioProductos(mysql)

LosAfiliados.desactivarUsuarios() #funcion de desactivar usuarios

@app.route('/')
def login():
    return render_template('auth/login.html')

@app.route('/Inicio')
def Inicio():
    return render_template('dashboard/index.html')
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
                    return redirect('/inicio')
                else:
                    return redirect('/')
        else:
            return render_template('auth/login.html', mensaje = "Acesso denegado")


@app.route('/dashboard/cerrar')
def cerrarSesion():
    session.clear()
    return redirect('/')

# ----------------------------- INVENTARIO PRODUCTOS ------------------------------------#

@app.route('/inventario')
def inventario():
    resultado = InvProductos.consultarProductos()

    resulCate = InvProductos.consultaCataegorias()

    return render_template('/dashboard/inventario_productos.html', productos = resultado, categorias = resulCate)

@app.route('/inventario/agregarProducto', methods = ['POST'])
def agregarProducto():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        cantidad = request.form['cantidad']
        estado = 'activo'

        InvProductos.agregarProducto([nombre, categoria, precio_compra, precio_venta, cantidad, estado])

        return redirect('/inventario')
    else:
        return redirect('/')

@app.route('/inventario/infoEditProducto/<id_producto>', methods = ['GET'])
def infoEdirProducto(id_producto):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        resultado = InvProductos.infoEditProducto(id_producto)
        resultadoCate = InvProductos.consultaCataegorias()
        return render_template('dashboard/editProducto.html', editProducto = resultado[0], resulCate = resultadoCate)
    else:
        return redirect('/')

@app.route('/inventario/editProducto', methods = ['POST'])
def editProducto():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        id_producto = request.form['txtID']
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        cantidad = request.form['cantidad']

        InvProductos.editProducto([id_producto, nombre, categoria, precio_compra, precio_venta, cantidad])

        return redirect('/inventario')
    else:
        return redirect('/')

@app.route('/inventario/desactivar/<id_productos>')
def desactivarProducto(id_productos):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        InvProductos.desactivarProductos(id_productos)
        return redirect('/inventario')
    else:
        return redirect('/')



#----------------------- CATEGORIA DE PRODUCTOS ---------------------------------#

@app.route('/categorias/agregarCategoria',methods=['POST'])
def agregarCategoria():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        nombre=request.form['nombre']
        estado = 'activo'

        InvProductos.agregarCategoria([nombre, estado])

        return redirect('/categorias')
    else:
        return redirect('/')

@app.route("/categorias")
def consultarCategoria():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        resultado = InvProductos.consultaCataegorias()
        print(resultado)
        return render_template('dashboard/categoria_productos.html', categorias = resultado)
    else:
        return redirect('/')

@app.route('/categorias/desactivarCategoria/<id_categoria>')
def desactivarCategoria(id_categoria):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        InvProductos.desactivarCategoria(id_categoria)
        return redirect('/categorias')
    else:
        return redirect('/')


# ------------------------ MEMBRESIAS ---------------------------------------------#

@app.route('/membresias')
def membresias():
    if session.get("logueado"):
        resultado = lasMembresias.consultarMembresias()
        return render_template('dashboard/membresias.html', membresias = resultado)
    else:
        return redirect('/')
    
@app.route('/membresias/agregarMembresia', methods = ['POST'])
def agregarMembresia():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        nombre = request.form['nombre']
        duracion = request.form['duracion']
        precio = request.form['precio']
        estado = 'activo'

        lasMembresias.agregarMembresia([nombre, duracion, precio, estado])

        return redirect('/membresias')
    else:
        return redirect('/')
    
@app.route('/membresias/desactivarMembresia/<id_membresia>')
def desactivarMembresia(id_membresia):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        lasMembresias.desactivarMembresia(id_membresia)
        return redirect('/membresias')
    else:
        return redirect('/')
    
@app.route('/membresias/infoEdit/<id_membresia>', methods = ['GET'])
def infoMembresiaEdit(id_membresia):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        resultado = lasMembresias.infoMembresia(id_membresia)

        return render_template('dashboard/edit_membresia.html', editMembresia = resultado[0])
    else:
        return redirect('/')
    
@app.route('/membresias/editarMembresia', methods = ['POST'])
def editMembresia():
    _id = request.form['txtID']
    nombre = request.form['nombre']
    duracion = request.form['duracion']
    precio = request.form['precio']

    lasMembresias.editMembresia([_id, nombre, duracion, precio])

    return redirect('/membresias')


# ------------------------ AFILIADOS ---------------------------------------------#

@app.route('/afiliados')
def afiliados():
    if session.get("logueado"):
        resultado = LosAfiliados.consultarAfiliados()
        print(resultado)
        membresias = lasMembresias.consultarMembresias()

        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))
        print(fecha_maxima)


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        print(fecha_minima)

        return render_template('dashboard/afiliados.html', afiliados = resultado, resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')

@app.route('/afiliados/agregarAfiliado', methods = ['GET', 'POST'])
def agregarAfiliados():
    if session.get("logueado"):

        cedula = request.form['cedula']
        nombre = request.form['nombres']
        apellido = request.form['apellidos']
        fecha_nacimiento = request.form['fecha_nac']
        telefono = request.form['telefono']
        correo = request.form['email']
        tarjeta_nfc = request.form['nfc']
        id_membresia = request.form['membresia']
        fecha_inicio = datetime.now()

        duracion_membresia = lasMembresias.consultaTiempoMembresia(id_membresia)
        duracion_timedelta = timedelta(days=duracion_membresia)

        fecha_vencimiento = fecha_inicio + duracion_timedelta
        
        fecha_registro = datetime.now().strftime('%Y-%m-%d')
        estado = 'activo'

        if not LosAfiliados.validarDatosAfiliados(cedula,correo,telefono):

            LosAfiliados.agregarAfiliados([cedula,nombre,apellido,fecha_nacimiento,telefono,correo,tarjeta_nfc,id_membresia,fecha_inicio,fecha_vencimiento,fecha_registro,estado], session['user_name'])
            return redirect('/afiliados')
        else:
            return redirect('/afiliados')
        

@app.route('/afiliados/desactivarAfiliado/<cedula>')
def desactivarAfiliados(cedula):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        LosAfiliados.desactivarAfiliados(cedula)
        return redirect('/afiliados')
    
    
@app.route('/afiliados/info/<cedula>', methods = ['GET'])
def infoAfiliados(cedula):
    if session.get("logueado"):

        resultado = LosAfiliados.infoAfiliados(cedula)

        return render_template('/dashboard/infoafiliados.html', afiliados = resultado[0])
    else:
        return redirect('/')
    
@app.route('/afiliados/actualizarUsuarios', methods = ['POST'])
def actualizarUsuario():
    
    if session.get("logueado"):

        cedula = request.form['cedula']
        correo = request.form['correo']
        telefono = request.form['celular']
        print(cedula, correo, telefono)
        

        LosAfiliados.actualizarUsuarios([cedula,correo,telefono])

        return redirect('/afiliados')
    else:
        return redirect('/')

    




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