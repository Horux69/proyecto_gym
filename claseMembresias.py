class Membresias:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consultarMembresias(self):
        sql = "SELECT * FROM membresias WHERE estado = 'activo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def consultaTiempoMembresia(self, id_membresia):
        sql = f"SELECT tiempo_duracion FROM membresias WHERE id_membresia = {id_membresia}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()[0]
        return resultado
    
    def agregarMembresia(self, membresias):
        sql = f"INSERT INTO membresias (id_membresia, nombre, tiempo_duracion, precio, estado) VALUES ('NULL', '{membresias[0]}','{membresias[1]}','{membresias[2]}','{membresias[3]}');"
        self.cursor.execute(sql)
        self.conexion.commit()

    def desactivarMembresia(self, id_membresia):
        sql = f"UPDATE membresias SET estado = 'inactivo' WHERE id_membresia = {id_membresia};"
        self.cursor.execute(sql)
        self.conexion.commit()

    def infoMembresia(self, id_membresia):
        consulta = f"SELECT * FROM membresias WHERE id_membresia = {id_membresia};"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def editMembresia(self, membresia):
        sql = f"UPDATE membresias SET nombre = '{membresia[1]}', tiempo_duracion = '{membresia[2]}', precio = '{membresia[3]}' WHERE id_membresia = '{membresia[0]}';"
        self.cursor.execute(sql)
        self.conexion.commit()