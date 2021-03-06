class MissingDataException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} is missing!'

class PhoneNumberFormatException(Exception):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.phone_number} is invalid!'

class EmailFormatException(Exception):

    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f'{self.email} is invalid!'

class Worker:

    def __init__(self, id, name, address, phone_number, email):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f'{self.id},{self.name},{self.address},{self.phone_number},{self.email}'

    def __eq__(self, other):
        if isinstance(other, Worker):
            return self.id == other.id
        else:
            return 'Nem osszehasonlithato'

    def __lt__(self, other):
        if isinstance(other, Worker):
            return self.id < other.id
        else:
            return 'Nem osszehasonlithato'

    def __le__(self, other):
        if isinstance(other, Worker):
            return self.id <= other.id
        else:
            return 'Nem osszehasonlithato'

    def __gt__(self, other):
        if isinstance(other, Worker):
            return self.id > other.id
        else:
            return 'Nem osszehasonlithato'

    def __ge__(self, other):
        if isinstance(other, Worker):
            return self.id >= other.id
        else:
            return 'Nem osszehasonlithato'