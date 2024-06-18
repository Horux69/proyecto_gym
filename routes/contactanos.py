from conexion import *
from flask import session, redirect, request, render_template
from models.contactanos import Datoscontacto


@app.route('/contacto')
def contacto():
    
    contacto_gym =Datoscontacto.consultaDatosgym()
    
    return render_template('dashboard/contactanos.html',contacto_gym = contacto_gym)




@app.route('/contactanos/agregar', methods = ['POST'])
def agregarDatosgym():
    
    if session.get("logueado") and session.get("rol") == 'super_admin':
    
        if request.method == 'POST': 
            nombre= request.form['nombre_gym']
            telefono = request.form['telefono_gym']
            correo= request.form['correo_gym']
            direccion= request.form['direccion_gym']
            barrio= request.form['barrio_gym']
            ubicacion = request.form['ubicacion_gym']
            
            Datoscontacto.agregarDatosgym(nombre,telefono,correo,direccion,barrio,ubicacion)
            return redirect('/contacto')
            
        else:
            return redirect('/contacto')
    
    else:
        
        return redirect('/')
    
@app.route('/contactanos/actualizar', methods=['POST'])
def actualizarDatosgym():
    if session.get("logueado") and  session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
    
        if request.method == 'POST':
            identificacion_=request.form['id_contacto']
            nombre_= request.form['nombre_gym']
            telefono_ = request.form['telefono_gym']
            correo_= request.form['correo_gym']
            direccion_= request.form['direccion_gym']
            barrio_= request.form['barrio_gym']
            ubicacion_ = request.form['ubicacion_gym']
            
            Datoscontacto.actualizarDatosgym(identificacion_,nombre_,telefono_,correo_,direccion_,barrio_,ubicacion_)
    
            return redirect('/contacto')
        else:
            return redirect('/contacto')    
            
            
    else:
        return redirect('/')