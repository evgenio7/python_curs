import pandas as pd
from person import Person


class Data:
    def __init__(self):
        self.people = []

    def load_data(self, file_name):
        df = pd.read_excel(file_name)
        for index, row in df.iterrows():
            person = Person(
                first_name=row['first_name'],
                last_name=row['last_name'],
                patronymic=row['patronymic'],
                birth_date=row['birth_date'],
                death_date=row['death_date'],
                gender=row['gender']
            )
            self.people.append(person)

    def save_data(self, file_name):
        data = []
        for person in self.people:
            data.append({
                'first_name': person.first_name,
                'last_name': person.last_name,
                'patronymic': person.patronymic,
                'birth_date': person.birth_date,
                'death_date': person.death_date,
                'gender': person.gender,
                'age': person.calculate_age()
            })
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)

    def add_person(self, person):
        self.people.append(person)

    def search_person(self, first_name):
        results = []
        for person in self.people:
            if person.first_name == first_name:
                results.append(person)
        return results
