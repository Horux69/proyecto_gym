from flask import session, redirect, request, render_template
from conexion import *
from models.Membresias import lasMembresias

# ------------------------ MEMBRESIAS ---------------------------------------------#

@app.route('/membresias')
def membresias():
    if session.get("logueado"):
        resultado = lasMembresias.consultarMembresias()
        return render_template('dashboard/membresias.html', membresias = resultado)
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

        return render_template('dashboard/edit_membresia.html', editMembresia = resultado[0])
    else:
        return redirect('/')
    
@app.route('/membresias/editarMembresia', methods = ['POST'])
def editMembresia():
    _id = request.form['txtID']
    nombre = request.form['nombre']
    duracion = request.form['duracion']
    precio = request.form['precio']

    lasMembresias.editMembresia([_id, nombre, duracion, precio])

    return redirect('/membresias')

