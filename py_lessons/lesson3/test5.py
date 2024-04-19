difinitely_string = 'some string, my lord'

capital_letters = []
for letter in difinitely_string:
    if letter.isupper():
        break
    print(letter)

else:
    print('else is working, my Lord')