import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Rizhiy', 10, 'Sasha')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')