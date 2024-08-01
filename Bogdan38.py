# Оператор распаковки словаря
my_dict_one = {
    'mouse': 'Razer',
    'price': 1500,
    'green color': True
}
my_dict_two = {
    'keybord': 'Motospeed',
    'price': 888,
    'blue color': True
}
my_dict_three = {
    'Phone': 'Apple Iphone',
    'price': 42000,
    'purple color': True
}

full_dict = {
    **my_dict_one,
    **my_dict_two,
    **my_dict_three
}
print(full_dict)

print(my_dict_one | my_dict_two | my_dict_three)

