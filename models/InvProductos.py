from conexion import get_db_connection

class InventarioProductos:
    def __init__(self, miBD):
        self.conexion = miBD
        try:
            self.cursor = miBD.cursor()
        except AttributeError as e:
            print(f"Error al intentar conectar a la base de datos: {e}")

    # PRODUCTOS

    def consultarProductos(self):
        sql = "SELECT prod.id_productos, prod.nombre, cate.nombre, prod.precio_compra, prod.precio_venta, prod.cantidad FROM inventario_productos AS prod JOIN categoria_productos AS cate ON prod.id_categoria = cate.id_categoria WHERE prod.estado = 'activo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def agregarProducto(self, producto):
        sql = "INSERT INTO inventario_productos (nombre, id_categoria, precio_compra, precio_venta, cantidad, estado) VALUES (%s, %s, %s, %s, %s, %s);"
        valores = (producto[0], producto[1], producto[2], producto[3], producto[4], producto[5])
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def infoEditProducto(self, id_producto):
        sql = "SELECT prod.id_productos, prod.nombre, cate.nombre, prod.precio_compra, prod.precio_venta, prod.cantidad FROM inventario_productos AS prod JOIN categoria_productos AS cate ON prod.id_categoria = cate.id_categoria WHERE id_productos = %s;"
        self.cursor.execute(sql, (id_producto,))
        resultado = self.cursor.fetchall()
        return resultado

    def editProducto(self, producto):
        sql = "UPDATE inventario_productos SET nombre = %s, id_categoria = %s, precio_compra = %s, precio_venta = %s, cantidad = %s WHERE id_productos = %s;"
        valores = (producto[1], producto[2], producto[3], producto[4], producto[5], producto[0])
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def desactivarProductos(self, id_productos):
        sql = "UPDATE inventario_productos SET estado = 'inactivo' WHERE id_productos = %s"
        self.cursor.execute(sql, (id_productos,))
        self.conexion.commit()

    # CATEGORIAS

    def consultaCategorias(self):
        sql = "SELECT * FROM categoria_productos WHERE estado = 'activo'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def agregarCategoria(self, categoria):
        sql = "INSERT INTO categoria_productos (nombre, estado) VALUES (%s, %s)"
        valores = (categoria[0], categoria[1])
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def desactivarCategoria(self, id_categoria):
        sql = "UPDATE categoria_productos SET estado = 'inactivo' WHERE id_categoria = %s;"
        self.cursor.execute(sql, (id_categoria,))
        self.conexion.commit()

# Obtener la conexión a la base de datos
miBD = get_db_connection()

# Instanciar la clase InventarioProductos con la conexión
InvProductos = InventarioProductos(miBD)
