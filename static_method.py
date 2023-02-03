from datetime import date
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def BirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

persona1 = Persona('mayank', 21)
persona2 = Persona.BirthYear('mayank', 1996)

print(persona1.age)
print(persona2.age)

print(Persona.isAdult(22))