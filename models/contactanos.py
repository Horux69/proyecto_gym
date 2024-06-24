from conexion import get_db_connection

class Contactanos:
    def __init__(self, miBD):
        self.conexion = miBD
        self.cursor = self.conexion.cursor()

    def consultaDatosgym(self):
        sql = "SELECT id_contacto, nombre_gym, telefono_gym, correo_gym, direccion_gym, barrio_gym, ubicacion_gym FROM contacto_gym WHERE id_contacto = 1"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def agregarDatosgym(self, nombre, telefono, correo, direccion, barrio, ubicacion):
        try:
            sql = "INSERT INTO contacto_gym (nombre_gym, telefono_gym, correo_gym, direccion_gym, barrio_gym, ubicacion_gym) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (nombre, telefono, correo, direccion, barrio, ubicacion)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar datos del gimnasio:", e)
            return False
    
    def actualizarDatosgym(self, identificacion, nombre, telefono, correo, direccion, barrio, ubicacion):
        try:
            sql = "UPDATE contacto_gym SET nombre_gym = %s, telefono_gym = %s, correo_gym = %s, direccion_gym = %s, barrio_gym = %s, ubicacion_gym = %s WHERE id_contacto = %s"
            valores = (nombre, telefono, correo, direccion, barrio, ubicacion, identificacion)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al actualizar datos del gimnasio:", e)
            return False

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase Contactanos con la conexión
Datoscontacto = Contactanos(miBD)
