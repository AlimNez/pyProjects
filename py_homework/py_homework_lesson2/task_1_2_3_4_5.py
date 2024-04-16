# Задача 1 и 2
user_text = input('Введите строку: ')
user_text = user_text.lower().replace('h' , 'H')
print(user_text + ' <---- Задача 2 - замена "h" на "H" ')
print(user_text[::-1], ' <---- Вот это поворот! - Задача 1')

# Задача 3,4,5
user_text1 = user_text + ' '
user_text1.split()
a = user_text1.split()

b,c = a
b,c = c,b
print(b,c + ' <---- Задача 5(переставил слова местами)')

count_1 = user_text1.count(' ')
print('Задача 3 - Количество слов с строке с методом split ---> ' + str(count_1))

user_text = user_text + ' '
count = user_text.count(' ')
print('Задача 4 -Количество слов с строке без метода split ---> ' + str(count))



