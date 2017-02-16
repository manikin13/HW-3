import sqlite3
connection = sqlite3.connect('database.db')
print('Opened database sucessfully');
connection.execute('CREATE TABLE food (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
print('Table created sucessfully');
connection.close()
