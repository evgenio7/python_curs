import datetime
from data import Data
from person import Person

def main():
    data = Data()
    while True:
        print('1. Load data from file')
        print('2. Save data to file')
        print('3. Add new person')
        print('4. Search person')
        print('5. Quit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            file_name = input('Enter file name: ')
            data.load_data(file_name)
        elif choice == 2:
            file_name = input('Enter file name: ')
            data.save_data(file_name)
        elif choice == 3:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name (optional): ')
            patronymic = input('Enter patronymic (optional): ')
            birth_date = datetime.datetime.strptime(input('Enter birth date (YYYY-MM-DD): '), '%Y-%m-%d').date()
            death_date = input('Enter death date (optional, YYYY-MM-DD): ')
            if death_date:
                death_date = datetime.datetime.strptime(death_date, '%Y-%m-%d').date()
            gender = input('Enter gender (optional): ')
            person = Person(first_name, last_name, patronymic, birth_date, death_date, gender)
            data.add_person(person)
        elif choice == 4:
            first_name = input('Enter first name: ')
            results = data.search_person(first_name)
            if results:
                for person in results:
                    print(f'Name: {person.first_name} {person.last_name} {person.patronymic}')
                    print(f'Birth Date: {person.birth_date}')
                    print(f'Death Date: {person.death_date}')
                    print(f'Gender: {person.gender}')
                    print(f'Age: {person.calculate_age()}')
                    print()
            else:
                print('No results found\n')
        else:
            break


if __name__ == '__main__':
    main()
