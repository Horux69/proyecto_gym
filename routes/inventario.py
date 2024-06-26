from flask import session, redirect, request, render_template, jsonify, flash
from conexion import *
from models.InvProductos import InvProductos
from datetime import datetime, timedelta
from models.Membresias import lasMembresias



# ----------------------------- INVENTARIO PRODUCTOS ------------------------------------#

def obtener_datos_inventario():
    try:
        # Aquí realizas la consulta a tu base de datos o donde tengas los datos
        resultados = InvProductos.consultarProductos()
        data = []

        for row in resultados:

            verMas = f"""<div class='btn-group'>
                            <button type='button' class='btn btn-primary' data-toggle='tooltip' data-placement='top' title='Ver más'>
                                <i class='fa fa-plus-circle' aria-hidden='true'></i>
                            </button>
                        </div>"""
            
            acciones = f"""<div class='btn-group'>
                            <a class='btn btn-danger delete-producto' href='#' data-id='{row[0]}'><i class='fa-solid fa-trash'></i></a>
                            <a class="btn btn-primary" href="/inventario/infoEditProducto/{row[0]}"><i class="fa-solid fa-pen-to-square" style="color: #ffffff;"></i></a>
                            </div>"""

            caso = {
                "VerMas": verMas,
                "Acciones": acciones,
                "Nombre": row[1],
                "NombreCategoria": row[2],
                "PrecioCompra": row[3],
                "PrecioVenta": row[4],
                "Cantidad": row[5]
            }

            data.append(caso)

        return data

    except Exception as e:
        # Manejo de errores
        print("Error:", e)
        return []
    
@app.route('/consultarDatosInventario')
def consultarDatosInventario():
    data = obtener_datos_inventario()

    return jsonify(data)

@app.route('/inventario')
def inventario():
    if session.get("logueado"):
        
        mensaje = ''  # Inicializar mensaje como None por defecto
        if 'mensaje' in session:
            mensaje = session.pop('mensaje')
    
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
        if request.method == 'POST':
            nombre = request.form['nombre']
            categoria = request.form['categoria']
            precio_compra = request.form['precio_compra']
            precio_venta = request.form['precio_venta']
            cantidad = int(request.form['cantidad'])
            estado = 'activo'
            
            if precio_venta > precio_compra:
                if cantidad > 0:
                    InvProductos.agregarProducto([nombre, categoria, precio_compra, precio_venta, cantidad, estado])
                    flash('El producto fue registra correctamente.', 'success')
                    return redirect('/inventario')
                else:
                    flash('La cantidad tiene que ser mayor a 0.', 'info')
                    return redirect('/inventario')
            else:
                flash('El precio de venta tiene que ser mayor al de compra.', 'info')
                return redirect('/inventario')
        else:
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
        if request.method == 'POST':
            id_producto = request.form['txtID']
            nombre = request.form['nombre']
            categoria = request.form['categoria']
            precio_compra = request.form['precio_compra']
            precio_venta = request.form['precio_venta']
            cantidad = request.form['cantidad']

            InvProductos.editProducto([id_producto, nombre, categoria, precio_compra, precio_venta, cantidad])

            return redirect('/inventario')
        else:
            session['mensaje'] = "Lo sentimos hubo un error de seguridad."
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
@app.route('/categorias/agregarCategoria', methods=['POST'])
def agregarCategoria():
    if session.get("logueado") and (session.get("rol") == 'administrador' or session.get("rol") == 'super_admin'):
            # esto es para que cuando verifique si existe o no use el medoto post
        if request.method == 'POST':
            nombre = request.form['nombre']
            estado = 'activo'
            
            # hacer la consulta de las categorías existentes para esta consulta deje el GET
            categorias = InvProductos.consultaCataegorias()
            
            # esto verifica si el nombre de la categoría ya existe o no en la base de datos
            nombres_categorias = [categoria[1] for categoria in categorias]  # tomamos los nombres de las categorías
            
            if nombre in nombres_categorias: # aqui verificamos si existe si no existe ejecuta el agregar si existe le recarga la pagina
                session['mensaje'] = "La categoria ya existe en la base de datos"
                return redirect('/categorias')
            else  : 
                InvProductos.agregarCategoria([nombre, estado])
                return redirect('/categorias')
        else:
            session['mensaje'] = "Lo sentimos hubo un error de seguridad."
            return render_template('/categorias') 
    else:
        return redirect('/')
    
    

@app.route("/categorias")
def consultarCategoria():
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        mensaje = ''  # Inicializar mensaje como None por defecto
        if 'mensaje' in session:
            mensaje = session.pop('mensaje')
        resultado = InvProductos.consultaCataegorias()
        
        
        
        """ MODAL DE REGISTRO AFILIADOS DEL NABVAR """
        membresias = lasMembresias.consultarMembresias()


        fecha_actual = datetime.now()

        # fecha de nacimiento maxima (hace 16 años)
        fecha_maxima = fecha_actual - timedelta(days=(16 * 365))


        # fecha de nacimiento minima (hace 70 años)
        fecha_minima = fecha_actual - timedelta(days=(70 * 365))
        
        return render_template('dashboard/categoria_productos.html',mensaje = mensaje, categorias = resultado, resulMem = membresias, minima = fecha_minima, maxima = fecha_maxima)
    else:
        return redirect('/')
    
    

@app.route('/categorias/desactivarCategoria/<id_categoria>')
def desactivarCategoria(id_categoria):
    if session.get("logueado") and session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
        InvProductos.desactivarCategoria(id_categoria)
        return redirect('/categorias')
    else:
        return redirect('/')
