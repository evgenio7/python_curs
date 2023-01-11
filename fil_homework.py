
inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

def politrem(i):
    i = str(i).casefold()
    if i == i[::-1]:
        return True
    else:
        return False

d = list(filter(politrem, inputdata))

print(d)
