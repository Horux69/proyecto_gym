from flask import session, redirect, request, render_template
from conexion import *
from models.Membresias import lasMembresias
from datetime import datetime, timedelta
from models.Membresias import lasMembresias




# ------------------------ MEMBRESIAS ---------------------------------------------#

@app.route('/membresias')
def membresias():
    if session.get("logueado"):
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
        
        _id = request.form['txtID']
        nombre = request.form['nombre']
        duracion = request.form['duracion']
        precio = request.form['precio']

        lasMembresias.editMembresia([_id, nombre, duracion, precio])

        return redirect('/membresias')
    
    else:
        return redirect('/')

