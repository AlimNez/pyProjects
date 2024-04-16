students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

all_people = students | employees
all_people = students.union(employees)
print("Все люди: " + str(all_people))
print("Все люди: " + str(all_people))

lern_work = students & employees
lern_work = students.intersection(employees)
print("Учатся и работают: " + str(lern_work))
print("Учатся и работают: " + str(lern_work))

work = employees - students
work = employees.difference(students)
print("Только аботают: " + str(work))
print("Только аботают: " + str(work))

lern = students - employees
lern = students.difference(employees)
print("Только учатся: " + str(lern))
print("Только учатся: " + str(lern))