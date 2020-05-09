# getting ready to access the database test.db
import sqlite3


class Users:
    def __init__(self, _id, name, password):
        self.id = _id
        self.name = name
        self.password = password

    # method to retrieve the user when we know the user name
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        row = cursor.execute('select * from test where name=?', (name,)).fetchone()
        connection.close()
        if row:
            return cls(*row)
        else:
            return None


