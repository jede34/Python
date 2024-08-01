def add_ingredients(func):
    def wrapper():
        print("Dobavlayem zelen i speczii")
        func()
    return wrapper

@add_ingredients
def make_omelet():
    print("Gotovim omlet")

make_omelet()
