user_text = input('Введите ФИО: ')
full_name = user_text.split()
a,b,c = full_name
name = list(b)
patronymic = list(c)

del name[1::1]
del patronymic [1::1]
d = ''.join(name)
e = ''.join(patronymic)

print(a, d+'.', e +'.' + ' <---- Фамилия и инициалы')

