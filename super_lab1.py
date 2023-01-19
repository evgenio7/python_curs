while True:
    s = input("Ввести любе значення : ")
    def check_int(s):
        if all(s == '0' for s in s) and len(s) > 0:
            print('Вы ввели ноль ', end=' ')
            return s
        elif s.isdigit():
            print('Вы ввели положительное целое число ', end=' ')
            return s
        elif s.lstrip('-').isdigit():
            print('Вы ввели отрицательное число: ', end=' ')
            return s
        elif s.replace('.','',1).isdigit() or s.replace(',','',1).isdigit():
            print(" Вы ввели дробное число: ", end=' ')
            return s
        elif s.lstrip('-').replace('.','',1).isdigit() or s.lstrip('-').replace(',','',1).isdigit():
            if s.count('-') == 1:
                print("Вы ввели отрицательное дробное число: ", end=' ')
                return s
            else:
                print("Вы ввели не корректное число: ", end=' ')
                return s
        else:
            print("Вы ввели не корректное число: ", end=" ")
            return s

    print(check_int(s))
    answer = input("Желаете выйти? (Д/Y)  выход, exit, quit, e или q :")
    if answer.upper() in ('Y', 'Д', "ВЫХОД", "EXIT", "QUIT", "E", "Q"):
        break

