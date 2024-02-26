from flask import session, render_template, redirect, request
from conexion import *
from datetime import datetime, timedelta
from models.Afiliados import LosAfiliados
from models.Membresias import lasMembresias

# ------------------------ AFILIADOS ---------------------------------------------#

@app.route('/afiliados')
def afiliados():
    if session.get("logueado"):
        resultado = LosAfiliados.consultarAfiliados()
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        

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
        sexo = request.form['sexo']
        sangre = request.form['sangre']
        huella = 'NULL'
        telefono_emergencia = request.form['telefono_emergencia']
        correo = request.form['email']
        contrasena = request.form['cedula']
        tarjeta_nfc = request.form['nfc']
        id_membresia = request.form['membresia']
        fecha_inicio = datetime.now()

        duracion_membresia = lasMembresias.consultaTiempoMembresia(id_membresia)
        duracion_timedelta = timedelta(days=duracion_membresia)
        fecha_vencimiento = fecha_inicio + duracion_timedelta
        
        fecha_registro = datetime.now().strftime('%Y-%m-%d')
        estado = 'activo'

        if not LosAfiliados.validarDatosAfiliados(cedula,correo,telefono):

            LosAfiliados.agregarAfiliados([cedula, nombre, apellido, fecha_nacimiento, telefono, sexo, sangre, huella, telefono_emergencia, correo, contrasena, tarjeta_nfc, id_membresia, fecha_inicio, fecha_vencimiento, fecha_registro, estado], session['user_name'])
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
        
        

        LosAfiliados.actualizarUsuarios([cedula,correo,telefono])

        return redirect('/afiliados')
    else:
        return redirect('/')
    
    
@app.route('/afiliados/infomedidas/<cedula>', methods = ['GET'])
def infomedidas(cedula):
    if session.get("logueado"):

        resultado = LosAfiliados.infoAfiliados(cedula)

        return render_template('/dashboard/medidas.html', afiliados = resultado[0])
    else:
        return redirect('/')

@app.route('/afiliados/agregarMedidas', methods = ['POST'])
def agregarMedidas():
    if session.get("logueado"):

        cedula = request.form['cedula']
        peso_corporal = request.form['peso_corporal']
        bicep_der = request.form['bicep_der']
        bicep_izq = request.form['bicep_izq']
        pecho = request.form['pecho']
        antebrazo_der = request.form['antebrazo_der']
        antebrazo_izq = request.form['antebrazo_izq']
        cintura = request.form['cintura']
        cadera = request.form['cadera']
        muslo_der = request.form['muslo_der']
        muslo_izq = request.form['muslo_izq']
        pantorrilla_der = request.form['pantorrilla_der']
        pantorrilla_izq = request.form['pantorrilla_izq']
        fecha_registro = datetime.now().strftime('%Y-%m-%d')
        
        
        
        
        LosAfiliados.agregarMedidas([cedula,fecha_registro,peso_corporal,bicep_der,bicep_izq,pecho,antebrazo_der,antebrazo_izq,cintura,cadera,muslo_der,muslo_izq,pantorrilla_der,pantorrilla_izq],session['user_name'])
        
        return redirect('/afiliados')
    else:
        return redirect('/')





