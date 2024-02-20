class InventarioProductos:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    # PRODUCTOS

    def consultarProductos(self):
        sql = "SELECT prod.id_productos, prod.nombre, cate.nombre, prod.precio_compra, prod.precio_venta, prod.cantidad FROM inventario_productos AS prod JOIN categoria_productos AS cate ON prod.id_categoria = cate.id_categoria WHERE prod.estado = 'activo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregarProducto(self, producto):
        sql = f"INSERT INTO inventario_productos (nombre, id_categoria, precio_compra, precio_venta, cantidad, estado) VALUES ('{producto[0]}','{producto[1]}','{producto[2]}','{producto[3]}','{producto[4]}','{producto[5]}');"
        print(sql)
        self.cursor.execute(sql)
        self.conexion.commit()

    def infoEditProducto(self, id_producto):
        sql = f"SELECT prod.id_productos, prod.nombre, cate.nombre, prod.precio_compra, prod.precio_venta, prod.cantidad FROM inventario_productos AS prod JOIN categoria_productos AS cate ON prod.id_categoria = cate.id_categoria WHERE id_productos = '{id_producto}';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def editProducto(self, producto):
        sql = f"UPDATE inventario_productos SET nombre = '{producto[1]}', id_categoria = '{producto[2]}', precio_compra = '{producto[3]}', precio_venta = '{producto[4]}', cantidad = '{producto[5]}' WHERE id_productos = '{producto[0]}';"
        print(sql)
        self.cursor.execute(sql)
        self.conexion.commit()

    def desactivarProductos(self,id_productos):
        sql = f"UPDATE `inventario_productos` SET `estado`='inactivo' WHERE `id_productos` = '{id_productos}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    # CATEGORIAS

    def consultaCataegorias(self):
        sql=f"SELECT * FROM categoria_productos WHERE estado = 'activo'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

    def agregarCategoria(self, categoria):
        sql=f"INSERT INTO categoria_productos (nombre, estado) VALUES ('{categoria[0]}','{categoria[1]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def desactivarCategoria(self, id_categoria):
        sql = f"UPDATE categoria_productos SET estado = 'inactivo' WHERE id_categoria = '{id_categoria}';"
        print(sql)
        self.cursor.execute(sql)
        self.conexion.commit()