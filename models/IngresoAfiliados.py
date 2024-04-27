from conexion import *

class IngresoAfiliados:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def agregarIngresoAfiliado(self, id_afiliado, fecha_ingreso):
        try:
            sql = f"INSERT INTO `ingreso_usuarios` (id_usuario, fecha_ingreso) VALUES ('{id_afiliado}', '{fecha_ingreso}')"
            self.cursor.execute(sql)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar usuario:", e)
            return False
    
    def consultarHorasConcurridas(self):
        sql = "SELECT HOUR(fecha_ingreso) AS hora, COUNT(*) AS cantidad FROM ingreso_usuarios GROUP BY HOUR(fecha_ingreso) ORDER BY HOUR(fecha_ingreso);"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.conexion.commit()
        datos_por_hora = {row[0]: row[1] for row in rows}
        return datos_por_hora
        
    

IngresoAfiliados = IngresoAfiliados(mysql)