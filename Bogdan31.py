# Адреса изменяемых объектов

my_list = [1, 2, 3]
print(id(my_list))

other_list = [1, 2, 3]
print(id(other_list))

print(id([1, 2, 3]))

# Как избежать изменений копий 
info = {
    'name': 'Bogdan',
    'is_instructor': True
}

info_copy = info.copy()

info_copy['reviews_qty'] = 5

print(info_copy)

print(info)

