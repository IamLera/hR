import random

from faker import Faker
from datetime import datetime


class Generators:

    @staticmethod
    def stringGeneratorMarked():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d%m%y")

        return f'py-{Faker().word()}-{formatted_time}'

    @staticmethod
    def stringGenerator():
        return f'Py{Faker().word()}'

    @staticmethod
    def emailGenerator():
        return Faker().email()

    @staticmethod
    def lastNameGenerator():
        return f'Py{Faker().last_name()}'

    @staticmethod
    def lastFirstGenerator():
        return f'Py{Faker().first_name()}'

    @staticmethod
    def firstNameGenerator():
        return f'Py{Faker().first_name()}'

    @staticmethod
    def phoneGenerator():
        a = random.randint(100, 999)
        b = random.randint(100, 999)
        c = random.randint(1000, 9999)
        return f'({a}) {b}-{c}'

    @staticmethod
    def numberGenerator(length):
        range_start = 10 ** (length - 1)
        range_end = (10 ** length) - 1
        return random.randint(range_start, range_end)

    @staticmethod
    def birthdayGenerator():
        return Faker().date_of_birth(minimum_age=21).strftime("%Y-%m-%d")
