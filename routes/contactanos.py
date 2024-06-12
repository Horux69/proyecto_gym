from conexion import *
from flask import session, redirect, request, render_template
from models.contactanos import Datoscontacto


@app.route('/contacto')
def contacto():
    
    contacto_gym =Datoscontacto.consultaDatosgym()
    
    return render_template('dashboard/contactanos.html',contacto_gym = contacto_gym)




@app.route('/contactanos/agregar', methods = ['POST'])
def agregarDatosgym():
    
    if session.get("logueado") and  session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
    
        if request.method == 'POST': 
            
            nombre_gym = request.form['nombre_gym']
            telefono_gym = request.form['telefono_gym']
            correo_gym = request.form['correo_gym']
            ubicacion_gym = request.form['ubicacion_gym']
            barrio_gym = request.form['barrio_gym']
            direccion_gym = request.form['direccion_gym']
            
            Datoscontacto.agregarDatosgym([nombre_gym,telefono_gym,correo_gym,direccion_gym,barrio_gym,ubicacion_gym])
            return redirect('/contacto')
            
        else:
            return redirect('/contacto')
    
    else:
        
        return redirect('/')
    
    
@app.route('/contactanos/actualizar', methods=['POST'])
def actualizarDatosgym():
    if session.get("logueado") and  session.get("rol") == 'administrador' or session.get("rol") == 'super_admin':
    
        if request.method == 'POST':
            
            id_contacto = request.form['id_contacto']
            nombre_gym = request.form['nombre_gym']
            telefono_gym = request.form['telefono_gym']
            correo_gym = request.form['correo_gym']
            ubicacion_gym = request.form['ubicacion_gym']
            barrio_gym = request.form['barrio_gym']
            direccion_gym = request.form['direccion_gym']
            
            Datoscontacto.actualizarDatosgym([id_contacto,nombre_gym,telefono_gym,correo_gym,ubicacion_gym,barrio_gym,direccion_gym])
            return redirect('/contacto')
        else:
            return redirect('/contacto')    
            
            
    else:
        return redirect('/')     