import sqlite3

db = sqlite3.connect("company.db")
cursor = db.cursor()

create_company_table = """
CREATE TABLE IF NOT EXISTS
users(id INTEGER PRIMARY KEY, name TEXT,
      monthly_salary int, yearly_bonus int, position TEXT)
"""
users = [
        ("Ivan Ivanov", 5000, 10000, "Software Developer"),
        ("Rado Rado", 500, 0, "Technical Support internn"),
        ("Ivo Ivo", 10000, 100000, "CEO"),
        ("Petar Petrov", 3000, 1000, "Marketing Manager"),
        ("Maria Georgieva", 8000, 10000, "COO")]
cursor.execute(create_company_table)
cursor.executemany(""" INSERT INTO users(
name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)""", users)
db.commit()
