# Встроенная функция zip

fruits = ['apple', 'banana', 'lime']

quintities = [100, 70, 50, 20]

fruit_qtys_zip = zip(fruits, quintities)

print(fruit_qtys_zip)

print(type(fruit_qtys_zip))

fruit_qtys_zip = list(fruit_qtys_zip)

print(fruit_qtys_zip)