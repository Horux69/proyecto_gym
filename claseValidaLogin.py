class ValidationLogin:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def validaLogin(self, usuario, password):
        consulta = f"SELECT nombre, usuario, contrasena, rol, estado FROM operadores WHERE usuario = '{usuario}' AND contrasena = '{password}' AND estado = 'activo'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado