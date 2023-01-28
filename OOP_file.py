class Auto(object):
    color = "White"
    weight = '3 T'


    def __init__(self, brand=None, age=0, mark=None):
        self.brand = brand
        self.mark = mark
        self.age = age

    def move(self):
        print("move")

    def birthday(self):
        return self.age + 1

    def stop(self):
        print("stop")


class Truck(Auto):

    def __init__(self, brand=None, age=0, mark=None, max_load='attention'):
        super().__init__(brand, age, mark)
        self.max_load = max_load


    def move(self):
        print(self.max_load)
        print("move")

    def load(self):
        from time import sleep
        for i in range(2):
            sleep(1)
            print("load")

class Car(Auto):
    max_speed = '<max_speed>'
    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")
x = Truck()
print(x.move())

y = Truck()

print(y.load())

c = Car()
print(c.move())