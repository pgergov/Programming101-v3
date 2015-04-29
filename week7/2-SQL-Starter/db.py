import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()
create_users_table = """
CREATE TABLE IF NOT EXISTS
users(id INTEGER PRIMARY KEY, age int, email TEXT, gender TEXT)
"""
cursor.execute(create_users_table)
db.commit()
