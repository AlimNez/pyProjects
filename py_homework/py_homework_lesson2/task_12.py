user_text = input("Введите строку с числами через запятую и без пробелов: ")
list(user_text)
user_text = user_text.lower().replace(',','')
print(list(user_text))
print(tuple(user_text))

