from flask import render_template
import mysql.connector
from routes.login import validaLogin
from routes.afiliados import afiliados
from routes.inventario import inventario
from routes.membresias import membresias
from routes.operadores import consultaOperadores
from models.Afiliados import LosAfiliados
from routes.rutinas import rutinas
from routes.contactanos import Datoscontacto
from conexion import *



@app.route('/')
def login():
    return render_template('auth/login.html')

