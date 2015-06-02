import sqlite3
import sql_manager
import random
import smtplib
import string
from money_and_email import connect, withdraw_money, get_balance, get_email, set_email, show_email, change_password_query
from settings import DATABASE_NAME
from querries import WITHDRAW_MONEY, GET_MONEY_AMMOUNT, CHANGE_PASSWORD, SET_EMAIL, GET_EMAIL_QUERY
import getpass as gp
from sending_settings import RECEIVER_EMAIL ,SENDER_EMAIL, SENDER_PASSWORD, SERVER, PORT



def wrapped_reset_password(logged_user):
    new_pass = generate_new_password()
    change_password_query(logged_user.get_username(),
                          sql_manager.hash_them_things(new_pass))
    send_reset_password(get_email(logged_user.get_username()), new_pass)

def wrapped_withdraw(logged_user):
    ammount =  float(input("Please select ammount of money you would like to withdraw: "))
    balance = get_balance(logged_user.get_username())
    if ammount > balance:
        print("Can't withdraw more than you have...")
    else:
        withdraw_money(logged_user.get_username(), balance-ammount)
        print("Money successfully withdrawn!")


def wrapped_deposit(logged_user):
    deposit = float(input("Enter the ammount you would like to deposit: "))
    if deposit <= 0:
        print("Please enter positive value: ")
    else:
        balance = get_balance(logged_user.get_username())
        withdraw_money(logged_user.get_username(), balance + deposit)
        print("Money deposited successfully!")




def print_username_password():
    username = input("Enter your username: ")
    password = gp.getpass(prompt="Enter your password: ")
    return {"username": username,
            "password": password
            }

def print_help():
    print("login - for logging in!")
    print("register - for creating new account!")
    print("exit - for closing program!")

def print_info():
    print("You are: " + logged_user.get_username())
    print("Your id is: " + str(logged_user.get_id()))
    print("Your balance is:" + str(logged_user.get_balance()) + '$')

def print_all_commands():
    print("info - for showing account info")
    print("changepass - for changing passowrd")
    print("change-message - for changing users message")
    print("show-message - for showing users message")


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            result = print_username_password()
            username = result['username']
            password = result['password']
            inp = sql_manager.register(username, password)
            if inp == True:
                print("Registration Successfull")
            else:
                print(inp['reason'])
        elif command == 'login':
            result = print_username_password()
            username = result['username']
            password = result['password']

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print_help()
        elif command == 'exit':
            break
        else:
            print("Not a valid command")





def send_reset_password(receiver, new_password):
    TO = receiver
    SUBJECT = "New password"
    TEXT = "Your new passowrd is  {}".format(new_password)
    server = smtplib.SMTP(SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, [TO], TEXT)


def generate_new_password():
    n = random.randint(15, 20)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))

def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")


        if command == 'info':
            print_info()
        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            inp = sql_manager.change_pass(new_pass, logged_user)
            if inp == True:
                print("Password changed sucessfully!!")
            else:
                print(inp['reason'])
        elif command == 'reset-password':
            wrapped_reset_password(logged_user)
        elif command == 'set-email':
            mail = input("Please enter your email: ")
            set_email(logged_user.get_username(), mail)

        elif command == 'show-email':
            print(show_email(logged_user.get_username()))

        elif command == 'show-balance':
            print("Current balance is: {}".format(get_balance(logged_user.get_username())))

        elif command == 'withdraw':
            wrapped_withdraw(logged_user)
        elif command == 'deposit':
            wrapped_deposit(logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == "logout":
            return

        elif command == 'help':
            print_all_commands()

def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
