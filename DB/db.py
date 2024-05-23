import fdb
import os

from executes import *
from db_command import *


def create_and_delete_db(db_path):
    try:
        if os.path.exists(db_path):
            os.remove(db_path)

        conn = fdb.create_database(host='localhost',
                                   user='sysdba',
                                   password='root',
                                   database=db_path)
        return conn
    except Exception as e:
        print('Произошла ошибка... Проверьте host, user, password и путь к БД\n', e)


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
    cursor.execute(table_diagnosis_healing)

    conn.commit()
    cursor.close()


def insert_table_db(conn):
    cursor = conn.cursor()
    documents_and_db = {
        'SPECIALITY_CODE': 'speciality_code.txt',
        'PROCEDURE_CODE': 'procedure_code.txt',
        'MEDICINES': 'medicines.txt',
        'HEALING': 'healing.txt',
        'HEALING_MEDICINE': 'healing_medicine.txt',
        'DOCTORS': 'doctors.txt',
        'DIAGNOSIS': 'diagnosis.txt',
        'DIAGNOSIS_HEALING': 'diagnosis_healing.txt',
        'CLIENT': 'client.txt',
    }
    for db, file_name in documents_and_db.items():
        path_to_file = os.path.join(os.getcwd(), 'data\\', file_name)
        cursor.execute(f"SELECT * FROM {db} WHERE 1=0")
        columns = [desc[0] for desc in cursor.description]
        with open(path_to_file, 'r', encoding='UTF-8') as f:
            try:
                values = f.readlines()
                for value in values:
                    value = value.split('|')
                    for i in range(len(value)):
                        try:
                            value[i] = int(value[i])
                        except ValueError:
                            continue

                    query = f"INSERT INTO {db} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in range(len(columns))])})"
                    cursor.execute(query, value)
                    conn.commit()
            except Exception as e:
                print('Произошла ошибка: ', e)


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
    insert_table_db(conn)
    db = DBCommand()
    db.show_all_tables()

    conn.close()


if __name__ == "__main__":
    main()
