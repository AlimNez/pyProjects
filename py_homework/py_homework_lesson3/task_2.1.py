a = input('Слово № 1: ')
b = input('Слово № 2: ')
c = input('Слово № 3: ')
slova =[a, b, c]
print(f'Массив слов: --->  + {slova}')

dlin_slovo = ''
for slovo in slova:
    if len(slovo) > len(dlin_slovo):
        dlin_slovo = slovo
print('Самое длинное слово: ---> ' + dlin_slovo)
