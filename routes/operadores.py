from flask import session, redirect, request, render_template
from conexion import *
from models.Operadores import losOperadores
from datetime import datetime, timedelta
from models.Membresias import lasMembresias
import os



# OPERADORES --------------------------------------------------------------------------------------------

@app.route('/operadores')
def consultaOperadores():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        
        mensaje = ''  # Inicializar mensaje como None por defecto
        if 'mensaje' in session:
            mensaje = session.pop('mensaje')
        
        resultado = losOperadores.consultaOperadores()
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        
        return render_template('dashboard/operadores.html', operadores = resultado,  resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima, mensaje = mensaje)
    
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
        

        if losOperadores.validarDatosOpe(usuario, cedula, correo, telefono):

            losOperadores.agregarOperador([usuario, nombre, apellido, cedula, telefono, correo, contrasena,  rol,  estado], session['user_name'])

            return redirect('/operadores')
        else:
            session['mensaje'] = "Cedula, Correo o Telefono no disponible."
            return redirect('/operadores')
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
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        return render_template('/dashboard/infoperador.html', operadores = resultado[0], resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')
