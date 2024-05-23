import fdb
import os


class DBCommand:
    """Class representing a DB commands"""
    # DB_PATH = os.path.join(os.getcwd(), 'MYDB.FDB')
    DB_PATH = 'C:\\Users\\admin\\Documents\\db\\DB\\MYDB.FDB'
    HOST = 'localhost'
    PASSWORD = 'root'
    USER = 'sysdba'

    def __init__(self):
        print('Initializing DB Command')
        self.conn = fdb.connect(
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            database=self.DB_PATH
        )
        self.cursor = self.conn.cursor()
        print(f'Connected to {self.DB_PATH}')

    def show_all_tables(self):
        self.cursor.execute("SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE RDB$SYSTEM_FLAG = 0")
        tables = self.cursor.fetchall()
        for table in tables:
            table_name = table[0]
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()
            print(f"Таблица: {table_name}")
            for row in rows:
                print(row)

    def show_table(self, table_name):
        print(table_name)
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def print_last_row(self, table_name):
        query = f"SELECT * FROM {table_name} ORDER BY ID DESC ROWS 1"

        self.cursor.execute(query)

        row = self.cursor.fetchone()

        if row:
            print("Последняя строка таблицы:")
            for value in row:
                print(value, end=' | ')
            print('\n')
        else:
            print("Таблица пуста")

    def add_rows(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
        columns = [desc[0] for desc in self.cursor.description]
        values = []
        for column in columns:
            value = input(f"Введите значение для поля {column}: ")
            values.append(value)

        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in range(len(columns))])})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def add_reception(self):
        self.print_last_row("RECEPTIONS")
        id_reception = int(input("Введите ID приема: "))
        self.show_table("CLIENT")
        id_client = int(input("Введите ID клиента: "))
        self.show_table("DOCTORS")
        id_doctor = int(input("Введите ID врача: "))
        self.show_table("PROCEDURE_CODE")
        procedure_code = int(input("Введите код процедуры: "))
        self.show_table("DIAGNOSIS")
        diagnosis = int(input("Введите ID диагноза: "))
        reception_date = input("Введите время приема (в формате 'YYYY-MM-DD HH:MM:SS'): ")

        try:
            query = f"INSERT INTO RECEPTIONS (ID, ID_CLIENT, ID_DOCTOR, PROCEDURE_CODE, DIAGNOSIS, RECEPTION_DATE) " \
                    f"VALUES ({id_reception}, {id_client}, {id_doctor}, {procedure_code}, {diagnosis}, '{reception_date}')"

            self.cursor.execute(query)

            self.conn.commit()
            print('Запись была успешно добавлена!')
        except Exception as e:
            print(f'Запись не добавлена, т.к. ошибка: {e}')

    def check_doctor(self):
        try:
            doctor_id = int(input('Введите id доктора'))
            self.cursor.execute("""
                SELECT *
                FROM RECEPTIONS
                WHERE ID_DOCTOR = ?
            """, (doctor_id))

            # Fetch all the rows returned by the query
            appointments = self.cursor.fetchall()

            # Print the appointments
            for appointment in appointments:
                print(appointment)
        except Exception as e:
            print('Произошла ошибка: ', e)
