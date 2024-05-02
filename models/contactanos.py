from conexion import *

class Contactanos:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
        
        
    def consultaDatosgym(self):
        sql = "SELECT id_contacto,nombre_gym,telefono_gym,correo_gym,direccion_gym, barrio_gym,hubicacion_gym FROM contacto_gym"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

        
    def agregarDatosgym(self,contacto):
        sql= f"INSERT INTO `contacto_gym` (`id_contacto`, `nombre_gym`, `telefono_gym`, `correo_gym`, `direccion_gym`, `barrio_gym`, `hubicacion_gym`) VALUES (NULL, '{contacto[0]}', '{contacto[1]}', '{contacto[2]}', '{contacto[3]}', '{contacto[4]}', '{contacto[5]}');"
        self.cursor.execute(sql)
        self.conexion.commit()
    
    def actualizarDatosgym(self,datoscontacto):
        sql= f"UPDATE `contacto_gym` SET `nombre_gym`='{datoscontacto[1]}', `telefono_gym`='{datoscontacto[2]}', `correo_gym`='{datoscontacto[3]}', `direccion_gym`='{datoscontacto[4]}', `barrio_gym`='{datoscontacto[5]}', `hubicacion_gym`='{datoscontacto[6]}' WHERE id_contacto ='{datoscontacto[0]}' "
        self.cursor.execute(sql)
        self.conexion.commit()
        
        
Datoscontacto = Contactanos(mysql)   