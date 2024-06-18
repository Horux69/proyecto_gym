from conexion import *

class Contactanos:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
        
        
    def consultaDatosgym(self):
        sql = "SELECT id_contacto,nombre_gym,telefono_gym,correo_gym,direccion_gym, barrio_gym,ubicacion_gym FROM contacto_gym WHERE id_contacto = 1"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

        
    def agregarDatosgym(self,nombre,telefono,correo,direccion,barrio,ubicacion):
        sql= f"INSERT INTO contacto_gym(nombre_gym, telefono_gym, correo_gym, direccion_gym, barrio_gym, ubicacion_gym) VALUES ('{nombre}','{telefono}','{correo}','{direccion}','{barrio}','{ubicacion}');"
        self.cursor.execute(sql)
        self.conexion.commit()
    
    def actualizarDatosgym(self,identificacion_,nombre_,telefono_,correo_,direccion_,barrio_,ubicacion_):
        sql= f"UPDATE contacto_gym SET nombre_gym='{nombre_}',telefono_gym='{telefono_}',correo_gym='{correo_}',direccion_gym='{direccion_}',barrio_gym='{barrio_}',ubicacion_gym='{ubicacion_}' WHERE id_contacto = '{identificacion_}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
        
Datoscontacto = Contactanos(mysql)   