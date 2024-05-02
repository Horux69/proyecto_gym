from datetime import datetime
from conexion import *

class Operadores:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consultaOperadores(self):
        sql = "SELECT usuario, nombre, apellido, cedula, telefono, correo, rol, fecha_registro, user_registro, estado FROM operadores"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def validarDatosOpe(self, usuario, cedula, correo, celular):
        consulta = f"SELECT * FROM operadores WHERE usuario = '{usuario}' AND correo = '{correo}' AND cedula = '{cedula}' AND telefono = '{celular}'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
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
        self.conexion.commit()
        return resultado
        
losOperadores = Operadores(mysql)

