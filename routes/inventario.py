from flask import session, redirect, request, render_template
from conexion import *
from models.InvProductos import InvProductos
from datetime import datetime, timedelta
from models.Membresias import lasMembresias



# ----------------------------- INVENTARIO PRODUCTOS ------------------------------------#

@app.route('/inventario')
def inventario():
    if session.get("logueado"):
    
        resultado = InvProductos.consultarProductos()

        resulCate = InvProductos.consultaCataegorias()
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        

        return render_template('/dashboard/inventario_productos.html', productos = resultado, categorias = resulCate, resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    
    else:
        return redirect('/')
    
    

@app.route('/inventario/agregarProducto', methods = ['POST'])
def agregarProducto():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        cantidad = request.form['cantidad']
        estado = 'activo'

        InvProductos.agregarProducto([nombre, categoria, precio_compra, precio_venta, cantidad, estado])

        return redirect('/inventario')
    else:
        return redirect('/')
    
    

@app.route('/inventario/infoEditProducto/<id_producto>', methods = ['GET'])
def infoEditProducto(id_producto):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        
        resultado = InvProductos.infoEditProducto(id_producto)
        resultadoCate = InvProductos.consultaCataegorias()
        
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        
        return render_template('dashboard/editProducto.html', editProducto = resultado[0], resulCate = resultadoCate, resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')
    
    

@app.route('/inventario/editProducto', methods = ['POST'])
def editProducto():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        id_producto = request.form['txtID']
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        cantidad = request.form['cantidad']

        InvProductos.editProducto([id_producto, nombre, categoria, precio_compra, precio_venta, cantidad])

        return redirect('/inventario')
    else:
        return redirect('/')
    
    

@app.route('/inventario/desactivar/<id_productos>')
def desactivarProducto(id_productos):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        InvProductos.desactivarProductos(id_productos)
        return redirect('/inventario')
    else:
        return redirect('/')



#----------------------- CATEGORIA DE PRODUCTOS ---------------------------------#
@app.route('/categorias/agregarCategoria',methods=['POST'])
def agregarCategoria():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        
        nombre=request.form['nombre']
        estado = 'activo'
        
        

        InvProductos.agregarCategoria([nombre, estado])

        return redirect('/categorias')
    else:
        return redirect('/')
    
    

@app.route("/categorias")
def consultarCategoria():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        resultado = InvProductos.consultaCataegorias()
        
        
        
        """ MODAL DE REGISTRO AFILIADOS DEL NABVAR """
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        
        return render_template('dashboard/categoria_productos.html', categorias = resultado, resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')
    
    

@app.route('/categorias/desactivarCategoria/<id_categoria>')
def desactivarCategoria(id_categoria):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        InvProductos.desactivarCategoria(id_categoria)
        return redirect('/categorias')
    else:
        return redirect('/')
