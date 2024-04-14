from flask import session, redirect, request, render_template, jsonify, flash
from conexion import *
from models.Membresias import lasMembresias
from datetime import datetime, timedelta
from models.Membresias import lasMembresias




# ------------------------ MEMBRESIAS ---------------------------------------------#

def obtener_datos_membresias():
    try:
        # Aquí realizas la consulta a tu base de datos o donde tengas los datos
        resultados = lasMembresias.consultarMembresias()
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
                            </div>"""

            precio = "${:,.2f}".format(row[3])
            caso = {
                "VerMas": verMas,
                "Acciones": acciones,
                "Nombre": row[1],
                "TiempoDuracion": row[2],
                "Precio": precio,
                "Estado": row[4]
            }

            data.append(caso)

        return data

    except Exception as e:
        # Manejo de errores
        print("Error:", e)
        return []
    
@app.route('/consultarDatosMembresias')
def consultarDatosMembresias():
    data = obtener_datos_membresias()

    return jsonify(data)

@app.route('/membresias')
def membresias():
    if session.get("logueado"):
        mensaje = ''  # Inicializar mensaje como None por defecto
        if 'mensaje' in session:
            mensaje = session.pop('mensaje')
            
        resultado = lasMembresias.consultarMembresias()
        
        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        
        
        return render_template('dashboard/membresias.html', membresias = resultado, resulMem = resultado, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')
    
    
    
@app.route('/membresias/agregarMembresia', methods = ['POST'])
def agregarMembresia():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        
        if request.method == 'POST':    
            nombre = request.form['nombre']
            duracion = request.form['duracion']
            precio = request.form['precio']
            estado = 'activo'

            lasMembresias.agregarMembresia([nombre, duracion, precio, estado])

            return redirect('/membresias')
        else:
            session['mensaje'] = "Lo sentimos hubo un error de seguridad."
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
        
        esultado = lasMembresias.consultarMembresias()
        
        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))

        return render_template('dashboard/edit_membresia.html', editMembresia = resultado[0], resulMem = resultado, minima = fecha_minima, maxima = fecha_maxima)
    
    
    else:
        return redirect('/')
    
    
    
@app.route('/membresias/editarMembresia', methods = ['POST'])
def editMembresia():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        if request.method == 'POST':
            _id = request.form['txtID']
            nombre = request.form['nombre']
            duracion = request.form['duracion']
            precio = request.form['precio']
            
            lasMembresias.editMembresia([_id, nombre, duracion, precio])

            return redirect('/membresias')
        else:
            session['mensaje'] = "Lo sentimos hubo un error de seguridad."
            return redirect('/membresias')
    else:
        return redirect('/')

