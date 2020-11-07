import sqlite3 

connection = sqlite3.connect('data.db')

crusor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXIST users (id INTEGER PRIMARY KEY, username text, password text)"
crusor.execute(create_table)

connection.commit()

connection.close()



