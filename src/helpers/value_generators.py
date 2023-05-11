from faker import Faker
from datetime import datetime


class Generators:

    @staticmethod
    def stringGenerator():

        current_time = datetime.now()
        formatted_time = current_time.strftime("%d%m%y")

        return f'py-{Faker().word()}-{formatted_time}'
