from flask import session, redirect, request, render_template
from conexion import *
from models.InvProductos import InvProductos

# ----------------------------- INVENTARIO PRODUCTOS ------------------------------------#

@app.route('/inventario')
def inventario():
    resultado = InvProductos.consultarProductos()

    resulCate = InvProductos.consultaCataegorias()

    return render_template('/dashboard/inventario_productos.html', productos = resultado, categorias = resulCate)

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
def infoEdirProducto(id_producto):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        resultado = InvProductos.infoEditProducto(id_producto)
        resultadoCate = InvProductos.consultaCataegorias()
        return render_template('dashboard/editProducto.html', editProducto = resultado[0], resulCate = resultadoCate)
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
        return render_template('dashboard/categoria_productos.html', categorias = resultado)
    else:
        return redirect('/')

@app.route('/categorias/desactivarCategoria/<id_categoria>')
def desactivarCategoria(id_categoria):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        InvProductos.desactivarCategoria(id_categoria)
        return redirect('/categorias')
    else:
        return redirect('/')
