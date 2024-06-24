from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
app.secret_key = "digitalforge"

def get_db_connection():
    mydb = mysql.connector.connect(
        host='localhost', 
        user='root',
        password='', 
        database='gym_control'
    )
    return mydb

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errores/404.html'), 404

def inicializador_app():
    app.register_error_handler(404, pagina_no_encontrada)
    return app
