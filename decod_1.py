
data = b'r\xc3\xa9sum\xc3\xa9'
print(data)
print('*' *40)
data_str = data.decode()
print(data_str)
print('*' *40)
data_latin = data_str.encode("Latin1")
print(data_latin)
print('*' *40)
data_str_lat = data_latin.decode('Latin1')
print(data_str_lat)