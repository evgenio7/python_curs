
while True:
    insert_name = input("Enter name : ")
    insert_age = input("Enter age : ")

    if not insert_age.isdigit() or int(insert_age) <= 0:
        print("“Ошибка, повторите ввод”")
        continue

    if int(insert_age) < 10:
        print(f"“Привет, шкет #{insert_name}#”;")
    elif int(insert_age) <= 18:
        print(f"“Как жизнь #{insert_name}#?”")
    elif int(insert_age) < 100:
        print(f"“Что желаете #{insert_name}#?”")
    else:
        print(f"“#{insert_name}#, вы лжете - в наше время столько не живут...”")

    answer = input("Желаете выйти? (Д/Y) ")

    if answer.upper() in ('Y', 'Д'):
        break
