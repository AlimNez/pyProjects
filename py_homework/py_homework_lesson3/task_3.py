a = 1
b = int(input('Введите число: '))
d = b
c = 0
while b > 0:
    a = a * b
    b = b - 1
    c += 1
    print('Шаг №' + str(c) + ': ' + str(b))

print(f'Рассчет факториала числа {d} ---> {a}')