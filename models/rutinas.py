from conexion import get_db_connection

class Rutinas:
    
    def __init__(self, miBD):
        self.conexion = miBD
        try:
            self.cursor = miBD.cursor()
        except AttributeError as e:
            print(f"Error al intentar conectar a la base de datos: {e}")

    def consultaTipos(self):
        sql = "SELECT * FROM tipos_entrenamiento"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def agregarEjercicios(self, ejercicio):
        sql = f"INSERT INTO `ejercicios` (`contador_ejercicio`, `nombre_ejercicio`, `repeciones`, `series`, `tipo`, `img`) VALUES (NULL, '{ejercicio[0]}', '{ejercicio[1]}', '{ejercicio[2]}', '{ejercicio[3]}', '{ejercicio[4]}');"
        self.cursor.execute(sql)
        self.conexion.commit()

    def agregarTipos(self, tipo):
        sql = f"INSERT INTO `tipos_entrenamiento` (`id_tipo`, `tipo_entrenamiento`) VALUES (NULL, '{tipo}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def cedulaCliente(self):
        sql = "SELECT `registro_usuarios`.`cedula` FROM registro_usuarios"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def Id_rutina(self):
        sql = "SELECT id_rutina, nombre FROM creador_rutina"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def Rutina_cliente(self, rutina):
        sql = f"INSERT INTO `rutina_cliente` (`id_rutina`, `cliente`, `dia`) VALUES ('{rutina[0]}', '{rutina[1]}', '{rutina[2]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def creador_rutina(self, creador_rutina):
        sql = f"INSERT INTO `creador_rutina` (`id_rutina`, `duracion`, `descripcion`) VALUES (NULL, '{creador_rutina[0]}', '{creador_rutina[1]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase Rutinas con la conexión
LasRutinas = Rutinas(miBD)
