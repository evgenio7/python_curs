s_file = open('laba1.txt', 'w')

enter_word_first, enter_word_second = map(str, input("enter the two words : ").split())

print(enter_word_first, enter_word_second, file=s_file)

y = (enter_word_first.upper()[::-1], enter_word_second.capitalize()[::-1])
print('! {0[0]} {0[1]} ?'.format(y), file=s_file)
print('! %s %s ?' % y, file=s_file)
print(f'! {y[0]} {y[1]} ?', file=s_file)


