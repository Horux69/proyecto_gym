from flask import session, redirect, request, render_template, jsonify, flash,send_from_directory
from conexion import *
from models.rutinas import LasRutinas
import os
from datetime import datetime


carpeta_up = os.path.join('static\imagenes_rutinas')
app.config['carpeta_up'] = carpeta_up

@app.route('/imagenes_rutinas/<nombre>')
def imagenes_rutinas(nombre):
    return send_from_directory(app.config['carpeta_up'],nombre)



@app.route('/rutinas')
def rutinas():
    
    resultado_tipos = LasRutinas.consultaTipos()
    
    return render_template('dashboard/rutinas.html', resulTipos = resultado_tipos)


@app.route('/rutinas/agregar', methods = ['POST'])
def agregarRutinas():
    
    if session.get("logueado") and session.get("rol") == 'entrenador' or session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
    
        if request.method == 'POST': 
        
            nombre = request.form['nombre']
            repeticiones = request.form['repeticiones']
            series = request.form['series']
            tipo = request.form['tipo']
            imagen = request.files['Foto']
            
            
            "Guardar la foto"
            ahora = datetime.now()
            tiempo = ahora.strftime("%Y%m%d%H%M%S")
            nom,extension = os.path.splitext(imagen.filename)
            nombre_foto = "Foto" + "-" + tiempo + "-" + extension
            imagen.save("static/imagenes_rutinas/"+nombre_foto)
            
            LasRutinas.agregarEjercicios([nombre, repeticiones, series, tipo, nombre_foto])
            
            return redirect('/rutinas')
            
        else:
            return redirect('/rutinas')
    
    else:
        return redirect('/')
    
    
@app.route('/rutinas/agregar/tipos', methods = ['POST'])
def agregarTipos():
    
    if session.get("logueado") and session.get("rol") == 'entrenador' or session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
    
        if request.method == 'POST': 
            
            nombre = request.form['NombreTipo']
            
            LasRutinas.agregarTipos(nombre)
            
            return redirect('/rutinas')
            
        else:
                return redirect('/rutinas')
    
    else:
        return redirect('/')
    