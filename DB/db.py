import fdb
import os

from executes import *


def create_and_delete_db(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = fdb.create_database(host='localhost',
                               user='sysdba',
                               password='root',
                               database=db_path)
    return conn


def create_table_db(conn):
    cursor = conn.cursor()

    cursor.execute(table_speciality_code)
    cursor.execute(table_doctor)
    cursor.execute(table_client)
    cursor.execute(table_medicines)
    cursor.execute(table_healing)
    cursor.execute(table_diagnosis)
    cursor.execute(table_procedure_code)
    cursor.execute(table_reception)
    cursor.execute(table_healing_medicines)

    conn.commit()
    cursor.close()


def show_table_db(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE RDB$SYSTEM_FLAG = 0")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT RDB$FIELD_NAME FROM RDB$RELATION_FIELDS WHERE RDB$RELATION_NAME = '{table_name}'")
        columns = cursor.fetchall()
        print(f"Таблица: {table_name}")
        for column in columns:
            print(column[0], end='')
        print('\n')

    cursor.close()


def main():
    db_path = os.path.join(os.getcwd(), 'MYDB.FDB')

    conn = create_and_delete_db(db_path)
    create_table_db(conn)
    show_table_db(conn)

    conn.close()


if __name__ == "__main__":
    main()
