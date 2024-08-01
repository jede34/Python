my_list_dict = [
    {'name': 'Ivan', 'age': 20, 'weight': 63},
    {'name': 'Sasha', 'age': 18, 'weight': 60},
    {'name': 'Renat', 'age': 19, 'weight': 70}
]

first_dict, second_dict, third_dict = my_list_dict

def unpack_and_print(dictionary, key1, key2):
    value1 = dictionary[key1]
    value2 = dictionary[key2]
    print(f"{key1}: {value1}, {key2}: {value2}")

# Example usage
unpack_and_print(first_dict, 'name', 'age')
unpack_and_print(second_dict, 'name', 'weight')
unpack_and_print(third_dict, 'age', 'weight')
