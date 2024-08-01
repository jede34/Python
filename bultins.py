class Cat(object):
    def __init__(self, age, color, name):
        self.age = age
        self.color = color
        self.name = name

    def meow(self):
        print(f"{self.name} says 'Meow'")

    
murchik = Cat(3, 'black', 'Murchik')
persick = Cat(2, 'white', 'Persick')

murchik.meow()
