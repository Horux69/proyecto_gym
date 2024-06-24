from flask import session, redirect, request, render_template, flash
from conexion import *
from models.ValidaLogin import validaLogin
from datetime import datetime, timedelta
from models.Membresias import lasMembresias
from models.Afiliados import LosAfiliados
from models.IngresoAfiliados import losIngresoAfiliados
import hashlib





@app.route('/validationAuth', methods=['POST'])
def validacionLogin():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['password'].lower()
        cifrada = hashlib.sha512(contrasena.encode('utf-8')).hexdigest()
        print(cifrada)

        resultados = validaLogin.validaLogin(usuario, cifrada)

        if len(resultados) > 0:
            if cifrada == resultados[0][2]:
                session["logueado"] = True
                session["user_name"] = resultados[0][0]
                session["rol"] = resultados[0][3]
                session["usuario"] = resultados[0][1]

                print(session['usuario'])
                if session["rol"] == 'administrador' or session["rol"] == 'super_admin' or session["rol"] == 'entrenador':
                    return redirect('/inicio')
                else:
                    return redirect('/')
        else:
            flash('Usuario o Contraseña Incorrectas.', 'error')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

        
def convertir_a_formato_12_horas(hora):
    return datetime.strptime(hora, "%H").strftime("%I %p")

@app.route('/inicio')
def inicio():
    if session.get("logueado"):
        
        membresias = lasMembresias.consultarMembresias()

        # ESTADISTICAS PARA CONSULTAR LA CANTIDAD DE USUARIOS CON MEMBRESIA ACTIVA E INACTIVA

        afiliadosActivos = LosAfiliados.consultarUsuariosPorEstadoMembresia()

        print(afiliadosActivos)

        # fecha_actual = datetime.now()

        # # fecha de nacimiento maxima (hace 16 años)
        # fecha_maxima = fecha_actual - timedelta(days=(16 * 365))

        # # fecha de nacimiento minima (hace 70 años)
        # fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        if afiliadosActivos[0][0] == 'inactivo':
            afiliadosActivos = (('activo', 0),) + afiliadosActivos

        renovadas = afiliadosActivos[0][1]
        no_renovadas = afiliadosActivos[1][1] if afiliadosActivos and len(afiliadosActivos) > 1 else 0

        data = [renovadas, no_renovadas]

        print(data)

        # ESTADISTICAS PARA CONSULTAR LAS HORAS MAS CONCURRIDAS DE INGRESO AL GYM

        datos_por_hora = losIngresoAfiliados.consultarHorasConcurridas()

        labels = [convertir_a_formato_12_horas(str(hora)) for hora in range(24)]
        datos = [datos_por_hora.get(hora, 0) for hora in range(24)]

        # minima = fecha_minima, maxima = fecha_maxima,
        
        return render_template('dashboard/index.html', resulMem = membresias, data=data, labels=labels, datos = datos)
    else:
        return redirect('/')


@app.route('/dashboard/cerrar')
def cerrarSesion():
    session.clear()
    return redirect('/')