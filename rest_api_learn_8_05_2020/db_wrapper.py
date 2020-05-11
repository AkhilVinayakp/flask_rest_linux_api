import sqlite3


class Db_wrap():
    def __init__(self):
        self.connection = sqlite3.connect('test.db')
        self.cursor = self.connection.cursor()

    def add_table(self):
        sql = 'CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except sqlite3.Error as e:
            return 1, str(e)
        return 0


    def __del__(self):
        self.connection.close()
