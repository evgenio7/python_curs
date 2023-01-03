value_first = 1
result = 0
insert_num = int(input("Enter number: "))

for x in range(value_first, insert_num+1):
    if x % 3 != 0:
        result += x ** 3

print(f'Res: {result}')