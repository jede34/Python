some_dict = {
    'a': 'Roma',
    'b': 'Sasha', 
    'c': 'Ivan'
}

other_dict = {}

for k, v in some_dict.items():
    other_dict[k] = v.upper()

print(other_dict)




some_list = ['Roma', 'Sasha', 'Ivan']

new_list = []

for v in some_list:
    new_list.append(len(v) > 3)

print(new_list)