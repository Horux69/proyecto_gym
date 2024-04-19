from conexion import *

class Rutinas:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
        
    def consultaTipos(self):
        sql = "SELECT * FROM tipos_entrenamiento"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregarEjercicios(self, ejercicio):
        
        sql = f"INSERT INTO `ejercicios` (`contador_ejercicio`, `nombre_ejercicio`, `repeciones`, `series`, `tipo`, `img`) VALUES (NULL, '{ejercicio[0]}', '{ejercicio[1]}', '{ejercicio[2]}', '{ejercicio[3]}', '{ejercicio[4]}');"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def agregarTipos(self, tipo):
        
        sql = f"INSERT INTO `tipos_entrenamiento` (`id_tipo`, `tipo_entrenamiento`) VALUES (NULL, '{tipo}')"
        self.cursor.execute(sql)
        self.conexion.commit()
    
    
LasRutinas = Rutinas(mysql)