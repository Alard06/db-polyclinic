table_doctor = """
        CREATE TABLE DOCTORS (
ID INTEGER NOT NULL PRIMARY KEY,
FIO VARCHAR(50),
TELEPHONE VARCHAR(13),
SPECIALITY_CODE INTEGER,
FOREIGN KEY (SPECIALITY_CODE) REFERENCES SPECIALITY_CODE(ID)
);"""

table_speciality_code = """
        CREATE TABLE SPECIALITY_CODE (
ID INTEGER NOT NULL PRIMARY KEY,
SPECIALITY_CODE VARCHAR(30),
NAME VARCHAR(40)
);"""


table_procedure_code = """
        CREATE TABLE PROCEDURE_CODE (
ID INTEGER NOT NULL PRIMARY KEY,
NAME VARCHAR(50),
DESCRIPTION VARCHAR(300),
PRICE INTEGER
);"""

table_diagnosis = """
 CREATE TABLE DIAGNOSIS (
ID INTEGER NOT NULL PRIMARY KEY,
NAME VARCHAR(30)
);
"""

table_diagnosis_healing = """
CREATE TABLE DIAGNOSIS_HEALING (
ID_DIAGNOSIS INTEGER REFERENCES DIAGNOSIS(ID),
ID_HEALING INTEGER REFERENCES HEALING(ID)
);
"""

table_healing = """
        CREATE TABLE HEALING (
ID INTEGER NOT NULL PRIMARY KEY,
DESCRIPTION VARCHAR(300),
RECOMMENDATION VARCHAR(300)
);"""

table_healing_medicines = """
CREATE TABLE HEALING_MEDICINE (
ID_MEDICINE INTEGER NOT NULL REFERENCES MEDICINES(ID),
ID_HEALING INTEGER NOT NULL REFERENCES HEALING(ID)
)
"""

table_client = """
        CREATE TABLE CLIENT (
ID INTEGER NOT NULL PRIMARY KEY,
FIO_PARENTS VARCHAR(50),
FIO_CHILDREN VARCHAR(50),
TELEPHONE VARCHAR(13),
MED_POLIS VARCHAR(30)
);"""

table_medicines = """
        CREATE TABLE MEDICINES (
ID INTEGER NOT NULL PRIMARY KEY,
NAME VARCHAR(50),
DESCRIPTION VARCHAR(300),
RECOMMENDATION VARCHAR(300),
CONTRAINDICATION VARCHAR(300)
);"""

table_reception = """
CREATE TABLE RECEPTIONS (
ID INTEGER NOT NULL PRIMARY KEY,
ID_CLIENT INTEGER REFERENCES CLIENT (ID),
ID_DOCTOR INTEGER REFERENCES DOCTORS (ID),
PROCEDURE_CODE INTEGER REFERENCES PROCEDURE_CODE(ID),
DIAGNOSIS INTEGER REFERENCES DIAGNOSIS(ID),
RECEPTION_DATE TIMESTAMP 
);
"""

