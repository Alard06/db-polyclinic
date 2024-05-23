from DB.db_command import *


def db_command():
    db = DBCommand()
    return db


def add_command(table):
    os.system('cls' if os.name == 'nt' else 'clear')
    db = db_command()
    try:
        db.print_last_row(table)
        db.add_rows(table)
    except fdb.fbcore.DatabaseError as e:
        print(20 * '!!!!!')
        print(f'Произошла ошибка при добавлении записи... \n{e}')


def show_command(table):
    db = db_command()
    os.system('cls' if os.name == 'nt' else 'clear')
    db.show_table(table)


def add_reception():
    db = db_command()
    db.add_reception()


def check_doctor():
    db = db_command()
    db.check_doctor()