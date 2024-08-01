import collections

Person = collections.namedtuple('Person',['first_name', 'last_name', 'age', 'birth_place', 'weight'])

person = Person('Sasha', 'Demchenko', 18, 'Kiev', 60)

print(person.first_name)
print(person.last_name)
print(person.weight)
print(person.age)
print(person.birth_place)