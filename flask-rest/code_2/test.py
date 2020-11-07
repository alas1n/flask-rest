import sqlite3 

connection = sqlite3.connect('data.db')

crusor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
crusor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
crusor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'annie', 'xyz')
]
crusor.executemany(insert_query, users)

select_qurey = "SELECT * FROM users"
for row in crusor.execute(select_qurey):
    print(row)

connection.commit()

connection.close()