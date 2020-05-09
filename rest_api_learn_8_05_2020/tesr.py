# creating a sqlite3  database and connect using python
import sqlite3
connection = sqlite3.connect('test.db')
cursor = connection.cursor()
'''
sql_string = "create table test (id int primary key, name varchar(24), password varchar(22))"
cursor.execute(sql_string)

data = (1, 'ravi', 'ravi123')

cursor.execute(sql_string, data)

# executing the sql commands commands one by one
sql_string = "insert into test values(?,?,?)"
users= [
    (2,'gopi','gopi123'),
    (3, 'ravi2', 'ravi342'),
    (4, 'gopik', 'gopika123')
]
cursor.executemany(sql_string, users)


connection.commit()
'''
for row in cursor.execute('select * from test'):
    print(row[0])
connection.close()
