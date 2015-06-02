import sqlite3
from Client import Client
from settings import DATABASE_FILE
import hashlib

conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

CREATE_QUERY = '''create table if not exists
    clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            email TEXT,
            balance REAL DEFAULT 0,
            message TEXT)'''

CHECK_IF_USER_EXISTS = '''
SELECT username
FROM clients
WHERE username=?
'''


UPDATE_SQL = "UPDATE clients SET message = ? WHERE id = ?"
UPDATE_SQL_PASSWORD = "UPDATE clients SET password = ? WHERE id = ?"
INSERT_SQL = "insert into clients (username, password) values (?, ?)"

NUMBERS = ['0', '1', '2', '3',
           '4', '5', '6', '7',
           '8', '9']


def test_for_strong_password(username ,password):
    to_str = str(password)
    if len(to_str) < 8:
        return {"state": False,
                "reason": "Password too short!"}
    if to_str.lower() == to_str:
        return {"state": False,
                "reason": "No uppercase letter found!"}

    if username in password:
        return {"state": False, 
                "reason": "Username in password!"
                }
        
    for number in NUMBERS:
        if number in to_str:
            return {"state": True,
                    "reason": "All good!"}
    return {"state": False,
            "reason": "No number found in password"
            }

def hash_them_things(thing):
    hash_object = hashlib.sha512(thing.encode())
    return hash_object.hexdigest()
def executor(update_sql, tple):
    cursor.execute(update_sql, tple)
    conn.commit()
    

def check_if_username_exists(username):
    pass

def create_clients_table():
    cursor.execute(CREATE_QUERY)


def change_message(new_message, logged_user):
    tple = (new_message, logged_user.get_id())
    executor(UPDATE_SQL, tple)
    logged_user.set_message(new_message)

def change_pass(new_pass, logged_user):
    test = test_for_strong_password(logged_user, new_pass)
    if test['state']:
        tple = (new_pass, logged_user.get_id())
        executor(UPDATE_SQL_PASSWORD, tple)
        return True
    else:
        return test
def register(username, password):
    test = test_for_strong_password(username, password)
    if test['state']:
        cursor = conn.cursor()
        row = cursor.execute(CHECK_IF_USER_EXISTS, (username,)).fetchall()
        if not len(row):
            tple = (username, hash_them_things(password))
            executor(INSERT_SQL, tple)
            return True
        else:
            return {'reason': "Username already exists",
                    'state': False}
    else:
        return test
def login(username, password):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1" 
    tple = (username, hash_them_things(password))
    
    cursor.execute(select_query, tple)
    user = cursor.fetchone()
    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
