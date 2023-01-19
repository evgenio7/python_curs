
a = input('Enter string1 : ')
b = input('Enter string2 : ')
c = input('Enter string3 : ')
d = input('Enter string4 : ')



with open('word.txt', 'w') as f:
    f.write(a)
    f.write('\n')
    f.write(b)
    f.write('\n')

try:
    f = open('word.txt', 'a')
    f.write(c)
    f.write('\n')
    f.write(d)
finally:
    f.close()





