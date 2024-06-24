from datetime import datetime
from conexion import get_db_connection

class Operadores:
    def __init__(self, miBD):
        self.conexion = miBD
        try:
            self.cursor = miBD.cursor()
        except AttributeError as e:
            print(f"Error al intentar conectar a la base de datos: {e}")

    def consultaOperadores(self):
        sql = "SELECT usuario, nombre, apellido, cedula, telefono, correo, rol, fecha_registro, user_registro, estado FROM operadores"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def validarDatosOpe(self, usuario, cedula, correo, celular):
        consulta = f"SELECT * FROM operadores WHERE usuario = '{usuario}' AND correo = '{correo}' AND cedula = '{cedula}' AND telefono = '{celular}'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        return len(resultado) > 0

    def agregarOperador(self, operadores, user_registro):
        try:
            fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = f"INSERT INTO operadores (usuario, nombre, apellido, cedula, telefono, correo, contrasena, rol, fecha_registro, user_registro, estado) VALUES ('{operadores[0]}', '{operadores[1]}', '{operadores[2]}', '{operadores[3]}', '{operadores[4]}', '{operadores[5]}', '{operadores[6]}', '{operadores[7]}', '{fecha_actual}', '{user_registro}', '{operadores[8]}')"
            self.cursor.execute(sql)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar operador:", e)
            return False

    def desactivarOpe(self, usuario, usuarioDelete):
        fecha_delete = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f"UPDATE `operadores` SET `estado`='inactivo', delete_at = '{fecha_delete}', delete_by = '{usuarioDelete}' WHERE `usuario` = '{usuario}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def eliminarOpe(self, usuario):
        sql = f"DELETE FROM operadores WHERE usuario = '{usuario}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def infoOperadores(self, usuario):
        consulta = f"SELECT * FROM operadores WHERE usuario = '{usuario}'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        return resultado

    def actualizarContra(self, nuevContra):
        sql = f"UPDATE operadores SET contrasena = '{nuevContra[1]}' WHERE cedula = '{nuevContra[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase Operadores con la conexión
losOperadores = Operadores(miBD)
