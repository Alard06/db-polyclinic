class SpecialityCode:
    """Constructor for SpecialityCode class"""

    def __init__(self, name, speciality_code):
        self.name = name
        self.speciality_code = speciality_code

    def __str__(self):
        return self.name + " " + self.speciality_code


class Doctor:
    """Constructor for doctor class"""

    def __init__(self, id_doctor, fio, telephone, speciality_code):
        self.id_doctor = id_doctor
        self.fio = fio
        self.telephone = telephone
        self.speciality_code = speciality_code

    def __str__(self):
        return f'{str(self.id_doctor)}: {self.fio}, {self.telephone}, {self.speciality_code}'


class Client:
    """Constructor for client class"""

    def __init__(self, id_client, fio_parents, fio_children, telephone, med_polis):
        self.id_client = id_client
        self.fio_parents = fio_parents
        self.fio_children = fio_children
        self.telephone = telephone
        self.med_polis = med_polis

    def __str__(self):
        return f'{self.id_client}, {self.fio_parents}, {self.fio_children}, {self.telephone}, {self.med_polis}'


class Diagnosis:
    """Constructor for diagnosis class"""

    def __init__(self, id_diagnosis, name, healing):
        self.id_diagnosis = id_diagnosis
        self.name = name
        self.healing = healing

    def __str__(self):
        return f'{self.id_diagnosis}, {self.name}, {self.healing}'


class Healing:
    """Constructor for Healing class"""

    def __init__(self, id_healing, description, recommendation, medicines):
        self.id_healing = id_healing
        self.description = description
        self.recommendation = recommendation
        self.medicines = medicines

    def __str__(self):
        return f'{self.id_healing}, {self.description}, {self.recommendation}, {self.medicines}'


class Medicines:
    """Constructor for Medicines class"""

    def __init__(self, name, description, recommendation, contraindication):
        self.name = name
        self.description = description
        self.recommendation = recommendation
        self.contraindication = contraindication

    def __str__(self):
        return f'{self.name}, {self.description}, {self.recommendation}, {self.contraindication}'


class Reception:
    """Constructor for Reception class"""

    def __init__(self, id_client, id_doctor, procedure_code, diagnosis, time):
        self.id_client = id_client
        self.id_doctor = id_doctor
        self.procedure_code = procedure_code
        self.diagnosis = diagnosis
        self.time = time

    def __str__(self):
        return f'{self.id_client}, {self.id_doctor}, {self.procedure_code}, {self.diagnosis}, {self.time}'
