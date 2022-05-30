from db_con import db_con


class product():
    def __init__(self, id=None, nombre='', marca='', referencia='', precio=0, descuento=0):
        """Modelo de producto
        Args:
            id (int): codigo del producto_
            nombre (str): nombre del producto
            marca (str): marca del producto
            referencia (str): modelo del producto
            precio (float): precio del producto
            descuento (float): % de descuento en decimal
        """
        self.con = db_con()
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.referencia = referencia
        self.precio = precio
        self.descuento = descuento

    def add_product(self, id, nombre, marca, referencia, precio, descuento):

        query = f'''
                INSERT INTO products 
                    (id, nombre, marca, referencia, precio, descuento)
                VALUES 
                    ({id},'{nombre}', '{marca}', '{referencia}', {precio}, {descuento})
                '''
        self.con.insert_data(query)

    def del_product(self, id):
        query = f'''
                DELETE FROM products
                WHERE id = {id}
                '''
        self.con.insert_data(query)

    def list_products(self):

        data = self.con.get_data('''SELECT * FROM products
                            ''')

        return self._factory_dict(data)

    def search_pattern(self, patron):
        data = self.con.get_data(f'''
                    SELECT * FROM products  
                    WHERE nombre LIKE "%{patron}%"
                ''')
        return self._factory_dict(data)

    def _factory_dict(self, data):
        data_list = []
        for rows in data:
            d = {}
            for i, col in enumerate(['id', 'nombre', 'marca', 'referencia', 'precio', 'descuento']):
                d[col] = rows[i]
            data_list.append(d)
        return data_list


if __name__ == '__main__':
    prod = product()
    print(prod.search_pattern(''))
