
'''
Перша умова.
  Создать 3 переменные одного и тоже типа с одинаковыми данными и с одинаковым id.
'''
print("Перша Умова \n")
a = 45
b = a
c = b

print(a == b == c)
print(a is b is c)

print(type(a))
print(id(a))
print(type(b))
print(id(b))
print(type(c))
print(id(c), '\n')

'''
Друга умова. 
  Создать 2 переменные одного и тоже типа с одинаковыми данными и с разными id.
'''
print("Друга Умова \n")

x = 23
y = x
print(x == y)
y += 1
print(x is y)

print(type(x))
print(id(x))
print(type(y))
print(id(y), '\n')

'''
Третя умова. 
  3*. Поменять их типы так, чтобы у 1-х трёх стали разные id, но при этом остались одинаковые данные (и одинаковый тип), 
  а у 2-х последних стали одинаковые id и остались одинаковые данные (и одинаковый тип).
'''
print("Третя Умова \n")

a = 45
b = a
c = b

print(a == b == c)
b += 1
c += 2
print(a is b is c)

print(type(a))
print(id(a))
print(type(b))
print(id(b))
print(type(c))
print(id(c))


x = 23
y = x
print(x == y)
print(x is y)

print(type(x))
print(id(x))
print(type(y))
print(id(y))