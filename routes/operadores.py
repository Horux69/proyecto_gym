from flask import session, redirect, request, render_template
from conexion import *
from models.Operadores import losOperadores

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
