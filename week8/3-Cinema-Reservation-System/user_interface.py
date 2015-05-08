import sqlite3
from prettytable import PrettyTable

db = sqlite3.connect("cinema_data.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def show_movies(call=True):
    table = PrettyTable(["ID", "Title", "Rating"])
    info = cursor.execute("SELECT id, movie_name, movie_rating FROM Movies")
    for row in info:
        table.add_row([row["id"], row["movie_name"], row["movie_rating"]])
    print("Current movies:\n")
    print(table)
    if call:
        main()


def show_movie_projections(movie_id, date=None, call=True):
    printed = False
    table = PrettyTable(["ID", "Date", "Starting_hour", "Type"])
    info = cursor.execute("""SELECT Projections.id, projection_type,
                                    projection_date, projection_time,
                                    movie_id, movie_name
                             FROM Projections
                             JOIN Movies
                             ON Projections.movie_id = Movies.id
                             WHERE movie_id = ?""", str(movie_id))
    for row in info:
        if not printed:
            print("Projections for movie '{}':".format(row["movie_name"]))
            printed = True
        table.add_row([row["id"], row["projection_date"],
                      row["projection_time"], row["projection_type"]])
    print(table)
    if call:
        main()


def make_reservation():
    username = input("Step 1 (User): Choose name> ")
    number_of_tickets = input("Step 1 (User): Choose number of tickets> ")

    show_movies(call=False)

    movie_id = input("Step 2 (Movie): Choose a movie ID> ")
    show_movie_projections(movie_id, call=False)

    projection_id = input("Step 3 (Projection): Choose a projection ID> ")
    take_available_seats()

    choose_seat(username, projection_id, number_of_tickets)
    main()


def take_available_seats():
    seats = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]
    take_row_col = """
    SELECT row, col FROM Reservations
    """
    info = cursor.execute(take_row_col)

    for row in info:
        seats_row = row['row']
        seats_col = row['col']
        seats[seats_row][seats_col] = 'X'

    print("  1    2    3    4    5    6    7    8    9    10")
    for i in range(0, len(seats)):
        print(seats[i])


def take_seat(username, projection_id, row, col):
    take_row_col = """
    SELECT row, col FROM Reservations
    """
    info = cursor.execute(take_row_col)

    for line in info:
        seats_row = line['row']
        seats_col = line['col']
        if row == seats_row and col == seats_col:
            print ('Lol...NO!')
            return False

    cursor.execute("""
    INSERT INTO Reservations(username, projection_id, row, col)
    VALUES(?, ?, ?, ?)
    """, (username, str(projection_id), str(row), str(col)))
    db.commit()
    return True


def choose_seat(username, projection_id, number):
    counter = 1
    seats = []
    number = int(number)
    while number > 0:
        print ('Step 4 (Seats): Choose seat {}>'. format(counter))
        row = int(input("Choose row: ")) - 1
        col = int(input("Choose col: ")) - 1
        if take_seat(username, projection_id, row, col):
            number -= 1
            counter += 1
            seats.append((row + 1, col + 1))
    else:
        info = cursor.execute("""
        SELECT projection_type, projection_date, projection_time,
        movie_name, movie_rating
        FROM Projections
        JOIN Movies
        ON Projections.movie_id = Movies.id
        WHERE Projections.id = ?
        """, str(projection_id))
        db.commit()
        for row in info:
            print ('This is your reservation:')
            print ('Movie: {} ({})'.format(
                row['movie_name'], row['movie_rating']))
            print ('Date and Time: {} ({})'.format(
                row['projection_date'], row['projection_type']))
            print ('Seats: {}'. format(seats))


def cancel_reservation(name):
    cursor.execute("DELETE FROM Reservations WHERE username = ?", (name, ))
    db.commit()
    main()


def exit():
    pass


def commands_help():
    print("You can use the following commands:\nshow_movies\n\
show_movie_projections <movie_id> [<date>]\nmake_reservation\n\
cancel_reservation <name>\nexit\nhelp")
    main()


def main():
    command = input("command>: ")
    try:
        command1 = command.split()[0]
        command2 = command.split()[1]
    except:
        pass
    if command1 not in commands:
        print("Your command is not valid.\n\
Try using <help> to see all the available commadns.")
        main()
    else:
        try:
            commands[command1](command2)
        except:
            commands[command1]()

commands = {
           "show_movies": show_movies,
           "show_movie_projections": show_movie_projections,
           "make_reservation": make_reservation,
           "cancel_reservation": cancel_reservation,
           "exit": exit,
           "help": commands_help
           }

if __name__ == '__main__':
    main()
