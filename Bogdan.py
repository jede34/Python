# Адреса неизменяемых объектов

my_number = 10
print(id(my_number))

other_number = 10
print(id(other_number))

print(id(10))

# Неизменяемые объекты 

first_num = 10
second_num = first_num

print(id(first_num))
print(id(other_number))

second_num += 5
print(second_num)
print(first_num)

print(id(second_num))
print(id(first_num))