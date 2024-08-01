my_fruits = ['apple', 'banana', 'lime']

my_apple, *remaining_fruits = my_fruits

print(my_apple)
print(remaining_fruits)

print(type(remaining_fruits))