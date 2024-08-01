my_set = {'abc', 'd', 'f', 'y'}
other_set = {'r', 'm', 'n'}

print(my_set == other_set)
print(my_set.__eq__(other_set))

print(my_set is other_set)

print('abc' in my_set)
print('r' in other_set)
print('r' not in other_set)