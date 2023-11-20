class Afiliados:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consultarAfiliados(self):
        sql = "SELECT * FROM registro_usuarios WHERE estado = 'activo'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregarAfiliados(self, afiliados, user_registro):
        sql = f"INSERT INTO registro_usuarios VALUES ('{afiliados[0]}','{afiliados[1]}','{afiliados[2]}','{afiliados[3]}','{afiliados[4]}','{afiliados[5]}','{afiliados[6]}','{afiliados[7]}','{afiliados[8]}','{afiliados[9]}','{afiliados[10]}','{user_registro}','{afiliados[11]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    
    def validarDatosAfiliados(self,cedula):
        sql = f"SELECT * FROM operadores WHERE  cedula = '{cedula}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return len(resultado) > 0
    
    def desactivarAfiliados(self,cedula):
        sql = f"UPDATE registro_usuarios SET `estado`='inactivo' WHERE `cedula` = '{cedula}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def infoAfiliados(self, cedula):
        sql = f"SELECT * FROM registro_usuarios WHERE cedula = '{cedula}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado