import messages
import os

from commands import *


def start_program():
    print('''База данных. \n\nВыберите роль: \n
администратор
врач
выйти
''')

    while True:
        role = str(input(">>>  ")).lower().strip()

        match role:
            case 'администратор':
                os.system('cls' if os.name == 'nt' else 'clear')
                administrator()
            case 'врач':
                os.system('cls' if os.name == 'nt' else 'clear')
                doctor()
            case 'выйти':
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
            case _:
                print('Повторите попытку')


def doctor():
    messages.print_doctor()
    command = 0
    while True:
        try:
            command = int(input(">>>  "))
        except ValueError:
            print('Вы ввели не числовой формат')

        match command:
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')

                print('Посмотреть записи')
            case 11:
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
            case _:
                print('Повторите попытку')


def administrator():
    messages.print_administrator()
    command = 0
    while True:
        try:
            command = int(input(">>>  "))
        except ValueError:
            print('Вы ввели не числовой формат')

        match command:
            case 1:
                add_command('CLIENT')
            case 2:
                show_command('CLIENT')
            case 3:
                add_command('DOCTORS')
            case 4:
                show_command('DOCTORS')
            case 5:
                add_command('HEALING')
            case 6:
                show_command('HEALING')
            case 7:
                add_command('MEDICINES')
            case 8:
                show_command('MEDICINES')
            case 9:
                add_command('DIAGNOSIS')
            case 10:
                show_command('DIAGNOSIS')
            case 11:
                add_command('PROCEDURE_CODE')
            case 12:
                show_command('PROCEDURE_CODE')
            case 13:
                add_command('SPECIALITY_CODE')
            case 14:
                show_command('SPECIALITY_CODE')
            case 15:
                add_reception()
            case 16:
                show_command('RECEPTIONS')
            case 17:
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
            case _:
                print('Повторите попытку')
        administrator()


if __name__ == '__main__':
    start_program()
