class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name 
        Person.count += 1

    def how_many_persons(self):
        print(f'Quantity of persons now {Person.count}')

first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()