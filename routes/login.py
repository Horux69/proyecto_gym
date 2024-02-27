from flask import session, redirect, request, render_template
from conexion import *
from models.ValidaLogin import validaLogin 



@app.route('/validationAuth', methods = ['GET', 'POST'])
def validacionLogin():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['password']

        resultados = validaLogin.validaLogin(usuario, contrasena)

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
        

@app.route('/inicio')
def inicio():
    if session.get("logueado"):
        return render_template('dashboard/index.html')
    else:
        return redirect('/')


@app.route('/dashboard/cerrar')
def cerrarSesion():
    session.clear()
    return redirect('/')