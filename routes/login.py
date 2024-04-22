from flask import session, redirect, request, render_template, flash
from conexion import *
from models.ValidaLogin import validaLogin
from datetime import datetime, timedelta
from models.Membresias import lasMembresias
from models.Afiliados import LosAfiliados




@app.route('/validationAuth', methods = ['POST'])
def validacionLogin():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['password'].lower()

        resultados = validaLogin.validaLogin(usuario, contrasena)
        

        if len(resultados) > 0:
            if contrasena == resultados[0][2]:
                session["logueado"] = True
                session["user_name"] = resultados[0][0] 
                session["rol"] = resultados[0][3]
                session["usuario"] = resultados[0][1]

                print(session['usuario'])
                if session["rol"] == 'administrador' or session["rol"] == 'super_admin' or session["rol"] == 'entrenador':
                    return redirect('/inicio')
                else:
                    flash('Credenciales incorrectas.', 'error')
                    return redirect('/')
        else:
            return render_template('auth/login.html', mensaje = "Acesso denegado")
        

@app.route('/inicio')
def inicio():
    if session.get("logueado"):
        
        membresias = lasMembresias.consultarMembresias()

        afiliadosActivos = LosAfiliados.consultarUsuariosPorEstadoMembresia()

        fecha_actual = datetime.now()

        print(afiliadosActivos)

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))

        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        renovadas = afiliadosActivos[0][1]
        no_renovadas = afiliadosActivos[1][1]

        data = [renovadas, no_renovadas]
        
        return render_template('dashboard/index.html', resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima, data=data)
    else:
        return redirect('/')


@app.route('/dashboard/cerrar')
def cerrarSesion():
    session.clear()
    return redirect('/')