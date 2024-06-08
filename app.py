from flask import render_template
from flaskext.mysql import MySQL
from routes.login import validaLogin
from routes.afiliados import afiliados
from routes.inventario import inventario
from routes.membresias import membresias
from routes.operadores import consultaOperadores
from models.Afiliados import LosAfiliados
from routes.rutinas import rutinas
from routes.contactanos import Datoscontacto
from conexion import *


LosAfiliados.desactivarUsuarios() #funcion de desactivar usuarios

@app.route('/')
def login():
    return render_template('auth/login.html')

