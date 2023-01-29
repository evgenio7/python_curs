class Auto(object):
    color = "White"
    weight = '3 T'



    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("move")

    def birthday(self):
        return self.age + 1

    def stop(self):
        print("stop")


y = Auto('asd', 23, 'zxczxcz')
print(y.move())
print(y.birthday())
print(y.stop())
print(y.color)
