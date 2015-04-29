import sqlite3

connection = sqlite3.connect("polyglot.db")
cursor = connection.cursor()

result = cursor.execute("SELECT id, language FROM languages")

for row in result:
    print(row)
