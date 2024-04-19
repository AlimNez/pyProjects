my_list = input("Введите данные для списка: ")

for index, item in enumerate(my_list, 3):
    if index % 3 == 0:
        print(f'Индекс: {index} : Элемент: {item}')