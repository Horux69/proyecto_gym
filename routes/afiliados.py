from flask import session, render_template, redirect, request, jsonify, flash
from conexion import *
from datetime import datetime, timedelta, date
from models.Afiliados import LosAfiliados
from models.Membresias import lasMembresias
from models.IngresoAfiliados import IngresoAfiliados
import hashlib

# ------------------------ AFILIADOS ---------------------------------------------#

@app.route('/afiliados/ingresoAfiliado', methods = ['POST'])
def consultarEstadoAfiliado():
    cedula_afiliado = request.form['cedula']

    infoAfiliado = LosAfiliados.infoAfiliados(cedula_afiliado)

    if infoAfiliado:

        id_afiliado = infoAfiliado[0][0]

        fecha_actual = datetime.now().date()

        fecha_vencimiento = infoAfiliado[0][14]

        dias_restantes = (fecha_vencimiento - fecha_actual).days

        nombre_afiliado = infoAfiliado[0][1] + ' ' + infoAfiliado[0][2]
        
        if infoAfiliado[0][17] == 'activo':
            fecha_ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            IngresoAfiliados.agregarIngresoAfiliado(id_afiliado, fecha_ingreso)

            return jsonify({
                            'valido': 'Valido',
                            'nombreAfiliado': nombre_afiliado,
                            'restantes': dias_restantes
                            })
        else:
            dias_restantes = 0

            return jsonify({
                            'valido': 'Invalido',
                            'nombreAfiliado': nombre_afiliado,
                            'restantes': dias_restantes
                            })
    else:
        return jsonify({
                            'valido': 'Error',
                            })

def obtener_datos_afiliados():
    try:
        # Aquí realizas la consulta a tu base de datos o donde tengas los datos
        resultados = LosAfiliados.consultarAfiliados()
        data = []

        for row in resultados:

            verMas = f"""<div class='btn-group'>
                            <button type='button' class='btn btn-primary' data-toggle='tooltip' data-placement='top' title='Ver más'>
                                <i class='fa fa-plus-circle' aria-hidden='true'></i>
                            </button>
                        </div>"""
            
            acciones = f"""<div class='btn-group'>
                            <a onclick='return confirm('Seguro quiere eliminar este operador?')' class='btn btn-danger delete-afiliado' href='#' data-id='{row[0]}'><i class='fa-solid fa-trash'></i></a>
                            <a class="btn btn-info" href="/afiliados/info/{row[0]}"><i class="fa-solid fa-address-card" style="color: #fff;"></i></a>
                            <a class="btn btn-primary" href="/afiliados/actualizarMembresias/{row[0]}"><i class="fa-solid fa-credit-card" style="color: #fff;"></i></a>
                            <a class="btn btn-primary" href="/afiliados/nuevacontra/{row[0]}"><i class="fa-solid fa-key" ></i></i></a>
                            
                            </div>"""

            cedula_formateada = "{0:,}".format(int(row[0])).replace(",", ".")
            caso = {
                "VerMas": verMas,
                "Acciones": acciones,
                "Nombre": row[1],
                "Apellido": row[2],
                "Cedula": cedula_formateada,
                "Telefono": row[4],
                "Correo": row[9],
                "FechaNac": row[3],
                "FechaRegistro": row[15],
                "Creador": row[16],
                "EstadoMembresia": row[17],
                "Sexo": row[5],
                "TipoSangre": row[6],
                "NumEmergencia": row[8],
                "FechaInicioM": row[13],
                "FechaFinalM": row[14],
            }

            data.append(caso)

        return data

    except Exception as e:
        # Manejo de errores
        print("Error:", e)
        return []
    
def obtener_datos_medidas():
    try:
        # Aquí realizas la consulta a tu base de datos o donde tengas los datos
        resultados = LosAfiliados.consultarMedidasAfiliados()
        data = []

        for row in resultados:

            verMas = f"""<div class='btn-group'>
                            <button type='button' class='btn btn-primary' data-toggle='tooltip' data-placement='top' title='Ver más'>
                                <i class='fa fa-plus-circle' aria-hidden='true'></i>"""
    
            acciones = f"""<div class='btn-group'>
                            <a class="btn btn-success" href="#"><i class="fa-solid fa-pen-to-square" style="color: #ffffff;"></i></a>
                            </div>"""   
            
            datos = {
                "VerMas": verMas,
                "Acciones": acciones,
                "cedula": row[1],
                "creador": row[2],
                "fecha_registro": row[3],
                "peso_corporal": row[4],
                "bicep_der": row[5],
                "bicep_izq": row[6],
                "pecho": row[7],
                "antebrazo_der": row[8],
                "antebrazo_izq": row[9],
                "cintura": row[10],
                "cadera": row[11],
                "muslo_der": row[12],
                "muslo_izq": row[13],
                "pantorrilla_der": row[14],
                "pantorrilla_izq": row[15]
            }

            data.append(datos)

        return data
            
    except Exception as e:
        # Manejo de errores
        print("Error:", e)
        return []
    

@app.route('/consultarMedidasAfiliados')
def consultarMedidasAfiliados():
    data = obtener_datos_medidas()

    return jsonify(data)

@app.route('/medidas')
def medidas():
    if session.get("logueado"): 
        afiliados = LosAfiliados.consultarAfiliados()
        # print(afiliados)
        return render_template('dashboard/medidas.html', afiliados = afiliados)
    else:
        return redirect('/')


    
@app.route('/consultarDatosAfiliados')
def consultarDatosAfiliados():
    data = obtener_datos_afiliados()

    return jsonify(data)

@app.route('/afiliados')
def afiliados():
    if session.get("logueado"):
        mensaje = ''  # Inicializar mensaje como None por defecto
        if 'mensaje' in session:
            mensaje = session.pop('mensaje')
            
        resultado = LosAfiliados.consultarAfiliados()
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        

        return render_template('dashboard/afiliados.html', resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')
    
    

@app.route('/afiliados/agregarAfiliado', methods = ['POST'])
def agregarAfiliados():
    if session.get("logueado"):
        if request.method == "POST":

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
            cifrada = hashlib.sha512(contrasena.encode('utf-8')).hexdigest()
            tarjeta_nfc = request.form['nfc']
            id_membresia = request.form['membresia']
            fecha_inicio = datetime.now()

            duracion_membresia = lasMembresias.consultaTiempoMembresia(id_membresia)
            duracion_timedelta = timedelta(days=duracion_membresia)
            fecha_vencimiento = fecha_inicio + duracion_timedelta
            
            fecha_registro = datetime.now().strftime('%Y-%m-%d')
            estado = 'activo'

            if LosAfiliados.validarDatosAfiliados(cedula,correo,telefono):
                flash('Cedula, Telefono o Correo ya Existentes.', 'error')
                return redirect('/afiliados')
            else:
                registroAfiliado = LosAfiliados.agregarAfiliados([cedula, nombre, apellido, fecha_nacimiento, telefono, sexo, sangre, huella, telefono_emergencia, correo, cifrada, tarjeta_nfc, id_membresia, fecha_inicio, fecha_vencimiento, fecha_registro, estado], session['user_name'])
                if registroAfiliado:
                    flash('El nuevo usuario fue registrado exitosamente', 'success')
                    return redirect('/afiliados')
                else:
                    flash('El usuario no fue registrado correctamente.', 'error')
                    return redirect('/afiliados')
        else:
            flash('El usuario no fue registrado correctamente.', 'error')
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
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        resultado = LosAfiliados.infoAfiliados(cedula)

        return render_template('/dashboard/infoafiliados.html', afiliados = resultado[0], resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
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
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        return render_template('/dashboard/medidas.html', afiliados = resultado[0], resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima, oculta=1)
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
        
        registroMedidas = LosAfiliados.agregarMedidas([cedula,fecha_registro,peso_corporal,bicep_der,bicep_izq,pecho,antebrazo_der,antebrazo_izq,cintura,cadera,muslo_der,muslo_izq,pantorrilla_der,pantorrilla_izq],session['user_name'])

        if registroMedidas:
            flash('Las medidas fueron registradas exitosamente', 'success')
            return redirect('/medidas')
        else:
            flash('Las medidas no fueron registradas correctamente.', 'error')
            return redirect('/medidas')
        
    else:
        return redirect('/')
    
    
    
@app.route('/afiliados/actualizarMembresias/<cedula>', methods = ['GET'])
def actualizarMembresiasInicio(cedula):
    if session.get("logueado"):
        
        membresias = lasMembresias.consultarMembresias()
        
        resultado = LosAfiliados.infoAfiliados(cedula)

        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        
        return render_template('/dashboard/actualizar_membresias.html', resulMem = membresias, afiliados = resultado, minima = fecha_minima, maxima = fecha_maxima)  
    
    else:
        return redirect('/')
    
    
    
@app.route('/afiliados/actulizarMembresias', methods = ['POST'])
def actualizarMembresias():
    if session.get("logueado"):
        
        cedula = request.form['cedula']
        id_membresia = request.form['membresia']
        fec_vencimiento = datetime.strptime(request.form['frevencimiento'], '%Y-%m-%d') 
        fec_inicio = request.form['freinicio']
        fecha_actual = datetime.now()
        resultado_dia = lasMembresias.consultaDias(id_membresia)
        
        if fecha_actual > fec_vencimiento:
            
            LosAfiliados.actualizarMembresias_y_fechaInico([cedula,fecha_actual,resultado_dia[0],id_membresia,fec_inicio])
            return redirect('/afiliados')
        
        else:
            LosAfiliados.actualizarMembresias([cedula,resultado_dia[0],id_membresia])
            return redirect('/afiliados')
    else:
        return redirect('/')
    
@app.route('/afiliados/actualizarContra', methods=['POST'])
def actualizarContra():
    if session.get("logueado"):
       
        contra1 = request.form['contra1']
        contra2 = request.form['contra2']
        cedula = request.form['cedula']
        
        if contra1 == contra2:
            cifrada = hashlib.sha512(contra1.encode('utf-8')).hexdigest()
            
            LosAfiliados.actualizarContra([cedula, cifrada])

            print("la contraseña se cambio correctamente")
        return redirect('/afiliados')  
    
    else:
        
        return redirect('/afiliados')
    
@app.route('/afiliados/nuevacontra/<cedula>')
def nuevacontra(cedula): 
        if session.get("logueado"):
        
            membresias = lasMembresias.consultarMembresias()


            fecha_actual = datetime.now()

            # fecha de nacimiento maxima (hace 16 años)
            fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


            # fecha de nacimiento minima (hace 70 años)
            fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        return render_template('/dashboard/nuevacontra.html',cedula = cedula , resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)




