
def count_time(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@count_time
def new_function():
    a = 2 + 4
    print('a =', a)
new_function()

print("*"*50)

@count_time
def new():
    a = 2 + ((4 * 5 / 6) **2)**5
    print('a =', a)
new()