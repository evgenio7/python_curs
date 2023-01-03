
dict = {'x':'cat', 'y':'dog', 'b':'duck', 'k':'lol', 'v':'wolf'}
print(dict)
dict = {x: y for y, x in dict.items()}
print(dict)