# Функции PYTHON

def increase_person_age(person):
    person['age'] += 1
    return person

person_one = {
    'name': 'Bob',
    'age': 21
}

increase_person_age(person_one)
print(person_one['age'])