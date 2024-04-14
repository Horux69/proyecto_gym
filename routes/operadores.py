from flask import session, redirect, request, render_template, jsonify, flash
from conexion import *
from models.Operadores import losOperadores
from datetime import datetime, timedelta
from models.Membresias import lasMembresias
import os



# OPERADORES --------------------------------------------------------------------------------------------

def obtener_datos_operadores():
    try:
        # Aquí realizas la consulta a tu base de datos o donde tengas los datos
        resultados = losOperadores.consultaOperadores()
        data = []

        for row in resultados:

            verMas = f"""<div class='btn-group'>
                            <button type='button' class='btn btn-primary' data-toggle='tooltip' data-placement='top' title='Ver más'>
                                <i class='fa fa-plus-circle' aria-hidden='true'></i>
                            </button>
                        </div>"""
            
            acciones = f"""<div class='btn-group'>
                            <a onclick='return confirm('Seguro quiere eliminar este operador?')' class='btn btn-danger delete-operador' href='#' data-id='{row[0]}'><i class='fa-solid fa-trash'></i></a>
                            
                            </div>"""

            caso = {
                "VerMas": verMas,
                "Acciones": acciones,
                "Usuario": row[0],
                "Nombre": row[1],
                "Apellido": row[2],
                "Cedula": row[3],
                "Telefono": row[4],
                "Correo": row[5],
                "Rol": row[6],
                "FechaRegistro": row[7],
                "Creador": row[8],
                "Estado": row[9],
            }

            data.append(caso)

        return data

    except Exception as e:
        # Manejo de errores
        print("Error:", e)
        return []

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
    
@app.route('/consultarDatosOperadores')
def consultarDatosOperadores():
    data = obtener_datos_operadores()

    return jsonify(data)

@app.route('/operadores/agregarOperador', methods= ["POST"])
def agregarOperadores():
    if  session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        if request.method == 'POST':
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
            flash('Cedula, Usuario o Correo ya Existentes.', 'error')
            return redirect('/operadores')
        else:
            registroOperadores = losOperadores.agregarOperador([usuario, nombre, apellido, cedula, telefono, correo, contrasena, rol, estado], session['user_name'])
            if registroOperadores:
                flash('El operador fue registrado exitosamente', 'success')
                return redirect('/operadores')
            else:
                flash('El operador no fue registrado correctamente.', 'error')
                return redirect('/operadores')
    else:
        return redirect('/')
    
@app.route('/operadores/desactivar/<usuario>')
def desactivarOperador(usuario):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        usuarioDelete = session['usuario']
        losOperadores.desactivarOpe(usuario, usuarioDelete)
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
