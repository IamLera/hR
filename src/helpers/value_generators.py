import random

from faker import Faker
from datetime import datetime


class Generators:

    @staticmethod
    def stringGenerator():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d%m%y")

        return f'py-{Faker().word()}-{formatted_time}'

    @staticmethod
    def emailGenerator():
        return Faker().email()

    @staticmethod
    def lastNameGenerator():
        return f'Py{Faker().last_name()}'

    @staticmethod
    def firstNameGenerator():
        return f'Py{Faker().first_name()}'

    @staticmethod
    def phoneGenerator():
        a = random.randint(100, 999)
        b = random.randint(100, 999)
        c = random.randint(1000, 9999)
        return f'({a}) {b}-{c}'
