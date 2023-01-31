class My_str(str):

    def __add__(self, other):
        return f'{str(self)}{str(other)}'

    def __sub__(self, other):
        x = str(other)
        y = str(self)
        return y.replace(x, '', 1)

a = My_str('New')
b = a + '890'
print(type(b))
print(b)
print("*" * 40)
a = My_str(1234)
b = a + 5678
print(type(b))
print(b)
print("*" * 40)
a = My_str('New')
b = a + 'castle'
print(type(b))
print(b)
print("*" * 40)
a = My_str('New')
b = a + 77
print(type(b))
print(b)
print("*" * 40)
a = My_str('New')
b = a + True
print(type(b))
print(b)
print("*" * 40)
a = My_str('New')
b = a + ['s', ' ', 23]
print(type(b))
print(b)
print("*" * 40)

a = My_str(557234567)
b = a - 7
print(type(b))
print(b)
print("*" * 40)
a = My_str('New bala7nce')
b = a - 7
print(type(b))
print(b)
print("*" * 40)
a = My_str('New balance')
b = a - 'Bal'
print(type(b))
print(b)
print("*" * 40)
a = My_str('pineapple apple pine')
b = a - "apple"
print(type(b))
print(b)
print("*" * 40)



