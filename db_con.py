import sqlite3


class db_con():

    def __init__(self) -> None:
        self.db = '.\\data\\products.db'

    def connect(self):
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()

    def insert_data(self, query):
        self.connect()
        with self.con:
            self.cur.execute(query)
            self.con.commit()
        if self.con:
            self.con.close()

    def get_data(self, query):
        self.connect()
        with self.con:
            self.cur.execute(query)
            data = self.cur.fetchall()
        if self.con:
            self.con.close()
        return data
