import math

class Calc:
    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mnogenya(self, a, b):
        return a * b

    def dilenya(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")

    def exponentiate(self, a, b):
        try:
            if b < 0:
                raise NegativeExponentError("Exponent cannot be negative")
            return a ** b
        except NegativeExponentError:
            print("Exponent cannot be negative")

    def square_root(self, a):
        try:
            if a < 0:
                raise NegativeNumberError("Square root of negative number not defined")
            return math.sqrt(a)
        except NegativeNumberError:
            print("Square root of negative number not defined")

class NegativeExponentError(Exception):
    pass

class NegativeNumberError(Exception):
    pass

calc = Calc()
print(calc.plus(2, 3))
print(calc.minus(5, 2))
print(calc.mnogenya(3, 4))
print(calc.dilenya(6, 2))
print(calc.exponentiate(2, 3))
print(calc.square_root(9))