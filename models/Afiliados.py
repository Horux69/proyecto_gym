from conexion import get_db_connection

class Afiliados:
    def __init__(self, miBD):
        self.conexion = miBD
        self.cursor = self.conexion.cursor()

    def consultarAfiliados(self):
        sql = "SELECT registro_usuarios.*, membresias.nombre AS nombre_membresia FROM registro_usuarios JOIN membresias ON registro_usuarios.id_membresia = membresias.id_membresia;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarUsuariosPorEstadoMembresia(self):
        sql = "SELECT estado, COUNT(*) as cantidad FROM registro_usuarios GROUP BY estado;"
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        return resultados
    
    def agregarAfiliados(self, afiliados, user_registro):
        try:
            sql = "INSERT INTO registro_usuarios (cedula, nombre, apellido, fecha_nac, telefono, sexo, tipo_sangre, huella, nuemero_emergencia, correo, contrasena, leciones, id_membresia, fecha_inicio, fecha_vencimiento, fecha_registro, user_registro, estado, leciones_descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (afiliados[0], afiliados[1], afiliados[2], afiliados[3], afiliados[4], afiliados[5], afiliados[6], afiliados[7], afiliados[8], afiliados[9], afiliados[10], afiliados[11], afiliados[12], afiliados[13], afiliados[14], afiliados[15], user_registro, afiliados[16], afiliados[17])
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar usuario:", e)
            return False

    def validarDatosAfiliados(self, cedula, correo, telefono):
        consulta = "SELECT * FROM registro_usuarios WHERE cedula = %s OR correo = %s OR telefono = %s"
        valores = (cedula, correo, telefono)
        self.cursor.execute(consulta, valores)
        resultado = self.cursor.fetchall()
        return len(resultado) > 0
    
    def desactivarAfiliados(self, cedula):
        sql = "UPDATE registro_usuarios SET estado = 'inactivo' WHERE cedula = %s"
        self.cursor.execute(sql, (cedula,))
        self.conexion.commit()

    def infoAfiliados(self, cedula):
        sql = "SELECT * FROM registro_usuarios WHERE cedula = %s"
        self.cursor.execute(sql, (cedula,))
        resultado = self.cursor.fetchall()
        return resultado
    
    def desactivarUsuarios(self):
        sql = "UPDATE registro_usuarios SET estado = 'inactivo', id_membresia = 6 WHERE fecha_vencimiento <= DATE(NOW())"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def actualizarUsuarios(self, datos_nuevos):
        sql = "UPDATE registro_usuarios SET correo = %s, telefono = %s WHERE cedula = %s"
        valores = (datos_nuevos[1], datos_nuevos[2], datos_nuevos[0])
        self.cursor.execute(sql, valores)
        self.conexion.commit()
        
    def agregarMedidas(self, medidas, session):
        sql = "INSERT INTO medidas (cedula, user_registro, mes_registro, peso_corporal, bicep_derecho, bicep_izquierdo, pecho, antebrazo_derecho, antebrazo_izquierdo, cintura, cadera, muslo_derecho, muslo_izquierdo, pantorrilla_derecha, pantorrilla_izquierda) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (medidas[0], session, medidas[1], medidas[2], medidas[3], medidas[4], medidas[5], medidas[6], medidas[7], medidas[8], medidas[9], medidas[10], medidas[11], medidas[12], medidas[13])
        self.cursor.execute(sql, valores)
        self.conexion.commit()
    
    def actualizarMembresias_y_fechaInico(self, nuevMen):
        sql = "UPDATE registro_usuarios SET fecha_vencimiento = DATE_ADD(%s, INTERVAL %s DAY), fecha_inicio = %s, id_membresia = %s, estado = 'activo' WHERE cedula = %s"
        valores = (nuevMen[1], nuevMen[2], nuevMen[3], nuevMen[3], nuevMen[0])
        self.cursor.execute(sql, valores)
        self.conexion.commit()
    
    def actualizarMembresias(self, nuevMen):
        sql = "UPDATE registro_usuarios SET fecha_vencimiento = DATE_ADD(fecha_vencimiento, INTERVAL %s DAY), id_membresia = %s, estado = 'activo' WHERE cedula = %s"
        valores = (nuevMen[1], nuevMen[2], nuevMen[0])
        self.cursor.execute(sql, valores)
        self.conexion.commit()
    
    def actualizarContra(self, nuevContra):
        sql = "UPDATE registro_usuarios SET contrasena = %s WHERE cedula = %s"
        valores = (nuevContra[1], nuevContra[0])
        self.cursor.execute(sql, valores)
        self.conexion.commit()

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase Afiliados con la conexión
LosAfiliados = Afiliados(miBD)
