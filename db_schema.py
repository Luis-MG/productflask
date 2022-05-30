from db_con import db_con
import csv


class db_schema():

    def __init__(self) -> None:
        self.con = db_con()
        self.drop_tables()
        self.create_tables()
        # self.get_tables()
        with open('.\\data\\bkp\\productos.csv') as doc:
            csvreader = csv.reader(doc, delimiter=',')
            self.populate_tables(csvreader)
        self.get_allproducts()

    def drop_tables(self):
        self.con.insert_data('''
                             DROP TABLE IF EXISTS products
                             ''')

    def create_tables(self):
        self.con.insert_data('''
                             CREATE TABLE IF NOT EXISTS products (
                                 id INTEGER PRIMARY KEY,
                                 nombre TEXT,
                                 marca TEXT,
                                 referencia TEXT,
                                 precio REAL,
                                 descuento REAL                                 
                             )
                             ''')

    def get_tables(self):
        data = self.con.get_data('''SELECT name FROM sqlite_schema
                                WHERE type='table'
                                ORDER BY name;
                            ''')
        for dat in data:
            print(dat)

    def populate_tables(self, csvdata):
        for row in csvdata:
            self.con.insert_data(f'''
                            INSERT INTO products 
                                (id, nombre, marca, referencia, precio, descuento)
                            VALUES 
                                ({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', {row[4]}, {row[5]})''')

    def get_allproducts(self):
        data = self.con.get_data('''SELECT * FROM products
                            ''')
        for dat in data:
            print(dat)


if __name__ == '__main__':
    db_schema()
