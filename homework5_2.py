numer = int(input("Enter number : "))
summa = 0
while numer > 0:
    if numer % 3 != 0:
        summa += numer ** 3
    numer -= 1
else:
    print("Normal result")

print(f'Resultat: {summa}')

