class Afiliados:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consultarAfiliados(self):
        sql = "SELECT registro_usuarios.*, membresias.nombre AS nombre_membresia FROM registro_usuarios JOIN membresias ON registro_usuarios.id_membresia = membresias.id_membresia WHERE registro_usuarios.estado = 'activo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
        
    
    def agregarAfiliados(self, afiliados, user_registro):
        sql = f"INSERT INTO registro_usuarios VALUES ('{afiliados[0]}','{afiliados[1]}','{afiliados[2]}','{afiliados[3]}','{afiliados[4]}','{afiliados[5]}','{afiliados[6]}','{afiliados[7]}','{afiliados[8]}','{afiliados[9]}','{afiliados[10]}','{user_registro}','{afiliados[11]}')"
        self.cursor.execute(sql)
        self.conexion.commit()


    def validarDatosAfiliados(self,cedula,correo,telefono):
        sql = f"SELECT * FROM operadores WHERE  cedula = '{cedula}' AND correo = '{correo}' AND telefono = '{telefono}'"
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
    
    def desactivarUsuarios(self):
        sql = "UPDATE registro_usuarios SET estado = 'inactivo' WHERE fecha_vencimiento <= DATE(NOW())"
        self.cursor.execute(sql)
        self.conexion.commit()
        
        
    def actualizarUsuarios(self,datos_nuevos):
        sql = f"UPDATE registro_usuarios SET correo = '{datos_nuevos[1]}', telefono = '{datos_nuevos[2]}' WHERE cedula = '{datos_nuevos[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def agregarMedidas(self,medidas,session):
       
        sql = f"INSERT INTO `medidas` (`Id`, `cedula`, `user_registro`, `mes_registro`, `peso_corporal`, `bicep_derecho`, `bicep_izquierdo`, `pecho`, `antebrazo_derecho`, `antebrazo_izquierdo`, `cintura`, `cadera`, `muslo_derecho`, `muslo_izquierdo`, `pantorrilla_derecha`, `pantorrilla_izquierda`) VALUES (NULL, '{medidas[0]}', '{session}', '{medidas[1]}', '{medidas[2]}', '{medidas[3]}', '{medidas[4]}', '{medidas[5]}', '{medidas[6]}', '{medidas[7]}', '{medidas[8]}', '{medidas[9]}', '{medidas[10]}', '{medidas[11]}', '{medidas[12]}', '{medidas[13]}');"
        self.cursor.execute(sql)
        self.conexion.commit()
        