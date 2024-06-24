from conexion import *

class ValidationLogin:
    def __init__(self, miBD):
        self.conexion = miBD
        try:
            self.cursor = miBD.cursor()
        except AttributeError as e:
            print(f"Error al intentar conectar a la base de datos: {e}")

    def validaLogin(self, usuario, password):
        consulta = f"SELECT nombre, usuario, contrasena, rol, estado FROM operadores WHERE usuario = '{usuario}' AND contrasena = '{password}' AND estado = 'activo'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase ValidationLogin con la conexión
validaLogin = ValidationLogin(miBD)

