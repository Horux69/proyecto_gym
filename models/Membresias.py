from conexion import get_db_connection

class Membresias:
    def __init__(self, miBD):
        self.conexion = miBD
        try:
            self.cursor = miBD.cursor()
        except AttributeError as e:
            print(f"Error al intentar conectar a la base de datos: {e}")

    def consultarMembresias(self):
        sql = "SELECT * FROM membresias WHERE estado = 'activo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultaTiempoMembresia(self, id_membresia):
        sql = f"SELECT tiempo_duracion FROM membresias WHERE id_membresia = {id_membresia}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()[0]
        return resultado

    def agregarMembresia(self, membresias):
        try:
            sql = "INSERT INTO membresias (nombre, tiempo_duracion, precio, estado) VALUES (%s, %s, %s, %s)"
            valores = (membresias[0], membresias[1], membresias[2], membresias[3])
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar membresia:", e)
            return False

    def desactivarMembresia(self, id_membresia):
        sql = f"UPDATE membresias SET estado = 'inactivo' WHERE id_membresia = {id_membresia};"
        self.cursor.execute(sql)
        self.conexion.commit()

    def infoMembresia(self, id_membresia):
        consulta = f"SELECT * FROM membresias WHERE id_membresia = {id_membresia};"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        return resultado

    def editMembresia(self, membresia):
        sql = f"UPDATE membresias SET nombre = '{membresia[1]}', tiempo_duracion = '{membresia[2]}', precio = '{membresia[3]}' WHERE id_membresia = '{membresia[0]}';"
        self.cursor.execute(sql)
        self.conexion.commit()

    def consultaDias(self, dia):
        sql = f"SELECT tiempo_duracion FROM membresias WHERE id_membresia = {dia}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        return resultado

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase Membresias con la conexión
lasMembresias = Membresias(miBD)
