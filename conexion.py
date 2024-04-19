from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)

app.secret_key = "digitalforge"

# AGREGAR UN CONTROL DE TIEMPO DE LA SESION, (SOLO SI ES REQUERIDO)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'gym_control2'

mysql.init_app(app)

conexion = mysql.connect()
cursor = conexion.cursor()

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializador_app():
    app.register_error_handler(404, pagina_no_encontrada)
    return app