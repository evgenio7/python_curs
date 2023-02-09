import datetime


class Person:
    def __init__(self, first_name, last_name=None, patronymic=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
