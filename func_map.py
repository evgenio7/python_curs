values = [1, 2, '3', 'forth', 'end', 99, True, None]

def func_map(lst):
    return list(map(lambda x: str(x) if type(x) == int else x, lst))

result = func_map(values)
print(result)