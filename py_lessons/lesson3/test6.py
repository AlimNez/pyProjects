numbers = [1,2,3,4,5]

def square_number(number):
    return number ** 2

squared = list(map(square_number,numbers))
print(squared)