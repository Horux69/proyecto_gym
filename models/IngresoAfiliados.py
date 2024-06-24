from conexion import get_db_connection
import mysql.connector

class IngresoAfiliados:
    def __init__(self, miBD):
        self.conexion = miBD
        self.cursor = self.conexion.cursor()

    def agregarIngresoAfiliado(self, id_afiliado, fecha_ingreso):
        try:
            sql = "INSERT INTO ingreso_usuarios (id_usuario, fecha_ingreso) VALUES (%s, %s)"
            valores = (id_afiliado, fecha_ingreso)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar usuario:", e)
            return False
    
    def consultarHorasConcurridas(self):
        sql = "SELECT HOUR(fecha_ingreso) AS hora, COUNT(*) AS cantidad FROM ingreso_usuarios GROUP BY HOUR(fecha_ingreso) ORDER BY HOUR(fecha_ingreso);"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        datos_por_hora = {row[0]: row[1] for row in rows}
        return datos_por_hora

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase IngresoAfiliados con la conexión
losIngresoAfiliados = IngresoAfiliados(miBD)
