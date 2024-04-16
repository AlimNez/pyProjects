a = [4,1,2,6,5]
b = [3,6,4,5]
c = a + b

print(str(c) + ' <---- Способ 1')

a.extend(b)
print(str(a) + ' <---- Способ 2')

c.sort()
c.remove(4)
c.remove(5)
c.remove(6)

print(str(c) + ' <---- Список отсортирован и без дублей')