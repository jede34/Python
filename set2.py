my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection('abcd'))

print(my_set.union(other_set))

print(other_set.issubset(my_set))
print(my_set.issuperset(other_set))

print(my_set.difference(other_set))

print(my_set.discard('d'))

print(my_set)

my_set.remove('abc')
print(my_set)

my_set1 = {'abc', 'd', 'f', 'l'}

copied_set = my_set1.copy()

my_set1.add('t')
copied_set.add('l')

print(my_set1 & copied_set)

print(my_set1)
print(copied_set)