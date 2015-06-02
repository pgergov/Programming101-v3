from querries import WITHDRAW_MONEY, GET_MONEY_AMMOUNT, CHANGE_PASSWORD, SET_EMAIL, GET_EMAIL_QUERY
import sqlite3


def connect():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn, cursor

def withdraw_money(username, ammount):
    conn, cursor = connect()
    cursor.execute(WITHDRAW_MONEY, (ammount, username))
    conn.commit()

def get_balance(username):
    conn, cursor = connect()
    return cursor.execute(GET_MONEY_AMMOUNT, (username,)).fetchone()['balance']

def get_email(username):
    conn, cursor = connect()
    data = cursor.execute(GET_EMAIL_QUERY, (username,)).fetchone()
    return data['email']

def set_email(username, email):
    conn, cursor = connect()
    cursor.execute(SET_EMAIL, (email, username))
    conn.commit()

def show_email(username):
    return get_email(username)

def change_password_query(username, password):
    conn, cursor = connect()
    cursor.execute(CHANGE_PASSWORD, (password, username))
    conn.commit()
