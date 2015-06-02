DATABASE_NAME = "bank.db"

WITHDRAW_MONEY = '''
UPDATE clients
SET balance = ?
WHERE username = ?
'''

GET_MONEY_AMMOUNT = '''
SELECT balance
FROM clients
WHERE username = ?
'''

CHANGE_PASSWORD = '''
UPDATE clients
SET password = ?
WHERE username = ?
'''
SET_EMAIL = '''
UPDATE clients
SET email = ?
WHERE username = ?
'''
GET_EMAIL_QUERY = '''
SELECT email
FROM clients
WHERE username = ?
'''
