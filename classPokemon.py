class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f'{self.name} attacks {other_pokemon.name}!')

    def dodge(self):
        print(f'{self.name} dodged the attack!')

    def evolve(self, new_form):
        print(f'{self.name} is evolving into {new_form}')

pikachu = Pokemon('Pikachu', 'Electric', 100)

pikachu.attack(Pokemon('Charmander', 'Fire', 100))
pikachu.dodge()
pikachu.evolve('Raichu')