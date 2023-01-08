import random

def func_1():
    r_value = random.randint(0, 100)
    for i in range(1, 11):
        choice = int(input("Enter a number between 0 and 100 : "))
        if choice > r_value:
            print('Carry a smaller number')
        elif choice < r_value:
            print("Carry a larger number")
        else:
            print(f"you guessed the number with {i} attempts")
            break
        print(f'You have {10 - i} attempts left')
    else:
        print(f" Alas, you are no longer in demand. It was planned {r_value}")

func_1()